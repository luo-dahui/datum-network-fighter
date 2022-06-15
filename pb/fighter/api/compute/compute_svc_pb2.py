# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fighter/api/compute/compute_svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from fighter.types import types_pb2 as fighter_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fighter/api/compute/compute_svc.proto',
  package='fighter.api.compute',
  syntax='proto3',
  serialized_options=b'Z:github.com/datumtechs/datum-network-carrier/pb/fighter/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%fighter/api/compute/compute_svc.proto\x12\x13\x66ighter.api.compute\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19\x66ighter/types/types.proto\"\xa7\x02\n\x0eGetStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x11\n\ttotal_cpu\x18\x03 \x01(\r\x12\x10\n\x08used_cpu\x18\x04 \x01(\r\x12\x10\n\x08idle_cpu\x18\x05 \x01(\r\x12\x14\n\x0ctotal_memory\x18\x06 \x01(\x04\x12\x13\n\x0bused_memory\x18\x07 \x01(\x04\x12\x13\n\x0bidle_memory\x18\x08 \x01(\x04\x12\x12\n\ntotal_disk\x18\t \x01(\x04\x12\x11\n\tused_disk\x18\n \x01(\x04\x12\x11\n\tidle_disk\x18\x0b \x01(\x04\x12\x17\n\x0ftotal_bandwidth\x18\x0c \x01(\x04\x12\x16\n\x0eused_bandwidth\x18\r \x01(\x04\x12\x16\n\x0eidle_bandwidth\x18\x0e \x01(\x04\"%\n\x11GetTaskDetailsReq\x12\x10\n\x08task_ids\x18\x01 \x03(\t\"\x89\x02\n\x13GetTaskDetailsReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x45\n\x0ctask_details\x18\x03 \x03(\x0b\x32/.fighter.api.compute.GetTaskDetailsReply.Detail\x1a\x8d\x01\n\x06\x44\x65tail\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x11\n\ttask_name\x18\x02 \x01(\t\x12\x13\n\x0b\x63ontract_id\x18\x03 \x01(\t\x12\x14\n\x0c\x65lapsed_time\x18\x04 \x01(\x03\x12\x13\n\x0bremain_time\x18\x05 \x01(\x03\x12\x10\n\x08progress\x18\x06 \x01(\t\x12\r\n\x05phase\x18\x07 \x01(\t2\xf4\x03\n\x0f\x43omputeProvider\x12\x64\n\tGetStatus\x12\x16.google.protobuf.Empty\x1a#.fighter.api.compute.GetStatusReply\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/compute/getStatus\x12\x86\x01\n\x0eGetTaskDetails\x12&.fighter.api.compute.GetTaskDetailsReq\x1a(.fighter.api.compute.GetTaskDetailsReply\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/compute/getTaskDetails:\x01*\x12z\n\x11HandleTaskReadyGo\x12\x1d.fighter.types.TaskReadyGoReq\x1a\x1f.fighter.types.TaskReadyGoReply\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/compute/handleTaskReadyGo:\x01*\x12v\n\x10HandleCancelTask\x12\x1c.fighter.types.TaskCancelReq\x1a\x1e.fighter.types.TaskCancelReply\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/compute/handleCancelTask:\x01*B<Z:github.com/datumtechs/datum-network-carrier/pb/fighter/apib\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,fighter_dot_types_dot_types__pb2.DESCRIPTOR,])




_GETSTATUSREPLY = _descriptor.Descriptor(
  name='GetStatusReply',
  full_name='fighter.api.compute.GetStatusReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fighter.api.compute.GetStatusReply.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='fighter.api.compute.GetStatusReply.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_cpu', full_name='fighter.api.compute.GetStatusReply.total_cpu', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='used_cpu', full_name='fighter.api.compute.GetStatusReply.used_cpu', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idle_cpu', full_name='fighter.api.compute.GetStatusReply.idle_cpu', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_memory', full_name='fighter.api.compute.GetStatusReply.total_memory', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='used_memory', full_name='fighter.api.compute.GetStatusReply.used_memory', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idle_memory', full_name='fighter.api.compute.GetStatusReply.idle_memory', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_disk', full_name='fighter.api.compute.GetStatusReply.total_disk', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='used_disk', full_name='fighter.api.compute.GetStatusReply.used_disk', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idle_disk', full_name='fighter.api.compute.GetStatusReply.idle_disk', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_bandwidth', full_name='fighter.api.compute.GetStatusReply.total_bandwidth', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='used_bandwidth', full_name='fighter.api.compute.GetStatusReply.used_bandwidth', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='idle_bandwidth', full_name='fighter.api.compute.GetStatusReply.idle_bandwidth', index=13,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=444,
)


_GETTASKDETAILSREQ = _descriptor.Descriptor(
  name='GetTaskDetailsReq',
  full_name='fighter.api.compute.GetTaskDetailsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_ids', full_name='fighter.api.compute.GetTaskDetailsReq.task_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=483,
)


_GETTASKDETAILSREPLY_DETAIL = _descriptor.Descriptor(
  name='Detail',
  full_name='fighter.api.compute.GetTaskDetailsReply.Detail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='fighter.api.compute.GetTaskDetailsReply.Detail.task_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_name', full_name='fighter.api.compute.GetTaskDetailsReply.Detail.task_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_id', full_name='fighter.api.compute.GetTaskDetailsReply.Detail.contract_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='elapsed_time', full_name='fighter.api.compute.GetTaskDetailsReply.Detail.elapsed_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remain_time', full_name='fighter.api.compute.GetTaskDetailsReply.Detail.remain_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress', full_name='fighter.api.compute.GetTaskDetailsReply.Detail.progress', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phase', full_name='fighter.api.compute.GetTaskDetailsReply.Detail.phase', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=751,
)

_GETTASKDETAILSREPLY = _descriptor.Descriptor(
  name='GetTaskDetailsReply',
  full_name='fighter.api.compute.GetTaskDetailsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fighter.api.compute.GetTaskDetailsReply.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='fighter.api.compute.GetTaskDetailsReply.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_details', full_name='fighter.api.compute.GetTaskDetailsReply.task_details', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETTASKDETAILSREPLY_DETAIL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=751,
)

_GETTASKDETAILSREPLY_DETAIL.containing_type = _GETTASKDETAILSREPLY
_GETTASKDETAILSREPLY.fields_by_name['task_details'].message_type = _GETTASKDETAILSREPLY_DETAIL
DESCRIPTOR.message_types_by_name['GetStatusReply'] = _GETSTATUSREPLY
DESCRIPTOR.message_types_by_name['GetTaskDetailsReq'] = _GETTASKDETAILSREQ
DESCRIPTOR.message_types_by_name['GetTaskDetailsReply'] = _GETTASKDETAILSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetStatusReply = _reflection.GeneratedProtocolMessageType('GetStatusReply', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSREPLY,
  '__module__' : 'fighter.api.compute.compute_svc_pb2'
  # @@protoc_insertion_point(class_scope:fighter.api.compute.GetStatusReply)
  })
_sym_db.RegisterMessage(GetStatusReply)

GetTaskDetailsReq = _reflection.GeneratedProtocolMessageType('GetTaskDetailsReq', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKDETAILSREQ,
  '__module__' : 'fighter.api.compute.compute_svc_pb2'
  # @@protoc_insertion_point(class_scope:fighter.api.compute.GetTaskDetailsReq)
  })
_sym_db.RegisterMessage(GetTaskDetailsReq)

GetTaskDetailsReply = _reflection.GeneratedProtocolMessageType('GetTaskDetailsReply', (_message.Message,), {

  'Detail' : _reflection.GeneratedProtocolMessageType('Detail', (_message.Message,), {
    'DESCRIPTOR' : _GETTASKDETAILSREPLY_DETAIL,
    '__module__' : 'fighter.api.compute.compute_svc_pb2'
    # @@protoc_insertion_point(class_scope:fighter.api.compute.GetTaskDetailsReply.Detail)
    })
  ,
  'DESCRIPTOR' : _GETTASKDETAILSREPLY,
  '__module__' : 'fighter.api.compute.compute_svc_pb2'
  # @@protoc_insertion_point(class_scope:fighter.api.compute.GetTaskDetailsReply)
  })
_sym_db.RegisterMessage(GetTaskDetailsReply)
_sym_db.RegisterMessage(GetTaskDetailsReply.Detail)


DESCRIPTOR._options = None

_COMPUTEPROVIDER = _descriptor.ServiceDescriptor(
  name='ComputeProvider',
  full_name='fighter.api.compute.ComputeProvider',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=754,
  serialized_end=1254,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='fighter.api.compute.ComputeProvider.GetStatus',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETSTATUSREPLY,
    serialized_options=b'\202\323\344\223\002\024\022\022/compute/getStatus',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTaskDetails',
    full_name='fighter.api.compute.ComputeProvider.GetTaskDetails',
    index=1,
    containing_service=None,
    input_type=_GETTASKDETAILSREQ,
    output_type=_GETTASKDETAILSREPLY,
    serialized_options=b'\202\323\344\223\002\034\"\027/compute/getTaskDetails:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleTaskReadyGo',
    full_name='fighter.api.compute.ComputeProvider.HandleTaskReadyGo',
    index=2,
    containing_service=None,
    input_type=fighter_dot_types_dot_types__pb2._TASKREADYGOREQ,
    output_type=fighter_dot_types_dot_types__pb2._TASKREADYGOREPLY,
    serialized_options=b'\202\323\344\223\002\037\"\032/compute/handleTaskReadyGo:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HandleCancelTask',
    full_name='fighter.api.compute.ComputeProvider.HandleCancelTask',
    index=3,
    containing_service=None,
    input_type=fighter_dot_types_dot_types__pb2._TASKCANCELREQ,
    output_type=fighter_dot_types_dot_types__pb2._TASKCANCELREPLY,
    serialized_options=b'\202\323\344\223\002\036\"\031/compute/handleCancelTask:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMPUTEPROVIDER)

DESCRIPTOR.services_by_name['ComputeProvider'] = _COMPUTEPROVIDER

# @@protoc_insertion_point(module_scope)