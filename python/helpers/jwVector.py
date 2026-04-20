from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class jwVector:

    @staticmethod
    def new_vector(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::new vector x: (X) y: (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def new_vector_from_magnitude(
        x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::new vector magnitude: (X) angle: (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def vector_x(vector: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::(VECTOR) x",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def vector_y(vector: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::(VECTOR) y",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def add(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::(X) + (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def subtract(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::(X) - (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def multiply_b(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::(X) * (Y) {{id=jwVector_multiplyB}}",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def divide_b(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::(X) / (Y) {{id=jwVector_divideB}}",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def magnitude(vector: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::magnitude of (VECTOR)",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def angle(vector: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::angle of (VECTOR)",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def normalize(vector: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::normalize (VECTOR)",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def absolute(vector: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::absolute (VECTOR)",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def rotate(vector: INPUT_COMPATIBLE_T, angle: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::rotate (VECTOR) by (ANGLE)",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue),
                "ANGLE": InputValue.try_as_input(angle, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def round(vector: INPUT_COMPATIBLE_T, rounding: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::[ROUNDING] of (VECTOR)",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "ROUNDING": p.SRDropdownValue(p.DropdownValueKind.STANDARD, rounding)
            },
        )

    @staticmethod
    def get_pos() -> p.SRBlock:
        return p.SRBlock(opcode="&jwVector::position", inputs={}, dropdowns={})

    @staticmethod
    def set_pos(vector: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::set position to (VECTOR)",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def get_stretch() -> p.SRBlock:
        return p.SRBlock(opcode="&jwVector::stretch", inputs={}, dropdowns={})

    @staticmethod
    def set_stretch(vector: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::set stretch to (VECTOR)",
            inputs={
                "VECTOR": InputValue.try_as_input(vector, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def get_mouse() -> p.SRBlock:
        return p.SRBlock(opcode="&jwVector::mouse position", inputs={}, dropdowns={})

    @staticmethod
    def divide_a(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::(X) / (Y) {{id=jwVector_divideA}}",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def multiply_a(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::(X) * (Y) {{id=jwVector_multiplyA}}",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_rounding_functions() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwVector::#menu:roundingFunctions", inputs={}, dropdowns={}
        )
