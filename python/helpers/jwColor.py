from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class jwColor:

    @staticmethod
    def new_color(color: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::new color (COLOR)",
            inputs={
                "COLOR": InputValue.try_as_input(color, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def from_rgb(
        r: INPUT_COMPATIBLE_T, g: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::from RGB (R) (G) (B)",
            inputs={
                "R": InputValue.try_as_input(r, p.SRBlockAndTextInputValue),
                "G": InputValue.try_as_input(g, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def from_hsv(
        h: INPUT_COMPATIBLE_T, s: INPUT_COMPATIBLE_T, v: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::from HSV (H) (S) (V)",
            inputs={
                "H": InputValue.try_as_input(h, p.SRBlockAndTextInputValue),
                "S": InputValue.try_as_input(s, p.SRBlockAndTextInputValue),
                "V": InputValue.try_as_input(v, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def from_hex(hex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::from hex (HEX)",
            inputs={"HEX": InputValue.try_as_input(hex, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def add(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::(A) + (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def sub(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::(A) - (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def mul(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::(A) * (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def interpolate(
        a: INPUT_COMPATIBLE_T,
        b: INPUT_COMPATIBLE_T,
        i: INPUT_COMPATIBLE_T,
        option: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::interpolate (A) to (B) by (I) using (OPTION)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
                "I": InputValue.try_as_input(i, p.SRBlockAndTextInputValue),
                "OPTION": InputValue.try_as_input(option, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get(color: INPUT_COMPATIBLE_T, option: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::get (OPTION) (COLOR)",
            inputs={
                "COLOR": InputValue.try_as_input(color, p.SRBlockAndTextInputValue),
                "OPTION": InputValue.try_as_input(option, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set(
        color: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T, option: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::set (OPTION) (COLOR) to (VALUE)",
            inputs={
                "COLOR": InputValue.try_as_input(color, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
                "OPTION": InputValue.try_as_input(option, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def to_decimal(color: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::(COLOR) to decimal",
            inputs={
                "COLOR": InputValue.try_as_input(color, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def to_hex(color: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::(COLOR) to hexadecimal",
            inputs={
                "COLOR": InputValue.try_as_input(color, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def menu_interpolate_option() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwColor::#menu:interpolateOption", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_prop_option() -> p.SRBlock:
        return p.SRBlock(opcode="&jwColor::#menu:propOption", inputs={}, dropdowns={})
