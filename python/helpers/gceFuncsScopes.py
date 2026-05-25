from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class gceFuncsScopes:

    @grepr_dataclass()
    class set_scope_var(ThirdBlock):
        OPCODE = "&gceFuncsScopes::set var (NAME) to (VALUE) in current scope"
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_scope_var(ThirdBlock):
        OPCODE = "&gceFuncsScopes::get var (NAME)"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NAME", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NAME", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class scope_var_exists(ThirdBlock):
        OPCODE = "&gceFuncsScopes::var (NAME) exists in [KIND]?"
        name: INPUT_COMPATIBLE_T
        kind: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class delete_scope_var(ThirdBlock):
        OPCODE = "&gceFuncsScopes::delete var (NAME) in current scope"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NAME", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NAME", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class all_variables(ThirdBlock):
        OPCODE = "&gceFuncsScopes::all variables in ([KIND])"
        kind: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("KIND", "kind", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("KIND", "kind", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class create_var_scope(ThirdBlock):
        OPCODE = "&gceFuncsScopes::create local variable scope {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SUBSTACK", "substack", p.SRScriptInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SUBSTACK", "substack", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class run_with_separate_globals(ThirdBlock):
        OPCODE = "&gceFuncsScopes::run with separate globals {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SUBSTACK", "substack", p.SRScriptInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SUBSTACK", "substack", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class bind_var_to_scope(ThirdBlock):
        OPCODE = "&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope"
        kind: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class configure_next_function_args(ThirdBlock):
        OPCODE = "&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)"
        argnames: INPUT_COMPATIBLE_T
        argdefaults: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARGNAMES", "argnames", p.SRBlockAndTextInputValue, None),
                    ("ARGDEFAULTS", "argdefaults", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARGNAMES", "argnames", p.SRBlockAndTextInputValue, None),
                    ("ARGDEFAULTS", "argdefaults", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class create_function_at(ThirdBlock):
        OPCODE = "&gceFuncsScopes::create function at var (NAME) {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class create_function_named(ThirdBlock):
        OPCODE = "&gceFuncsScopes::create function named (NAME) {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class return_value(ThirdBlock):
        OPCODE = "&gceFuncsScopes::return (VALUE)"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class call_function(ThirdBlock):
        OPCODE = "&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)"
        func: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("FUNC", "func", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("FUNC", "func", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class object_as_string(ThirdBlock):
        OPCODE = "&gceFuncsScopes::(VALUE) as string"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class typeof_value(ThirdBlock):
        OPCODE = "&gceFuncsScopes::typeof (VALUE)"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class typeof_value_is_menu(ThirdBlock):
        OPCODE = "&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?"
        value: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class typeof_value_selection(ThirdBlock):
        OPCODE = "&gceFuncsScopes::([TYPE])"
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TYPE", "type", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TYPE", "type", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class check_identity(ThirdBlock):
        OPCODE = "&gceFuncsScopes::(VALUE1) is (VALUE2) ?"
        value1: INPUT_COMPATIBLE_T
        value2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("VALUE1", "value1", p.SRBlockAndTextInputValue, None),
                    ("VALUE2", "value2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("VALUE1", "value1", p.SRBlockAndTextInputValue, None),
                    ("VALUE2", "value2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class nothing(ThirdBlock):
        OPCODE = "&gceFuncsScopes::Nothing"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class execute_expression(ThirdBlock):
        OPCODE = "&gceFuncsScopes::execute expression (EXPR)"
        expr: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("EXPR", "expr", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("EXPR", "expr", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class menu_variable_available_kind(ThirdBlock):
        OPCODE = "&gceFuncsScopes::#menu:variableAvailableKind"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_bind_var_origin_kind(ThirdBlock):
        OPCODE = "&gceFuncsScopes::#menu:bindVarOriginKind"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_typeof_menu(ThirdBlock):
        OPCODE = "&gceFuncsScopes::#menu:typeofMenu"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
