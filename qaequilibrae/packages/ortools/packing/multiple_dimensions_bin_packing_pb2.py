# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/packing/multiple_dimensions_bin_packing.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5ortools/packing/multiple_dimensions_bin_packing.proto\x12\x1boperations_research.packing\"7\n!MultipleDimensionsBinPackingShape\x12\x12\n\ndimensions\x18\x01 \x03(\x03\"\x81\x01\n MultipleDimensionsBinPackingItem\x12N\n\x06shapes\x18\x01 \x03(\x0b\x32>.operations_research.packing.MultipleDimensionsBinPackingShape\x12\r\n\x05value\x18\x02 \x01(\x03\"\xc6\x01\n#MultipleDimensionsBinPackingProblem\x12Q\n\tbox_shape\x18\x01 \x01(\x0b\x32>.operations_research.packing.MultipleDimensionsBinPackingShape\x12L\n\x05items\x18\x02 \x03(\x0b\x32=.operations_research.packing.MultipleDimensionsBinPackingItemB\x02P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.packing.multiple_dimensions_bin_packing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'P\001'
  _globals['_MULTIPLEDIMENSIONSBINPACKINGSHAPE']._serialized_start=86
  _globals['_MULTIPLEDIMENSIONSBINPACKINGSHAPE']._serialized_end=141
  _globals['_MULTIPLEDIMENSIONSBINPACKINGITEM']._serialized_start=144
  _globals['_MULTIPLEDIMENSIONSBINPACKINGITEM']._serialized_end=273
  _globals['_MULTIPLEDIMENSIONSBINPACKINGPROBLEM']._serialized_start=276
  _globals['_MULTIPLEDIMENSIONSBINPACKINGPROBLEM']._serialized_end=474
# @@protoc_insertion_point(module_scope)
