from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwLambda:

    @grepr_dataclass()
    class arg(ThirdBlock):
        OPCODE = "&jwLambda::argument"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class new_lambda(ThirdBlock):
        OPCODE = "&jwLambda::new lambda {:ARG:} {SUBSTACK}"
        INPUT_SPECS = (
            ("ARG", "arg", p.SREmbeddedBlockInputValue, jwLambda.arg),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class raw_lambda_input(ThirdBlock):
        OPCODE = "&jwLambda::(FIELD)"
        INPUT_SPECS = (("FIELD", "field", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        field: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class raw_lambda(ThirdBlock):
        OPCODE = "&jwLambda::new lambda {:RAW:}"
        INPUT_SPECS = (
            ("RAW", "raw", p.SREmbeddedBlockInputValue, jwLambda.raw_lambda_input),
        )
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class execute_r(ThirdBlock):
        OPCODE = "&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_executeR}}"
        INPUT_SPECS = (
            ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
            ("ARG", "arg", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        lambda_: INPUT_COMPATIBLE_T
        arg: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class this(ThirdBlock):
        OPCODE = "&jwLambda::this lambda"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class times_executed(ThirdBlock):
        OPCODE = "&jwLambda::times (LAMBDA) executed"
        INPUT_SPECS = (("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        lambda_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class execute(ThirdBlock):
        OPCODE = "&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_execute}}"
        INPUT_SPECS = (
            ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
            ("ARG", "arg", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        lambda_: INPUT_COMPATIBLE_T
        arg: INPUT_COMPATIBLE_T
