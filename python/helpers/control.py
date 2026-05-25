from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class control:

    @grepr_dataclass()
    class wait(ThirdBlock):
        OPCODE = "&control::wait (SECONDS) seconds"
        seconds: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class waitsecondsoruntil(ThirdBlock):
        OPCODE = "&control::wait (SECONDS) seconds or until <CONDITION>"
        seconds: INPUT_COMPATIBLE_T
        condition: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class repeat(ThirdBlock):
        OPCODE = "&control::repeat (TIMES) {BODY}"
        times: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TIMES", "times", p.SRBlockAndTextInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TIMES", "times", p.SRBlockAndTextInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class forever(ThirdBlock):
        OPCODE = "&control::forever {BODY}"
        body: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("BODY", "body", p.SRScriptInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BODY", "body", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&control::for each [VARIABLE] in (RANGE) {BODY}"
        range: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T
        variable: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("RANGE", "range", p.SRBlockAndTextInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (("VARIABLE", "variable"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("RANGE", "range", p.SRBlockAndTextInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (("VARIABLE", "variable"),),
            )

    @grepr_dataclass()
    class exit_loop(ThirdBlock):
        OPCODE = "&control::escape loop"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class continue_loop(ThirdBlock):
        OPCODE = "&control::continue loop"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class switch(ThirdBlock):
        OPCODE = "&control::switch (CONDITION) {CASES}"
        condition: INPUT_COMPATIBLE_T
        cases: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
                    ("CASES", "cases", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
                    ("CASES", "cases", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class switch_default(ThirdBlock):
        OPCODE = "&control::switch (CONDITION) {CASES} default {DEFAULT}"
        condition: INPUT_COMPATIBLE_T
        cases: INPUT_COMPATIBLE_T
        default: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
                    ("CASES", "cases", p.SRScriptInputValue, None),
                    ("DEFAULT", "default", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
                    ("CASES", "cases", p.SRScriptInputValue, None),
                    ("DEFAULT", "default", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class exit_case(ThirdBlock):
        OPCODE = "&control::exit case"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class case_next(ThirdBlock):
        OPCODE = "&control::run next case when (CONDITION)"
        condition: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class case(ThirdBlock):
        OPCODE = "&control::case (CONDITION) {BODY}"
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndTextInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndTextInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class if_(ThirdBlock):
        OPCODE = "&control::if <CONDITION> then {THEN}"
        condition: INPUT_COMPATIBLE_T
        then: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("THEN", "then", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("THEN", "then", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class if_else(ThirdBlock):
        OPCODE = "&control::if <CONDITION> then {THEN} else {ELSE}"
        condition: INPUT_COMPATIBLE_T
        then: INPUT_COMPATIBLE_T
        else_: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("THEN", "then", p.SRScriptInputValue, None),
                    ("ELSE", "else_", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("THEN", "then", p.SRScriptInputValue, None),
                    ("ELSE", "else_", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class if_return_else_return(ThirdBlock):
        OPCODE = "&control::if <CONDITION> then (TRUEVALUE) else (FALSEVALUE)"
        condition: INPUT_COMPATIBLE_T
        truevalue: INPUT_COMPATIBLE_T
        falsevalue: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("TRUEVALUE", "truevalue", p.SRBlockAndTextInputValue, None),
                    ("FALSEVALUE", "falsevalue", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("TRUEVALUE", "truevalue", p.SRBlockAndTextInputValue, None),
                    ("FALSEVALUE", "falsevalue", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class wait_until(ThirdBlock):
        OPCODE = "&control::wait until <CONDITION>"
        condition: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class repeat_until(ThirdBlock):
        OPCODE = "&control::repeat until <CONDITION> {BODY}"
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class while_(ThirdBlock):
        OPCODE = "&control::while <CONDITION> {BODY}"
        condition: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class all_at_once(ThirdBlock):
        OPCODE = "&control::all at once {BODY}"
        body: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("BODY", "body", p.SRScriptInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BODY", "body", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class run_as_sprite(ThirdBlock):
        OPCODE = "&control::as ([TARGET]) {BODY}"
        target: INPUT_COMPATIBLE_T
        body: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
                    ("BODY", "body", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class try_catch(ThirdBlock):
        OPCODE = "&control::try to do {TRY} if a block errors {IFERROR}"
        try_: INPUT_COMPATIBLE_T
        iferror: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TRY", "try_", p.SRScriptInputValue, None),
                    ("IFERROR", "iferror", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TRY", "try_", p.SRScriptInputValue, None),
                    ("IFERROR", "iferror", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class throw_error(ThirdBlock):
        OPCODE = "&control::throw error (ERROR)"
        error: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ERROR", "error", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ERROR", "error", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class error(ThirdBlock):
        OPCODE = "&control::error"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class back_to_green_flag(ThirdBlock):
        OPCODE = "&control::run flag"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class stop_sprite(ThirdBlock):
        OPCODE = "&control::stop sprite ([TARGET])"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE = "&control::stop script [TARGET]"
        target: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("TARGET", "target"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("TARGET", "target"),))

    @grepr_dataclass()
    class start_as_clone(ThirdBlock):
        OPCODE = "&control::when I start as a clone"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class create_clone_of(ThirdBlock):
        OPCODE = "&control::create clone of ([TARGET])"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class delete_clones_of(ThirdBlock):
        OPCODE = "&control::delete clones of ([TARGET])"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class delete_this_clone(ThirdBlock):
        OPCODE = "&control::delete this clone"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class is_clone(ThirdBlock):
        OPCODE = "&control::is clone?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class stop_sprite_menu(ThirdBlock):
        OPCODE = "&control::#STOP SPRITE MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class create_clone_of_menu(ThirdBlock):
        OPCODE = "&control::#CLONE TARGET MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class run_as_sprite_menu(ThirdBlock):
        OPCODE = "&control::#RUN AS SPRITE MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class expandable_if(ThirdBlock):
        OPCODE = "&control::{{EXPANDABLE IF-THEN-ELSE CHAIN}}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    @grepr_dataclass()
    class repeat_for_seconds(ThirdBlock):
        OPCODE = "&control::repeat for (TIMES) seconds {SUBSTACK}"
        times: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TIMES", "times", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TIMES", "times", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class inline_stack_output(ThirdBlock):
        OPCODE = "&control::inline block {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SUBSTACK", "substack", p.SRScriptInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SUBSTACK", "substack", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class waittick(ThirdBlock):
        OPCODE = "&control::wait until next tick"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class get_counter(ThirdBlock):
        OPCODE = "&control::counter"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class incr_counter(ThirdBlock):
        OPCODE = "&control::increment counter"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class decr_counter(ThirdBlock):
        OPCODE = "&control::decrement counter"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class set_counter(ThirdBlock):
        OPCODE = "&control::set counter to (VALUE)"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class clear_counter(ThirdBlock):
        OPCODE = "&control::clear counter"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
