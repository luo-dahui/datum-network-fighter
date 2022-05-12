# coding:utf-8

import os
import sys
import math
import json
import time
import copy
import logging
import shutil
import traceback
import numpy as np
import pandas as pd
import tensorflow as tf
import latticex.rosetta as rtt
from functools import wraps


np.set_printoptions(suppress=True)
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
rtt.set_backend_loglevel(3)  # All(0), Trace(1), Debug(2), Info(3), Warn(4), Error(5), Fatal(6)
logger = logging.getLogger(__name__)
class LogWithStage():
    def __init__(self, name):
        self.run_stage = 'init log.'
        self.logger = logging.getLogger(name)

    def info(self, content):
        self.run_stage = content
        self.logger.info(content)
    
    def debug(self, content):
        self.logger.debug(content)
log = LogWithStage(__name__)


class ErrorTraceback():
    def __init__(self, algo_type):
        self.algo_type = algo_type
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                log.info(f"start {func.__name__} function. algo: {self.algo_type}.")
                result = func(*args, **kwargs)
                log.info(f"finish {func.__name__} function. algo: {self.algo_type}.")
            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                all_error = traceback.extract_tb(exc_traceback)
                error_algo_file = all_error[0].filename
                error_filename = os.path.split(error_algo_file)[1]
                error_lineno, error_function = [], []
                for one_error in all_error:
                    if one_error.filename == error_algo_file:  # only report the algo file error
                        error_lineno.append(one_error.lineno)
                        error_function.append(one_error.name)
                error_msg = repr(e)
                raise Exception(f"<ALGO>:{self.algo_type}. <RUN_STAGE>:{log.run_stage} "
                                f"<ERROR>: {error_filename},{error_lineno},{error_function},{error_msg}")
            return result
        return wrapper

class BaseAlgorithm(object):
    def __init__(self,
                 io_channel,
                 cfg_dict: dict,
                 data_party: list,
                 compute_party: list,
                 result_party: list,
                 results_dir: str):
        log.info(f"cfg_dict:{cfg_dict}")
        log.info(f"data_party:{data_party}, compute_party:{compute_party}, result_party:{result_party}, results_dir:{results_dir}")
        self.check_params_type(cfg_dict=(cfg_dict, dict), data_party=(data_party, list), compute_party=(compute_party, list), 
                               result_party=(result_party, list), results_dir=(results_dir, str))        
        log.info(f"start get input parameter.")
        self.io_channel = io_channel
        self.data_party = list(data_party)
        self.compute_party = list(compute_party)
        self.result_party = list(result_party)
        self.results_dir = results_dir
        self.parse_algo_cfg(cfg_dict)
        self.check_parameters()
        self.temp_dir = self.get_temp_dir()
        log.info("finish get input parameter.")
    
    def check_params_type(self, **kargs):
        for key,value in kargs.items():
            assert isinstance(value[0], value[1]), f'{key} must be type({value[1]}), not {type(value[0])}'
    
    def parse_algo_cfg(self, cfg_dict):
        raise NotImplementedError(f'{sys._getframe().f_code.co_name} fuction is not implemented.')
    
    def check_parameters(self):
        raise NotImplementedError(f'{sys._getframe().f_code.co_name} fuction is not implemented.')
        
    def get_temp_dir(self):
        '''
        Get the directory for temporarily saving files
        '''
        temp_dir = os.path.join(self.results_dir, 'temp')
        self.mkdir(temp_dir)
        return temp_dir
    
    def remove_temp_dir(self):
        '''
        for result party, only delete the temp dir.
        for non-result party, that is data and compute party, delete the all results
        '''
        if self.party_id in self.result_party:
            temp_dir = self.temp_dir
        else:
            temp_dir = self.results_dir
        self.remove_dir(temp_dir)
    
    def mkdir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    def remove_dir(self, directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)


class PrivacyDnnPredict(BaseAlgorithm):
    '''
    Privacy Dnn predict base on rosetta.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_file = os.path.join(self.results_dir, "result_predict.csv")

    def parse_algo_cfg(self, cfg_dict):
        '''
        cfg_dict:
        {
            "self_cfg_params": {
                "party_id": "data1",
                "input_data": [
                    {
                        "input_type": 1,
                        "data_type": 1,
                        "data_path": "path/to/data",
                        "key_column": "col1",
                        "selected_columns": ["col2", "col3"]
                    }
                ]
            },
            "algorithm_dynamic_params": {
                "model_restore_party": "model1",
                "hyperparams": {
                    "layer_units": [32, 1],
                    "layer_activation": ["sigmoid", "sigmoid"],
                    "use_intercept": true,
                    "predict_threshold": 0.5
                }
            }

        }
        '''
        self.party_id = cfg_dict["self_cfg_params"]["party_id"]
        input_data = cfg_dict["self_cfg_params"]["input_data"]
        if self.party_id in self.data_party:
            for data in input_data:
                input_type = data["input_type"]
                data_type = data["data_type"]
                if input_type == 1:
                    self.input_file = data["data_path"]
                    self.key_column = data.get("key_column")
                    self.selected_columns = data.get("selected_columns")
                elif input_type == 2:
                    self.model_path = data["data_path"]
                    self.model_file = os.path.join(self.model_path, "model")
                else:
                    raise Exception("paramter error. input_type only support 1/2, not {input_type}")

        dynamic_parameter = cfg_dict["algorithm_dynamic_params"]
        self.model_restore_party = dynamic_parameter["model_restore_party"]
        hyperparams = dynamic_parameter["hyperparams"]
        self.layer_units = hyperparams.get("layer_units", [32, 1])
        self.layer_activation = hyperparams.get("layer_activation", ["sigmoid", "sigmoid"])
        self.use_intercept = hyperparams.get("use_intercept", True)  # True: use b, False: not use b        
        self.predict_threshold = hyperparams.get("predict_threshold", 0.5)
        self.data_party.remove(self.model_restore_party)  # except restore party

    def check_parameters(self):
        log.info(f"check parameter start.")
        self._check_input_data()
        self.check_params_type(model_restore_party=(self.model_restore_party, str),
                               layer_units=(self.layer_units, list),
                               layer_activation=(self.layer_activation, list),
                               use_intercept=(self.use_intercept, bool),
                               predict_threshold=(self.predict_threshold, float))
        if self.party_id == self.model_restore_party:
            assert os.path.exists(self.model_path), f"model_path is not exist. model_path={self.model_path}"
        assert 0 <= self.predict_threshold <= 1, f"predict threshold must be between [0,1], not {self.predict_threshold}"
        assert self.layer_units, f"layer_units must not empty, not {self.layer_units}"
        assert self.layer_activation, f"layer_activation must not empty, not {self.layer_activation}"
        assert len(self.layer_units) == len(self.layer_activation), \
                f"the length of layer_units:{len(self.layer_units)} and layer_activation:{len(self.layer_activation)} not same"
        for i in self.layer_units:
            assert isinstance(i, int) and i > 0, f"layer_units'element can only be type(int) and greater 0, not {i}"
        for i in self.layer_activation:
            if i not in ["", "sigmoid", "relu", None]:
                raise Exception(f'layer_activation can only be ""/"sigmoid"/"relu"/None, not {i}')
        if self.layer_activation[-1] == 'sigmoid':
            if self.layer_units[-1] != 1:
                raise Exception(f"output layer activation is sigmoid, output layer units must be 1, not {self.layer_units[-1]}")
        log.info(f"check parameter finish.")
    
    def _check_input_data(self):
        if self.party_id in self.data_party:
            self.check_params_type(data_path=(self.input_file, str), 
                                    key_column=(self.key_column, str),
                                    selected_columns=(self.selected_columns, list))
            self.input_file = self.input_file.strip()
            if os.path.exists(self.input_file):
                file_suffix = os.path.splitext(self.input_file)[-1][1:]
                assert file_suffix == "csv", f"input_file must csv file, not {file_suffix}"
                input_columns = pd.read_csv(self.input_file, nrows=0)
                input_columns = list(input_columns.columns)
                assert self.key_column in input_columns, f"key_column:{self.key_column} not in input_file"
                error_col = []
                for col in self.selected_columns:
                    if col not in input_columns:
                        error_col.append(col)   
                assert not error_col, f"selected_columns:{error_col} not in input_file"
                assert self.key_column not in self.selected_columns, f"key_column:{self.key_column} can not in selected_columns"
            else:
                raise Exception(f"input_file is not exist. input_file={self.input_file}")

    def predict(self):
        '''
        predict algorithm implementation function
        '''

        log.info("extract feature or id.")
        file_x, id_col = self.extract_feature_or_index()
        
        log.info("start set channel.")
        rtt.set_channel("", self.io_channel.channel)
        log.info("waiting other party connect...")
        rtt.activate("SecureNN")
        log.info("protocol has been activated.")
        
        log.info(f"start set restore model. restore party={self.model_restore_party}")
        rtt.set_restore_model(False, plain_model=self.model_restore_party)
        # sharing data
        log.info(f"start sharing data. data_owner={self.data_party}")
        shard_x = rtt.PrivateDataset(data_owner=self.data_party).load_X(file_x, header=0)
        log.info("finish sharing data .")
        column_total_num = shard_x.shape[1]
        log.info(f"column_total_num = {column_total_num}.")

        if self.party_id not in self.data_party:  
            # mean the compute party and result party
            log.info("compute start.")
            X = tf.placeholder(tf.float64, [None, column_total_num], name='X')
            output = self.dnn(X, column_total_num)
            output_layer_activation = self.layer_activation[-1]
            with tf.name_scope('output'):
                if not output_layer_activation:
                    pred_Y = output
                elif output_layer_activation == 'sigmoid':
                    pred_Y = tf.sigmoid(output)
                elif output_layer_activation == 'relu':
                    pred_Y = tf.nn.relu(output)
                else:
                    raise Exception('output layer not support {output_layer_activation} activation.')
            saver = tf.train.Saver(var_list=None, max_to_keep=5, name='v2')
            init = tf.global_variables_initializer()
            reveal_Y = rtt.SecureReveal(pred_Y)  # only reveal to result party

            with tf.Session() as sess:
                log.info("session init.")
                sess.run(init)
                log.info("start restore model.")
                if self.party_id == self.model_restore_party:
                    if os.path.exists(os.path.join(self.model_path, "checkpoint")):
                        log.info(f"model restore from: {self.model_file}.")
                        saver.restore(sess, self.model_file)
                    else:
                        raise Exception("model not found or model damaged")
                else:
                    log.info("restore model...")
                    temp_file = os.path.join(self.get_temp_dir(), 'ckpt_temp_file')
                    with open(temp_file, "w") as f:
                        pass
                    saver.restore(sess, temp_file)
                log.info("finish restore model.")
                
                # predict
                log.info("predict start.")
                predict_start_time = time.time()
                Y_pred = sess.run(reveal_Y, feed_dict={X: shard_x})
                log.debug(f"Y_pred:\n {Y_pred[:10]}")
                predict_use_time = round(time.time() - predict_start_time, 3)
                log.info(f"predict finish. predict_use_time={predict_use_time}s")
        else:
            log.info("computing, please waiting for compute finish...")
        rtt.deactivate()
        log.info("rtt deactivate finish.")
        
        result_path, result_type = "", ""
        if self.party_id in self.result_party:
            log.info("predict result write to file.")
            Y_pred = Y_pred.astype("float")
            if (not output_layer_activation) or (output_layer_activation == 'relu'):
                Y_result = pd.DataFrame(Y_pred, columns=["Y_pred"])
            elif output_layer_activation == 'sigmoid':
                Y_prob = pd.DataFrame(Y_pred, columns=["Y_prob"])
                Y_class = (Y_pred > self.predict_threshold) * 1
                Y_class = pd.DataFrame(Y_class, columns=[f"Y_class(>{self.predict_threshold})"])
                Y_result = pd.concat([Y_prob, Y_class], axis=1)
            Y_result.to_csv(self.output_file, header=True, index=False)
            result_path = self.output_file
            result_type = "csv"
        log.info("start remove temp dir.")
        self.remove_temp_dir()
        log.info("predict success all.")
        return result_path, result_type

    def layer(self, input_tensor, input_dim, output_dim, activation, layer_name='Dense'):
        with tf.name_scope(layer_name):
            W = tf.Variable(tf.random_normal([input_dim, output_dim], dtype=tf.float64), name='W')
            if self.use_intercept:
                b = tf.Variable(tf.random_normal([output_dim], dtype=tf.float64), name='b')
                with tf.name_scope('logits'):
                    logits = tf.matmul(input_tensor, W) + b
            else:
                with tf.name_scope('logits'):
                    logits = tf.matmul(input_tensor, W)
            if not activation:
                one_layer = logits
            elif activation == 'sigmoid':
                one_layer = tf.sigmoid(logits)
            elif activation == 'relu':
                one_layer = tf.nn.relu(logits)
            else:
                raise Exception(f'not support {activation} activation.')
            return one_layer
    
    def dnn(self, input_X, input_dim):
        layer_activation = copy.deepcopy(self.layer_activation[:-1])
        layer_activation.append("")
        for i in range(len(self.layer_units)):
            if i == 0:
                input_units = input_dim
                previous_output = input_X
            else:
                input_units = self.layer_units[i-1]
                previous_output = output
            output = self.layer(previous_output, 
                                input_units, 
                                self.layer_units[i], 
                                layer_activation[i], 
                                layer_name=f"Dense_{i}")
        return output
        
    def extract_feature_or_index(self):
        '''
        Extract feature columns or index column from input file.
        '''
        file_x = ""
        id_col = None
        temp_dir = self.get_temp_dir()
        if self.party_id in self.data_party:
            usecols = [self.key_column] + self.selected_columns
            input_data = pd.read_csv(self.input_file, usecols=usecols, dtype="str")
            input_data = input_data[usecols]
            assert input_data.shape[0] > 0, 'input file is no data.'
            id_col = input_data[self.key_column]
            file_x = os.path.join(temp_dir, f"file_x_{self.party_id}.csv")
            x_data = input_data.drop(labels=self.key_column, axis=1)
            x_data.to_csv(file_x, header=True, index=False)

        return file_x, id_col
    

@ErrorTraceback("privacy_dnn_predict")
def main(io_channel, cfg_dict: dict, data_party: list, compute_party: list, result_party: list, results_dir: str, **kwargs):
    '''
    This is the entrance to this module
    '''
    privacy_dnn = PrivacyDnnPredict(io_channel, cfg_dict, data_party, compute_party, result_party, results_dir)
    result_path, result_type = privacy_dnn.predict()
    return result_path, result_type