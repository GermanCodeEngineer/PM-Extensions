from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class SPjavascriptV2:

    @staticmethod
    def code_input(code: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::(CODE)",
            inputs={"CODE": ThirdInputValue.as_input(code, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def argument_report() -> p.SRBlock:
        return p.SRBlock(opcode="&SPjavascriptV2::data", inputs={}, dropdowns={})

    @staticmethod
    def return_data(data: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::return (DATA)",
            inputs={"DATA": ThirdInputValue.as_input(data, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def js_reporter(code: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}",
            inputs={"CODE": ThirdInputValue.as_input(code, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def js_boolean(code: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsBoolean}}",
            inputs={"CODE": ThirdInputValue.as_input(code, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def js_reporter_binded(args: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsReporterBinded}}",
            inputs={
                "CODE": ThirdInputValue.as_input(
                    ThirdInputValue(SPjavascriptV2.code_input()),
                    p.SREmbeddedBlockInputValue,
                ),
                "ARGS": ThirdInputValue.as_input(args, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def js_boolean_binded(args: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsBooleanBinded}}",
            inputs={
                "CODE": ThirdInputValue.as_input(
                    ThirdInputValue(SPjavascriptV2.code_input()),
                    p.SREmbeddedBlockInputValue,
                ),
                "ARGS": ThirdInputValue.as_input(args, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_global_func(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::create global function named (NAME) with code {:CODE:}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "CODE": ThirdInputValue.as_input(
                    ThirdInputValue(SPjavascriptV2.code_input()),
                    p.SREmbeddedBlockInputValue,
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def define_scratch_code(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::create local function named (NAME) with code {:CODE:} {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "CODE": ThirdInputValue.as_input(
                    ThirdInputValue(SPjavascriptV2.argument_report()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def delete_global_func(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::delete global function (NAME)",
            inputs={"NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def js_command_binded(args: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsCommandBinded}}",
            inputs={
                "CODE": ThirdInputValue.as_input(
                    ThirdInputValue(SPjavascriptV2.code_input()),
                    p.SREmbeddedBlockInputValue,
                ),
                "ARGS": ThirdInputValue.as_input(args, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def js_command(code: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsCommand}}",
            inputs={"CODE": ThirdInputValue.as_input(code, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )
