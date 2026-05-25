from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class jwTargets:

    @grepr_dataclass()
    class this(ThirdBlock):
        OPCODE = "&jwTargets::this target"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class stage(ThirdBlock):
        OPCODE = "&jwTargets::stage target"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class from_name(ThirdBlock):
        OPCODE = "&jwTargets::(SPRITE) target"
        sprite: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SPRITE", "sprite", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SPRITE", "sprite", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class clone_origin(ThirdBlock):
        OPCODE = "&jwTargets::origin of (TARGET)"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TARGET", "target", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE = "&jwTargets::(TARGET) (MENU)"
        target: INPUT_COMPATIBLE_T
        menu: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                    ("MENU", "menu", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                    ("MENU", "menu", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&jwTargets::set (TARGET) (MENU) to (VALUE)"
        target: INPUT_COMPATIBLE_T
        menu: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                    ("MENU", "menu", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                    ("MENU", "menu", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_clone(ThirdBlock):
        OPCODE = "&jwTargets::is (TARGET) a clone"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TARGET", "target", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class is_touching_object(ThirdBlock):
        OPCODE = "&jwTargets::is (A) touching (B) {{id=jwTargets_isTouchingObject}}"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockOnlyInputValue, None),
                    ("B", "b", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockOnlyInputValue, None),
                    ("B", "b", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_var(ThirdBlock):
        OPCODE = "&jwTargets::var (NAME) of (TARGET)"
        target: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_var(ThirdBlock):
        OPCODE = "&jwTargets::set var (NAME) of (TARGET) to (VALUE)"
        target: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class clone_r(ThirdBlock):
        OPCODE = "&jwTargets::create clone of (TARGET) {{id=jwTargets_cloneR}}"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TARGET", "target", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class delete_clone(ThirdBlock):
        OPCODE = "&jwTargets::delete clone (TARGET)"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TARGET", "target", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class all(ThirdBlock):
        OPCODE = "&jwTargets::all targets"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class touching(ThirdBlock):
        OPCODE = "&jwTargets::targets touching (TARGET)"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TARGET", "target", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class clones(ThirdBlock):
        OPCODE = "&jwTargets::clones of (TARGET)"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TARGET", "target", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class array_has_target(ThirdBlock):
        OPCODE = "&jwTargets::(ARRAY) has clone of (TARGET)"
        array: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_touching(ThirdBlock):
        OPCODE = "&jwTargets::is (A) touching (B) {{id=jwTargets_isTouching}}"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockOnlyInputValue, None),
                    ("B", "b", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockOnlyInputValue, None),
                    ("B", "b", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class clone(ThirdBlock):
        OPCODE = "&jwTargets::create clone of (TARGET) {{id=jwTargets_clone}}"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TARGET", "target", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class menu_sprite(ThirdBlock):
        OPCODE = "&jwTargets::#menu:sprite"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_target_property(ThirdBlock):
        OPCODE = "&jwTargets::#menu:targetProperty"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_target_property_set(ThirdBlock):
        OPCODE = "&jwTargets::#menu:targetPropertySet"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_touching_object(ThirdBlock):
        OPCODE = "&jwTargets::#menu:touchingObject"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
