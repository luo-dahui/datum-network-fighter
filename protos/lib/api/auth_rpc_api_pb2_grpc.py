# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from lib.api import auth_rpc_api_pb2 as lib_dot_api_dot_auth__rpc__api__pb2
from lib.common import base_pb2 as lib_dot_common_dot_base__pb2


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ApplyIdentityJoin = channel.unary_unary(
                '/rpcapi.AuthService/ApplyIdentityJoin',
                request_serializer=lib_dot_api_dot_auth__rpc__api__pb2.ApplyIdentityJoinRequest.SerializeToString,
                response_deserializer=lib_dot_common_dot_base__pb2.SimpleResponse.FromString,
                )
        self.RevokeIdentityJoin = channel.unary_unary(
                '/rpcapi.AuthService/RevokeIdentityJoin',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=lib_dot_common_dot_base__pb2.SimpleResponse.FromString,
                )
        self.GetNodeIdentity = channel.unary_unary(
                '/rpcapi.AuthService/GetNodeIdentity',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.GetNodeIdentityResponse.FromString,
                )
        self.GetIdentityList = channel.unary_unary(
                '/rpcapi.AuthService/GetIdentityList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.GetIdentityListResponse.FromString,
                )
        self.ApplyMetadataAuthority = channel.unary_unary(
                '/rpcapi.AuthService/ApplyMetadataAuthority',
                request_serializer=lib_dot_api_dot_auth__rpc__api__pb2.ApplyMetadataAuthorityRequest.SerializeToString,
                response_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.ApplyMetadataAuthorityResponse.FromString,
                )
        self.RevokeMetadataAuthority = channel.unary_unary(
                '/rpcapi.AuthService/RevokeMetadataAuthority',
                request_serializer=lib_dot_api_dot_auth__rpc__api__pb2.RevokeMetadataAuthorityRequest.SerializeToString,
                response_deserializer=lib_dot_common_dot_base__pb2.SimpleResponse.FromString,
                )
        self.AuditMetadataAuthority = channel.unary_unary(
                '/rpcapi.AuthService/AuditMetadataAuthority',
                request_serializer=lib_dot_api_dot_auth__rpc__api__pb2.AuditMetadataAuthorityRequest.SerializeToString,
                response_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.AuditMetadataAuthorityResponse.FromString,
                )
        self.GetMetadataAuthorityList = channel.unary_unary(
                '/rpcapi.AuthService/GetMetadataAuthorityList',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListResponse.FromString,
                )
        self.GetMetadataAuthorityListByUser = channel.unary_unary(
                '/rpcapi.AuthService/GetMetadataAuthorityListByUser',
                request_serializer=lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListByUserRequest.SerializeToString,
                response_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListResponse.FromString,
                )


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ApplyIdentityJoin(self, request, context):
        """组织身份入网申请
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeIdentityJoin(self, request, context):
        """注销准入网络
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNodeIdentity(self, request, context):
        """查询自己组织的identity信息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIdentityList(self, request, context):
        """查询全网组织的身份信息列表(已入网的)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApplyMetadataAuthority(self, request, context):
        """发起数据授权申请
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeMetadataAuthority(self, request, context):
        """撤销数据授权申请
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuditMetadataAuthority(self, request, context):
        """数据授权审核
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetadataAuthorityList(self, request, context):
        """当前(组织)的所有元数据的授权申请及审核结果详情列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetadataAuthorityListByUser(self, request, context):
        """当前(用户)的所有元数据的授权申请及审核结果详情列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ApplyIdentityJoin': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplyIdentityJoin,
                    request_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.ApplyIdentityJoinRequest.FromString,
                    response_serializer=lib_dot_common_dot_base__pb2.SimpleResponse.SerializeToString,
            ),
            'RevokeIdentityJoin': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeIdentityJoin,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=lib_dot_common_dot_base__pb2.SimpleResponse.SerializeToString,
            ),
            'GetNodeIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNodeIdentity,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=lib_dot_api_dot_auth__rpc__api__pb2.GetNodeIdentityResponse.SerializeToString,
            ),
            'GetIdentityList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIdentityList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=lib_dot_api_dot_auth__rpc__api__pb2.GetIdentityListResponse.SerializeToString,
            ),
            'ApplyMetadataAuthority': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplyMetadataAuthority,
                    request_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.ApplyMetadataAuthorityRequest.FromString,
                    response_serializer=lib_dot_api_dot_auth__rpc__api__pb2.ApplyMetadataAuthorityResponse.SerializeToString,
            ),
            'RevokeMetadataAuthority': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokeMetadataAuthority,
                    request_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.RevokeMetadataAuthorityRequest.FromString,
                    response_serializer=lib_dot_common_dot_base__pb2.SimpleResponse.SerializeToString,
            ),
            'AuditMetadataAuthority': grpc.unary_unary_rpc_method_handler(
                    servicer.AuditMetadataAuthority,
                    request_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.AuditMetadataAuthorityRequest.FromString,
                    response_serializer=lib_dot_api_dot_auth__rpc__api__pb2.AuditMetadataAuthorityResponse.SerializeToString,
            ),
            'GetMetadataAuthorityList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetadataAuthorityList,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListResponse.SerializeToString,
            ),
            'GetMetadataAuthorityListByUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetadataAuthorityListByUser,
                    request_deserializer=lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListByUserRequest.FromString,
                    response_serializer=lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rpcapi.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ApplyIdentityJoin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/ApplyIdentityJoin',
            lib_dot_api_dot_auth__rpc__api__pb2.ApplyIdentityJoinRequest.SerializeToString,
            lib_dot_common_dot_base__pb2.SimpleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeIdentityJoin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/RevokeIdentityJoin',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            lib_dot_common_dot_base__pb2.SimpleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNodeIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/GetNodeIdentity',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            lib_dot_api_dot_auth__rpc__api__pb2.GetNodeIdentityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIdentityList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/GetIdentityList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            lib_dot_api_dot_auth__rpc__api__pb2.GetIdentityListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ApplyMetadataAuthority(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/ApplyMetadataAuthority',
            lib_dot_api_dot_auth__rpc__api__pb2.ApplyMetadataAuthorityRequest.SerializeToString,
            lib_dot_api_dot_auth__rpc__api__pb2.ApplyMetadataAuthorityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevokeMetadataAuthority(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/RevokeMetadataAuthority',
            lib_dot_api_dot_auth__rpc__api__pb2.RevokeMetadataAuthorityRequest.SerializeToString,
            lib_dot_common_dot_base__pb2.SimpleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuditMetadataAuthority(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/AuditMetadataAuthority',
            lib_dot_api_dot_auth__rpc__api__pb2.AuditMetadataAuthorityRequest.SerializeToString,
            lib_dot_api_dot_auth__rpc__api__pb2.AuditMetadataAuthorityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetadataAuthorityList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/GetMetadataAuthorityList',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetadataAuthorityListByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rpcapi.AuthService/GetMetadataAuthorityListByUser',
            lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListByUserRequest.SerializeToString,
            lib_dot_api_dot_auth__rpc__api__pb2.GetMetadataAuthorityListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)