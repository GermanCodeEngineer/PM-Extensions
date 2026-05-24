from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class SPjavascriptV2:

    @grepr_dataclass()
    class code_input(ThirdBlock):
        code: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::(CODE)",
                inputs={
                    "CODE": ThirdInputValue.as_input(self.code, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class argument_report(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&SPjavascriptV2::data", inputs={}, dropdowns={})

    @grepr_dataclass()
    class return_data(ThirdBlock):
        data: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::return (DATA)",
                inputs={
                    "DATA": ThirdInputValue.as_input(
                        self.data, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class js_reporter(ThirdBlock):
        code: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}",
                inputs={
                    "CODE": ThirdInputValue.as_input(
                        self.code, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class js_boolean(ThirdBlock):
        code: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsBoolean}}",
                inputs={
                    "CODE": ThirdInputValue.as_input(
                        self.code, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class js_reporter_binded(ThirdBlock):
        args: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsReporterBinded}}",
                inputs={
                    "CODE": ThirdInputValue.as_input(
                        ThirdInputValue(SPjavascriptV2.code_input()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "ARGS": ThirdInputValue.as_input(
                        self.args, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class js_boolean_binded(ThirdBlock):
        args: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsBooleanBinded}}",
                inputs={
                    "CODE": ThirdInputValue.as_input(
                        ThirdInputValue(SPjavascriptV2.code_input()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "ARGS": ThirdInputValue.as_input(
                        self.args, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class define_global_func(ThirdBlock):
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::create global function named (NAME) with code {:CODE:}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "CODE": ThirdInputValue.as_input(
                        ThirdInputValue(SPjavascriptV2.code_input()),
                        p.SREmbeddedBlockInputValue,
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class define_scratch_code(ThirdBlock):
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::create local function named (NAME) with code {:CODE:} {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "CODE": ThirdInputValue.as_input(
                        ThirdInputValue(SPjavascriptV2.argument_report()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class delete_global_func(ThirdBlock):
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::delete global function (NAME)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class js_command_binded(ThirdBlock):
        args: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsCommandBinded}}",
                inputs={
                    "CODE": ThirdInputValue.as_input(
                        ThirdInputValue(SPjavascriptV2.code_input()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "ARGS": ThirdInputValue.as_input(
                        self.args, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class js_command(ThirdBlock):
        code: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsCommand}}",
                inputs={
                    "CODE": ThirdInputValue.as_input(
                        self.code, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )
