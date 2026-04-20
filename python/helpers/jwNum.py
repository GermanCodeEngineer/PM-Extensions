from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class jwNum:

    @staticmethod
    def add(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) + (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def sub(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) - (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def mul(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) * (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def div(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) / (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def pow(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) ^ (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def fact(a: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::[A]!",
            inputs={"A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def eq(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) = (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def gt(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) > (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def gte(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) >= (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def lt(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) < (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def lte(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) <= (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def root(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::root (A) (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def ssqrt(a: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::square super-root (A)",
            inputs={"A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def log(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::log (A) (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def slog(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::super log (A) (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def mod(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) % (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def round(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::([A]) (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndDropdownInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_integer(a: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::is (A) an integer?",
            inputs={"A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def hyper(
        a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T, c: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) hyper (B) (C)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
                "C": InputValue.try_as_input(c, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def arrow(
        a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T, c: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) arrow (B) (C)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
                "C": InputValue.try_as_input(c, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def reverse_arrow(
        a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T, c: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(C) reverse arrow (B) (A)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
                "C": InputValue.try_as_input(c, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def expansion(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) expansion (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def to_string(a: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) to string",
            inputs={"A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def to_string_d(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) to string with (B) decimal places",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def to_hyper_e(a: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwNum::(A) to hyper E",
            inputs={"A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def menu_round() -> p.SRBlock:
        return p.SRBlock(opcode="&jwNum::#menu:round", inputs={}, dropdowns={})
