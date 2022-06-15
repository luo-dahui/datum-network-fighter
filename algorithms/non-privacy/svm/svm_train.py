# coding:utf-8

import os
import sys
import math
import json
import time
import logging
import traceback
import numpy as np
import pandas as pd
import shutil
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib
from functools import wraps


np.set_printoptions(suppress=True)
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
        self.check_params_type(cfg_dict=(cfg_dict, dict), 
                                data_party=(data_party, list), compute_party=(compute_party, list), 
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
    

class SVMTrain(BaseAlgorithm):
    '''
    Plaintext SVM train.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_dir_name = "model"
        self.model_file_name = "svm_model"
        self.output_dir = self._get_output_dir()
        self.output_file = os.path.join(self.output_dir, self.model_file_name)
        self.model_describe_file = os.path.join(self.output_dir, "describe.json")
        self.set_random_seed(self.random_seed)
    
    @staticmethod
    def set_random_seed(seed):
        random.seed(seed)
        np.random.seed(seed)  

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
                "label_owner": "data1",
                "label_column": "Y",
                "hyperparams": {
                    "C": 1.0,
                    "kernel": "rbf",
                    "degree": 3,
                    "max_iter": -1,
                    "decision_function_shape": "ovr",
                    "tol": 0.001,
                    "use_validation_set": true,
                    "validation_set_rate": 0.2,
                    "random_seed": null
                },
                "data_flow_restrict": {
                    "data1": ["compute1"],
                    "compute1": ["result1"]
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
                else:
                    raise Exception(f"paramter error. input_type only support 1, not {input_type}")
        
        dynamic_parameter = cfg_dict["algorithm_dynamic_params"]
        self.label_owner = dynamic_parameter["label_owner"]
        self.label_column = dynamic_parameter["label_column"]
        if self.party_id == self.label_owner:
            self.data_with_label = True
        else:
            self.data_with_label = False                  
        hyperparams = dynamic_parameter["hyperparams"]
        self.C = hyperparams.get("C", 1.0)
        self.kernel = hyperparams.get("kernel", "rbf")
        self.degree = hyperparams.get("degree", 3)
        self.max_iter = hyperparams.get("max_iter", -1)
        self.decision_function_shape = hyperparams.get("decision_function_shape", "ovr")
        self.tol = hyperparams.get("tol", 0.001)
        self.use_validation_set = hyperparams.get("use_validation_set", True)
        self.validation_set_rate = hyperparams.get("validation_set_rate", 0.2)
        self.random_seed = hyperparams.get("random_seed", None)
        self.data_flow_restrict = dynamic_parameter["data_flow_restrict"]

    def check_parameters(self):
        log.info(f"check parameter start.")
        self._check_input_data()            
        self.check_params_type(C=(self.C, float),
                               kernel=(self.kernel, str),
                               degree=(self.degree, int),
                               max_iter=(self.max_iter, int),
                               decision_function_shape=(self.decision_function_shape, str),
                               tol=(self.tol, float),
                               use_validation_set=(self.use_validation_set, bool),
                               validation_set_rate=(self.validation_set_rate, float),
                               random_seed=(self.random_seed, (int, type(None))),
                               data_flow_restrict=(self.data_flow_restrict, dict))
        assert self.C >= 0, f"C must be greater_equal 0, not {self.C}"
        assert self.kernel in ["rbf", "linear", "poly", "sigmoid"], f"kernel supprot rbf,linear,poly,sigmoid. not {self.kernel}"
        if self.kernel == "poly":
            assert self.degree > 0, f"degree must be greater 0, not {self.degree}"
        assert self.max_iter > 0 or self.max_iter == -1, f"max_iter must be greater 0 or equal to -1, not {self.max_iter}"
        assert self.decision_function_shape in ["ovr", "ovo"], f"decision_function_shape support ovr,ovo. not {self.decision_function_shape}"
        assert 0 < self.tol <= 1, f"tol must betweem (0,1], not {self.tol}"
        if self.use_validation_set:
            assert 0 < self.validation_set_rate < 1, f"validattion_set_rate must be between (0,1), not {self.validation_set_rate}"
        if self.random_seed:
            assert 0 <= self.random_seed <= 2**32 - 1, f"random_seed must be between [0,2^32-1], not {self.random_seed}"
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
                if self.data_with_label:
                    assert self.label_column in input_columns, f"label_column:{self.label_column} not in input_file"
                    assert self.label_column not in self.selected_columns, f"label_column:{self.label_column} can not in selected_columns"
            else:
                raise Exception(f"input_file is not exist. input_file={self.input_file}")
                        
        
    def train(self):
        '''
        Logistic regression training algorithm implementation function
        '''
        log.info("start data party extract data column.")
        usecols_file = self._extract_data_column()
        log.info("start data party send data to compute party.")
        self._send_data_to_compute_party(usecols_file)
        evaluate_result = ""
        if self.party_id in self.compute_party:
            log.info("compute party start  compute.")
            evaluate_result = self.compute(usecols_file)
        log.info("start compute party send data to result party.")
        evaluate_result = self._send_data_to_result_party(self.output_dir, evaluate_result)
        result_path, result_type = '', ''
        if self.party_id in self.result_party:
            result_path = self.output_dir
            result_type = 'dir'
        log.info("start remove temp dir.")
        self.remove_temp_dir()
        log.info("train success all.")
        return result_path, result_type, evaluate_result

    def _send_data_to_compute_party(self, data_path):
        if self.party_id in self.data_party:
            compute_party = self.data_flow_restrict[self.party_id][0]
            self.io_channel.send_data_to_other_party(compute_party, data_path)
        elif self.party_id in self.compute_party:
            for party in self.data_party:
                if self.party_id == self.data_flow_restrict[party][0]:
                    self.io_channel.recv_data_from_other_party(party, data_path)
        else:
            pass
    
    def _send_data_to_result_party(self, data_path, evaluate_result):
        if self.party_id in self.compute_party:
            if os.path.isdir(data_path):
                temp_model_dir = os.path.join(self.temp_dir, self.model_dir_name)
                data_path = shutil.make_archive(base_name=temp_model_dir, format='zip', root_dir=data_path)
            result_party = self.data_flow_restrict[self.party_id][0]
            self.io_channel.send_data_to_other_party(result_party, data_path)
            self.io_channel.send_sth(result_party, evaluate_result)
        elif self.party_id in self.result_party:
            for party in self.compute_party:
                if self.party_id == self.data_flow_restrict[party][0]:
                    temp_model_dir = os.path.join(self.temp_dir, f'{self.model_dir_name}.zip')
                    self.io_channel.recv_data_from_other_party(party, temp_model_dir)
                    shutil.unpack_archive(temp_model_dir, self.output_dir)
                    evaluate_result = self.io_channel.recv_sth(party)
                    evaluate_result = evaluate_result.decode()
                    log.info(f'evaluate_result: {evaluate_result}')
        else:
            pass
        return evaluate_result

    def _extract_data_column(self):
        '''
        Extract data column from input file,
        and then write to a new file.
        '''
        usecols_file = os.path.join(self.temp_dir, f"usecols_{self.party_id}.csv")

        if self.party_id in self.data_party:
            use_cols = self.selected_columns
            if self.data_with_label:
                use_cols += [self.label_column]
            log.info("read input file and write to new file.")
            usecols_data = pd.read_csv(self.input_file, usecols=use_cols, dtype="str")
            assert usecols_data.shape[0] > 0, 'no data after select columns.'
            usecols_data = usecols_data[use_cols]
            usecols_data.to_csv(usecols_file, header=True, index=False)
        return usecols_file

    def _read_and_split_data(self, usecols_file):
        '''
        Extract feature columns or label column from input file,
        and then divide them into train set and validation set.
        '''
        input_data = pd.read_csv(usecols_file)
        y_data = input_data[self.label_column]
        del input_data[self.label_column]
        x_data = input_data
        if self.use_validation_set:
            train_x, val_x, train_y, val_y = train_test_split(x_data, y_data, stratify=y_data,
                        test_size=self.validation_set_rate, random_state=self.random_seed)
        else:
            # val_x, val_y is invalid.
            train_x, val_x, train_y, val_y = x_data, x_data, y_data, y_data
        return train_x, val_x, train_y, val_y
    
    def save_model_describe(self, feature_num, class_num, feature_name, label_name, evaluate_result):
        '''save model description for prediction'''
        model_desc = {
            "model_file_name": self.model_file_name,
            "feature_num": feature_num,
            "class_num": class_num,
            "kernel": self.kernel,
            "feature_name": feature_name, 
            "label_name": label_name,
            "evaluate_result": evaluate_result
        }
        log.info(f"model_desc: {model_desc}")
        with open(self.model_describe_file, 'w') as f:
            json.dump(model_desc, f, indent=4)

    def compute(self, usecols_file):
        log.info("extract feature or label.")
        train_x, val_x, train_y, val_y = self._read_and_split_data(usecols_file)
        feature_num = train_x.shape[1]
        feature_name = list(train_x.columns)
        label_name = train_y.name
        train_x, val_x, train_y, val_y = train_x.values, val_x.values, train_y.values, val_y.values
        class_num = np.unique(train_y).shape[0]
        assert class_num >= 2, f"in train set, the class num of label must greater or equal to 2, not {class_num}"

        log.info("train start.")
        train_start_time = time.time()
        classifier = SVC(C=self.C,
                         kernel=self.kernel,
                         degree=self.degree,
                         gamma='auto',
                         max_iter=self.max_iter, 
                         decision_function_shape=self.decision_function_shape,
                         tol=self.tol, 
                         random_state=self.random_seed)
        classifier.fit(train_x, train_y)
        log.info(f"model save to: {self.output_file}")
        joblib.dump(classifier, self.output_file)
        train_use_time = round(time.time()-train_start_time, 3)
        log.info(f"save model success. train_use_time={train_use_time}s")
        
        if self.use_validation_set:
            pred_y = classifier.predict(val_x)
            evaluate = Evaluate(val_y, pred_y)
            if class_num == 2:
                evaluate_result = evaluate.binary_classify()
            else:
                evaluate_result = evaluate.multiclass_classify()
        else:
            evaluate_result = ""
        log.info(f"evaluate_result = {evaluate_result}")
        self.save_model_describe(feature_num, class_num, feature_name, label_name, evaluate_result)
        log.info(f"save model describe success.")
        evaluate_result = json.dumps(evaluate_result)
        return evaluate_result
    
    def _get_output_dir(self):
        output_dir = os.path.join(self.results_dir, self.model_dir_name)
        self.mkdir(output_dir)
        return output_dir

class BaseEvaluate():
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
    
    def binary_classify(self, *args, **kwargs):
        '''binary class classification'''
        raise NotImplementedError(f'{sys._getframe().f_code.co_name} fuction is not implemented.')
    
    def multiclass_classify(self, *args, **kwargs):
        '''multi-class classification'''
        raise NotImplementedError(f'{sys._getframe().f_code.co_name} fuction is not implemented.')
    
    def regression(self, *args, **kwargs):
        '''regression evaluation'''
        raise NotImplementedError(f'{sys._getframe().f_code.co_name} fuction is not implemented.')

class Evaluate(BaseEvaluate):    
    def binary_classify(self):
        from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, precision_score, recall_score
        log.info("start evaluate auc score.")
        y_true = self.y_true.reshape(-1,)
        y_pred_class = self.y_pred.reshape(-1,)
        log.info("start evaluate accuracy score.")
        accuracy = accuracy_score(y_true, y_pred_class)
        log.info("start evaluate f1_score.")
        f1_score = f1_score(y_true, y_pred_class)
        log.info("start evaluate precision score.")
        precision = precision_score(y_true, y_pred_class)
        log.info("start evaluate recall score.")
        recall = recall_score(y_true, y_pred_class)
        accuracy = round(accuracy, 6)
        f1_score = round(f1_score, 6)
        precision = round(precision, 6)
        recall = round(recall, 6)
        evaluate_result = {
            "accuracy": accuracy,
            "f1_score": f1_score,
            "precision": precision,
            "recall": recall
        }
        log.info("evaluate success.")
        return evaluate_result
    
    def multiclass_classify(self):
        from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
        y_true = self.y_true.reshape(-1,)
        y_pred_class = self.y_pred.reshape(-1,)
        accuracy = accuracy_score(y_true, y_pred_class)
        f1_score_micro = f1_score(y_true, y_pred_class, average='micro')
        precision_micro = precision_score(y_true, y_pred_class, average='micro')
        recall_micro = recall_score(y_true, y_pred_class, average='micro')
        f1_score_macro = f1_score(y_true, y_pred_class, average='macro')
        precision_macro = precision_score(y_true, y_pred_class, average='macro')
        recall_macro = recall_score(y_true, y_pred_class, average='macro')
        accuracy = round(accuracy, 6)
        f1_score_micro = round(f1_score_micro, 6)
        precision_micro = round(precision_micro, 6)
        recall_micro = round(recall_micro, 6)
        f1_score_macro = round(f1_score_macro, 6)
        precision_macro = round(precision_macro, 6)
        recall_macro = round(recall_macro, 6)
        evaluate_result = {
            "accuracy": accuracy,
            "f1_score_micro": f1_score_micro,
            "precision_micro": precision_micro,
            "recall_micro": recall_micro,
            "f1_score_macro": f1_score_macro,
            "precision_macro": precision_macro,
            "recall_macro": recall_macro
        }
        log.info("evaluate success.")
        return evaluate_result


@ErrorTraceback("non-privacy_svm_train")
def main(io_channel, cfg_dict: dict, data_party: list, compute_party: list, result_party: list, results_dir: str, **kwargs):
    '''
    This is the entrance to this module
    '''
    svm = SVMTrain(io_channel, cfg_dict, data_party, compute_party, result_party, results_dir)
    result_path, result_type, extra = svm.train()
    return result_path, result_type, extra