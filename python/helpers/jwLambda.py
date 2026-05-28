from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwLambda:

    @grepr_dataclass()
    class arg(ThirdBlock):
        OPCODE: ClassVar = "&jwLambda::argument"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class new_lambda(ThirdBlock):
        OPCODE: ClassVar = "&jwLambda::new lambda {:ARG:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("ARG", "arg", p.SREmbeddedBlockInputValue, lambda: jwLambda.arg()),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class raw_lambda_input(ThirdBlock):
        OPCODE: ClassVar = "&jwLambda::(FIELD)"
        INPUT_SPECS: ClassVar = (("FIELD", "field", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        field: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class raw_lambda(ThirdBlock):
        OPCODE: ClassVar = "&jwLambda::new lambda {:RAW:}"
        INPUT_SPECS: ClassVar = (
            (
                "RAW",
                "raw",
                p.SREmbeddedBlockInputValue,
                lambda: jwLambda.raw_lambda_input(),
            ),
        )
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class execute_r(ThirdBlock):
        OPCODE: ClassVar = (
            "&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_executeR}}"
        )
        INPUT_SPECS: ClassVar = (
            ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
            ("ARG", "arg", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        lambda_: INPUT_COMPATIBLE_T
        arg: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class this(ThirdBlock):
        OPCODE: ClassVar = "&jwLambda::this lambda"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class times_executed(ThirdBlock):
        OPCODE: ClassVar = "&jwLambda::times (LAMBDA) executed"
        INPUT_SPECS: ClassVar = (("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        lambda_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class execute(ThirdBlock):
        OPCODE: ClassVar = (
            "&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_execute}}"
        )
        INPUT_SPECS: ClassVar = (
            ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
            ("ARG", "arg", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        lambda_: INPUT_COMPATIBLE_T
        arg: INPUT_COMPATIBLE_T
