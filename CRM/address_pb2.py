# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: address.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\raddress.proto\x12\x04main\"/\n\x0eServiceRequest\x12\r\n\x05house\x18\x01 \x01(\t\x12\x0e\n\x06street\x18\x02 \x01(\t\"(\n\x0fServiceResponse\x12\x15\n\requipment_url\x18\x01 \x01(\t2;\n\x03NRI\x12\x34\n\x05\x43heck\x12\x14.main.ServiceRequest\x1a\x15.main.ServiceResponseB\"Z github.com/NRI.service/pkg/pb;pbb\x06proto3')



_SERVICEREQUEST = DESCRIPTOR.message_types_by_name['ServiceRequest']
_SERVICERESPONSE = DESCRIPTOR.message_types_by_name['ServiceResponse']
ServiceRequest = _reflection.GeneratedProtocolMessageType('ServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEREQUEST,
  '__module__' : 'address_pb2'
  # @@protoc_insertion_point(class_scope:main.ServiceRequest)
  })
_sym_db.RegisterMessage(ServiceRequest)

ServiceResponse = _reflection.GeneratedProtocolMessageType('ServiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVICERESPONSE,
  '__module__' : 'address_pb2'
  # @@protoc_insertion_point(class_scope:main.ServiceResponse)
  })
_sym_db.RegisterMessage(ServiceResponse)

_NRI = DESCRIPTOR.services_by_name['NRI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z github.com/NRI.service/pkg/pb;pb'
  _SERVICEREQUEST._serialized_start=23
  _SERVICEREQUEST._serialized_end=70
  _SERVICERESPONSE._serialized_start=72
  _SERVICERESPONSE._serialized_end=112
  _NRI._serialized_start=114
  _NRI._serialized_end=173
# @@protoc_insertion_point(module_scope)
