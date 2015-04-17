# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sqlInput.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sqlInput.proto',
  package='knime',
  serialized_pb='\n\x0esqlInput.proto\x12\x05knime\"\xdc\x01\n\x08SQLInput\x12\x0e\n\x06\x64river\x18\x01 \x02(\t\x12\x0f\n\x07JDBCUrl\x18\x02 \x02(\t\x12\x10\n\x08userName\x18\x03 \x02(\t\x12\x10\n\x08password\x18\x04 \x02(\t\x12\r\n\x05query\x18\x05 \x02(\t\x12\x14\n\x0c\x64\x62Identifier\x18\x06 \x02(\t\x12\x19\n\x11\x63onnectionTimeout\x18\x07 \x02(\x05\x12\x12\n\nautocommit\x18\x08 \x02(\x08\x12\x10\n\x08timezone\x18\t \x02(\t\x12\x0c\n\x04jars\x18\n \x03(\t\x12\x17\n\x0fidentifierQuote\x18\x0b \x02(\tB6\n\x1dorg.knime.python.kernel.protoB\x15ProtobufKnimeSQLInput')




_SQLINPUT = _descriptor.Descriptor(
  name='SQLInput',
  full_name='knime.SQLInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver', full_name='knime.SQLInput.driver', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JDBCUrl', full_name='knime.SQLInput.JDBCUrl', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userName', full_name='knime.SQLInput.userName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='knime.SQLInput.password', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query', full_name='knime.SQLInput.query', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbIdentifier', full_name='knime.SQLInput.dbIdentifier', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connectionTimeout', full_name='knime.SQLInput.connectionTimeout', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='autocommit', full_name='knime.SQLInput.autocommit', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='knime.SQLInput.timezone', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jars', full_name='knime.SQLInput.jars', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifierQuote', full_name='knime.SQLInput.identifierQuote', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=26,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['SQLInput'] = _SQLINPUT

class SQLInput(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SQLINPUT

  # @@protoc_insertion_point(class_scope:knime.SQLInput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\035org.knime.python.kernel.protoB\025ProtobufKnimeSQLInput')
# @@protoc_insertion_point(module_scope)
