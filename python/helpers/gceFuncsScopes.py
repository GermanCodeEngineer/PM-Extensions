from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class gceFuncsScopes:

    @staticmethod
    def set_scope_var(name: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_scope_var(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::get var (NAME)",
            inputs={"NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def scope_var_exists(
        name: INPUT_COMPATIBLE_T, kind: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::var (NAME) exists in [KIND]?",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "KIND": InputValue.try_as_input(kind, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def delete_scope_var(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::delete var (NAME) in current scope",
            inputs={"NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def all_variables(kind: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::all variables in ([KIND])",
            inputs={
                "KIND": InputValue.try_as_input(kind, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def create_var_scope(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::create local variable scope {SUBSTACK}",
            inputs={
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def bind_var_to_scope(
        kind: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope",
            inputs={
                "KIND": InputValue.try_as_input(kind, p.SRBlockAndDropdownInputValue),
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def configure_next_function_args(
        argnames: INPUT_COMPATIBLE_T, argdefaults: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)",
            inputs={
                "ARGNAMES": InputValue.try_as_input(
                    argnames, p.SRBlockAndTextInputValue
                ),
                "ARGDEFAULTS": InputValue.try_as_input(
                    argdefaults, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def create_function_at(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_function_named(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def return_value(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::return (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def call_function(
        func: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)",
            inputs={
                "FUNC": InputValue.try_as_input(func, p.SRBlockAndTextInputValue),
                "POSARGS": InputValue.try_as_input(posargs, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def object_as_string(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::(VALUE) as string",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def typeof_value(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::typeof (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def typeof_value_is_menu(
        value: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def check_identity(
        value1: INPUT_COMPATIBLE_T, value2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
            inputs={
                "VALUE1": InputValue.try_as_input(value1, p.SRBlockAndTextInputValue),
                "VALUE2": InputValue.try_as_input(value2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def nothing() -> p.SRBlock:
        return p.SRBlock(opcode="&gceFuncsScopes::Nothing", inputs={}, dropdowns={})

    @staticmethod
    def execute_expression(expr: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::execute expression (EXPR)",
            inputs={"EXPR": InputValue.try_as_input(expr, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def menu_variable_available_kind() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::#menu:variableAvailableKind",
            inputs={},
            dropdowns={},
        )

    @staticmethod
    def menu_bind_var_origin_kind() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::#menu:bindVarOriginKind", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_typeof_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::#menu:typeofMenu", inputs={}, dropdowns={}
        )
