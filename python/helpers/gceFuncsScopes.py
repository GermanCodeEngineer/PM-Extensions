from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class gceFuncsScopes:

    @grepr_dataclass()
    class set_scope_var(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::set var (NAME) to (VALUE) in current scope"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_scope_var(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::get var (NAME)"
        INPUT_SPECS: ClassVar = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class scope_var_exists(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::var (NAME) exists in [KIND]?"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        kind: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_scope_var(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::delete var (NAME) in current scope"
        INPUT_SPECS: ClassVar = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class all_variables(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::all variables in ([KIND])"
        INPUT_SPECS: ClassVar = (
            ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        kind: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_var_scope(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::create local variable scope {SUBSTACK}"
        INPUT_SPECS: ClassVar = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class run_with_separate_globals(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::run with separate globals {SUBSTACK}"
        INPUT_SPECS: ClassVar = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class bind_var_to_scope(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope"
        )
        INPUT_SPECS: ClassVar = (
            ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        kind: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class configure_next_function_args(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)"
        )
        INPUT_SPECS: ClassVar = (
            ("ARGNAMES", "argnames", p.SRBlockAndTextInputValue, None),
            ("ARGDEFAULTS", "argdefaults", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        argnames: INPUT_COMPATIBLE_T
        argdefaults: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_function_at(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::create function at var (NAME) {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_function_named(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::create function named (NAME) {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class return_value(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::return (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class call_function(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)"
        )
        INPUT_SPECS: ClassVar = (
            ("FUNC", "func", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        func: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class object_as_string(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::(VALUE) as string"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class typeof_value(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::typeof (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class typeof_value_is_menu(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?"
        INPUT_SPECS: ClassVar = (
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class typeof_value_selection(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::([TYPE])"
        INPUT_SPECS: ClassVar = (
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class check_identity(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::(VALUE1) is (VALUE2) ?"
        INPUT_SPECS: ClassVar = (
            ("VALUE1", "value1", p.SRBlockAndTextInputValue, None),
            ("VALUE2", "value2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        value1: INPUT_COMPATIBLE_T
        value2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class nothing(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::Nothing"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class execute_expression(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::execute expression (EXPR)"
        INPUT_SPECS: ClassVar = (("EXPR", "expr", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        expr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_variable_available_kind(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::#menu:variableAvailableKind"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_bind_var_origin_kind(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::#menu:bindVarOriginKind"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_typeof_menu(ThirdBlock):
        OPCODE: ClassVar = "&gceFuncsScopes::#menu:typeofMenu"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
