from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class jwVector:

    @grepr_dataclass()
    class new_vector(ThirdBlock):
        OPCODE = "&jwVector::new vector x: (X) y: (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class new_vector_from_magnitude(ThirdBlock):
        OPCODE = "&jwVector::new vector magnitude: (X) angle: (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class vector_x(ThirdBlock):
        OPCODE = "&jwVector::(VECTOR) x"
        INPUT_SPECS = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class vector_y(ThirdBlock):
        OPCODE = "&jwVector::(VECTOR) y"
        INPUT_SPECS = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&jwVector::(X) + (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class subtract(ThirdBlock):
        OPCODE = "&jwVector::(X) - (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class multiply_b(ThirdBlock):
        OPCODE = "&jwVector::(X) * (Y) {{id=jwVector_multiplyB}}"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class divide_b(ThirdBlock):
        OPCODE = "&jwVector::(X) / (Y) {{id=jwVector_divideB}}"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class magnitude(ThirdBlock):
        OPCODE = "&jwVector::magnitude of (VECTOR)"
        INPUT_SPECS = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class angle(ThirdBlock):
        OPCODE = "&jwVector::angle of (VECTOR)"
        INPUT_SPECS = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class normalize(ThirdBlock):
        OPCODE = "&jwVector::normalize (VECTOR)"
        INPUT_SPECS = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class absolute(ThirdBlock):
        OPCODE = "&jwVector::absolute (VECTOR)"
        INPUT_SPECS = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class rotate(ThirdBlock):
        OPCODE = "&jwVector::rotate (VECTOR) by (ANGLE)"
        INPUT_SPECS = (
            ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            ("ANGLE", "angle", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T
        angle: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class round(ThirdBlock):
        OPCODE = "&jwVector::(ROUNDING) of (VECTOR)"
        INPUT_SPECS = (
            ("ROUNDING", "rounding", p.SRBlockOnlyInputValue, None),
            ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        rounding: INPUT_COMPATIBLE_T
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pos(ThirdBlock):
        OPCODE = "&jwVector::position"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class set_pos(ThirdBlock):
        OPCODE = "&jwVector::set position to (VECTOR)"
        INPUT_SPECS = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_stretch(ThirdBlock):
        OPCODE = "&jwVector::stretch"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class set_stretch(ThirdBlock):
        OPCODE = "&jwVector::set stretch to (VECTOR)"
        INPUT_SPECS = (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        vector: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_mouse(ThirdBlock):
        OPCODE = "&jwVector::mouse position"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class divide_a(ThirdBlock):
        OPCODE = "&jwVector::(X) / (Y) {{id=jwVector_divideA}}"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class multiply_a(ThirdBlock):
        OPCODE = "&jwVector::(X) * (Y) {{id=jwVector_multiplyA}}"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockOnlyInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_rounding_functions(ThirdBlock):
        OPCODE = "&jwVector::#menu:roundingFunctions"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
