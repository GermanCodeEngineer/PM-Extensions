from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class jwColor:

    @grepr_dataclass()
    class new_color(ThirdBlock):
        OPCODE = "&jwColor::new color (COLOR)"
        color: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("COLOR", "color", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("COLOR", "color", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class from_rgb(ThirdBlock):
        OPCODE = "&jwColor::from RGB (R) (G) (B)"
        r: INPUT_COMPATIBLE_T
        g: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("R", "r", p.SRBlockAndTextInputValue, None),
                    ("G", "g", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("R", "r", p.SRBlockAndTextInputValue, None),
                    ("G", "g", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class from_hsv(ThirdBlock):
        OPCODE = "&jwColor::from HSV (H) (S) (V)"
        h: INPUT_COMPATIBLE_T
        s: INPUT_COMPATIBLE_T
        v: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("H", "h", p.SRBlockAndTextInputValue, None),
                    ("S", "s", p.SRBlockAndTextInputValue, None),
                    ("V", "v", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("H", "h", p.SRBlockAndTextInputValue, None),
                    ("S", "s", p.SRBlockAndTextInputValue, None),
                    ("V", "v", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class from_hex(ThirdBlock):
        OPCODE = "&jwColor::from hex (HEX)"
        hex: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("HEX", "hex", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("HEX", "hex", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&jwColor::(A) + (B)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class sub(ThirdBlock):
        OPCODE = "&jwColor::(A) - (B)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class mul(ThirdBlock):
        OPCODE = "&jwColor::(A) * (B)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class interpolate(ThirdBlock):
        OPCODE = "&jwColor::interpolate (A) to (B) by (I) using (OPTION)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        i: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                    ("I", "i", p.SRBlockAndTextInputValue, None),
                    ("OPTION", "option", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                    ("I", "i", p.SRBlockAndTextInputValue, None),
                    ("OPTION", "option", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE = "&jwColor::get (OPTION) (COLOR)"
        color: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("COLOR", "color", p.SRBlockAndTextInputValue, None),
                    ("OPTION", "option", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("COLOR", "color", p.SRBlockAndTextInputValue, None),
                    ("OPTION", "option", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&jwColor::set (OPTION) (COLOR) to (VALUE)"
        color: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("COLOR", "color", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("OPTION", "option", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("COLOR", "color", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("OPTION", "option", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class to_decimal(ThirdBlock):
        OPCODE = "&jwColor::(COLOR) to decimal"
        color: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("COLOR", "color", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("COLOR", "color", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class to_hex(ThirdBlock):
        OPCODE = "&jwColor::(COLOR) to hexadecimal"
        color: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("COLOR", "color", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("COLOR", "color", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class menu_interpolate_option(ThirdBlock):
        OPCODE = "&jwColor::#menu:interpolateOption"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_prop_option(ThirdBlock):
        OPCODE = "&jwColor::#menu:propOption"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
