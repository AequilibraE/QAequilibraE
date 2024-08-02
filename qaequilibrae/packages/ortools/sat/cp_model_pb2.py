# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ortools/sat/cp_model.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aortools/sat/cp_model.proto\x12\x17operations_research.sat\"4\n\x14IntegerVariableProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x03(\x03\"%\n\x11\x42oolArgumentProto\x12\x10\n\x08literals\x18\x01 \x03(\x05\"E\n\x15LinearExpressionProto\x12\x0c\n\x04vars\x18\x01 \x03(\x05\x12\x0e\n\x06\x63oeffs\x18\x02 \x03(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\"\x94\x01\n\x13LinearArgumentProto\x12>\n\x06target\x18\x01 \x01(\x0b\x32..operations_research.sat.LinearExpressionProto\x12=\n\x05\x65xprs\x18\x02 \x03(\x0b\x32..operations_research.sat.LinearExpressionProto\"\\\n\x1b\x41llDifferentConstraintProto\x12=\n\x05\x65xprs\x18\x01 \x03(\x0b\x32..operations_research.sat.LinearExpressionProto\"E\n\x15LinearConstraintProto\x12\x0c\n\x04vars\x18\x01 \x03(\x05\x12\x0e\n\x06\x63oeffs\x18\x02 \x03(\x03\x12\x0e\n\x06\x64omain\x18\x03 \x03(\x03\"E\n\x16\x45lementConstraintProto\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0e\n\x06target\x18\x02 \x01(\x05\x12\x0c\n\x04vars\x18\x03 \x03(\x05\"\xd3\x01\n\x17IntervalConstraintProto\x12=\n\x05start\x18\x04 \x01(\x0b\x32..operations_research.sat.LinearExpressionProto\x12;\n\x03\x65nd\x18\x05 \x01(\x0b\x32..operations_research.sat.LinearExpressionProto\x12<\n\x04size\x18\x06 \x01(\x0b\x32..operations_research.sat.LinearExpressionProto\"-\n\x18NoOverlapConstraintProto\x12\x11\n\tintervals\x18\x01 \x03(\x05\"F\n\x1aNoOverlap2DConstraintProto\x12\x13\n\x0bx_intervals\x18\x01 \x03(\x05\x12\x13\n\x0by_intervals\x18\x02 \x03(\x05\"\xb1\x01\n\x19\x43umulativeConstraintProto\x12@\n\x08\x63\x61pacity\x18\x01 \x01(\x0b\x32..operations_research.sat.LinearExpressionProto\x12\x11\n\tintervals\x18\x02 \x03(\x05\x12?\n\x07\x64\x65mands\x18\x03 \x03(\x0b\x32..operations_research.sat.LinearExpressionProto\"\xea\x01\n\x18ReservoirConstraintProto\x12\x11\n\tmin_level\x18\x01 \x01(\x03\x12\x11\n\tmax_level\x18\x02 \x01(\x03\x12\x42\n\ntime_exprs\x18\x03 \x03(\x0b\x32..operations_research.sat.LinearExpressionProto\x12\x45\n\rlevel_changes\x18\x06 \x03(\x0b\x32..operations_research.sat.LinearExpressionProto\x12\x17\n\x0f\x61\x63tive_literals\x18\x05 \x03(\x05J\x04\x08\x04\x10\x05\"H\n\x16\x43ircuitConstraintProto\x12\r\n\x05tails\x18\x03 \x03(\x05\x12\r\n\x05heads\x18\x04 \x03(\x05\x12\x10\n\x08literals\x18\x05 \x03(\x05\"j\n\x15RoutesConstraintProto\x12\r\n\x05tails\x18\x01 \x03(\x05\x12\r\n\x05heads\x18\x02 \x03(\x05\x12\x10\n\x08literals\x18\x03 \x03(\x05\x12\x0f\n\x07\x64\x65mands\x18\x04 \x03(\x05\x12\x10\n\x08\x63\x61pacity\x18\x05 \x01(\x03\"E\n\x14TableConstraintProto\x12\x0c\n\x04vars\x18\x01 \x03(\x05\x12\x0e\n\x06values\x18\x02 \x03(\x03\x12\x0f\n\x07negated\x18\x03 \x01(\x08\"=\n\x16InverseConstraintProto\x12\x10\n\x08\x66_direct\x18\x01 \x03(\x05\x12\x11\n\tf_inverse\x18\x02 \x03(\x05\"\xa2\x01\n\x18\x41utomatonConstraintProto\x12\x16\n\x0estarting_state\x18\x02 \x01(\x03\x12\x14\n\x0c\x66inal_states\x18\x03 \x03(\x03\x12\x17\n\x0ftransition_tail\x18\x04 \x03(\x03\x12\x17\n\x0ftransition_head\x18\x05 \x03(\x03\x12\x18\n\x10transition_label\x18\x06 \x03(\x03\x12\x0c\n\x04vars\x18\x07 \x03(\x05\"$\n\x14ListOfVariablesProto\x12\x0c\n\x04vars\x18\x01 \x03(\x05\"\xf0\x0c\n\x0f\x43onstraintProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x13\x65nforcement_literal\x18\x02 \x03(\x05\x12=\n\x07\x62ool_or\x18\x03 \x01(\x0b\x32*.operations_research.sat.BoolArgumentProtoH\x00\x12>\n\x08\x62ool_and\x18\x04 \x01(\x0b\x32*.operations_research.sat.BoolArgumentProtoH\x00\x12\x41\n\x0b\x61t_most_one\x18\x1a \x01(\x0b\x32*.operations_research.sat.BoolArgumentProtoH\x00\x12\x41\n\x0b\x65xactly_one\x18\x1d \x01(\x0b\x32*.operations_research.sat.BoolArgumentProtoH\x00\x12>\n\x08\x62ool_xor\x18\x05 \x01(\x0b\x32*.operations_research.sat.BoolArgumentProtoH\x00\x12?\n\x07int_div\x18\x07 \x01(\x0b\x32,.operations_research.sat.LinearArgumentProtoH\x00\x12?\n\x07int_mod\x18\x08 \x01(\x0b\x32,.operations_research.sat.LinearArgumentProtoH\x00\x12@\n\x08int_prod\x18\x0b \x01(\x0b\x32,.operations_research.sat.LinearArgumentProtoH\x00\x12?\n\x07lin_max\x18\x1b \x01(\x0b\x32,.operations_research.sat.LinearArgumentProtoH\x00\x12@\n\x06linear\x18\x0c \x01(\x0b\x32..operations_research.sat.LinearConstraintProtoH\x00\x12H\n\x08\x61ll_diff\x18\r \x01(\x0b\x32\x34.operations_research.sat.AllDifferentConstraintProtoH\x00\x12\x42\n\x07\x65lement\x18\x0e \x01(\x0b\x32/.operations_research.sat.ElementConstraintProtoH\x00\x12\x42\n\x07\x63ircuit\x18\x0f \x01(\x0b\x32/.operations_research.sat.CircuitConstraintProtoH\x00\x12@\n\x06routes\x18\x17 \x01(\x0b\x32..operations_research.sat.RoutesConstraintProtoH\x00\x12>\n\x05table\x18\x10 \x01(\x0b\x32-.operations_research.sat.TableConstraintProtoH\x00\x12\x46\n\tautomaton\x18\x11 \x01(\x0b\x32\x31.operations_research.sat.AutomatonConstraintProtoH\x00\x12\x42\n\x07inverse\x18\x12 \x01(\x0b\x32/.operations_research.sat.InverseConstraintProtoH\x00\x12\x46\n\treservoir\x18\x18 \x01(\x0b\x32\x31.operations_research.sat.ReservoirConstraintProtoH\x00\x12\x44\n\x08interval\x18\x13 \x01(\x0b\x32\x30.operations_research.sat.IntervalConstraintProtoH\x00\x12G\n\nno_overlap\x18\x14 \x01(\x0b\x32\x31.operations_research.sat.NoOverlapConstraintProtoH\x00\x12L\n\rno_overlap_2d\x18\x15 \x01(\x0b\x32\x33.operations_research.sat.NoOverlap2DConstraintProtoH\x00\x12H\n\ncumulative\x18\x16 \x01(\x0b\x32\x32.operations_research.sat.CumulativeConstraintProtoH\x00\x12I\n\x10\x64ummy_constraint\x18\x1e \x01(\x0b\x32-.operations_research.sat.ListOfVariablesProtoH\x00\x42\x0c\n\nconstraint\"\xe0\x01\n\x10\x43pObjectiveProto\x12\x0c\n\x04vars\x18\x01 \x03(\x05\x12\x0e\n\x06\x63oeffs\x18\x04 \x03(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x01\x12\x16\n\x0escaling_factor\x18\x03 \x01(\x01\x12\x0e\n\x06\x64omain\x18\x05 \x03(\x03\x12\x19\n\x11scaling_was_exact\x18\x06 \x01(\x08\x12\x1d\n\x15integer_before_offset\x18\x07 \x01(\x03\x12\x1c\n\x14integer_after_offset\x18\t \x01(\x03\x12\x1e\n\x16integer_scaling_factor\x18\x08 \x01(\x03\"U\n\x13\x46loatObjectiveProto\x12\x0c\n\x04vars\x18\x01 \x03(\x05\x12\x0e\n\x06\x63oeffs\x18\x02 \x03(\x01\x12\x0e\n\x06offset\x18\x03 \x01(\x01\x12\x10\n\x08maximize\x18\x04 \x01(\x08\"\xe9\x04\n\x15\x44\x65\x63isionStrategyProto\x12\x11\n\tvariables\x18\x01 \x03(\x05\x12=\n\x05\x65xprs\x18\x05 \x03(\x0b\x32..operations_research.sat.LinearExpressionProto\x12m\n\x1bvariable_selection_strategy\x18\x02 \x01(\x0e\x32H.operations_research.sat.DecisionStrategyProto.VariableSelectionStrategy\x12i\n\x19\x64omain_reduction_strategy\x18\x03 \x01(\x0e\x32\x46.operations_research.sat.DecisionStrategyProto.DomainReductionStrategy\"\x94\x01\n\x19VariableSelectionStrategy\x12\x10\n\x0c\x43HOOSE_FIRST\x10\x00\x12\x15\n\x11\x43HOOSE_LOWEST_MIN\x10\x01\x12\x16\n\x12\x43HOOSE_HIGHEST_MAX\x10\x02\x12\x1a\n\x16\x43HOOSE_MIN_DOMAIN_SIZE\x10\x03\x12\x1a\n\x16\x43HOOSE_MAX_DOMAIN_SIZE\x10\x04\"\x8c\x01\n\x17\x44omainReductionStrategy\x12\x14\n\x10SELECT_MIN_VALUE\x10\x00\x12\x14\n\x10SELECT_MAX_VALUE\x10\x01\x12\x15\n\x11SELECT_LOWER_HALF\x10\x02\x12\x15\n\x11SELECT_UPPER_HALF\x10\x03\x12\x17\n\x13SELECT_MEDIAN_VALUE\x10\x04\"9\n\x19PartialVariableAssignment\x12\x0c\n\x04vars\x18\x01 \x03(\x05\x12\x0e\n\x06values\x18\x02 \x03(\x03\">\n\x16SparsePermutationProto\x12\x0f\n\x07support\x18\x01 \x03(\x05\x12\x13\n\x0b\x63ycle_sizes\x18\x02 \x03(\x05\"G\n\x10\x44\x65nseMatrixProto\x12\x10\n\x08num_rows\x18\x01 \x01(\x05\x12\x10\n\x08num_cols\x18\x02 \x01(\x05\x12\x0f\n\x07\x65ntries\x18\x03 \x03(\x05\"\x94\x01\n\rSymmetryProto\x12\x45\n\x0cpermutations\x18\x01 \x03(\x0b\x32/.operations_research.sat.SparsePermutationProto\x12<\n\torbitopes\x18\x02 \x03(\x0b\x32).operations_research.sat.DenseMatrixProto\"\x8e\x04\n\x0c\x43pModelProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\tvariables\x18\x02 \x03(\x0b\x32-.operations_research.sat.IntegerVariableProto\x12=\n\x0b\x63onstraints\x18\x03 \x03(\x0b\x32(.operations_research.sat.ConstraintProto\x12<\n\tobjective\x18\x04 \x01(\x0b\x32).operations_research.sat.CpObjectiveProto\x12N\n\x18\x66loating_point_objective\x18\t \x01(\x0b\x32,.operations_research.sat.FloatObjectiveProto\x12G\n\x0fsearch_strategy\x18\x05 \x03(\x0b\x32..operations_research.sat.DecisionStrategyProto\x12I\n\rsolution_hint\x18\x06 \x01(\x0b\x32\x32.operations_research.sat.PartialVariableAssignment\x12\x13\n\x0b\x61ssumptions\x18\x07 \x03(\x05\x12\x38\n\x08symmetry\x18\x08 \x01(\x0b\x32&.operations_research.sat.SymmetryProto\"\"\n\x10\x43pSolverSolution\x12\x0e\n\x06values\x18\x01 \x03(\x03\"\x95\x06\n\x10\x43pSolverResponse\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.operations_research.sat.CpSolverStatus\x12\x10\n\x08solution\x18\x02 \x03(\x03\x12\x17\n\x0fobjective_value\x18\x03 \x01(\x01\x12\x1c\n\x14\x62\x65st_objective_bound\x18\x04 \x01(\x01\x12G\n\x14\x61\x64\x64itional_solutions\x18\x1b \x03(\x0b\x32).operations_research.sat.CpSolverSolution\x12J\n\x13tightened_variables\x18\x15 \x03(\x0b\x32-.operations_research.sat.IntegerVariableProto\x12\x30\n(sufficient_assumptions_for_infeasibility\x18\x17 \x03(\x05\x12\x44\n\x11integer_objective\x18\x1c \x01(\x0b\x32).operations_research.sat.CpObjectiveProto\x12#\n\x1binner_objective_lower_bound\x18\x1d \x01(\x03\x12\x14\n\x0cnum_integers\x18\x1e \x01(\x03\x12\x14\n\x0cnum_booleans\x18\n \x01(\x03\x12\x15\n\rnum_conflicts\x18\x0b \x01(\x03\x12\x14\n\x0cnum_branches\x18\x0c \x01(\x03\x12\x1f\n\x17num_binary_propagations\x18\r \x01(\x03\x12 \n\x18num_integer_propagations\x18\x0e \x01(\x03\x12\x14\n\x0cnum_restarts\x18\x18 \x01(\x03\x12\x19\n\x11num_lp_iterations\x18\x19 \x01(\x03\x12\x11\n\twall_time\x18\x0f \x01(\x01\x12\x11\n\tuser_time\x18\x10 \x01(\x01\x12\x1a\n\x12\x64\x65terministic_time\x18\x11 \x01(\x01\x12\x14\n\x0cgap_integral\x18\x16 \x01(\x01\x12\x15\n\rsolution_info\x18\x14 \x01(\t\x12\x11\n\tsolve_log\x18\x1a \x01(\t*[\n\x0e\x43pSolverStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rMODEL_INVALID\x10\x01\x12\x0c\n\x08\x46\x45\x41SIBLE\x10\x02\x12\x0e\n\nINFEASIBLE\x10\x03\x12\x0b\n\x07OPTIMAL\x10\x04\x42@\n\x16\x63om.google.ortools.satB\x0f\x43pModelProtobufP\x01\xaa\x02\x12Google.OrTools.Satb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ortools.sat.cp_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.google.ortools.satB\017CpModelProtobufP\001\252\002\022Google.OrTools.Sat'
  _globals['_CPSOLVERSTATUS']._serialized_start=6164
  _globals['_CPSOLVERSTATUS']._serialized_end=6255
  _globals['_INTEGERVARIABLEPROTO']._serialized_start=55
  _globals['_INTEGERVARIABLEPROTO']._serialized_end=107
  _globals['_BOOLARGUMENTPROTO']._serialized_start=109
  _globals['_BOOLARGUMENTPROTO']._serialized_end=146
  _globals['_LINEAREXPRESSIONPROTO']._serialized_start=148
  _globals['_LINEAREXPRESSIONPROTO']._serialized_end=217
  _globals['_LINEARARGUMENTPROTO']._serialized_start=220
  _globals['_LINEARARGUMENTPROTO']._serialized_end=368
  _globals['_ALLDIFFERENTCONSTRAINTPROTO']._serialized_start=370
  _globals['_ALLDIFFERENTCONSTRAINTPROTO']._serialized_end=462
  _globals['_LINEARCONSTRAINTPROTO']._serialized_start=464
  _globals['_LINEARCONSTRAINTPROTO']._serialized_end=533
  _globals['_ELEMENTCONSTRAINTPROTO']._serialized_start=535
  _globals['_ELEMENTCONSTRAINTPROTO']._serialized_end=604
  _globals['_INTERVALCONSTRAINTPROTO']._serialized_start=607
  _globals['_INTERVALCONSTRAINTPROTO']._serialized_end=818
  _globals['_NOOVERLAPCONSTRAINTPROTO']._serialized_start=820
  _globals['_NOOVERLAPCONSTRAINTPROTO']._serialized_end=865
  _globals['_NOOVERLAP2DCONSTRAINTPROTO']._serialized_start=867
  _globals['_NOOVERLAP2DCONSTRAINTPROTO']._serialized_end=937
  _globals['_CUMULATIVECONSTRAINTPROTO']._serialized_start=940
  _globals['_CUMULATIVECONSTRAINTPROTO']._serialized_end=1117
  _globals['_RESERVOIRCONSTRAINTPROTO']._serialized_start=1120
  _globals['_RESERVOIRCONSTRAINTPROTO']._serialized_end=1354
  _globals['_CIRCUITCONSTRAINTPROTO']._serialized_start=1356
  _globals['_CIRCUITCONSTRAINTPROTO']._serialized_end=1428
  _globals['_ROUTESCONSTRAINTPROTO']._serialized_start=1430
  _globals['_ROUTESCONSTRAINTPROTO']._serialized_end=1536
  _globals['_TABLECONSTRAINTPROTO']._serialized_start=1538
  _globals['_TABLECONSTRAINTPROTO']._serialized_end=1607
  _globals['_INVERSECONSTRAINTPROTO']._serialized_start=1609
  _globals['_INVERSECONSTRAINTPROTO']._serialized_end=1670
  _globals['_AUTOMATONCONSTRAINTPROTO']._serialized_start=1673
  _globals['_AUTOMATONCONSTRAINTPROTO']._serialized_end=1835
  _globals['_LISTOFVARIABLESPROTO']._serialized_start=1837
  _globals['_LISTOFVARIABLESPROTO']._serialized_end=1873
  _globals['_CONSTRAINTPROTO']._serialized_start=1876
  _globals['_CONSTRAINTPROTO']._serialized_end=3524
  _globals['_CPOBJECTIVEPROTO']._serialized_start=3527
  _globals['_CPOBJECTIVEPROTO']._serialized_end=3751
  _globals['_FLOATOBJECTIVEPROTO']._serialized_start=3753
  _globals['_FLOATOBJECTIVEPROTO']._serialized_end=3838
  _globals['_DECISIONSTRATEGYPROTO']._serialized_start=3841
  _globals['_DECISIONSTRATEGYPROTO']._serialized_end=4458
  _globals['_DECISIONSTRATEGYPROTO_VARIABLESELECTIONSTRATEGY']._serialized_start=4167
  _globals['_DECISIONSTRATEGYPROTO_VARIABLESELECTIONSTRATEGY']._serialized_end=4315
  _globals['_DECISIONSTRATEGYPROTO_DOMAINREDUCTIONSTRATEGY']._serialized_start=4318
  _globals['_DECISIONSTRATEGYPROTO_DOMAINREDUCTIONSTRATEGY']._serialized_end=4458
  _globals['_PARTIALVARIABLEASSIGNMENT']._serialized_start=4460
  _globals['_PARTIALVARIABLEASSIGNMENT']._serialized_end=4517
  _globals['_SPARSEPERMUTATIONPROTO']._serialized_start=4519
  _globals['_SPARSEPERMUTATIONPROTO']._serialized_end=4581
  _globals['_DENSEMATRIXPROTO']._serialized_start=4583
  _globals['_DENSEMATRIXPROTO']._serialized_end=4654
  _globals['_SYMMETRYPROTO']._serialized_start=4657
  _globals['_SYMMETRYPROTO']._serialized_end=4805
  _globals['_CPMODELPROTO']._serialized_start=4808
  _globals['_CPMODELPROTO']._serialized_end=5334
  _globals['_CPSOLVERSOLUTION']._serialized_start=5336
  _globals['_CPSOLVERSOLUTION']._serialized_end=5370
  _globals['_CPSOLVERRESPONSE']._serialized_start=5373
  _globals['_CPSOLVERRESPONSE']._serialized_end=6162
# @@protoc_insertion_point(module_scope)
