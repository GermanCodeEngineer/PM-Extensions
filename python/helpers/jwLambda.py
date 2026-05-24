from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwLambda:

    @grepr_dataclass()
    class arg(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwLambda::argument", inputs={}, dropdowns={})

    @grepr_dataclass()
    class new_lambda(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwLambda::new lambda {:ARG:} {SUBSTACK}",
                inputs={
                    "ARG": ThirdInputValue.as_input(
                        ThirdInputValue(jwLambda.arg()), p.SREmbeddedBlockInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class raw_lambda_input(ThirdBlock):
        field: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwLambda::(FIELD)",
                inputs={
                    "FIELD": ThirdInputValue.as_input(
                        self.field, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class raw_lambda(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwLambda::new lambda {:RAW:}",
                inputs={
                    "RAW": ThirdInputValue.as_input(
                        ThirdInputValue(jwLambda.raw_lambda_input()),
                        p.SREmbeddedBlockInputValue,
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class execute_r(ThirdBlock):
        lambda_: INPUT_COMPATIBLE_T
        arg: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_executeR}}",
                inputs={
                    "LAMBDA": ThirdInputValue.as_input(
                        self.lambda_, p.SRBlockOnlyInputValue
                    ),
                    "ARG": ThirdInputValue.as_input(
                        self.arg, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class this(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwLambda::this lambda", inputs={}, dropdowns={})

    @grepr_dataclass()
    class times_executed(ThirdBlock):
        lambda_: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwLambda::times (LAMBDA) executed",
                inputs={
                    "LAMBDA": ThirdInputValue.as_input(
                        self.lambda_, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class execute(ThirdBlock):
        lambda_: INPUT_COMPATIBLE_T
        arg: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_execute}}",
                inputs={
                    "LAMBDA": ThirdInputValue.as_input(
                        self.lambda_, p.SRBlockOnlyInputValue
                    ),
                    "ARG": ThirdInputValue.as_input(
                        self.arg, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )
