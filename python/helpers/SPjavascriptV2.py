from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class SPjavascriptV2:

    class code_input(ThirdBlock):

        def __init__(self, code: INPUT_COMPATIBLE_T):
            self.code = code

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&SPjavascriptV2::(CODE)",
                inputs={
                    "CODE": ThirdInputValue.as_input(self.code, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class argument_report(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&SPjavascriptV2::data", inputs={}, dropdowns={})

    class return_data(ThirdBlock):

        def __init__(self, data: INPUT_COMPATIBLE_T):
            self.data = data

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

    class js_reporter(ThirdBlock):

        def __init__(self, code: INPUT_COMPATIBLE_T):
            self.code = code

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

    class js_boolean(ThirdBlock):

        def __init__(self, code: INPUT_COMPATIBLE_T):
            self.code = code

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

    class js_reporter_binded(ThirdBlock):

        def __init__(self, args: INPUT_COMPATIBLE_T):
            self.args = args

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

    class js_boolean_binded(ThirdBlock):

        def __init__(self, args: INPUT_COMPATIBLE_T):
            self.args = args

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

    class define_global_func(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T):
            self.name = name

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

    class define_scratch_code(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

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

    class delete_global_func(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T):
            self.name = name

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

    class js_command_binded(ThirdBlock):

        def __init__(self, args: INPUT_COMPATIBLE_T):
            self.args = args

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

    class js_command(ThirdBlock):

        def __init__(self, code: INPUT_COMPATIBLE_T):
            self.code = code

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
