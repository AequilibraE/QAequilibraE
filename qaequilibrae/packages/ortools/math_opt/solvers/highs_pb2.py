# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/math_opt/solvers/highs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$ortools/math_opt/solvers/highs.proto\x12\x1coperations_research.math_opt\"\xcc\x04\n\x11HighsOptionsProto\x12Z\n\x0estring_options\x18\x01 \x03(\x0b\x32\x42.operations_research.math_opt.HighsOptionsProto.StringOptionsEntry\x12Z\n\x0e\x64ouble_options\x18\x02 \x03(\x0b\x32\x42.operations_research.math_opt.HighsOptionsProto.DoubleOptionsEntry\x12T\n\x0bint_options\x18\x03 \x03(\x0b\x32?.operations_research.math_opt.HighsOptionsProto.IntOptionsEntry\x12V\n\x0c\x62ool_options\x18\x04 \x03(\x0b\x32@.operations_research.math_opt.HighsOptionsProto.BoolOptionsEntry\x1a\x34\n\x12StringOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x34\n\x12\x44oubleOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x31\n\x0fIntOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x32\n\x10\x42oolOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x42\x1e\n\x1a\x63om.google.ortools.mathoptP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.math_opt.solvers.highs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.google.ortools.mathoptP\001'
  _globals['_HIGHSOPTIONSPROTO_STRINGOPTIONSENTRY']._loaded_options = None
  _globals['_HIGHSOPTIONSPROTO_STRINGOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_HIGHSOPTIONSPROTO_DOUBLEOPTIONSENTRY']._loaded_options = None
  _globals['_HIGHSOPTIONSPROTO_DOUBLEOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_HIGHSOPTIONSPROTO_INTOPTIONSENTRY']._loaded_options = None
  _globals['_HIGHSOPTIONSPROTO_INTOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_HIGHSOPTIONSPROTO_BOOLOPTIONSENTRY']._loaded_options = None
  _globals['_HIGHSOPTIONSPROTO_BOOLOPTIONSENTRY']._serialized_options = b'8\001'
  _globals['_HIGHSOPTIONSPROTO']._serialized_start=71
  _globals['_HIGHSOPTIONSPROTO']._serialized_end=659
  _globals['_HIGHSOPTIONSPROTO_STRINGOPTIONSENTRY']._serialized_start=450
  _globals['_HIGHSOPTIONSPROTO_STRINGOPTIONSENTRY']._serialized_end=502
  _globals['_HIGHSOPTIONSPROTO_DOUBLEOPTIONSENTRY']._serialized_start=504
  _globals['_HIGHSOPTIONSPROTO_DOUBLEOPTIONSENTRY']._serialized_end=556
  _globals['_HIGHSOPTIONSPROTO_INTOPTIONSENTRY']._serialized_start=558
  _globals['_HIGHSOPTIONSPROTO_INTOPTIONSENTRY']._serialized_end=607
  _globals['_HIGHSOPTIONSPROTO_BOOLOPTIONSENTRY']._serialized_start=609
  _globals['_HIGHSOPTIONSPROTO_BOOLOPTIONSENTRY']._serialized_end=659
# @@protoc_insertion_point(module_scope)
