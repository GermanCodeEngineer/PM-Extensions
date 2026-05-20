from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwVector:

    class new_vector(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::new vector x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class new_vector_from_magnitude(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::new vector magnitude: (X) angle: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class vector_x(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T):
            self.vector = vector

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

    class vector_y(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T):
            self.vector = vector

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

    class add(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) + (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class subtract(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) - (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class multiply_b(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) * (Y) {{id=jwVector_multiplyB}}",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class divide_b(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) / (Y) {{id=jwVector_divideB}}",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class magnitude(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T):
            self.vector = vector

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

    class angle(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T):
            self.vector = vector

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

    class normalize(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T):
            self.vector = vector

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

    class absolute(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T):
            self.vector = vector

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

    class rotate(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T, angle: INPUT_COMPATIBLE_T):
            self.vector = vector
            self.angle = angle

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

    class round(ThirdBlock):

        def __init__(self, rounding: INPUT_COMPATIBLE_T, vector: INPUT_COMPATIBLE_T):
            self.rounding = rounding
            self.vector = vector

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

    class get_pos(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwVector::position", inputs={}, dropdowns={})

    class set_pos(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T):
            self.vector = vector

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

    class get_stretch(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwVector::stretch", inputs={}, dropdowns={})

    class set_stretch(ThirdBlock):

        def __init__(self, vector: INPUT_COMPATIBLE_T):
            self.vector = vector

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

    class get_mouse(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::mouse position", inputs={}, dropdowns={}
            )

    class divide_a(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) / (Y) {{id=jwVector_divideA}}",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class multiply_a(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::(X) * (Y) {{id=jwVector_multiplyA}}",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockOnlyInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class menu_rounding_functions(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwVector::#menu:roundingFunctions", inputs={}, dropdowns={}
            )
