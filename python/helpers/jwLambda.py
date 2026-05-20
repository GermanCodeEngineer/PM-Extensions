from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class jwLambda:

    @staticmethod
    def arg() -> p.SRBlock:
        return p.SRBlock(opcode="&jwLambda::argument", inputs={}, dropdowns={})

    @staticmethod
    def new_lambda(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwLambda::new lambda {:ARG:} {SUBSTACK}",
            inputs={
                "ARG": ThirdInputValue.as_input(
                    ThirdInputValue(jwLambda.arg()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def raw_lambda_input(field: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwLambda::(FIELD)",
            inputs={"FIELD": ThirdInputValue.as_input(field, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def raw_lambda() -> p.SRBlock:
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

    @staticmethod
    def execute_r(lambda_: INPUT_COMPATIBLE_T, arg: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_executeR}}",
            inputs={
                "LAMBDA": ThirdInputValue.as_input(lambda_, p.SRBlockOnlyInputValue),
                "ARG": ThirdInputValue.as_input(arg, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def this() -> p.SRBlock:
        return p.SRBlock(opcode="&jwLambda::this lambda", inputs={}, dropdowns={})

    @staticmethod
    def times_executed(lambda_: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwLambda::times (LAMBDA) executed",
            inputs={
                "LAMBDA": ThirdInputValue.as_input(lambda_, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def execute(lambda_: INPUT_COMPATIBLE_T, arg: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_execute}}",
            inputs={
                "LAMBDA": ThirdInputValue.as_input(lambda_, p.SRBlockOnlyInputValue),
                "ARG": ThirdInputValue.as_input(arg, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )
