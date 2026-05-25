from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class control:

    @grepr_dataclass()
    class wait(ThirdBlock):
        OPCODE = "&control::wait (SECONDS) seconds"
        INPUT_SPECS = (("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class waitsecondsoruntil(ThirdBlock):
        OPCODE = "&control::wait (SECONDS) seconds or until <CONDITION>"
        INPUT_SPECS = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        seconds: INPUT_COMPATIBLE_T
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class repeat(ThirdBlock):
        OPCODE = "&control::repeat (TIMES) {BODY}"
        INPUT_SPECS = (
            ("TIMES", "times", p.SRBlockAndTextInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        times: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class forever(ThirdBlock):
        OPCODE = "&control::forever {BODY}"
        INPUT_SPECS = (("BODY", "body", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&control::for each [VARIABLE] in (RANGE) {BODY}"
        INPUT_SPECS = (
            ("RANGE", "range", p.SRBlockAndTextInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = (("VARIABLE", "variable"),)
        range: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T
        variable: str

    @grepr_dataclass()
    class exit_loop(ThirdBlock):
        OPCODE = "&control::escape loop"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class continue_loop(ThirdBlock):
        OPCODE = "&control::continue loop"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class switch(ThirdBlock):
        OPCODE = "&control::switch (CONDITION) {CASES}"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
            ("CASES", "cases", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        cases: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class switch_default(ThirdBlock):
        OPCODE = "&control::switch (CONDITION) {CASES} default {DEFAULT}"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
            ("CASES", "cases", p.SRScriptInputValue, None),
            ("DEFAULT", "default", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        cases: INPUT_COMPATIBLE_T
        default: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class exit_case(ThirdBlock):
        OPCODE = "&control::exit case"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class case_next(ThirdBlock):
        OPCODE = "&control::run next case when (CONDITION)"
        INPUT_SPECS = (("CONDITION", "condition", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class case(ThirdBlock):
        OPCODE = "&control::case (CONDITION) {BODY}"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockAndTextInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_(ThirdBlock):
        OPCODE = "&control::if <CONDITION> then {THEN}"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("THEN", "then", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        then: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_else(ThirdBlock):
        OPCODE = "&control::if <CONDITION> then {THEN} else {ELSE}"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("THEN", "then", p.SRScriptInputValue, None),
            ("ELSE", "else_", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        then: INPUT_COMPATIBLE_T
        else_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_return_else_return(ThirdBlock):
        OPCODE = "&control::if <CONDITION> then (TRUEVALUE) else (FALSEVALUE)"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("TRUEVALUE", "truevalue", p.SRBlockAndTextInputValue, None),
            ("FALSEVALUE", "falsevalue", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        truevalue: INPUT_COMPATIBLE_T
        falsevalue: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class wait_until(ThirdBlock):
        OPCODE = "&control::wait until <CONDITION>"
        INPUT_SPECS = (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),)
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class repeat_until(ThirdBlock):
        OPCODE = "&control::repeat until <CONDITION> {BODY}"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class while_(ThirdBlock):
        OPCODE = "&control::while <CONDITION> {BODY}"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class all_at_once(ThirdBlock):
        OPCODE = "&control::all at once {BODY}"
        INPUT_SPECS = (("BODY", "body", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class run_as_sprite(ThirdBlock):
        OPCODE = "&control::as ([TARGET]) {BODY}"
        INPUT_SPECS = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class try_catch(ThirdBlock):
        OPCODE = "&control::try to do {TRY} if a block errors {IFERROR}"
        INPUT_SPECS = (
            ("TRY", "try_", p.SRScriptInputValue, None),
            ("IFERROR", "iferror", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        try_: INPUT_COMPATIBLE_T
        iferror: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class throw_error(ThirdBlock):
        OPCODE = "&control::throw error (ERROR)"
        INPUT_SPECS = (("ERROR", "error", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        error: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class error(ThirdBlock):
        OPCODE = "&control::error"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class back_to_green_flag(ThirdBlock):
        OPCODE = "&control::run flag"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class stop_sprite(ThirdBlock):
        OPCODE = "&control::stop sprite ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE = "&control::stop script [TARGET]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TARGET", "target"),)
        target: str

    @grepr_dataclass()
    class start_as_clone(ThirdBlock):
        OPCODE = "&control::when I start as a clone"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class create_clone_of(ThirdBlock):
        OPCODE = "&control::create clone of ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_clones_of(ThirdBlock):
        OPCODE = "&control::delete clones of ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_this_clone(ThirdBlock):
        OPCODE = "&control::delete this clone"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class is_clone(ThirdBlock):
        OPCODE = "&control::is clone?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class stop_sprite_menu(ThirdBlock):
        OPCODE = "&control::#STOP SPRITE MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class create_clone_of_menu(ThirdBlock):
        OPCODE = "&control::#CLONE TARGET MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class run_as_sprite_menu(ThirdBlock):
        OPCODE = "&control::#RUN AS SPRITE MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class expandable_if(ThirdBlock):
        OPCODE = "&control::{{EXPANDABLE IF-THEN-ELSE CHAIN}}"
        INPUT_SPECS = None
        DROPDOWN_SPECS = None

    @grepr_dataclass()
    class repeat_for_seconds(ThirdBlock):
        OPCODE = "&control::repeat for (TIMES) seconds {SUBSTACK}"
        INPUT_SPECS = (
            ("TIMES", "times", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        times: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class inline_stack_output(ThirdBlock):
        OPCODE = "&control::inline block {SUBSTACK}"
        INPUT_SPECS = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class waittick(ThirdBlock):
        OPCODE = "&control::wait until next tick"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class get_counter(ThirdBlock):
        OPCODE = "&control::counter"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class incr_counter(ThirdBlock):
        OPCODE = "&control::increment counter"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class decr_counter(ThirdBlock):
        OPCODE = "&control::decrement counter"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class set_counter(ThirdBlock):
        OPCODE = "&control::set counter to (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clear_counter(ThirdBlock):
        OPCODE = "&control::clear counter"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
