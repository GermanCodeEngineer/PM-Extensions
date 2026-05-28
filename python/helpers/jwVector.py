from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwVector:

    @grepr_dataclass()
    class new_vector(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::new vector x: (X) y: (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class new_vector_from_magnitude(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::new vector magnitude: (X) angle: (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class vector_x(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(VECTOR) x"
        INPUT_SPECS: ClassVar = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class vector_y(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(VECTOR) y"
        INPUT_SPECS: ClassVar = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(X) + (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class subtract(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(X) - (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class multiply_b(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(X) * (Y) {{id=jwVector_multiplyB}}"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class divide_b(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(X) / (Y) {{id=jwVector_divideB}}"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class magnitude(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::magnitude of (VECTOR)"
        INPUT_SPECS: ClassVar = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class angle(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::angle of (VECTOR)"
        INPUT_SPECS: ClassVar = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class normalize(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::normalize (VECTOR)"
        INPUT_SPECS: ClassVar = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class absolute(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::absolute (VECTOR)"
        INPUT_SPECS: ClassVar = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class rotate(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::rotate (VECTOR) by (ANGLE)"
        INPUT_SPECS: ClassVar = (
            ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            ("ANGLE", "angle", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T
        angle: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class round(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(ROUNDING) of (VECTOR)"
        INPUT_SPECS: ClassVar = (
            ("ROUNDING", "rounding", p.SRBlockOnlyInputValue, None),
            ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        rounding: INPUT_COMPATIBLE_T
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pos(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::position"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class set_pos(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::set position to (VECTOR)"
        INPUT_SPECS: ClassVar = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_stretch(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::stretch"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class set_stretch(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::set stretch to (VECTOR)"
        INPUT_SPECS: ClassVar = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_mouse(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::mouse position"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class divide_a(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(X) / (Y) {{id=jwVector_divideA}}"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class multiply_a(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::(X) * (Y) {{id=jwVector_multiplyA}}"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_rounding_functions(ThirdBlock):
        OPCODE: ClassVar = "&jwVector::#menu:roundingFunctions"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
