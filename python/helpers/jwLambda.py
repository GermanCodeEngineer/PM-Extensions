from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class jwLambda:

    @grepr_dataclass()
    class arg(ThirdBlock):
        OPCODE = "&jwLambda::argument"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class new_lambda(ThirdBlock):
        OPCODE = "&jwLambda::new lambda {:ARG:} {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARG", "arg", p.SREmbeddedBlockInputValue, jwLambda.arg),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARG", "arg", p.SREmbeddedBlockInputValue, jwLambda.arg),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class raw_lambda_input(ThirdBlock):
        OPCODE = "&jwLambda::(FIELD)"
        field: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("FIELD", "field", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("FIELD", "field", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class raw_lambda(ThirdBlock):
        OPCODE = "&jwLambda::new lambda {:RAW:}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "RAW",
                        "raw",
                        p.SREmbeddedBlockInputValue,
                        jwLambda.raw_lambda_input,
                    ),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "RAW",
                        "raw",
                        p.SREmbeddedBlockInputValue,
                        jwLambda.raw_lambda_input,
                    ),
                ),
                (),
            )

    @grepr_dataclass()
    class execute_r(ThirdBlock):
        OPCODE = "&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_executeR}}"
        lambda_: INPUT_COMPATIBLE_T
        arg: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
                    ("ARG", "arg", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
                    ("ARG", "arg", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class this(ThirdBlock):
        OPCODE = "&jwLambda::this lambda"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class times_executed(ThirdBlock):
        OPCODE = "&jwLambda::times (LAMBDA) executed"
        lambda_: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class execute(ThirdBlock):
        OPCODE = "&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_execute}}"
        lambda_: INPUT_COMPATIBLE_T
        arg: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
                    ("ARG", "arg", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
                    ("ARG", "arg", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )
