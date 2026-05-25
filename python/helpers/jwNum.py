from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class jwNum:

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&jwNum::(A) + (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class sub(ThirdBlock):
        OPCODE = "&jwNum::(A) - (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mul(ThirdBlock):
        OPCODE = "&jwNum::(A) * (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class div(ThirdBlock):
        OPCODE = "&jwNum::(A) / (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pow(ThirdBlock):
        OPCODE = "&jwNum::(A) ^ (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fact(ThirdBlock):
        OPCODE = "&jwNum::[A]!"
        INPUT_SPECS = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eq(ThirdBlock):
        OPCODE = "&jwNum::(A) = (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gt(ThirdBlock):
        OPCODE = "&jwNum::(A) > (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gte(ThirdBlock):
        OPCODE = "&jwNum::(A) >= (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class lt(ThirdBlock):
        OPCODE = "&jwNum::(A) < (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class lte(ThirdBlock):
        OPCODE = "&jwNum::(A) <= (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class root(ThirdBlock):
        OPCODE = "&jwNum::root (A) (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class ssqrt(ThirdBlock):
        OPCODE = "&jwNum::square super-root (A)"
        INPUT_SPECS = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class log(ThirdBlock):
        OPCODE = "&jwNum::log (A) (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class slog(ThirdBlock):
        OPCODE = "&jwNum::super log (A) (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mod(ThirdBlock):
        OPCODE = "&jwNum::(A) % (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class round(ThirdBlock):
        OPCODE = "&jwNum::([A]) (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndDropdownInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_integer(ThirdBlock):
        OPCODE = "&jwNum::is (A) an integer?"
        INPUT_SPECS = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class hyper(ThirdBlock):
        OPCODE = "&jwNum::(A) hyper (B) (C)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
            ("C", "c", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class arrow(ThirdBlock):
        OPCODE = "&jwNum::(A) arrow (B) (C)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
            ("C", "c", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse_arrow(ThirdBlock):
        OPCODE = "&jwNum::(C) reverse arrow (B) (A)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
            ("C", "c", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class expansion(ThirdBlock):
        OPCODE = "&jwNum::(A) expansion (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&jwNum::(A) to string"
        INPUT_SPECS = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string_d(ThirdBlock):
        OPCODE = "&jwNum::(A) to string with (B) decimal places"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_hyper_e(ThirdBlock):
        OPCODE = "&jwNum::(A) to hyper E"
        INPUT_SPECS = (("A", "a", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_round(ThirdBlock):
        OPCODE = "&jwNum::#menu:round"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
