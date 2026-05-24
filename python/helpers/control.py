from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class control:

    @grepr_dataclass()
    class wait(ThirdBlock):
        seconds: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::wait (SECONDS) seconds",
                inputs={
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class waitsecondsoruntil(ThirdBlock):
        seconds: INPUT_COMPATIBLE_T
        condition: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::wait (SECONDS) seconds or until <CONDITION>",
                inputs={
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    ),
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class repeat(ThirdBlock):
        times: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::repeat (TIMES) {BODY}",
                inputs={
                    "TIMES": ThirdInputValue.as_input(
                        self.times, p.SRBlockAndTextInputValue
                    ),
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class forever(ThirdBlock):
        body: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::forever {BODY}",
                inputs={
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class for_each(ThirdBlock):
        range: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T
        variable: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::for each [VARIABLE] in (RANGE) {BODY}",
                inputs={
                    "RANGE": ThirdInputValue.as_input(
                        self.range, p.SRBlockAndTextInputValue
                    ),
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue),
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    @grepr_dataclass()
    class exit_loop(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::escape loop", inputs={}, dropdowns={})

    @grepr_dataclass()
    class continue_loop(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::continue loop", inputs={}, dropdowns={})

    @grepr_dataclass()
    class switch(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        cases: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::switch (CONDITION) {CASES}",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockOnlyInputValue
                    ),
                    "CASES": ThirdInputValue.as_input(self.cases, p.SRScriptInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class switch_default(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        cases: INPUT_COMPATIBLE_T
        default: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::switch (CONDITION) {CASES} default {DEFAULT}",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockOnlyInputValue
                    ),
                    "CASES": ThirdInputValue.as_input(self.cases, p.SRScriptInputValue),
                    "DEFAULT": ThirdInputValue.as_input(
                        self.default, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class exit_case(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::exit case", inputs={}, dropdowns={})

    @grepr_dataclass()
    class case_next(ThirdBlock):
        condition: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::run next case when (CONDITION)",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class case(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::case (CONDITION) {BODY}",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndTextInputValue
                    ),
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class if_(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        then: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::if <CONDITION> then {THEN}",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "THEN": ThirdInputValue.as_input(self.then, p.SRScriptInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class if_else(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        then: INPUT_COMPATIBLE_T
        else_: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::if <CONDITION> then {THEN} else {ELSE}",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "THEN": ThirdInputValue.as_input(self.then, p.SRScriptInputValue),
                    "ELSE": ThirdInputValue.as_input(self.else_, p.SRScriptInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class if_return_else_return(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        truevalue: INPUT_COMPATIBLE_T
        falsevalue: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::if <CONDITION> then (TRUEVALUE) else (FALSEVALUE)",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "TRUEVALUE": ThirdInputValue.as_input(
                        self.truevalue, p.SRBlockAndTextInputValue
                    ),
                    "FALSEVALUE": ThirdInputValue.as_input(
                        self.falsevalue, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class wait_until(ThirdBlock):
        condition: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::wait until <CONDITION>",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class repeat_until(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::repeat until <CONDITION> {BODY}",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class while_(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::while <CONDITION> {BODY}",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class all_at_once(ThirdBlock):
        body: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::all at once {BODY}",
                inputs={
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class run_as_sprite(ThirdBlock):
        target: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::as ([TARGET]) {BODY}",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    ),
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class try_catch(ThirdBlock):
        try_: INPUT_COMPATIBLE_T
        iferror: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::try to do {TRY} if a block errors {IFERROR}",
                inputs={
                    "TRY": ThirdInputValue.as_input(self.try_, p.SRScriptInputValue),
                    "IFERROR": ThirdInputValue.as_input(
                        self.iferror, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class throw_error(ThirdBlock):
        error: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::throw error (ERROR)",
                inputs={
                    "ERROR": ThirdInputValue.as_input(
                        self.error, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class error(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::error", inputs={}, dropdowns={})

    @grepr_dataclass()
    class back_to_green_flag(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::run flag", inputs={}, dropdowns={})

    @grepr_dataclass()
    class stop_sprite(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::stop sprite ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class stop(ThirdBlock):
        target: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::stop script [TARGET]",
                inputs={},
                dropdowns={
                    "TARGET": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.target
                    )
                },
            )

    @grepr_dataclass()
    class start_as_clone(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::when I start as a clone", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class create_clone_of(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::create clone of ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class delete_clones_of(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::delete clones of ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class delete_this_clone(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::delete this clone", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class is_clone(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::is clone?", inputs={}, dropdowns={})

    @grepr_dataclass()
    class stop_sprite_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::#STOP SPRITE MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class create_clone_of_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::#CLONE TARGET MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class run_as_sprite_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::#RUN AS SPRITE MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class expandable_if(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    @grepr_dataclass()
    class repeat_for_seconds(ThirdBlock):
        times: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::repeat for (TIMES) seconds {SUBSTACK}",
                inputs={
                    "TIMES": ThirdInputValue.as_input(
                        self.times, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class inline_stack_output(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::inline block {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class waittick(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::wait until next tick", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class get_counter(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::counter", inputs={}, dropdowns={})

    @grepr_dataclass()
    class incr_counter(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::increment counter", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class decr_counter(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::decrement counter", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class set_counter(ThirdBlock):
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::set counter to (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class clear_counter(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::clear counter", inputs={}, dropdowns={})
