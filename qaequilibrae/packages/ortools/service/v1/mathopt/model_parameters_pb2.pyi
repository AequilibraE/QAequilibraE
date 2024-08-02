"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Solve parameters that are specific to the model."""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ortools.service.v1.mathopt.solution_pb2
import ortools.service.v1.mathopt.sparse_containers_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SolutionHintProto(google.protobuf.message.Message):
    """A suggested starting solution for the solver.

    MIP solvers generally only want primal information (`variable_values`), while
    LP solvers want both primal and dual information (`dual_values`).

    Many MIP solvers can work with: (1) partial solutions that do not specify all
    variables or (2) infeasible solutions. In these cases, solvers typically
    solve a sub-MIP to complete/correct the hint.

    How the hint is used by the solver, if at all, is highly dependent on the
    solver, the problem type, and the algorithm used. The most reliable way to
    ensure your hint has an effect is to read the underlying solvers logs with
    and without the hint.

    Simplex-based LP solvers typically prefer an initial basis to a solution hint
    (they need to crossover to convert the hint to a basic feasible solution
    otherwise).

    TODO(b/183616124): Add hint-priorities to variable_values.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VARIABLE_VALUES_FIELD_NUMBER: builtins.int
    DUAL_VALUES_FIELD_NUMBER: builtins.int
    @property
    def variable_values(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto:
        """A possibly partial assignment of values to the primal variables of the
        problem. The solver-independent requirements for this sub-message are:
         * variable_values.ids are elements of VariablesProto.ids.
         * variable_values.values must all be finite.
        """

    @property
    def dual_values(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto:
        """A (potentially partial) assignment of values to the linear constraints of
        the problem.

         Requirements:
          * dual_values.ids are elements of LinearConstraintsProto.ids.
          * dual_values.values must all be finite.
        """

    def __init__(
        self,
        *,
        variable_values: ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto | None = ...,
        dual_values: ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["dual_values", b"dual_values", "variable_values", b"variable_values"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["dual_values", b"dual_values", "variable_values", b"variable_values"]) -> None: ...

global___SolutionHintProto = SolutionHintProto

@typing.final
class ModelSolveParametersProto(google.protobuf.message.Message):
    """TODO(b/183628247): follow naming convention in fields below.
    Parameters to control a single solve that that are specific to the input
    model (see SolveParametersProto for model independent parameters).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VARIABLE_VALUES_FILTER_FIELD_NUMBER: builtins.int
    DUAL_VALUES_FILTER_FIELD_NUMBER: builtins.int
    REDUCED_COSTS_FILTER_FIELD_NUMBER: builtins.int
    INITIAL_BASIS_FIELD_NUMBER: builtins.int
    SOLUTION_HINTS_FIELD_NUMBER: builtins.int
    BRANCHING_PRIORITIES_FIELD_NUMBER: builtins.int
    @property
    def variable_values_filter(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseVectorFilterProto:
        """Filter that is applied to all returned sparse containers keyed by variables
        in PrimalSolutionProto and PrimalRayProto
        (PrimalSolutionProto.variable_values, PrimalRayProto.variable_values).

        Requirements:
         * filtered_ids are elements of VariablesProto.ids.
        """

    @property
    def dual_values_filter(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseVectorFilterProto:
        """Filter that is applied to all returned sparse containers keyed by linear
        constraints in DualSolutionProto and DualRay
        (DualSolutionProto.dual_values, DualRay.dual_values).

        Requirements:
         * filtered_ids are elements of LinearConstraints.ids.
        """

    @property
    def reduced_costs_filter(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseVectorFilterProto:
        """Filter that is applied to all returned sparse containers keyed by variables
        in DualSolutionProto and DualRay (DualSolutionProto.reduced_costs,
        DualRay.reduced_costs).

        Requirements:
         * filtered_ids are elements of VariablesProto.ids.
        """

    @property
    def initial_basis(self) -> ortools.service.v1.mathopt.solution_pb2.BasisProto:
        """Optional initial basis for warm starting simplex LP solvers. If set, it is
        expected to be valid according to `ValidateBasis` in
        `validators/solution_validator.h` for the current `ModelSummary`.
        """

    @property
    def solution_hints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SolutionHintProto]:
        """Optional solution hints. If the underlying solver only accepts a single
        hint, the first hint is used.
        """

    @property
    def branching_priorities(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseInt32VectorProto:
        """Optional branching priorities. Variables with higher values will be
        branched on first. Variables for which priorities are not set get the
        solver's default priority (usually zero).

        Requirements:
         * branching_priorities.values must be finite.
         * branching_priorities.ids must be elements of VariablesProto.ids.
        """

    def __init__(
        self,
        *,
        variable_values_filter: ortools.service.v1.mathopt.sparse_containers_pb2.SparseVectorFilterProto | None = ...,
        dual_values_filter: ortools.service.v1.mathopt.sparse_containers_pb2.SparseVectorFilterProto | None = ...,
        reduced_costs_filter: ortools.service.v1.mathopt.sparse_containers_pb2.SparseVectorFilterProto | None = ...,
        initial_basis: ortools.service.v1.mathopt.solution_pb2.BasisProto | None = ...,
        solution_hints: collections.abc.Iterable[global___SolutionHintProto] | None = ...,
        branching_priorities: ortools.service.v1.mathopt.sparse_containers_pb2.SparseInt32VectorProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["branching_priorities", b"branching_priorities", "dual_values_filter", b"dual_values_filter", "initial_basis", b"initial_basis", "reduced_costs_filter", b"reduced_costs_filter", "variable_values_filter", b"variable_values_filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["branching_priorities", b"branching_priorities", "dual_values_filter", b"dual_values_filter", "initial_basis", b"initial_basis", "reduced_costs_filter", b"reduced_costs_filter", "solution_hints", b"solution_hints", "variable_values_filter", b"variable_values_filter"]) -> None: ...

global___ModelSolveParametersProto = ModelSolveParametersProto
