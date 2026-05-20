from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class gceFuncsScopes:

    class set_scope_var(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.name = name
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::set var (NAME) to (VALUE) in current scope",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class get_scope_var(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T):
            self.name = name

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::get var (NAME)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class scope_var_exists(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, kind: INPUT_COMPATIBLE_T):
            self.name = name
            self.kind = kind

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::var (NAME) exists in [KIND]?",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "KIND": ThirdInputValue.as_input(
                        self.kind, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class delete_scope_var(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T):
            self.name = name

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::delete var (NAME) in current scope",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class all_variables(ThirdBlock):

        def __init__(self, kind: INPUT_COMPATIBLE_T):
            self.kind = kind

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::all variables in ([KIND])",
                inputs={
                    "KIND": ThirdInputValue.as_input(
                        self.kind, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    class create_var_scope(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::create local variable scope {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    class run_with_separate_globals(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::run with separate globals {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    class bind_var_to_scope(ThirdBlock):

        def __init__(self, kind: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T):
            self.kind = kind
            self.name = name

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope",
                inputs={
                    "KIND": ThirdInputValue.as_input(
                        self.kind, p.SRBlockAndDropdownInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class configure_next_function_args(ThirdBlock):

        def __init__(
            self, argnames: INPUT_COMPATIBLE_T, argdefaults: INPUT_COMPATIBLE_T
        ):
            self.argnames = argnames
            self.argdefaults = argdefaults

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)",
                inputs={
                    "ARGNAMES": ThirdInputValue.as_input(
                        self.argnames, p.SRBlockAndTextInputValue
                    ),
                    "ARGDEFAULTS": ThirdInputValue.as_input(
                        self.argdefaults, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class create_function_at(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::create function at var (NAME) {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class create_function_named(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::create function named (NAME) {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class return_value(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::return (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class call_function(ThirdBlock):

        def __init__(self, func: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T):
            self.func = func
            self.posargs = posargs

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)",
                inputs={
                    "FUNC": ThirdInputValue.as_input(
                        self.func, p.SRBlockAndTextInputValue
                    ),
                    "POSARGS": ThirdInputValue.as_input(
                        self.posargs, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class object_as_string(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::(VALUE) as string",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class typeof_value(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::typeof (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class typeof_value_is_menu(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T):
            self.value = value
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class typeof_value_selection(ThirdBlock):

        def __init__(self, type: INPUT_COMPATIBLE_T):
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::([TYPE])",
                inputs={
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    class check_identity(ThirdBlock):

        def __init__(self, value1: INPUT_COMPATIBLE_T, value2: INPUT_COMPATIBLE_T):
            self.value1 = value1
            self.value2 = value2

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::(VALUE1) is (VALUE2) ?",
                inputs={
                    "VALUE1": ThirdInputValue.as_input(
                        self.value1, p.SRBlockAndTextInputValue
                    ),
                    "VALUE2": ThirdInputValue.as_input(
                        self.value2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class nothing(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&gceFuncsScopes::Nothing", inputs={}, dropdowns={})

    class execute_expression(ThirdBlock):

        def __init__(self, expr: INPUT_COMPATIBLE_T):
            self.expr = expr

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::execute expression (EXPR)",
                inputs={
                    "EXPR": ThirdInputValue.as_input(
                        self.expr, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class menu_variable_available_kind(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::#menu:variableAvailableKind",
                inputs={},
                dropdowns={},
            )

    class menu_bind_var_origin_kind(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::#menu:bindVarOriginKind",
                inputs={},
                dropdowns={},
            )

    class menu_typeof_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::#menu:typeofMenu", inputs={}, dropdowns={}
            )
