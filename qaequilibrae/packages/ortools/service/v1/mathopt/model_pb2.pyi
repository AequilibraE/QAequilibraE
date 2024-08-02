"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
An encoding format for mathematical optimization problems."""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ortools.service.v1.mathopt.sparse_containers_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class VariablesProto(google.protobuf.message.Message):
    """As used below, we define "#variables" = size(VariablesProto.ids)."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDS_FIELD_NUMBER: builtins.int
    LOWER_BOUNDS_FIELD_NUMBER: builtins.int
    UPPER_BOUNDS_FIELD_NUMBER: builtins.int
    INTEGERS_FIELD_NUMBER: builtins.int
    NAMES_FIELD_NUMBER: builtins.int
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Must be nonnegative and strictly increasing. The max(int64) value can't be
        used.
        """

    @property
    def lower_bounds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Should have length equal to #variables, values in [-inf, inf)."""

    @property
    def upper_bounds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Should have length equal to #variables, values in (-inf, inf]."""

    @property
    def integers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]:
        """Should have length equal to #variables. Value is false for continuous
        variables and true for integer variables.
        """

    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """If not set, assumed to be all empty strings. Otherwise, should have length
        equal to #variables.

        All nonempty names must be distinct. TODO(b/169575522): we may relax this.
        """

    def __init__(
        self,
        *,
        ids: collections.abc.Iterable[builtins.int] | None = ...,
        lower_bounds: collections.abc.Iterable[builtins.float] | None = ...,
        upper_bounds: collections.abc.Iterable[builtins.float] | None = ...,
        integers: collections.abc.Iterable[builtins.bool] | None = ...,
        names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ids", b"ids", "integers", b"integers", "lower_bounds", b"lower_bounds", "names", b"names", "upper_bounds", b"upper_bounds"]) -> None: ...

global___VariablesProto = VariablesProto

@typing.final
class ObjectiveProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAXIMIZE_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LINEAR_COEFFICIENTS_FIELD_NUMBER: builtins.int
    QUADRATIC_COEFFICIENTS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    PRIORITY_FIELD_NUMBER: builtins.int
    maximize: builtins.bool
    """false is minimize, true is maximize"""
    offset: builtins.float
    """Must be finite and not NaN."""
    name: builtins.str
    """Parent messages may have uniqueness requirements on this field; e.g., see
    ModelProto.objectives and AuxiliaryObjectivesUpdatesProto.new_objectives.
    """
    priority: builtins.int
    """For multi-objective problems, the priority of this objective relative to
    the others (lower is more important). This value must be nonnegative.
    Furthermore, each objective priority in the model must be distinct at solve
    time. This condition is not validated at the proto level, so models may
    temporarily have objectives with the same priority.
    """
    @property
    def linear_coefficients(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto:
        """ObjectiveProto terms that are linear in the decision variables.

        Requirements:
         * linear_coefficients.ids are elements of VariablesProto.ids.
         * VariablesProto not specified correspond to zero.
         * linear_coefficients.values must all be finite.
         * linear_coefficients.values can be zero, but this just wastes space.
        """

    @property
    def quadratic_coefficients(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleMatrixProto:
        """Objective terms that are quadratic in the decision variables.

        Requirements in addition to those on SparseDoubleMatrixProto messages:
         * Each element of quadratic_coefficients.row_ids and each element of
           quadratic_coefficients.column_ids must be an element of
           VariablesProto.ids.
         * The matrix must be upper triangular: for each i,
           quadratic_coefficients.row_ids[i] <=
           quadratic_coefficients.column_ids[i].

        Notes:
         * Terms not explicitly stored have zero coefficient.
         * Elements of quadratic_coefficients.coefficients can be zero, but this
           just wastes space.
        """

    def __init__(
        self,
        *,
        maximize: builtins.bool = ...,
        offset: builtins.float = ...,
        linear_coefficients: ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto | None = ...,
        quadratic_coefficients: ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleMatrixProto | None = ...,
        name: builtins.str = ...,
        priority: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["linear_coefficients", b"linear_coefficients", "quadratic_coefficients", b"quadratic_coefficients"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["linear_coefficients", b"linear_coefficients", "maximize", b"maximize", "name", b"name", "offset", b"offset", "priority", b"priority", "quadratic_coefficients", b"quadratic_coefficients"]) -> None: ...

global___ObjectiveProto = ObjectiveProto

@typing.final
class LinearConstraintsProto(google.protobuf.message.Message):
    """As used below, we define "#linear constraints" =
    size(LinearConstraintsProto.ids).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDS_FIELD_NUMBER: builtins.int
    LOWER_BOUNDS_FIELD_NUMBER: builtins.int
    UPPER_BOUNDS_FIELD_NUMBER: builtins.int
    NAMES_FIELD_NUMBER: builtins.int
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Must be nonnegative and strictly increasing. The max(int64) value can't be
        used.
        """

    @property
    def lower_bounds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Should have length equal to #linear constraints, values in [-inf, inf)."""

    @property
    def upper_bounds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Should have length equal to #linear constraints, values in (-inf, inf]."""

    @property
    def names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """If not set, assumed to be all empty strings. Otherwise, should have length
        equal to #linear constraints.

        All nonempty names must be distinct. TODO(b/169575522): we may relax this.
        """

    def __init__(
        self,
        *,
        ids: collections.abc.Iterable[builtins.int] | None = ...,
        lower_bounds: collections.abc.Iterable[builtins.float] | None = ...,
        upper_bounds: collections.abc.Iterable[builtins.float] | None = ...,
        names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ids", b"ids", "lower_bounds", b"lower_bounds", "names", b"names", "upper_bounds", b"upper_bounds"]) -> None: ...

global___LinearConstraintsProto = LinearConstraintsProto

@typing.final
class QuadraticConstraintProto(google.protobuf.message.Message):
    """A single quadratic constraint of the form:
       lb <= sum{linear_terms} + sum{quadratic_terms} <= ub.

    If a variable involved in this constraint is deleted, it is treated as if it
    were set to zero.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LINEAR_TERMS_FIELD_NUMBER: builtins.int
    QUADRATIC_TERMS_FIELD_NUMBER: builtins.int
    LOWER_BOUND_FIELD_NUMBER: builtins.int
    UPPER_BOUND_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    lower_bound: builtins.float
    """Must have value in [-inf, inf), and be less than or equal to `upper_bound`."""
    upper_bound: builtins.float
    """Must have value in (-inf, inf], and be greater than or equal to
    `lower_bound`.
    """
    name: builtins.str
    """Parent messages may have uniqueness requirements on this field; e.g., see
    ModelProto.quadratic_constraints and
    QuadraticConstraintUpdatesProto.new_constraints.
    """
    @property
    def linear_terms(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto:
        """Terms that are linear in the decision variables.

        In addition to requirements on SparseDoubleVectorProto messages we require
        that:
         * linear_terms.ids are elements of VariablesProto.ids.
         * linear_terms.values must all be finite and not-NaN.

        Notes:
         * Variable ids omitted have a corresponding coefficient of zero.
         * linear_terms.values can be zero, but this just wastes space.
        """

    @property
    def quadratic_terms(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleMatrixProto:
        """Terms that are quadratic in the decision variables.

        In addition to requirements on SparseDoubleMatrixProto messages we require
        that:
         * Each element of quadratic_terms.row_ids and each element of
           quadratic_terms.column_ids must be an element of VariablesProto.ids.
         * The matrix must be upper triangular: for each i,
           quadratic_terms.row_ids[i] <= quadratic_terms.column_ids[i].

        Notes:
         * Terms not explicitly stored have zero coefficient.
         * Elements of quadratic_terms.coefficients can be zero, but this just
           wastes space.
        """

    def __init__(
        self,
        *,
        linear_terms: ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto | None = ...,
        quadratic_terms: ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleMatrixProto | None = ...,
        lower_bound: builtins.float = ...,
        upper_bound: builtins.float = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["linear_terms", b"linear_terms", "quadratic_terms", b"quadratic_terms"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["linear_terms", b"linear_terms", "lower_bound", b"lower_bound", "name", b"name", "quadratic_terms", b"quadratic_terms", "upper_bound", b"upper_bound"]) -> None: ...

global___QuadraticConstraintProto = QuadraticConstraintProto

@typing.final
class SecondOrderConeConstraintProto(google.protobuf.message.Message):
    """A single second-order cone constraint of the form:

       ||`arguments_to_norm`||_2 <= `upper_bound`,

    where `upper_bound` and each element of `arguments_to_norm` are linear
    expressions.

    If a variable involved in this constraint is deleted, it is treated as if it
    were set to zero.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPPER_BOUND_FIELD_NUMBER: builtins.int
    ARGUMENTS_TO_NORM_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Parent messages may have uniqueness requirements on this field; e.g., see
    `ModelProto.second_order_cone_constraints` and
    `SecondOrderConeConstraintUpdatesProto.new_constraints`.
    """
    @property
    def upper_bound(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.LinearExpressionProto: ...
    @property
    def arguments_to_norm(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ortools.service.v1.mathopt.sparse_containers_pb2.LinearExpressionProto]: ...
    def __init__(
        self,
        *,
        upper_bound: ortools.service.v1.mathopt.sparse_containers_pb2.LinearExpressionProto | None = ...,
        arguments_to_norm: collections.abc.Iterable[ortools.service.v1.mathopt.sparse_containers_pb2.LinearExpressionProto] | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["upper_bound", b"upper_bound"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["arguments_to_norm", b"arguments_to_norm", "name", b"name", "upper_bound", b"upper_bound"]) -> None: ...

global___SecondOrderConeConstraintProto = SecondOrderConeConstraintProto

@typing.final
class SosConstraintProto(google.protobuf.message.Message):
    """Data for representing a single SOS1 or SOS2 constraint.

    If a variable involved in this constraint is deleted, it is treated as if it
    were set to zero.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXPRESSIONS_FIELD_NUMBER: builtins.int
    WEIGHTS_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Parent messages may have uniqueness requirements on this field; e.g., see
    ModelProto.sos1_constraints and SosConstraintUpdatesProto.new_constraints.
    """
    @property
    def expressions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ortools.service.v1.mathopt.sparse_containers_pb2.LinearExpressionProto]:
        """The expressions over which to apply the SOS constraint:
          * SOS1: At most one element takes a nonzero value.
          * SOS2: At most two elements take nonzero values, and they must be
                  adjacent in the repeated ordering.
        """

    @property
    def weights(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Either empty or of equal length to expressions. If empty, default weights
        are 1, 2, ...
        If present, the entries must be unique.
        """

    def __init__(
        self,
        *,
        expressions: collections.abc.Iterable[ortools.service.v1.mathopt.sparse_containers_pb2.LinearExpressionProto] | None = ...,
        weights: collections.abc.Iterable[builtins.float] | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["expressions", b"expressions", "name", b"name", "weights", b"weights"]) -> None: ...

global___SosConstraintProto = SosConstraintProto

@typing.final
class IndicatorConstraintProto(google.protobuf.message.Message):
    """Data for representing a single indicator constraint of the form:
       Variable(indicator_id) = (activate_on_zero ? 0 : 1) ⇒
       lower_bound <= expression <= upper_bound.

    If a variable involved in this constraint (either the indicator, or appearing
    in `expression`) is deleted, it is treated as if it were set to zero. In
    particular, deleting the indicator variable means that the indicator
    constraint is vacuous if `activate_on_zero` is false, and that it is
    equivalent to a linear constraint if `activate_on_zero` is true.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INDICATOR_ID_FIELD_NUMBER: builtins.int
    ACTIVATE_ON_ZERO_FIELD_NUMBER: builtins.int
    EXPRESSION_FIELD_NUMBER: builtins.int
    LOWER_BOUND_FIELD_NUMBER: builtins.int
    UPPER_BOUND_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    indicator_id: builtins.int
    """An ID corresponding to a binary variable, or unset. If unset, the indicator
    constraint is ignored. If set, we require that:
      * VariablesProto.integers[indicator_id] = true,
      * VariablesProto.lower_bounds[indicator_id] >= 0,
      * VariablesProto.upper_bounds[indicator_id] <= 1.
    These conditions are not validated by MathOpt, but if not satisfied will
    lead to the solver returning an error upon solving.
    """
    activate_on_zero: builtins.bool
    """If true, then if the indicator variable takes value 0, the implied
    constraint must hold. Otherwise, if the indicator variable takes value 1,
    then the implied constraint must hold.
    """
    lower_bound: builtins.float
    """Must have value in [-inf, inf); cannot be NaN."""
    upper_bound: builtins.float
    """Must have value in (-inf, inf]; cannot be NaN."""
    name: builtins.str
    """Parent messages may have uniqueness requirements on this field; e.g., see
    `ModelProto.indicator_constraints` and
    `IndicatorConstraintUpdatesProto.new_constraints`.
    """
    @property
    def expression(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto:
        """Must be a valid linear expression with respect to the containing model:
          * All stated conditions on `SparseDoubleVectorProto`,
          * All elements of `expression.values` must be finite,
          * `expression.ids` are a subset of `VariablesProto.ids`.
        """

    def __init__(
        self,
        *,
        indicator_id: builtins.int | None = ...,
        activate_on_zero: builtins.bool = ...,
        expression: ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleVectorProto | None = ...,
        lower_bound: builtins.float = ...,
        upper_bound: builtins.float = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_indicator_id", b"_indicator_id", "expression", b"expression", "indicator_id", b"indicator_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_indicator_id", b"_indicator_id", "activate_on_zero", b"activate_on_zero", "expression", b"expression", "indicator_id", b"indicator_id", "lower_bound", b"lower_bound", "name", b"name", "upper_bound", b"upper_bound"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_indicator_id", b"_indicator_id"]) -> typing.Literal["indicator_id"] | None: ...

global___IndicatorConstraintProto = IndicatorConstraintProto

@typing.final
class ModelProto(google.protobuf.message.Message):
    """An optimization problem.
    MathOpt supports:
      - Continuous and integer decision variables with optional finite bounds.
      - Linear and quadratic objectives (single or multiple objectives), either
      minimized or maximized.
      - A number of constraints types, including:
        * Linear constraints
        * Quadratic constraints
        * Second-order cone constraints
        * Logical constraints
          > SOS1 and SOS2 constraints
          > Indicator constraints

    By default, constraints are represented in "id-to-data" maps. However, we
    represent linear constraints in a more efficient "struct-of-arrays" format.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class AuxiliaryObjectivesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___ObjectiveProto: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___ObjectiveProto | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class QuadraticConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___QuadraticConstraintProto: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___QuadraticConstraintProto | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class SecondOrderConeConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___SecondOrderConeConstraintProto: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___SecondOrderConeConstraintProto | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class Sos1ConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___SosConstraintProto: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___SosConstraintProto | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class Sos2ConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___SosConstraintProto: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___SosConstraintProto | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class IndicatorConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___IndicatorConstraintProto: ...
        def __init__(
            self,
            *,
            key: builtins.int = ...,
            value: global___IndicatorConstraintProto | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    VARIABLES_FIELD_NUMBER: builtins.int
    OBJECTIVE_FIELD_NUMBER: builtins.int
    AUXILIARY_OBJECTIVES_FIELD_NUMBER: builtins.int
    LINEAR_CONSTRAINTS_FIELD_NUMBER: builtins.int
    LINEAR_CONSTRAINT_MATRIX_FIELD_NUMBER: builtins.int
    QUADRATIC_CONSTRAINTS_FIELD_NUMBER: builtins.int
    SECOND_ORDER_CONE_CONSTRAINTS_FIELD_NUMBER: builtins.int
    SOS1_CONSTRAINTS_FIELD_NUMBER: builtins.int
    SOS2_CONSTRAINTS_FIELD_NUMBER: builtins.int
    INDICATOR_CONSTRAINTS_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def variables(self) -> global___VariablesProto: ...
    @property
    def objective(self) -> global___ObjectiveProto:
        """The primary objective in the model."""

    @property
    def auxiliary_objectives(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___ObjectiveProto]:
        """Auxiliary objectives for use in multi-objective models.

        Map key IDs must be in [0, max(int64)). Each priority, and each nonempty
        name, must be unique and also distinct from the primary `objective`.
        """

    @property
    def linear_constraints(self) -> global___LinearConstraintsProto: ...
    @property
    def linear_constraint_matrix(self) -> ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleMatrixProto:
        """The variable coefficients for the linear constraints.

        If a variable involved in this constraint is deleted, it is treated as if
        it were set to zero.

        Requirements:
         * linear_constraint_matrix.row_ids are elements of linear_constraints.ids.
         * linear_constraint_matrix.column_ids are elements of variables.ids.
         * Matrix entries not specified are zero.
         * linear_constraint_matrix.values must all be finite.
        """

    @property
    def quadratic_constraints(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___QuadraticConstraintProto]:
        """Mapped constraints (i.e., stored in "constraint ID"-to-"constraint data"
        map). For each subsequent submessage, we require that:
          * Each key is in [0, max(int64)).
          * Each key is unique in its respective map (but not necessarily across
            constraint types)
          * Each value contains a name field (called `name`), and each nonempty
            name must be distinct across all map entries (but not necessarily
            across constraint types).

        Quadratic constraints in the model.
        """

    @property
    def second_order_cone_constraints(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___SecondOrderConeConstraintProto]:
        """Second-order cone constraints in the model."""

    @property
    def sos1_constraints(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___SosConstraintProto]:
        """SOS1 constraints in the model, which constrain that at most one
        `expression` can be nonzero. The optional `weights` entries are an
        implementation detail used by the solver to (hopefully) converge more
        quickly. In more detail, solvers may (or may not) use these weights to
        select branching decisions that produce "balanced" children nodes.
        """

    @property
    def sos2_constraints(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___SosConstraintProto]:
        """SOS2 constraints in the model, which constrain that at most two entries of
        `expression` can be nonzero, and they must be adjacent in their ordering.
        If no `weights` are provided, this ordering is their linear ordering in the
        `expressions` list; if `weights` are presented, the ordering is taken with
        respect to these values in increasing order.
        """

    @property
    def indicator_constraints(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___IndicatorConstraintProto]:
        """Indicator constraints in the model, which enforce that, if a binary
        "indicator variable" is set to one, then an "implied constraint" must hold.
        """

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        variables: global___VariablesProto | None = ...,
        objective: global___ObjectiveProto | None = ...,
        auxiliary_objectives: collections.abc.Mapping[builtins.int, global___ObjectiveProto] | None = ...,
        linear_constraints: global___LinearConstraintsProto | None = ...,
        linear_constraint_matrix: ortools.service.v1.mathopt.sparse_containers_pb2.SparseDoubleMatrixProto | None = ...,
        quadratic_constraints: collections.abc.Mapping[builtins.int, global___QuadraticConstraintProto] | None = ...,
        second_order_cone_constraints: collections.abc.Mapping[builtins.int, global___SecondOrderConeConstraintProto] | None = ...,
        sos1_constraints: collections.abc.Mapping[builtins.int, global___SosConstraintProto] | None = ...,
        sos2_constraints: collections.abc.Mapping[builtins.int, global___SosConstraintProto] | None = ...,
        indicator_constraints: collections.abc.Mapping[builtins.int, global___IndicatorConstraintProto] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["linear_constraint_matrix", b"linear_constraint_matrix", "linear_constraints", b"linear_constraints", "objective", b"objective", "variables", b"variables"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auxiliary_objectives", b"auxiliary_objectives", "indicator_constraints", b"indicator_constraints", "linear_constraint_matrix", b"linear_constraint_matrix", "linear_constraints", b"linear_constraints", "name", b"name", "objective", b"objective", "quadratic_constraints", b"quadratic_constraints", "second_order_cone_constraints", b"second_order_cone_constraints", "sos1_constraints", b"sos1_constraints", "sos2_constraints", b"sos2_constraints", "variables", b"variables"]) -> None: ...

global___ModelProto = ModelProto
