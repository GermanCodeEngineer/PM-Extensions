from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwColor:

    class new_color(ThirdBlock):

        def __init__(self, color: INPUT_COMPATIBLE_T):
            self.color = color

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::new color (COLOR)",
                inputs={
                    "COLOR": ThirdInputValue.as_input(
                        self.color, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class from_rgb(ThirdBlock):

        def __init__(
            self, r: INPUT_COMPATIBLE_T, g: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T
        ):
            self.r = r
            self.g = g
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::from RGB (R) (G) (B)",
                inputs={
                    "R": ThirdInputValue.as_input(self.r, p.SRBlockAndTextInputValue),
                    "G": ThirdInputValue.as_input(self.g, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class from_hsv(ThirdBlock):

        def __init__(
            self, h: INPUT_COMPATIBLE_T, s: INPUT_COMPATIBLE_T, v: INPUT_COMPATIBLE_T
        ):
            self.h = h
            self.s = s
            self.v = v

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::from HSV (H) (S) (V)",
                inputs={
                    "H": ThirdInputValue.as_input(self.h, p.SRBlockAndTextInputValue),
                    "S": ThirdInputValue.as_input(self.s, p.SRBlockAndTextInputValue),
                    "V": ThirdInputValue.as_input(self.v, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class from_hex(ThirdBlock):

        def __init__(self, hex: INPUT_COMPATIBLE_T):
            self.hex = hex

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::from hex (HEX)",
                inputs={
                    "HEX": ThirdInputValue.as_input(
                        self.hex, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class add(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::(A) + (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class sub(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::(A) - (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class mul(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::(A) * (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class interpolate(ThirdBlock):

        def __init__(
            self,
            a: INPUT_COMPATIBLE_T,
            b: INPUT_COMPATIBLE_T,
            i: INPUT_COMPATIBLE_T,
            option: INPUT_COMPATIBLE_T,
        ):
            self.a = a
            self.b = b
            self.i = i
            self.option = option

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::interpolate (A) to (B) by (I) using (OPTION)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                    "I": ThirdInputValue.as_input(self.i, p.SRBlockAndTextInputValue),
                    "OPTION": ThirdInputValue.as_input(
                        self.option, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class get(ThirdBlock):

        def __init__(self, color: INPUT_COMPATIBLE_T, option: INPUT_COMPATIBLE_T):
            self.color = color
            self.option = option

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::get (OPTION) (COLOR)",
                inputs={
                    "COLOR": ThirdInputValue.as_input(
                        self.color, p.SRBlockAndTextInputValue
                    ),
                    "OPTION": ThirdInputValue.as_input(
                        self.option, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class set(ThirdBlock):

        def __init__(
            self,
            color: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
            option: INPUT_COMPATIBLE_T,
        ):
            self.color = color
            self.value = value
            self.option = option

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::set (OPTION) (COLOR) to (VALUE)",
                inputs={
                    "COLOR": ThirdInputValue.as_input(
                        self.color, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "OPTION": ThirdInputValue.as_input(
                        self.option, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class to_decimal(ThirdBlock):

        def __init__(self, color: INPUT_COMPATIBLE_T):
            self.color = color

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::(COLOR) to decimal",
                inputs={
                    "COLOR": ThirdInputValue.as_input(
                        self.color, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class to_hex(ThirdBlock):

        def __init__(self, color: INPUT_COMPATIBLE_T):
            self.color = color

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::(COLOR) to hexadecimal",
                inputs={
                    "COLOR": ThirdInputValue.as_input(
                        self.color, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class menu_interpolate_option(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::#menu:interpolateOption", inputs={}, dropdowns={}
            )

    class menu_prop_option(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::#menu:propOption", inputs={}, dropdowns={}
            )
