from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwNum:

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) + (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class sub(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) - (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mul(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) * (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class div(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) / (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pow(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) ^ (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fact(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::[A]!"
        INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eq(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) = (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gt(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) > (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gte(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) >= (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class lt(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) < (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class lte(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) <= (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class root(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::root (A) (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class ssqrt(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::square super-root (A)"
        INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class log(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::log (A) (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class slog(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::super log (A) (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mod(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) % (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class round(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::([A]) (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndDropdownInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_integer(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::is (A) an integer?"
        INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class hyper(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) hyper (B) (C)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
            ("C", "c", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class arrow(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) arrow (B) (C)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
            ("C", "c", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse_arrow(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(C) reverse arrow (B) (A)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
            ("C", "c", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class expansion(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) expansion (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) to string"
        INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string_d(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) to string with (B) decimal places"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_hyper_e(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::(A) to hyper E"
        INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_round(ThirdBlock):
        OPCODE: ClassVar = "&jwNum::#menu:round"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
