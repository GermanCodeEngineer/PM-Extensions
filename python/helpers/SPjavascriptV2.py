from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class SPjavascriptV2:

    @grepr_dataclass()
    class code_input(ThirdBlock):
        OPCODE: ClassVar = "&SPjavascriptV2::(CODE)"
        INPUT_SPECS: ClassVar = (("CODE", "code", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        code: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class argument_report(ThirdBlock):
        OPCODE: ClassVar = "&SPjavascriptV2::data"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class return_data(ThirdBlock):
        OPCODE: ClassVar = "&SPjavascriptV2::return (DATA)"
        INPUT_SPECS: ClassVar = (("DATA", "data", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class js_reporter(ThirdBlock):
        OPCODE: ClassVar = (
            "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}"
        )
        INPUT_SPECS: ClassVar = (("CODE", "code", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        code: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class js_boolean(ThirdBlock):
        OPCODE: ClassVar = "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsBoolean}}"
        INPUT_SPECS: ClassVar = (("CODE", "code", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        code: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class js_reporter_binded(ThirdBlock):
        OPCODE: ClassVar = (
            "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsReporterBinded}}"
        )
        INPUT_SPECS: ClassVar = (
            (
                "CODE",
                "code",
                p.SREmbeddedBlockInputValue,
                lambda: SPjavascriptV2.code_input(),
            ),
            ("ARGS", "args", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        args: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class js_boolean_binded(ThirdBlock):
        OPCODE: ClassVar = (
            "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsBooleanBinded}}"
        )
        INPUT_SPECS: ClassVar = (
            (
                "CODE",
                "code",
                p.SREmbeddedBlockInputValue,
                lambda: SPjavascriptV2.code_input(),
            ),
            ("ARGS", "args", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        args: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_global_func(ThirdBlock):
        OPCODE: ClassVar = (
            "&SPjavascriptV2::create global function named (NAME) with code {:CODE:}"
        )
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            (
                "CODE",
                "code",
                p.SREmbeddedBlockInputValue,
                lambda: SPjavascriptV2.code_input(),
            ),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_scratch_code(ThirdBlock):
        OPCODE: ClassVar = (
            "&SPjavascriptV2::create local function named (NAME) with code {:CODE:} {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            (
                "CODE",
                "code",
                p.SREmbeddedBlockInputValue,
                lambda: SPjavascriptV2.argument_report(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_global_func(ThirdBlock):
        OPCODE: ClassVar = "&SPjavascriptV2::delete global function (NAME)"
        INPUT_SPECS: ClassVar = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class js_command_binded(ThirdBlock):
        OPCODE: ClassVar = (
            "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsCommandBinded}}"
        )
        INPUT_SPECS: ClassVar = (
            (
                "CODE",
                "code",
                p.SREmbeddedBlockInputValue,
                lambda: SPjavascriptV2.code_input(),
            ),
            ("ARGS", "args", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        args: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class js_command(ThirdBlock):
        OPCODE: ClassVar = "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsCommand}}"
        INPUT_SPECS: ClassVar = (("CODE", "code", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        code: INPUT_COMPATIBLE_T
