from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class jwVector:

    @grepr_dataclass()
    class new_vector(ThirdBlock):
        OPCODE = "&jwVector::new vector x: (X) y: (Y)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class new_vector_from_magnitude(ThirdBlock):
        OPCODE = "&jwVector::new vector magnitude: (X) angle: (Y)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class vector_x(ThirdBlock):
        OPCODE = "&jwVector::(VECTOR) x"
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class vector_y(ThirdBlock):
        OPCODE = "&jwVector::(VECTOR) y"
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&jwVector::(X) + (Y)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class subtract(ThirdBlock):
        OPCODE = "&jwVector::(X) - (Y)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class multiply_b(ThirdBlock):
        OPCODE = "&jwVector::(X) * (Y) {{id=jwVector_multiplyB}}"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class divide_b(ThirdBlock):
        OPCODE = "&jwVector::(X) / (Y) {{id=jwVector_divideB}}"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class magnitude(ThirdBlock):
        OPCODE = "&jwVector::magnitude of (VECTOR)"
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class angle(ThirdBlock):
        OPCODE = "&jwVector::angle of (VECTOR)"
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class normalize(ThirdBlock):
        OPCODE = "&jwVector::normalize (VECTOR)"
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class absolute(ThirdBlock):
        OPCODE = "&jwVector::absolute (VECTOR)"
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class rotate(ThirdBlock):
        OPCODE = "&jwVector::rotate (VECTOR) by (ANGLE)"
        vector: INPUT_COMPATIBLE_T
        angle: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
                    ("ANGLE", "angle", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
                    ("ANGLE", "angle", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class round(ThirdBlock):
        OPCODE = "&jwVector::(ROUNDING) of (VECTOR)"
        rounding: INPUT_COMPATIBLE_T
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ROUNDING", "rounding", p.SRBlockOnlyInputValue, None),
                    ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ROUNDING", "rounding", p.SRBlockOnlyInputValue, None),
                    ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_pos(ThirdBlock):
        OPCODE = "&jwVector::position"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class set_pos(ThirdBlock):
        OPCODE = "&jwVector::set position to (VECTOR)"
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_stretch(ThirdBlock):
        OPCODE = "&jwVector::stretch"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class set_stretch(ThirdBlock):
        OPCODE = "&jwVector::set stretch to (VECTOR)"
        vector: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VECTOR", "vector", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_mouse(ThirdBlock):
        OPCODE = "&jwVector::mouse position"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class divide_a(ThirdBlock):
        OPCODE = "&jwVector::(X) / (Y) {{id=jwVector_divideA}}"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class multiply_a(ThirdBlock):
        OPCODE = "&jwVector::(X) * (Y) {{id=jwVector_multiplyA}}"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockOnlyInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_rounding_functions(ThirdBlock):
        OPCODE = "&jwVector::#menu:roundingFunctions"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
