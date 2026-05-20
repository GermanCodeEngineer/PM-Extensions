from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwLambda:

    class arg(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwLambda::argument", inputs={}, dropdowns={})

    class new_lambda(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

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

    class raw_lambda_input(ThirdBlock):

        def __init__(self, field: INPUT_COMPATIBLE_T):
            self.field = field

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

    class raw_lambda(ThirdBlock):

        def __init__(self):
            pass

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

    class execute_r(ThirdBlock):

        def __init__(self, lambda_: INPUT_COMPATIBLE_T, arg: INPUT_COMPATIBLE_T):
            self.lambda_ = lambda_
            self.arg = arg

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

    class this(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwLambda::this lambda", inputs={}, dropdowns={})

    class times_executed(ThirdBlock):

        def __init__(self, lambda_: INPUT_COMPATIBLE_T):
            self.lambda_ = lambda_

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

    class execute(ThirdBlock):

        def __init__(self, lambda_: INPUT_COMPATIBLE_T, arg: INPUT_COMPATIBLE_T):
            self.lambda_ = lambda_
            self.arg = arg

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
