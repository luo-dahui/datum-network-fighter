# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lib/types/consensusstate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from lib.common import base_pb2 as lib_dot_common_dot_base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lib/types/consensusstate.proto',
  package='types',
  syntax='proto3',
  serialized_options=b'Z+github.com/RosettaFlow/Carrier-Go/lib/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1elib/types/consensusstate.proto\x12\x05types\x1a\x15lib/common/base.proto\"\xb1\x02\n\x10OrgProposalState\x12\x1d\n\x15pre_period_start_time\x18\x01 \x01(\x04\x12\x19\n\x11period_start_time\x18\x02 \x01(\x04\x12\x19\n\x11\x64\x65\x61\x64line_duration\x18\x03 \x01(\x04\x12\x11\n\tcreate_at\x18\x04 \x01(\x04\x12)\n\ttask_role\x18\x05 \x01(\x0e\x32\x16.api.protobuf.TaskRole\x12\x30\n\x08task_org\x18\x06 \x01(\x0b\x32\x1e.api.protobuf.TaskOrganization\x12\x12\n\nperiod_num\x18\x07 \x01(\r\x12\x0f\n\x07task_id\x18\x08 \x01(\t\x12\x33\n\x0btask_sender\x18\t \x01(\x0b\x32\x1e.api.protobuf.TaskOrganization\"M\n\x13PrepareVoteResource\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\x12\x10\n\x08party_id\x18\x04 \x01(\t\"\xca\x01\n\tMsgOption\x12+\n\x0bsender_role\x18\x01 \x01(\x0e\x32\x16.api.protobuf.TaskRole\x12\x17\n\x0fsender_party_id\x18\x02 \x01(\t\x12-\n\rreceiver_role\x18\x03 \x01(\x0e\x32\x16.api.protobuf.TaskRole\x12\x19\n\x11receiver_party_id\x18\x04 \x01(\t\x12-\n\x05owner\x18\x05 \x01(\x0b\x32\x1e.api.protobuf.TaskOrganization\"\x9d\x01\n\x10PrepareVoteState\x12$\n\nmsg_option\x18\x01 \x01(\x0b\x32\x10.types.MsgOption\x12\x13\n\x0bvote_option\x18\x02 \x01(\r\x12-\n\tpeer_info\x18\x03 \x01(\x0b\x32\x1a.types.PrepareVoteResource\x12\x11\n\tcreate_at\x18\x04 \x01(\x04\x12\x0c\n\x04sign\x18\x05 \x01(\x0c\"n\n\x10\x43onfirmVoteState\x12$\n\nmsg_option\x18\x01 \x01(\x0b\x32\x10.types.MsgOption\x12\x13\n\x0bvote_option\x18\x02 \x01(\r\x12\x11\n\tcreate_at\x18\x03 \x01(\x04\x12\x0c\n\x04sign\x18\x04 \x01(\x0c\x42-Z+github.com/RosettaFlow/Carrier-Go/lib/typesb\x06proto3'
  ,
  dependencies=[lib_dot_common_dot_base__pb2.DESCRIPTOR,])




_ORGPROPOSALSTATE = _descriptor.Descriptor(
  name='OrgProposalState',
  full_name='types.OrgProposalState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pre_period_start_time', full_name='types.OrgProposalState.pre_period_start_time', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period_start_time', full_name='types.OrgProposalState.period_start_time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deadline_duration', full_name='types.OrgProposalState.deadline_duration', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='types.OrgProposalState.create_at', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_role', full_name='types.OrgProposalState.task_role', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_org', full_name='types.OrgProposalState.task_org', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period_num', full_name='types.OrgProposalState.period_num', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='types.OrgProposalState.task_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_sender', full_name='types.OrgProposalState.task_sender', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=65,
  serialized_end=370,
)


_PREPAREVOTERESOURCE = _descriptor.Descriptor(
  name='PrepareVoteResource',
  full_name='types.PrepareVoteResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='types.PrepareVoteResource.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='types.PrepareVoteResource.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='types.PrepareVoteResource.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='party_id', full_name='types.PrepareVoteResource.party_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=372,
  serialized_end=449,
)


_MSGOPTION = _descriptor.Descriptor(
  name='MsgOption',
  full_name='types.MsgOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender_role', full_name='types.MsgOption.sender_role', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender_party_id', full_name='types.MsgOption.sender_party_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver_role', full_name='types.MsgOption.receiver_role', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver_party_id', full_name='types.MsgOption.receiver_party_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='types.MsgOption.owner', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=452,
  serialized_end=654,
)


_PREPAREVOTESTATE = _descriptor.Descriptor(
  name='PrepareVoteState',
  full_name='types.PrepareVoteState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_option', full_name='types.PrepareVoteState.msg_option', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_option', full_name='types.PrepareVoteState.vote_option', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer_info', full_name='types.PrepareVoteState.peer_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='types.PrepareVoteState.create_at', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sign', full_name='types.PrepareVoteState.sign', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=657,
  serialized_end=814,
)


_CONFIRMVOTESTATE = _descriptor.Descriptor(
  name='ConfirmVoteState',
  full_name='types.ConfirmVoteState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_option', full_name='types.ConfirmVoteState.msg_option', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_option', full_name='types.ConfirmVoteState.vote_option', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='types.ConfirmVoteState.create_at', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sign', full_name='types.ConfirmVoteState.sign', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=816,
  serialized_end=926,
)

_ORGPROPOSALSTATE.fields_by_name['task_role'].enum_type = lib_dot_common_dot_base__pb2._TASKROLE
_ORGPROPOSALSTATE.fields_by_name['task_org'].message_type = lib_dot_common_dot_base__pb2._TASKORGANIZATION
_ORGPROPOSALSTATE.fields_by_name['task_sender'].message_type = lib_dot_common_dot_base__pb2._TASKORGANIZATION
_MSGOPTION.fields_by_name['sender_role'].enum_type = lib_dot_common_dot_base__pb2._TASKROLE
_MSGOPTION.fields_by_name['receiver_role'].enum_type = lib_dot_common_dot_base__pb2._TASKROLE
_MSGOPTION.fields_by_name['owner'].message_type = lib_dot_common_dot_base__pb2._TASKORGANIZATION
_PREPAREVOTESTATE.fields_by_name['msg_option'].message_type = _MSGOPTION
_PREPAREVOTESTATE.fields_by_name['peer_info'].message_type = _PREPAREVOTERESOURCE
_CONFIRMVOTESTATE.fields_by_name['msg_option'].message_type = _MSGOPTION
DESCRIPTOR.message_types_by_name['OrgProposalState'] = _ORGPROPOSALSTATE
DESCRIPTOR.message_types_by_name['PrepareVoteResource'] = _PREPAREVOTERESOURCE
DESCRIPTOR.message_types_by_name['MsgOption'] = _MSGOPTION
DESCRIPTOR.message_types_by_name['PrepareVoteState'] = _PREPAREVOTESTATE
DESCRIPTOR.message_types_by_name['ConfirmVoteState'] = _CONFIRMVOTESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrgProposalState = _reflection.GeneratedProtocolMessageType('OrgProposalState', (_message.Message,), {
  'DESCRIPTOR' : _ORGPROPOSALSTATE,
  '__module__' : 'lib.types.consensusstate_pb2'
  # @@protoc_insertion_point(class_scope:types.OrgProposalState)
  })
_sym_db.RegisterMessage(OrgProposalState)

PrepareVoteResource = _reflection.GeneratedProtocolMessageType('PrepareVoteResource', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREVOTERESOURCE,
  '__module__' : 'lib.types.consensusstate_pb2'
  # @@protoc_insertion_point(class_scope:types.PrepareVoteResource)
  })
_sym_db.RegisterMessage(PrepareVoteResource)

MsgOption = _reflection.GeneratedProtocolMessageType('MsgOption', (_message.Message,), {
  'DESCRIPTOR' : _MSGOPTION,
  '__module__' : 'lib.types.consensusstate_pb2'
  # @@protoc_insertion_point(class_scope:types.MsgOption)
  })
_sym_db.RegisterMessage(MsgOption)

PrepareVoteState = _reflection.GeneratedProtocolMessageType('PrepareVoteState', (_message.Message,), {
  'DESCRIPTOR' : _PREPAREVOTESTATE,
  '__module__' : 'lib.types.consensusstate_pb2'
  # @@protoc_insertion_point(class_scope:types.PrepareVoteState)
  })
_sym_db.RegisterMessage(PrepareVoteState)

ConfirmVoteState = _reflection.GeneratedProtocolMessageType('ConfirmVoteState', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMVOTESTATE,
  '__module__' : 'lib.types.consensusstate_pb2'
  # @@protoc_insertion_point(class_scope:types.ConfirmVoteState)
  })
_sym_db.RegisterMessage(ConfirmVoteState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)