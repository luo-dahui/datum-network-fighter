
bash kill.sh

source config.ini
via_svc_num=${via_svc_num}
schedule_svc_num=$[${data_svc_num} + ${compute_svc_num}]
schedule_port=${schedule_svc_base_port}

mkdir -p log
scripts_path=$(cd $(dirname $0); pwd)
log_path=${scripts_path}"/log"
base_dir=${scripts_path}"/../.."
cfg=config.yaml
ip=0.0.0.0
use_ssl=0      # 0: not use ssl,  1: use ssl
use_consul=0   # 0: not use consul, 1: use consul
# if modify, must absolute path to python37
python_command=python3

############## consul_svc #############
if [ $use_consul -ne 0 ]
then
    cd $base_dir/third_party/consul_server
    bash run_consul.sh ${ip}
    sleep 5
fi

############## data_svc #############
cd $base_dir/data_svc
data_svc_log=${log_path}"/data_svc"
mkdir -p ${data_svc_log}
for port in $(seq ${data_svc_base_port} $[${data_svc_base_port}+${data_svc_num}-1])
do 
    echo "start data_svc that use port ${port}"
    nohup $python_command -u main.py $cfg --bind_ip=${ip} --port=${port} --schedule_svc=${ip}:${schedule_port} --use_consul=${use_consul} > ${data_svc_log}/data_svc_${port}.log 2>&1 &
    if [ $use_consul -eq 0 ]
    then
        schedule_port=$[${schedule_port}+1]
    fi
done


############## compute_svc #############
cd $base_dir/compute_svc
compute_svc_log=${log_path}"/compute_svc"
mkdir -p ${compute_svc_log}
for port in $(seq ${compute_svc_base_port} $[${compute_svc_base_port}+${compute_svc_num}-1])
do 
    echo "start compute_svc that use port ${port}"
    nohup $python_command -u main.py $cfg --bind_ip=${ip} --port=${port} --schedule_svc=${ip}:${schedule_port} --use_consul=${use_consul} > ${compute_svc_log}/compute_svc_${port}.log 2>&1 &
    if [ $use_consul -eq 0 ]
    then
        schedule_port=$[${schedule_port}+1]
    fi
done


############## schedule_svc #############
cd $base_dir/tests/schedule_svc
schedule_svc_log=${log_path}"/schedule_svc"
mkdir -p ${schedule_svc_log}
if [ $use_consul -eq 0 ]
then
    for port in $(seq ${schedule_svc_base_port} $[${schedule_svc_base_port}+${schedule_svc_num}-1])
    do
        echo "start schedule_svc that use port ${port}"
        nohup $python_command -u main.py $cfg --bind_ip=${ip} --port=${port} --use_consul=${use_consul} > ${schedule_svc_log}/schedule_svc_${port}.log 2>&1 &
    done
else
    nohup $python_command -u main.py $cfg --bind_ip=${ip} --port=${schedule_port} --use_consul=${use_consul} > ${schedule_svc_log}/schedule_svc_${schedule_port}.log 2>&1 &
fi


############## console #############
cd $base_dir/console
echo "start console that connect to data_svc which internal port ${data_svc_base_port}"
echo "run task command: comp_run_task <task_id> <task_cfg_file>"
echo "################### privacy example"
echo "     psi: comp_run_task psi_001 privacy/task_cfg_psi.json"
echo "   train: comp_run_task train_001 privacy/task_cfg_lr_train.json"
echo " predict: comp_run_task predict_001 privacy/task_cfg_lr_predict.json"
echo "   train: comp_run_task train_002 privacy/task_cfg_linr_train.json"
echo " predict: comp_run_task predict_002 privacy/task_cfg_linr_predict.json"
echo "   train: comp_run_task train_003 privacy/task_cfg_dnn_train.json"
echo " predict: comp_run_task predict_003 privacy/task_cfg_dnn_predict.json"
echo "   train: comp_run_task train_004 privacy/task_cfg_xgb_train.json"
echo " predict: comp_run_task predict_004 privacy/task_cfg_xgb_predict.json"
echo "#################### non-privacy example "
echo "   train: comp_run_task train_101 non-privacy/task_cfg_lr_train.json"
echo " predict: comp_run_task predict_101 non-privacy/task_cfg_lr_predict.json"
echo "   train: comp_run_task train_102 non-privacy/task_cfg_linr_train.json"
echo " predict: comp_run_task predict_102 non-privacy/task_cfg_linr_predict.json"
echo "   train: comp_run_task train_103 non-privacy/task_cfg_dnn_train.json"
echo " predict: comp_run_task predict_103 non-privacy/task_cfg_dnn_predict.json"
echo "   train: comp_run_task train_104 non-privacy/task_cfg_knn_train.json"
echo " predict: comp_run_task predict_104 non-privacy/task_cfg_knn_predict.json"
echo "   train: comp_run_task train_105 non-privacy/task_cfg_kmeans_train.json"
echo " predict: comp_run_task predict_105 non-privacy/task_cfg_kmeans_predict.json"
echo "   train: comp_run_task train_106 non-privacy/task_cfg_xgb_train.json"
echo " predict: comp_run_task predict_106 non-privacy/task_cfg_xgb_predict.json"
echo "   train: comp_run_task train_107 non-privacy/task_cfg_svm_train.json"
echo " predict: comp_run_task predict_107 non-privacy/task_cfg_svm_predict.json"
$python_command -u main.py --config=$cfg --data_svc_ip=${ip} --data_svc_port=${data_svc_base_port}
