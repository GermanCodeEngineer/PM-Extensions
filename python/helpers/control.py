from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class control:

    @grepr_dataclass()
    class wait(ThirdBlock):
        OPCODE: ClassVar = "&control::wait (SECONDS) seconds"
        INPUT_SPECS: ClassVar = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class waitsecondsoruntil(ThirdBlock):
        OPCODE: ClassVar = "&control::wait (SECONDS) seconds or until <CONDITION>"
        INPUT_SPECS: ClassVar = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        seconds: INPUT_COMPATIBLE_T
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class repeat(ThirdBlock):
        OPCODE: ClassVar = "&control::repeat (TIMES) {BODY}"
        INPUT_SPECS: ClassVar = (
            ("TIMES", "times", p.SRBlockAndTextInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        times: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class forever(ThirdBlock):
        OPCODE: ClassVar = "&control::forever {BODY}"
        INPUT_SPECS: ClassVar = (("BODY", "body", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE: ClassVar = "&control::for each [VARIABLE] in (RANGE) {BODY}"
        INPUT_SPECS: ClassVar = (
            ("RANGE", "range", p.SRBlockAndTextInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
        range: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T
        variable: str

    @grepr_dataclass()
    class exit_loop(ThirdBlock):
        OPCODE: ClassVar = "&control::escape loop"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class continue_loop(ThirdBlock):
        OPCODE: ClassVar = "&control::continue loop"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class switch(ThirdBlock):
        OPCODE: ClassVar = "&control::switch (CONDITION) {CASES}"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
            ("CASES", "cases", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T
        cases: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class switch_default(ThirdBlock):
        OPCODE: ClassVar = "&control::switch (CONDITION) {CASES} default {DEFAULT}"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
            ("CASES", "cases", p.SRScriptInputValue, None),
            ("DEFAULT", "default", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T
        cases: INPUT_COMPATIBLE_T
        default: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class exit_case(ThirdBlock):
        OPCODE: ClassVar = "&control::exit case"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class case_next(ThirdBlock):
        OPCODE: ClassVar = "&control::run next case when (CONDITION)"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class case(ThirdBlock):
        OPCODE: ClassVar = "&control::case (CONDITION) {BODY}"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndTextInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_(ThirdBlock):
        OPCODE: ClassVar = "&control::if <CONDITION> then {THEN}"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("THEN", "then", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T
        then: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_else(ThirdBlock):
        OPCODE: ClassVar = "&control::if <CONDITION> then {THEN} else {ELSE}"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("THEN", "then", p.SRScriptInputValue, None),
            ("ELSE", "else_", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T
        then: INPUT_COMPATIBLE_T
        else_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_return_else_return(ThirdBlock):
        OPCODE: ClassVar = "&control::if <CONDITION> then (TRUEVALUE) else (FALSEVALUE)"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("TRUEVALUE", "truevalue", p.SRBlockAndTextInputValue, None),
            ("FALSEVALUE", "falsevalue", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T
        truevalue: INPUT_COMPATIBLE_T
        falsevalue: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class wait_until(ThirdBlock):
        OPCODE: ClassVar = "&control::wait until <CONDITION>"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class repeat_until(ThirdBlock):
        OPCODE: ClassVar = "&control::repeat until <CONDITION> {BODY}"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class while_(ThirdBlock):
        OPCODE: ClassVar = "&control::while <CONDITION> {BODY}"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class all_at_once(ThirdBlock):
        OPCODE: ClassVar = "&control::all at once {BODY}"
        INPUT_SPECS: ClassVar = (("BODY", "body", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class run_as_sprite(ThirdBlock):
        OPCODE: ClassVar = "&control::as ([TARGET]) {BODY}"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            ("BODY", "body", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class try_catch(ThirdBlock):
        OPCODE: ClassVar = "&control::try to do {TRY} if a block errors {IFERROR}"
        INPUT_SPECS: ClassVar = (
            ("TRY", "try_", p.SRScriptInputValue, None),
            ("IFERROR", "iferror", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        try_: INPUT_COMPATIBLE_T
        iferror: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class throw_error(ThirdBlock):
        OPCODE: ClassVar = "&control::throw error (ERROR)"
        INPUT_SPECS: ClassVar = (("ERROR", "error", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        error: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class error(ThirdBlock):
        OPCODE: ClassVar = "&control::error"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class back_to_green_flag(ThirdBlock):
        OPCODE: ClassVar = "&control::run flag"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class stop_sprite(ThirdBlock):
        OPCODE: ClassVar = "&control::stop sprite ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE: ClassVar = "&control::stop script [TARGET]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TARGET", "target"),)
        target: str

    @grepr_dataclass()
    class start_as_clone(ThirdBlock):
        OPCODE: ClassVar = "&control::when I start as a clone"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class create_clone_of(ThirdBlock):
        OPCODE: ClassVar = "&control::create clone of ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_clones_of(ThirdBlock):
        OPCODE: ClassVar = "&control::delete clones of ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_this_clone(ThirdBlock):
        OPCODE: ClassVar = "&control::delete this clone"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class is_clone(ThirdBlock):
        OPCODE: ClassVar = "&control::is clone?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class stop_sprite_menu(ThirdBlock):
        OPCODE: ClassVar = "&control::#STOP SPRITE MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class create_clone_of_menu(ThirdBlock):
        OPCODE: ClassVar = "&control::#CLONE TARGET MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class run_as_sprite_menu(ThirdBlock):
        OPCODE: ClassVar = "&control::#RUN AS SPRITE MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class expandable_if(ThirdBlock):
        OPCODE: ClassVar = "&control::{{EXPANDABLE IF-THEN-ELSE CHAIN}}"
        INPUT_SPECS: ClassVar = None
        DROPDOWN_SPECS: ClassVar = None

    @grepr_dataclass()
    class repeat_for_seconds(ThirdBlock):
        OPCODE: ClassVar = "&control::repeat for (TIMES) seconds {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("TIMES", "times", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        times: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class inline_stack_output(ThirdBlock):
        OPCODE: ClassVar = "&control::inline block {SUBSTACK}"
        INPUT_SPECS: ClassVar = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class waittick(ThirdBlock):
        OPCODE: ClassVar = "&control::wait until next tick"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class get_counter(ThirdBlock):
        OPCODE: ClassVar = "&control::counter"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class incr_counter(ThirdBlock):
        OPCODE: ClassVar = "&control::increment counter"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class decr_counter(ThirdBlock):
        OPCODE: ClassVar = "&control::decrement counter"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class set_counter(ThirdBlock):
        OPCODE: ClassVar = "&control::set counter to (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clear_counter(ThirdBlock):
        OPCODE: ClassVar = "&control::clear counter"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
