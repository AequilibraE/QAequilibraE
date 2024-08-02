"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2010-2024 Google LLC
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class HighsOptionsProto(google.protobuf.message.Message):
    """The options exposed by HiGHS. Use at your own risk, these are completely
    undocumented.

    Option names are given as strings in HighsOptions.h, see:
    https://github.com/ERGO-Code/HiGHS/blob/7421e44b09563f637dc6422ea461a8832b29e543/src/lp_data/HighsOptions.h
    Each member of HighsOptionsStruct has a corresponding OptionRecord with a
    string name (that appears to match the field name), use these as keys below.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class StringOptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class DoubleOptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.float
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.float = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class IntOptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.int
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class BoolOptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bool
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    STRING_OPTIONS_FIELD_NUMBER: builtins.int
    DOUBLE_OPTIONS_FIELD_NUMBER: builtins.int
    INT_OPTIONS_FIELD_NUMBER: builtins.int
    BOOL_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def string_options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Example keys: "presolve", "solver", "parallel" """

    @property
    def double_options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.float]:
        """Example keys: "time_limit", "primal_feasibility_tolerance" """

    @property
    def int_options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.int]:
        """Example keys: "random_seed", "simplex_strategy" """

    @property
    def bool_options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bool]:
        """Example keys: "log_to_console", "allow_unbounded_or_infeasible" """

    def __init__(
        self,
        *,
        string_options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        double_options: collections.abc.Mapping[builtins.str, builtins.float] | None = ...,
        int_options: collections.abc.Mapping[builtins.str, builtins.int] | None = ...,
        bool_options: collections.abc.Mapping[builtins.str, builtins.bool] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bool_options", b"bool_options", "double_options", b"double_options", "int_options", b"int_options", "string_options", b"string_options"]) -> None: ...

global___HighsOptionsProto = HighsOptionsProto
