# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/math_opt/solvers/gurobi.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ortools/math_opt/solvers/gurobi.proto\x12\x1coperations_research.math_opt\"\xb9\x01\n\x16GurobiInitializerProto\x12L\n\x07isv_key\x18\x01 \x01(\x0b\x32;.operations_research.math_opt.GurobiInitializerProto.ISVKey\x1aQ\n\x06ISVKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x02 \x01(\t\x12\x12\n\nexpiration\x18\x03 \x01(\x05\x12\x0b\n\x03key\x18\x04 \x01(\t\"\x94\x01\n\x15GurobiParametersProto\x12Q\n\nparameters\x18\x01 \x03(\x0b\x32=.operations_research.math_opt.GurobiParametersProto.Parameter\x1a(\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.math_opt.solvers.gurobi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GUROBIINITIALIZERPROTO']._serialized_start=72
  _globals['_GUROBIINITIALIZERPROTO']._serialized_end=257
  _globals['_GUROBIINITIALIZERPROTO_ISVKEY']._serialized_start=176
  _globals['_GUROBIINITIALIZERPROTO_ISVKEY']._serialized_end=257
  _globals['_GUROBIPARAMETERSPROTO']._serialized_start=260
  _globals['_GUROBIPARAMETERSPROTO']._serialized_end=408
  _globals['_GUROBIPARAMETERSPROTO_PARAMETER']._serialized_start=368
  _globals['_GUROBIPARAMETERSPROTO_PARAMETER']._serialized_end=408
# @@protoc_insertion_point(module_scope)
