import logging
import math
import threading
import time
import psutil
from common_module.consts import ERROR_CODE
from pb.fighter.types import types_pb2
from pb.fighter.api.compute import compute_svc_pb2, compute_svc_pb2_grpc

log = logging.getLogger(__name__)


def get_sys_stat(cfg):
    stat = compute_svc_pb2.GetStatusReply()
    stat.total_cpu = psutil.cpu_count()
    stat.used_cpu = math.ceil(stat.total_cpu * psutil.cpu_percent(0.1) / 100)
    stat.idle_cpu = max(stat.total_cpu - stat.used_cpu, 0)

    stat.total_memory = psutil.virtual_memory().total
    stat.used_memory = psutil.virtual_memory().used
    stat.idle_memory = psutil.virtual_memory().free

    stat.total_disk = psutil.disk_usage('/').total
    stat.used_disk = psutil.disk_usage('/').used
    stat.idle_disk = psutil.disk_usage('/').free

    stat.total_bandwidth = cfg["total_bandwidth"]
    net_1 = psutil.net_io_counters()
    time.sleep(1)
    net_2 = psutil.net_io_counters()
    stat.used_bandwidth = (net_2.bytes_sent - net_1.bytes_sent) + (net_2.bytes_recv - net_1.bytes_recv)
    stat.idle_bandwidth = max(stat.total_bandwidth - stat.used_bandwidth, 0)

    stat.status = ERROR_CODE["OK"]
    stat.msg = 'get system status success.'
    str_res = '{' + str(stat).replace('\n', ' ').replace('  ', ' ').replace('{', ':{') + '}'
    log.debug(f"get sys stat: {str_res}")
    return stat


class ComputeProvider(compute_svc_pb2_grpc.ComputeProviderServicer):
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def GetStatus(self, request, context):
        return get_sys_stat(self.task_manager.cfg)

    def GetTaskDetails(self, request, context):
        ret = compute_svc_pb2.GetTaskDetailsReply()
        for task_id in request.task_ids:
            task = self.task_manager.get_task(task_id)
            if task is not None:
                detail = ret.task_details.add()
                detail.task_id = task_id
                detail.elapsed_time = task.get_elapsed_time()
        ret.status = ERROR_CODE["OK"]
        ret.msg = 'get task details success.'
        return ret

    def UploadShard(self, request_it, context):
        for req in request_it:
            yield compute_svc_pb2.UploadShardReply(status=-1, msg='deprecated')

    def HandleTaskReadyGo(self, request, context):
        log.info(f'{context.peer()} submit a task {request.task_id}, thread id: {threading.get_ident()}')
        status, msg = self.task_manager.start(request)
        return types_pb2.TaskReadyGoReply(status=status, msg=msg)

    def HandleCancelTask(self, request, context):
        task_name = f'{request.task_id[:15]}-{request.party_id}'
        log.info(f'{context.peer()} want to cancel task {task_name}')
        status, msg = self.task_manager.cancel_task(request.task_id, request.party_id)
        log.info(f'cancel task status:{status}, {msg}')
        return types_pb2.TaskCancelReply(status=status, msg=msg)
