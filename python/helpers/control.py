from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class control:

    @staticmethod
    def wait(seconds: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::wait (SECONDS) seconds",
            inputs={
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def waitsecondsoruntil(
        seconds: INPUT_COMPATIBLE_T, condition: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::wait (SECONDS) seconds or until <CONDITION>",
            inputs={
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue),
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def repeat(times: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::repeat (TIMES) {BODY}",
            inputs={
                "TIMES": InputValue.try_as_input(times, p.SRBlockAndTextInputValue),
                "BODY": InputValue.try_as_input(body, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def forever(body: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::forever {BODY}",
            inputs={"BODY": InputValue.try_as_input(body, p.SRScriptInputValue)},
            dropdowns={},
        )

    @staticmethod
    def for_each(
        range: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T, variable: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::for each [VARIABLE] in (RANGE) {BODY}",
            inputs={
                "RANGE": InputValue.try_as_input(range, p.SRBlockAndTextInputValue),
                "BODY": InputValue.try_as_input(body, p.SRScriptInputValue),
            },
            dropdowns={
                "VARIABLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, variable)
            },
        )

    @staticmethod
    def exit_loop() -> p.SRBlock:
        return p.SRBlock(opcode="&control::escape loop", inputs={}, dropdowns={})

    @staticmethod
    def continue_loop() -> p.SRBlock:
        return p.SRBlock(opcode="&control::continue loop", inputs={}, dropdowns={})

    @staticmethod
    def switch(condition: INPUT_COMPATIBLE_T, cases: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::switch (CONDITION) {CASES}",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockOnlyInputValue
                ),
                "CASES": InputValue.try_as_input(cases, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def switch_default(
        condition: INPUT_COMPATIBLE_T,
        cases: INPUT_COMPATIBLE_T,
        default: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::switch (CONDITION) {CASES} default {DEFAULT}",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockOnlyInputValue
                ),
                "CASES": InputValue.try_as_input(cases, p.SRScriptInputValue),
                "DEFAULT": InputValue.try_as_input(default, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def exit_case() -> p.SRBlock:
        return p.SRBlock(opcode="&control::exit case", inputs={}, dropdowns={})

    @staticmethod
    def case_next(condition: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::run next case when (CONDITION)",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def case(condition: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::case (CONDITION) {BODY}",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndTextInputValue
                ),
                "BODY": InputValue.try_as_input(body, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def if_(condition: INPUT_COMPATIBLE_T, then: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::if <CONDITION> then {THEN}",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "THEN": InputValue.try_as_input(then, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def if_else(
        condition: INPUT_COMPATIBLE_T,
        then: INPUT_COMPATIBLE_T,
        else_: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::if <CONDITION> then {THEN} else {ELSE}",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "THEN": InputValue.try_as_input(then, p.SRScriptInputValue),
                "ELSE": InputValue.try_as_input(else_, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def if_return_else_return(
        condition: INPUT_COMPATIBLE_T,
        truevalue: INPUT_COMPATIBLE_T,
        falsevalue: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::if <CONDITION> then (TRUEVALUE) else (FALSEVALUE)",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "TRUEVALUE": InputValue.try_as_input(
                    truevalue, p.SRBlockAndTextInputValue
                ),
                "FALSEVALUE": InputValue.try_as_input(
                    falsevalue, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def wait_until(condition: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::wait until <CONDITION>",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def repeat_until(
        condition: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::repeat until <CONDITION> {BODY}",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "BODY": InputValue.try_as_input(body, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def while_(condition: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::while <CONDITION> {BODY}",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "BODY": InputValue.try_as_input(body, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def all_at_once(body: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::all at once {BODY}",
            inputs={"BODY": InputValue.try_as_input(body, p.SRScriptInputValue)},
            dropdowns={},
        )

    @staticmethod
    def run_as_sprite(
        target: INPUT_COMPATIBLE_T, body: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::as ([TARGET]) {BODY}",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                ),
                "BODY": InputValue.try_as_input(body, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def try_catch(try_: INPUT_COMPATIBLE_T, iferror: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::try to do {TRY} if a block errors {IFERROR}",
            inputs={
                "TRY": InputValue.try_as_input(try_, p.SRScriptInputValue),
                "IFERROR": InputValue.try_as_input(iferror, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def throw_error(error: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::throw error (ERROR)",
            inputs={
                "ERROR": InputValue.try_as_input(error, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def error() -> p.SRBlock:
        return p.SRBlock(opcode="&control::error", inputs={}, dropdowns={})

    @staticmethod
    def back_to_green_flag() -> p.SRBlock:
        return p.SRBlock(opcode="&control::run flag", inputs={}, dropdowns={})

    @staticmethod
    def stop_sprite(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::stop sprite ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def stop(target: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::stop script [TARGET]",
            inputs={},
            dropdowns={
                "TARGET": p.SRDropdownValue(p.DropdownValueKind.STANDARD, target)
            },
        )

    @staticmethod
    def start_as_clone() -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::when I start as a clone", inputs={}, dropdowns={}
        )

    @staticmethod
    def create_clone_of(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::create clone of ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def delete_clones_of(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::delete clones of ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def delete_this_clone() -> p.SRBlock:
        return p.SRBlock(opcode="&control::delete this clone", inputs={}, dropdowns={})

    @staticmethod
    def is_clone() -> p.SRBlock:
        return p.SRBlock(opcode="&control::is clone?", inputs={}, dropdowns={})

    @staticmethod
    def stop_sprite_menu() -> p.SRBlock:
        return p.SRBlock(opcode="&control::#STOP SPRITE MENU", inputs={}, dropdowns={})

    @staticmethod
    def create_clone_of_menu() -> p.SRBlock:
        return p.SRBlock(opcode="&control::#CLONE TARGET MENU", inputs={}, dropdowns={})

    @staticmethod
    def run_as_sprite_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::#RUN AS SPRITE MENU", inputs={}, dropdowns={}
        )

    @staticmethod
    def expandable_if() -> p.SRBlock:
        raise NotImplementedError(
            "This opcode is not supported yet, because it requires flexible input counts."
        )

    @staticmethod
    def repeat_for_seconds(
        times: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::repeat for (TIMES) seconds {SUBSTACK}",
            inputs={
                "TIMES": InputValue.try_as_input(times, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def inline_stack_output(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::inline block {SUBSTACK}",
            inputs={
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def waittick() -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::wait until next tick", inputs={}, dropdowns={}
        )

    @staticmethod
    def get_counter() -> p.SRBlock:
        return p.SRBlock(opcode="&control::counter", inputs={}, dropdowns={})

    @staticmethod
    def incr_counter() -> p.SRBlock:
        return p.SRBlock(opcode="&control::increment counter", inputs={}, dropdowns={})

    @staticmethod
    def decr_counter() -> p.SRBlock:
        return p.SRBlock(opcode="&control::decrement counter", inputs={}, dropdowns={})

    @staticmethod
    def set_counter(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&control::set counter to (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def clear_counter() -> p.SRBlock:
        return p.SRBlock(opcode="&control::clear counter", inputs={}, dropdowns={})
