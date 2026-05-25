from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class gceFuncsScopes:

    @grepr_dataclass()
    class set_scope_var(ThirdBlock):
        OPCODE = "&gceFuncsScopes::set var (NAME) to (VALUE) in current scope"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_scope_var(ThirdBlock):
        OPCODE = "&gceFuncsScopes::get var (NAME)"
        INPUT_SPECS = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class scope_var_exists(ThirdBlock):
        OPCODE = "&gceFuncsScopes::var (NAME) exists in [KIND]?"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        kind: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_scope_var(ThirdBlock):
        OPCODE = "&gceFuncsScopes::delete var (NAME) in current scope"
        INPUT_SPECS = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class all_variables(ThirdBlock):
        OPCODE = "&gceFuncsScopes::all variables in ([KIND])"
        INPUT_SPECS = (("KIND", "kind", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        kind: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_var_scope(ThirdBlock):
        OPCODE = "&gceFuncsScopes::create local variable scope {SUBSTACK}"
        INPUT_SPECS = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class run_with_separate_globals(ThirdBlock):
        OPCODE = "&gceFuncsScopes::run with separate globals {SUBSTACK}"
        INPUT_SPECS = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class bind_var_to_scope(ThirdBlock):
        OPCODE = "&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope"
        INPUT_SPECS = (
            ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        kind: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class configure_next_function_args(ThirdBlock):
        OPCODE = "&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)"
        INPUT_SPECS = (
            ("ARGNAMES", "argnames", p.SRBlockAndTextInputValue, None),
            ("ARGDEFAULTS", "argdefaults", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        argnames: INPUT_COMPATIBLE_T
        argdefaults: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_function_at(ThirdBlock):
        OPCODE = "&gceFuncsScopes::create function at var (NAME) {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_function_named(ThirdBlock):
        OPCODE = "&gceFuncsScopes::create function named (NAME) {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class return_value(ThirdBlock):
        OPCODE = "&gceFuncsScopes::return (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class call_function(ThirdBlock):
        OPCODE = "&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)"
        INPUT_SPECS = (
            ("FUNC", "func", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        func: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class object_as_string(ThirdBlock):
        OPCODE = "&gceFuncsScopes::(VALUE) as string"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class typeof_value(ThirdBlock):
        OPCODE = "&gceFuncsScopes::typeof (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class typeof_value_is_menu(ThirdBlock):
        OPCODE = "&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?"
        INPUT_SPECS = (
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class typeof_value_selection(ThirdBlock):
        OPCODE = "&gceFuncsScopes::([TYPE])"
        INPUT_SPECS = (("TYPE", "type", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class check_identity(ThirdBlock):
        OPCODE = "&gceFuncsScopes::(VALUE1) is (VALUE2) ?"
        INPUT_SPECS = (
            ("VALUE1", "value1", p.SRBlockAndTextInputValue, None),
            ("VALUE2", "value2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        value1: INPUT_COMPATIBLE_T
        value2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class nothing(ThirdBlock):
        OPCODE = "&gceFuncsScopes::Nothing"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class execute_expression(ThirdBlock):
        OPCODE = "&gceFuncsScopes::execute expression (EXPR)"
        INPUT_SPECS = (("EXPR", "expr", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        expr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_variable_available_kind(ThirdBlock):
        OPCODE = "&gceFuncsScopes::#menu:variableAvailableKind"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_bind_var_origin_kind(ThirdBlock):
        OPCODE = "&gceFuncsScopes::#menu:bindVarOriginKind"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_typeof_menu(ThirdBlock):
        OPCODE = "&gceFuncsScopes::#menu:typeofMenu"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
