from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class gceFuncsScopes:

    @grepr_dataclass()
    class set_scope_var(ThirdBlock):
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class get_scope_var(ThirdBlock):
        name: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class scope_var_exists(ThirdBlock):
        name: INPUT_COMPATIBLE_T
        kind: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class delete_scope_var(ThirdBlock):
        name: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class all_variables(ThirdBlock):
        kind: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class create_var_scope(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class run_with_separate_globals(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class bind_var_to_scope(ThirdBlock):
        kind: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class configure_next_function_args(ThirdBlock):
        argnames: INPUT_COMPATIBLE_T
        argdefaults: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class create_function_at(ThirdBlock):
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class create_function_named(ThirdBlock):
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class return_value(ThirdBlock):
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class call_function(ThirdBlock):
        func: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class object_as_string(ThirdBlock):
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class typeof_value(ThirdBlock):
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class typeof_value_is_menu(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class typeof_value_selection(ThirdBlock):
        type: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class check_identity(ThirdBlock):
        value1: INPUT_COMPATIBLE_T
        value2: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class nothing(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&gceFuncsScopes::Nothing", inputs={}, dropdowns={})

    @grepr_dataclass()
    class execute_expression(ThirdBlock):
        expr: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class menu_variable_available_kind(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::#menu:variableAvailableKind",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_bind_var_origin_kind(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::#menu:bindVarOriginKind",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_typeof_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceFuncsScopes::#menu:typeofMenu", inputs={}, dropdowns={}
            )
