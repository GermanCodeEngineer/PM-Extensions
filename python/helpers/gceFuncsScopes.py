from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class gceFuncsScopes:

    @staticmethod
    def set_scope_var(name: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_scope_var(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::get var (NAME)",
            inputs={"NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def scope_var_exists(
        name: INPUT_COMPATIBLE_T, kind: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::var (NAME) exists in [KIND]?",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "KIND": ThirdInputValue.as_input(kind, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def delete_scope_var(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::delete var (NAME) in current scope",
            inputs={"NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def all_variables(kind: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::all variables in ([KIND])",
            inputs={
                "KIND": ThirdInputValue.as_input(kind, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def create_var_scope(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::create local variable scope {SUBSTACK}",
            inputs={
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def run_with_separate_globals(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::run with separate globals {SUBSTACK}",
            inputs={
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue)
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
                "KIND": ThirdInputValue.as_input(kind, p.SRBlockAndDropdownInputValue),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
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
                "ARGNAMES": ThirdInputValue.as_input(
                    argnames, p.SRBlockAndTextInputValue
                ),
                "ARGDEFAULTS": ThirdInputValue.as_input(
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
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
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
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def return_value(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::return (VALUE)",
            inputs={
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue)
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
                "FUNC": ThirdInputValue.as_input(func, p.SRBlockAndTextInputValue),
                "POSARGS": ThirdInputValue.as_input(
                    posargs, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def object_as_string(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::(VALUE) as string",
            inputs={
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def typeof_value(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::typeof (VALUE)",
            inputs={
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue)
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
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
                "TYPE": ThirdInputValue.as_input(type, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def typeof_value_selection(type: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceFuncsScopes::([TYPE])",
            inputs={
                "TYPE": ThirdInputValue.as_input(type, p.SRBlockAndDropdownInputValue)
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
                "VALUE1": ThirdInputValue.as_input(value1, p.SRBlockAndTextInputValue),
                "VALUE2": ThirdInputValue.as_input(value2, p.SRBlockAndTextInputValue),
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
            inputs={"EXPR": ThirdInputValue.as_input(expr, p.SRBlockAndTextInputValue)},
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
