
bash kill.sh

source config.ini
via_svc_num=$[${data_svc_num} + ${compute_svc_num}]
schedule_svc_num=$[${data_svc_num} + ${compute_svc_num}]
via_port=${via_svc_base_port}
schedule_port=${schedule_svc_base_port}

export PYTHONPATH=$PYTHONPATH:..:../protos/:../common
mkdir -p log
current_dir=$(cd $(dirname $0); pwd)
log_path=${current_dir}"/log"
base_dir=${current_dir}"/../.."
cfg=config.yaml
ip=127.0.0.1


############## data_svc #############
cd $base_dir; cd data_svc
data_svc_log=${log_path}"/data_svc"
mkdir -p ${data_svc_log}
for port in $(seq ${data_svc_base_port} $[${data_svc_base_port}+${data_svc_num}-1])
do 
    echo "start data_svc that use port ${port}"
    nohup python main.py $cfg --bind_ip=${ip} --port=${port} --via_svc=${ip}:${via_port} --schedule_svc=${ip}:${schedule_port} > ${data_svc_log}/data_svc_${port}.log 2>&1 &
    via_port=$[${via_port}+1]
    schedule_port=$[${schedule_port}+1]
done


############## compute_svc #############
cd $base_dir; cd compute_svc
compute_svc_log=${log_path}"/compute_svc"
mkdir -p ${compute_svc_log}
for port in $(seq ${compute_svc_base_port} $[${compute_svc_base_port}+${compute_svc_num}-1])
do 
    echo "start compute_svc that use port ${port}"
    nohup python main.py $cfg --bind_ip=${ip} --port=${port} --via_svc=${ip}:${via_port} --schedule_svc=${ip}:${schedule_port} > ${compute_svc_log}/compute_svc_${port}.log 2>&1 &
    via_port=$[${via_port}+1]
    schedule_port=$[${schedule_port}+1]
done


############## via_svc #############
cd $base_dir; cd third_party/via_svc
via_svc_log=${log_path}"/via_svc"
mkdir -p ${via_svc_log}
for port in $(seq ${via_svc_base_port} $[${via_svc_base_port}+${via_svc_num}-1])
do
    echo "start via_svc that use port ${port}"
    nohup ./via-go -ssl ./conf/ssl-conf.yml -address 0.0.0.0:${port} > ${via_svc_log}/via_svc_${port}.log 2>&1 &
done


############## schedule_svc #############
cd $base_dir; cd tests/schedule_svc
schedule_svc_log=${log_path}"/schedule_svc"
mkdir -p ${schedule_svc_log}
for port in $(seq ${schedule_svc_base_port} $[${schedule_svc_base_port}+${schedule_svc_num}-1])
do
    echo "start schedule_svc that use port ${port}"
    PYTHONPATH="../..:../../protos/:../../common" nohup python main.py $cfg --bind_ip=${ip} --port=${port} > ${schedule_svc_log}/schedule_svc_${port}.log 2>&1 &
done


############## console #############
cd $base_dir; cd console
# python get_task_cfg.py
echo "start console that connect to data_svc which internal port ${data_svc_base_port}"
python main.py --config=$cfg --data_svc_ip=${ip} --data_svc_port=${data_svc_base_port}