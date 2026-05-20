from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class control:

    class wait(ThirdBlock):

        def __init__(self, seconds: INPUT_COMPATIBLE_T):
            self.seconds = seconds

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

    class waitsecondsoruntil(ThirdBlock):

        def __init__(self, seconds: INPUT_COMPATIBLE_T, condition: INPUT_COMPATIBLE_T):
            self.seconds = seconds
            self.condition = condition

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

    class repeat(ThirdBlock):

        def __init__(self, times: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T):
            self.times = times
            self.body = body

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

    class forever(ThirdBlock):

        def __init__(self, body: INPUT_COMPATIBLE_T):
            self.body = body

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::forever {BODY}",
                inputs={
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue)
                },
                dropdowns={},
            )

    class for_each(ThirdBlock):

        def __init__(
            self, range: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T, variable: str
        ):
            self.range = range
            self.body = body
            self.variable = variable

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

    class exit_loop(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::escape loop", inputs={}, dropdowns={})

    class continue_loop(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::continue loop", inputs={}, dropdowns={})

    class switch(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T, cases: INPUT_COMPATIBLE_T):
            self.condition = condition
            self.cases = cases

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

    class switch_default(ThirdBlock):

        def __init__(
            self,
            condition: INPUT_COMPATIBLE_T,
            cases: INPUT_COMPATIBLE_T,
            default: INPUT_COMPATIBLE_T,
        ):
            self.condition = condition
            self.cases = cases
            self.default = default

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

    class exit_case(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::exit case", inputs={}, dropdowns={})

    class case_next(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T):
            self.condition = condition

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

    class case(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T):
            self.condition = condition
            self.body = body

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

    class if_(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T, then: INPUT_COMPATIBLE_T):
            self.condition = condition
            self.then = then

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

    class if_else(ThirdBlock):

        def __init__(
            self,
            condition: INPUT_COMPATIBLE_T,
            then: INPUT_COMPATIBLE_T,
            else_: INPUT_COMPATIBLE_T,
        ):
            self.condition = condition
            self.then = then
            self.else_ = else_

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

    class if_return_else_return(ThirdBlock):

        def __init__(
            self,
            condition: INPUT_COMPATIBLE_T,
            truevalue: INPUT_COMPATIBLE_T,
            falsevalue: INPUT_COMPATIBLE_T,
        ):
            self.condition = condition
            self.truevalue = truevalue
            self.falsevalue = falsevalue

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

    class wait_until(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T):
            self.condition = condition

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

    class repeat_until(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T):
            self.condition = condition
            self.body = body

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

    class while_(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T):
            self.condition = condition
            self.body = body

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

    class all_at_once(ThirdBlock):

        def __init__(self, body: INPUT_COMPATIBLE_T):
            self.body = body

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::all at once {BODY}",
                inputs={
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue)
                },
                dropdowns={},
            )

    class run_as_sprite(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T):
            self.target = target
            self.body = body

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

    class try_catch(ThirdBlock):

        def __init__(self, try_: INPUT_COMPATIBLE_T, iferror: INPUT_COMPATIBLE_T):
            self.try_ = try_
            self.iferror = iferror

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

    class throw_error(ThirdBlock):

        def __init__(self, error: INPUT_COMPATIBLE_T):
            self.error = error

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

    class error(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::error", inputs={}, dropdowns={})

    class back_to_green_flag(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::run flag", inputs={}, dropdowns={})

    class stop_sprite(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class stop(ThirdBlock):

        def __init__(self, target: str):
            self.target = target

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

    class start_as_clone(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::when I start as a clone", inputs={}, dropdowns={}
            )

    class create_clone_of(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class delete_clones_of(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class delete_this_clone(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::delete this clone", inputs={}, dropdowns={}
            )

    class is_clone(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::is clone?", inputs={}, dropdowns={})

    class stop_sprite_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::#STOP SPRITE MENU", inputs={}, dropdowns={}
            )

    class create_clone_of_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::#CLONE TARGET MENU", inputs={}, dropdowns={}
            )

    class run_as_sprite_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::#RUN AS SPRITE MENU", inputs={}, dropdowns={}
            )

    class expandable_if(ThirdBlock):

        def __init__(self):
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    class repeat_for_seconds(ThirdBlock):

        def __init__(self, times: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.times = times
            self.substack = substack

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

    class inline_stack_output(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

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

    class waittick(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::wait until next tick", inputs={}, dropdowns={}
            )

    class get_counter(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::counter", inputs={}, dropdowns={})

    class incr_counter(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::increment counter", inputs={}, dropdowns={}
            )

    class decr_counter(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&control::decrement counter", inputs={}, dropdowns={}
            )

    class set_counter(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

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

    class clear_counter(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&control::clear counter", inputs={}, dropdowns={})
