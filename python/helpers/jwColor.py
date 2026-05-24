from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwColor:

    @grepr_dataclass()
    class new_color(ThirdBlock):
        color: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class from_rgb(ThirdBlock):
        r: INPUT_COMPATIBLE_T
        g: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class from_hsv(ThirdBlock):
        h: INPUT_COMPATIBLE_T
        s: INPUT_COMPATIBLE_T
        v: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class from_hex(ThirdBlock):
        hex: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class add(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::(A) + (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class sub(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::(A) - (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class mul(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::(A) * (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class interpolate(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        i: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class get(ThirdBlock):
        color: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class set(ThirdBlock):
        color: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class to_decimal(ThirdBlock):
        color: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class to_hex(ThirdBlock):
        color: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class menu_interpolate_option(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::#menu:interpolateOption", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_prop_option(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwColor::#menu:propOption", inputs={}, dropdowns={}
            )
