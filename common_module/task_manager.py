from email import policy
import json
import logging
import multiprocessing as mp
import threading
from collections import namedtuple
from common_module.task import Task
from common_module.consts import ERROR_CODE
from common_module.utils import check_input_param_type
from pb.common.constant import fighter_enum_pb2

log = logging.getLogger(__name__)
TParty = namedtuple('TParty', ['ip', 'port', 'party_id', 'name'])

class TaskManager:
    def __init__(self, cfg):
        self.cfg = cfg
        self.tasks = {}  # (task_id, party_id) => task
        self.procs = {}  # (task_id, party_id) => task

    def start(self, req):
        '''
        message Party {
            string ip = 1;
            int32 port = 2;
            string party_id = 3;
            string name = 4;
        }
        enum ConnectPolicyFormat {
            ConnectPolicyFormat_Unknown = 0;
            ConnectPolicyFormat_Str = 1;
            ConnectPolicyFormat_Json = 2;
        }
        message TaskReadyGoReq {
            string task_id = 1;
            string party_id = 2;
            string env_id = 3;
            repeated Party parties = 4;
            string algorithm_code = 5;
            string self_cfg_params = 6;
            string algorithm_dynamic_params = 7;
            repeated string data_party_ids = 8;
            repeated string computation_party_ids = 9;
            repeated string result_party_ids = 10;
            uint64 duration = 11;
            uint64 memory = 12;
            uint32 processor = 13;
            uint64 bandwidth = 14;
            ConnectPolicyFormat connect_policy_format = 15;
            string connect_policy = 16;
        }
        '''
        log.info("#################### Get a task request. the request information is as follows.")
        task_id = req.task_id
        party_id = req.party_id
        env_id = req.env_id
        parties = req.parties
        algorithm_code = req.algorithm_code
        self_cfg_params = req.self_cfg_params
        algorithm_dynamic_params = req.algorithm_dynamic_params
        data_party_ids = req.data_party_ids
        computation_party_ids = req.computation_party_ids
        result_party_ids = req.result_party_ids
        duration = req.duration
        limit_memory = req.memory
        limit_cpu  = req.processor
        limit_bandwidth = req.bandwidth
        connect_policy_format = req.connect_policy_format
        connect_policy = req.connect_policy
        log.info(f"task_id: {task_id}, party_id: {party_id}")
        str_parties = str(parties).replace('\n', ' ')
        log.info(f"parties: {str_parties}")
        log.info(f"self_cfg_params: {self_cfg_params}, algorithm_dynamic_params: {algorithm_dynamic_params}")
        log.info(f"data_party_ids:{data_party_ids}, computation_party_ids:{computation_party_ids}, result_party_ids:{result_party_ids}, "
                f"duration:{duration}, memory:{limit_memory}, processor:{limit_cpu}, bandwidth:{limit_bandwidth}, "
                f"connect_policy_format:{connect_policy_format}, connect_policy:{connect_policy}")
        check_input_param_type(task_id=(task_id, str), 
                                party_id=(party_id, str), 
                                env_id=(env_id, str),
                                algorithm_code=(algorithm_code, str), 
                                self_cfg_params=(self_cfg_params, str),
                                algorithm_dynamic_params=(algorithm_dynamic_params, str),
                                duration=(duration, int), 
                                memory=(limit_memory, int), 
                                processor=(limit_cpu, int), 
                                bandwidth=(limit_bandwidth, int),
                                connect_policy=(connect_policy, str))

        uniq_task = (task_id, party_id)
        task_name = f'{task_id[:15]}-{party_id}'
        if uniq_task in self.tasks:
            log.info(f'task: {task_name} repetitive submit')
            return ERROR_CODE["DUPLICATE_SUBMIT_ERROR"], f'task: {task_name} repetitive submit'
        parties = tuple(TParty(p.ip, p.port, p.party_id, p.name) for p in parties)
        data_party_ids = list(data_party_ids)
        computation_party_ids = list(computation_party_ids)
        result_party_ids = list(result_party_ids)
        if connect_policy_format == fighter_enum_pb2.ConnectPolicyFormat_Json:
            connect_policy = json.loads(connect_policy)
        elif connect_policy_format == fighter_enum_pb2.ConnectPolicyFormat_Str:
            pass
        else:
            return  ERROR_CODE["PARAMS_ERROR"], \
                    f'Unknown connect_policy_format: {connect_policy_format}. only support str/json.'
        
        task = Task(self.cfg, task_id, party_id, env_id, parties, algorithm_code, self_cfg_params,
                    algorithm_dynamic_params, data_party_ids, computation_party_ids, result_party_ids, duration, 
                    limit_memory, limit_cpu, limit_bandwidth, connect_policy)
        self.tasks[uniq_task] = task
        log.info(f'new task: {task_name}, thread id: {threading.get_ident()}')
        p = mp.Process(target=Task.run, args=(task,), name=task_name, daemon=True)
        self.procs[uniq_task] = p
        p.start()
        return ERROR_CODE["OK"], f'submit task {task_name} success.'

    def get_task(self, task_id):
        raise NotImplementedError('deprecated, to remove')

    def cancel_task(self, task_id, party_id):
        uniq_task = (task_id, party_id)
        task_name = f'{task_id[:15]}-{party_id}'
        if uniq_task not in self.procs:
            return ERROR_CODE["TASK_NOT_FOUND_ERROR"], f'process for task {task_name} not found'
        p = self.procs[uniq_task]
        if (not p._closed) and p.is_alive():
            p.kill()
            log.info(f'wait {task_name} terminate')
            p.join()
            msg = 'will soon' if p.is_alive() else 'success'
            p.close()
            self.tasks.pop(uniq_task, None)
            self.procs.pop(uniq_task, None)
        else:
            msg = 'success'
        return ERROR_CODE["OK"], f'cancel task {task_name} {msg}.'

    def clean(self):
        exited = []
        for uniq_task, p in self.procs.items():
            if p._closed or (p.exitcode is not None):
                # log.info(f"p.exitcode: {p.exitcode}, uniq_task: {uniq_task}")
                exited.append(uniq_task)
        # log.info(f'detect {len(exited)} out of {len(self.procs)} tasks has terminated')
        for uniq_task in exited:
            self.tasks.pop(uniq_task, None)
            self.procs.pop(uniq_task, None)