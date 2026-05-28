from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwColor:

    @grepr_dataclass()
    class new_color(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::new color (COLOR)"
        INPUT_SPECS: ClassVar = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_rgb(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::from RGB (R) (G) (B)"
        INPUT_SPECS: ClassVar = (
            ("R", "r", p.SRBlockAndTextInputValue, None),
            ("G", "g", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        r: INPUT_COMPATIBLE_T
        g: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_hsv(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::from HSV (H) (S) (V)"
        INPUT_SPECS: ClassVar = (
            ("H", "h", p.SRBlockAndTextInputValue, None),
            ("S", "s", p.SRBlockAndTextInputValue, None),
            ("V", "v", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        h: INPUT_COMPATIBLE_T
        s: INPUT_COMPATIBLE_T
        v: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_hex(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::from hex (HEX)"
        INPUT_SPECS: ClassVar = (("HEX", "hex", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        hex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::(A) + (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class sub(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::(A) - (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mul(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::(A) * (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class interpolate(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::interpolate (A) to (B) by (I) using (OPTION)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
            ("I", "i", p.SRBlockAndTextInputValue, None),
            ("OPTION", "option", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        i: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::get (OPTION) (COLOR)"
        INPUT_SPECS: ClassVar = (
            ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            ("OPTION", "option", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        color: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::set (OPTION) (COLOR) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("OPTION", "option", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        color: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_decimal(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::(COLOR) to decimal"
        INPUT_SPECS: ClassVar = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_hex(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::(COLOR) to hexadecimal"
        INPUT_SPECS: ClassVar = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_interpolate_option(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::#menu:interpolateOption"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_prop_option(ThirdBlock):
        OPCODE: ClassVar = "&jwColor::#menu:propOption"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
