# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lib/common/data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lib/common/data.proto',
  package='api.protobuf',
  syntax='proto3',
  serialized_options=b'Z,github.com/RosettaFlow/Carrier-Go/lib/common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15lib/common/data.proto\x12\x0c\x61pi.protobuf\"a\n\x17TaskResourceCostDeclare\x12\x0e\n\x06memory\x18\x01 \x01(\x04\x12\x11\n\tprocessor\x18\x02 \x01(\r\x12\x11\n\tbandwidth\x18\x03 \x01(\x04\x12\x10\n\x08\x64uration\x18\x04 \x01(\x04\x42.Z,github.com/RosettaFlow/Carrier-Go/lib/commonb\x06proto3'
)




_TASKRESOURCECOSTDECLARE = _descriptor.Descriptor(
  name='TaskResourceCostDeclare',
  full_name='api.protobuf.TaskResourceCostDeclare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='memory', full_name='api.protobuf.TaskResourceCostDeclare.memory', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processor', full_name='api.protobuf.TaskResourceCostDeclare.processor', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bandwidth', full_name='api.protobuf.TaskResourceCostDeclare.bandwidth', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='api.protobuf.TaskResourceCostDeclare.duration', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=39,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['TaskResourceCostDeclare'] = _TASKRESOURCECOSTDECLARE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskResourceCostDeclare = _reflection.GeneratedProtocolMessageType('TaskResourceCostDeclare', (_message.Message,), {
  'DESCRIPTOR' : _TASKRESOURCECOSTDECLARE,
  '__module__' : 'lib.common.data_pb2'
  # @@protoc_insertion_point(class_scope:api.protobuf.TaskResourceCostDeclare)
  })
_sym_db.RegisterMessage(TaskResourceCostDeclare)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
