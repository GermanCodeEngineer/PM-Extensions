from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class SPjavascriptV2:

    @grepr_dataclass()
    class code_input(ThirdBlock):
        OPCODE = "&SPjavascriptV2::(CODE)"
        code: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CODE", "code", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("CODE", "code", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class argument_report(ThirdBlock):
        OPCODE = "&SPjavascriptV2::data"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class return_data(ThirdBlock):
        OPCODE = "&SPjavascriptV2::return (DATA)"
        data: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("DATA", "data", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("DATA", "data", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class js_reporter(ThirdBlock):
        OPCODE = "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}"
        code: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CODE", "code", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("CODE", "code", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class js_boolean(ThirdBlock):
        OPCODE = "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsBoolean}}"
        code: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CODE", "code", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("CODE", "code", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class js_reporter_binded(ThirdBlock):
        OPCODE = "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsReporterBinded}}"
        args: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.code_input,
                    ),
                    ("ARGS", "args", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.code_input,
                    ),
                    ("ARGS", "args", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class js_boolean_binded(ThirdBlock):
        OPCODE = "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsBooleanBinded}}"
        args: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.code_input,
                    ),
                    ("ARGS", "args", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.code_input,
                    ),
                    ("ARGS", "args", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class define_global_func(ThirdBlock):
        OPCODE = (
            "&SPjavascriptV2::create global function named (NAME) with code {:CODE:}"
        )
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.code_input,
                    ),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.code_input,
                    ),
                ),
                (),
            )

    @grepr_dataclass()
    class define_scratch_code(ThirdBlock):
        OPCODE = "&SPjavascriptV2::create local function named (NAME) with code {:CODE:} {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.argument_report,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.argument_report,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class delete_global_func(ThirdBlock):
        OPCODE = "&SPjavascriptV2::delete global function (NAME)"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NAME", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NAME", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class js_command_binded(ThirdBlock):
        OPCODE = "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsCommandBinded}}"
        args: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.code_input,
                    ),
                    ("ARGS", "args", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "CODE",
                        "code",
                        p.SREmbeddedBlockInputValue,
                        SPjavascriptV2.code_input,
                    ),
                    ("ARGS", "args", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class js_command(ThirdBlock):
        OPCODE = "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsCommand}}"
        code: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CODE", "code", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("CODE", "code", p.SRBlockAndTextInputValue, None),), ()
            )
