from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class jwColor:

    @grepr_dataclass()
    class new_color(ThirdBlock):
        OPCODE = "&jwColor::new color (COLOR)"
        INPUT_SPECS = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_rgb(ThirdBlock):
        OPCODE = "&jwColor::from RGB (R) (G) (B)"
        INPUT_SPECS = (
            ("R", "r", p.SRBlockAndTextInputValue, None),
            ("G", "g", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        r: INPUT_COMPATIBLE_T
        g: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_hsv(ThirdBlock):
        OPCODE = "&jwColor::from HSV (H) (S) (V)"
        INPUT_SPECS = (
            ("H", "h", p.SRBlockAndTextInputValue, None),
            ("S", "s", p.SRBlockAndTextInputValue, None),
            ("V", "v", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        h: INPUT_COMPATIBLE_T
        s: INPUT_COMPATIBLE_T
        v: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_hex(ThirdBlock):
        OPCODE = "&jwColor::from hex (HEX)"
        INPUT_SPECS = (("HEX", "hex", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        hex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&jwColor::(A) + (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class sub(ThirdBlock):
        OPCODE = "&jwColor::(A) - (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mul(ThirdBlock):
        OPCODE = "&jwColor::(A) * (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class interpolate(ThirdBlock):
        OPCODE = "&jwColor::interpolate (A) to (B) by (I) using (OPTION)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
            ("I", "i", p.SRBlockAndTextInputValue, None),
            ("OPTION", "option", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        i: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE = "&jwColor::get (OPTION) (COLOR)"
        INPUT_SPECS = (
            ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            ("OPTION", "option", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        color: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&jwColor::set (OPTION) (COLOR) to (VALUE)"
        INPUT_SPECS = (
            ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("OPTION", "option", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        color: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        option: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_decimal(ThirdBlock):
        OPCODE = "&jwColor::(COLOR) to decimal"
        INPUT_SPECS = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_hex(ThirdBlock):
        OPCODE = "&jwColor::(COLOR) to hexadecimal"
        INPUT_SPECS = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_interpolate_option(ThirdBlock):
        OPCODE = "&jwColor::#menu:interpolateOption"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_prop_option(ThirdBlock):
        OPCODE = "&jwColor::#menu:propOption"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
