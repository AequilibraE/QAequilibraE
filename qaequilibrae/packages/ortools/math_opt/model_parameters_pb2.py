# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/math_opt/model_parameters.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ortools.math_opt import solution_pb2 as ortools_dot_math__opt_dot_solution__pb2
from ortools.math_opt import sparse_containers_pb2 as ortools_dot_math__opt_dot_sparse__containers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ortools/math_opt/model_parameters.proto\x12\x1coperations_research.math_opt\x1a\x1fortools/math_opt/solution.proto\x1a(ortools/math_opt/sparse_containers.proto\"\xaf\x01\n\x11SolutionHintProto\x12N\n\x0fvariable_values\x18\x01 \x01(\x0b\x32\x35.operations_research.math_opt.SparseDoubleVectorProto\x12J\n\x0b\x64ual_values\x18\x02 \x01(\x0b\x32\x35.operations_research.math_opt.SparseDoubleVectorProto\"\xe2\x01\n\x18ObjectiveParametersProto\x12\x35\n(objective_degradation_absolute_tolerance\x18\x07 \x01(\x01H\x00\x88\x01\x01\x12\x35\n(objective_degradation_relative_tolerance\x18\x08 \x01(\x01H\x01\x88\x01\x01\x42+\n)_objective_degradation_absolute_toleranceB+\n)_objective_degradation_relative_tolerance\"\xfb\x06\n\x19ModelSolveParametersProto\x12U\n\x16variable_values_filter\x18\x01 \x01(\x0b\x32\x35.operations_research.math_opt.SparseVectorFilterProto\x12Q\n\x12\x64ual_values_filter\x18\x02 \x01(\x0b\x32\x35.operations_research.math_opt.SparseVectorFilterProto\x12S\n\x14reduced_costs_filter\x18\x03 \x01(\x0b\x32\x35.operations_research.math_opt.SparseVectorFilterProto\x12?\n\rinitial_basis\x18\x04 \x01(\x0b\x32(.operations_research.math_opt.BasisProto\x12G\n\x0esolution_hints\x18\x05 \x03(\x0b\x32/.operations_research.math_opt.SolutionHintProto\x12R\n\x14\x62ranching_priorities\x18\x06 \x01(\x0b\x32\x34.operations_research.math_opt.SparseInt32VectorProto\x12\\\n\x1cprimary_objective_parameters\x18\x07 \x01(\x0b\x32\x36.operations_research.math_opt.ObjectiveParametersProto\x12\x81\x01\n\x1e\x61uxiliary_objective_parameters\x18\x08 \x03(\x0b\x32Y.operations_research.math_opt.ModelSolveParametersProto.AuxiliaryObjectiveParametersEntry\x12\"\n\x1alazy_linear_constraint_ids\x18\t \x03(\x03\x1a{\n!AuxiliaryObjectiveParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x45\n\x05value\x18\x02 \x01(\x0b\x32\x36.operations_research.math_opt.ObjectiveParametersProto:\x02\x38\x01\x42\x1e\n\x1a\x63om.google.ortools.mathoptP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.math_opt.model_parameters_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.google.ortools.mathoptP\001'
  _globals['_MODELSOLVEPARAMETERSPROTO_AUXILIARYOBJECTIVEPARAMETERSENTRY']._loaded_options = None
  _globals['_MODELSOLVEPARAMETERSPROTO_AUXILIARYOBJECTIVEPARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_SOLUTIONHINTPROTO']._serialized_start=149
  _globals['_SOLUTIONHINTPROTO']._serialized_end=324
  _globals['_OBJECTIVEPARAMETERSPROTO']._serialized_start=327
  _globals['_OBJECTIVEPARAMETERSPROTO']._serialized_end=553
  _globals['_MODELSOLVEPARAMETERSPROTO']._serialized_start=556
  _globals['_MODELSOLVEPARAMETERSPROTO']._serialized_end=1447
  _globals['_MODELSOLVEPARAMETERSPROTO_AUXILIARYOBJECTIVEPARAMETERSENTRY']._serialized_start=1324
  _globals['_MODELSOLVEPARAMETERSPROTO_AUXILIARYOBJECTIVEPARAMETERSENTRY']._serialized_end=1447
# @@protoc_insertion_point(module_scope)
