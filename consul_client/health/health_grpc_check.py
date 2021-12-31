# grpc health check detail see
# https://github.com/grpc/grpc/blob/master/doc/health-checking.md
from compute_svc.main import log as compute_log
from data_svc.main import log as data_log
from consul_client.health import health_pb2
from consul_client.health import health_pb2_grpc


class DataServiceHealth(health_pb2_grpc.HealthServicer):
    def Check(self, request, context):
        data_log.debug(f"DataService Health Check...{request}")
        return health_pb2.HealthCheckResponse(status=health_pb2.HealthCheckResponse.ServingStatus.SERVING)

    def Watch(self, request, context):
        return


class JobServiceHealth(health_pb2_grpc.HealthServicer):
    def Check(self, request, context):
        compute_log.debug(f"JobServiceHealth Health Check...{request}")
        return health_pb2.HealthCheckResponse(status=health_pb2.HealthCheckResponse.ServingStatus.SERVING)

    def Watch(self, request, context):
        return


def add_service(server, _type):
    if _type == 'dataNode':
        health_pb2_grpc.add_HealthServicer_to_server(DataServiceHealth(), server)
    elif _type == 'jobNode':
        health_pb2_grpc.add_HealthServicer_to_server(JobServiceHealth(), server)
    else:
        raise Exception(f'Unknown service type {_type}')