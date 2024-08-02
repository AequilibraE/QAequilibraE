"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

This file contains a protocol buffer definition for search limits.
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class RegularLimitParameters(google.protobuf.message.Message):
    """A search limit
    The default values for int64 fields is the maxima value, i.e., 2^63-1
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_FIELD_NUMBER: builtins.int
    BRANCHES_FIELD_NUMBER: builtins.int
    FAILURES_FIELD_NUMBER: builtins.int
    SOLUTIONS_FIELD_NUMBER: builtins.int
    SMART_TIME_CHECK_FIELD_NUMBER: builtins.int
    CUMULATIVE_FIELD_NUMBER: builtins.int
    time: builtins.int
    """TODO(user): Specify the time units or switch to google.Duration proto."""
    branches: builtins.int
    failures: builtins.int
    solutions: builtins.int
    smart_time_check: builtins.bool
    cumulative: builtins.bool
    def __init__(
        self,
        *,
        time: builtins.int = ...,
        branches: builtins.int = ...,
        failures: builtins.int = ...,
        solutions: builtins.int = ...,
        smart_time_check: builtins.bool = ...,
        cumulative: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["branches", b"branches", "cumulative", b"cumulative", "failures", b"failures", "smart_time_check", b"smart_time_check", "solutions", b"solutions", "time", b"time"]) -> None: ...

global___RegularLimitParameters = RegularLimitParameters
