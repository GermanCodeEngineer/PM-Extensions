from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwVector:

    @grepr_dataclass()
    class new_vector(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::new vector x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class new_vector_from_magnitude(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::new vector magnitude: (X) angle: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class vector_x(ThirdBlock):
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(VECTOR) x",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class vector_y(ThirdBlock):
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(VECTOR) y",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class add(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) + (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class subtract(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) - (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class multiply_b(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) * (Y) {{id=jwVector_multiplyB}}",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class divide_b(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) / (Y) {{id=jwVector_divideB}}",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class magnitude(ThirdBlock):
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::magnitude of (VECTOR)",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class angle(ThirdBlock):
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::angle of (VECTOR)",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class normalize(ThirdBlock):
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::normalize (VECTOR)",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class absolute(ThirdBlock):
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::absolute (VECTOR)",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class rotate(ThirdBlock):
        vector: INPUT_COMPATIBLE_T
        angle: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::rotate (VECTOR) by (ANGLE)",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    ),
                    "ANGLE": ThirdInputValue.as_input(
                        self.angle, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class round(ThirdBlock):
        rounding: INPUT_COMPATIBLE_T
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(ROUNDING) of (VECTOR)",
                inputs={
                    "ROUNDING": ThirdInputValue.as_input(
                        self.rounding, p.SRBlockOnlyInputValue
                    ),
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_pos(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwVector::position", inputs={}, dropdowns={})

    @grepr_dataclass()
    class set_pos(ThirdBlock):
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::set position to (VECTOR)",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_stretch(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwVector::stretch", inputs={}, dropdowns={})

    @grepr_dataclass()
    class set_stretch(ThirdBlock):
        vector: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::set stretch to (VECTOR)",
                inputs={
                    "VECTOR": ThirdInputValue.as_input(
                        self.vector, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_mouse(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::mouse position", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class divide_a(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) / (Y) {{id=jwVector_divideA}}",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class multiply_a(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) * (Y) {{id=jwVector_multiplyA}}",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_rounding_functions(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::#menu:roundingFunctions", inputs={}, dropdowns={}
            )
