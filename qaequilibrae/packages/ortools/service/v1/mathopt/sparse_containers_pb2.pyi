"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Data structures used throughout MathOpt to model sparse vectors and matrices."""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SparseDoubleVectorProto(google.protobuf.message.Message):
    """A sparse representation of a vector of doubles."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDS_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Must be sorted (in increasing ordering) with all elements distinct."""

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Must have equal length to ids. May not contain NaN."""

    def __init__(
        self,
        *,
        ids: collections.abc.Iterable[builtins.int] | None = ...,
        values: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ids", b"ids", "values", b"values"]) -> None: ...

global___SparseDoubleVectorProto = SparseDoubleVectorProto

@typing.final
class SparseBoolVectorProto(google.protobuf.message.Message):
    """A sparse representation of a vector of bools."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDS_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Should be sorted (in increasing ordering) with all elements distinct."""

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]:
        """Must have equal length to ids."""

    def __init__(
        self,
        *,
        ids: collections.abc.Iterable[builtins.int] | None = ...,
        values: collections.abc.Iterable[builtins.bool] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ids", b"ids", "values", b"values"]) -> None: ...

global___SparseBoolVectorProto = SparseBoolVectorProto

@typing.final
class SparseInt32VectorProto(google.protobuf.message.Message):
    """A sparse representation of a vector of ints."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDS_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Should be sorted (in increasing ordering) with all elements distinct."""

    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Must have equal length to ids."""

    def __init__(
        self,
        *,
        ids: collections.abc.Iterable[builtins.int] | None = ...,
        values: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ids", b"ids", "values", b"values"]) -> None: ...

global___SparseInt32VectorProto = SparseInt32VectorProto

@typing.final
class SparseVectorFilterProto(google.protobuf.message.Message):
    """This message allows to query/set specific parts of a SparseXxxxVector.
    The default behavior is not to filter out anything.
    A common usage is to query only parts of solutions (only non-zero values,
    and/or just a hand-picked set of variable values).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SKIP_ZERO_VALUES_FIELD_NUMBER: builtins.int
    FILTER_BY_IDS_FIELD_NUMBER: builtins.int
    FILTERED_IDS_FIELD_NUMBER: builtins.int
    skip_zero_values: builtins.bool
    """For SparseBoolVectorProto "zero" is `false`."""
    filter_by_ids: builtins.bool
    """When true, return only the values corresponding to the IDs listed in
    filtered_ids.
    """
    @property
    def filtered_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """The list of IDs to use when filter_by_ids is true. Must be empty when
        filter_by_ids is false.
        NOTE: if this is empty, and filter_by_ids is true, you are saying that
        you do not want any information in the result.
        """

    def __init__(
        self,
        *,
        skip_zero_values: builtins.bool = ...,
        filter_by_ids: builtins.bool = ...,
        filtered_ids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter_by_ids", b"filter_by_ids", "filtered_ids", b"filtered_ids", "skip_zero_values", b"skip_zero_values"]) -> None: ...

global___SparseVectorFilterProto = SparseVectorFilterProto

@typing.final
class SparseDoubleMatrixProto(google.protobuf.message.Message):
    """A sparse representation of a matrix of doubles.

    The matrix is stored as triples of row id, column id, and coefficient. These
    three vectors must be of equal length. For all i, the tuple (row_ids[i],
    column_ids[i]) should be distinct. Entries must be in row major order.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROW_IDS_FIELD_NUMBER: builtins.int
    COLUMN_IDS_FIELD_NUMBER: builtins.int
    COEFFICIENTS_FIELD_NUMBER: builtins.int
    @property
    def row_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def column_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def coefficients(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """May not contain NaN."""

    def __init__(
        self,
        *,
        row_ids: collections.abc.Iterable[builtins.int] | None = ...,
        column_ids: collections.abc.Iterable[builtins.int] | None = ...,
        coefficients: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["coefficients", b"coefficients", "column_ids", b"column_ids", "row_ids", b"row_ids"]) -> None: ...

global___SparseDoubleMatrixProto = SparseDoubleMatrixProto

@typing.final
class LinearExpressionProto(google.protobuf.message.Message):
    """A sparse representation of a linear expression (a weighted sum of variables,
    plus a constant offset).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDS_FIELD_NUMBER: builtins.int
    COEFFICIENTS_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    offset: builtins.float
    """Must be finite and may not be NaN."""
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Ids of variables. Must be sorted (in increasing ordering) with all elements
        distinct.
        """

    @property
    def coefficients(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """Must have equal length to ids. Values must be finite may not be NaN."""

    def __init__(
        self,
        *,
        ids: collections.abc.Iterable[builtins.int] | None = ...,
        coefficients: collections.abc.Iterable[builtins.float] | None = ...,
        offset: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["coefficients", b"coefficients", "ids", b"ids", "offset", b"offset"]) -> None: ...

global___LinearExpressionProto = LinearExpressionProto
