# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/scheduling/rcpsp.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eortools/scheduling/rcpsp.proto\x12$operations_research.scheduling.rcpsp\"\\\n\x08Resource\x12\x14\n\x0cmax_capacity\x18\x01 \x01(\x05\x12\x14\n\x0cmin_capacity\x18\x02 \x01(\x05\x12\x11\n\trenewable\x18\x03 \x01(\x08\x12\x11\n\tunit_cost\x18\x04 \x01(\x05\">\n\x06Recipe\x12\x10\n\x08\x64uration\x18\x01 \x01(\x05\x12\x0f\n\x07\x64\x65mands\x18\x02 \x03(\x05\x12\x11\n\tresources\x18\x03 \x03(\x05\"%\n\x0fPerRecipeDelays\x12\x12\n\nmin_delays\x18\x01 \x03(\x05\"b\n\x12PerSuccessorDelays\x12L\n\rrecipe_delays\x18\x01 \x03(\x0b\x32\x35.operations_research.scheduling.rcpsp.PerRecipeDelays\"\xad\x01\n\x04Task\x12\x12\n\nsuccessors\x18\x01 \x03(\x05\x12=\n\x07recipes\x18\x02 \x03(\x0b\x32,.operations_research.scheduling.rcpsp.Recipe\x12R\n\x10successor_delays\x18\x03 \x03(\x0b\x32\x38.operations_research.scheduling.rcpsp.PerSuccessorDelays\"\x83\x03\n\x0cRcpspProblem\x12\x41\n\tresources\x18\x01 \x03(\x0b\x32..operations_research.scheduling.rcpsp.Resource\x12\x39\n\x05tasks\x18\x02 \x03(\x0b\x32*.operations_research.scheduling.rcpsp.Task\x12\x1c\n\x14is_consumer_producer\x18\x03 \x01(\x08\x12\x1e\n\x16is_resource_investment\x18\x04 \x01(\x08\x12\x14\n\x0cis_rcpsp_max\x18\x05 \x01(\x08\x12\x10\n\x08\x64\x65\x61\x64line\x18\x06 \x01(\x05\x12\x0f\n\x07horizon\x18\x07 \x01(\x05\x12\x14\n\x0crelease_date\x18\x08 \x01(\x05\x12\x16\n\x0etardiness_cost\x18\t \x01(\x05\x12\x10\n\x08mpm_time\x18\n \x01(\x05\x12\x0c\n\x04seed\x18\x0b \x01(\x03\x12\x10\n\x08\x62\x61sedata\x18\x0c \x01(\t\x12\x10\n\x08\x64ue_date\x18\r \x01(\x05\x12\x0c\n\x04name\x18\x0e \x01(\t\"I\n\x0fRcpspAssignment\x12\x15\n\rstart_of_task\x18\x01 \x03(\x03\x12\x1f\n\x17selected_recipe_of_task\x18\x02 \x03(\x05\x42I\n#com.google.ortools.scheduling.rcpspP\x01\xaa\x02\x1fGoogle.OrTools.Scheduling.Rcpspb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.scheduling.rcpsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ortools.scheduling.rcpspP\001\252\002\037Google.OrTools.Scheduling.Rcpsp'
  _globals['_RESOURCE']._serialized_start=72
  _globals['_RESOURCE']._serialized_end=164
  _globals['_RECIPE']._serialized_start=166
  _globals['_RECIPE']._serialized_end=228
  _globals['_PERRECIPEDELAYS']._serialized_start=230
  _globals['_PERRECIPEDELAYS']._serialized_end=267
  _globals['_PERSUCCESSORDELAYS']._serialized_start=269
  _globals['_PERSUCCESSORDELAYS']._serialized_end=367
  _globals['_TASK']._serialized_start=370
  _globals['_TASK']._serialized_end=543
  _globals['_RCPSPPROBLEM']._serialized_start=546
  _globals['_RCPSPPROBLEM']._serialized_end=933
  _globals['_RCPSPASSIGNMENT']._serialized_start=935
  _globals['_RCPSPASSIGNMENT']._serialized_end=1008
# @@protoc_insertion_point(module_scope)
