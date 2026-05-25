from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class gceTestRunner:

    @grepr_dataclass()
    class test_scope(ThirdBlock):
        OPCODE = "&gceTestRunner::test scope named (NAME) {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_(ThirdBlock):
        OPCODE = "&gceTestRunner::assert <CONDITION>"
        condition: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class assert_not(ThirdBlock):
        OPCODE = "&gceTestRunner::assert not <CONDITION>"
        condition: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class assert_msg(ThirdBlock):
        OPCODE = "&gceTestRunner::assert <CONDITION> message (MSG)"
        condition: INPUT_COMPATIBLE_T
        msg: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("MSG", "msg", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("MSG", "msg", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_not_msg(ThirdBlock):
        OPCODE = "&gceTestRunner::assert not <CONDITION> message (MSG)"
        condition: INPUT_COMPATIBLE_T
        msg: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("MSG", "msg", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                    ("MSG", "msg", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_strict_equal(ThirdBlock):
        OPCODE = "&gceTestRunner::assert typed equality (A) = (B)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_strict_not_equal(ThirdBlock):
        OPCODE = "&gceTestRunner::assert typed inequality (A) != (B)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_unstrict_equal(ThirdBlock):
        OPCODE = "&gceTestRunner::assert string equality (A) = (B)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_unstrict_not_equal(ThirdBlock):
        OPCODE = "&gceTestRunner::assert string inequality (A) != (B)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_text_in_value(ThirdBlock):
        OPCODE = "&gceTestRunner::assert text (TEXT) in value (VALUE)"
        text: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_text_not_in_value(ThirdBlock):
        OPCODE = "&gceTestRunner::assert text (TEXT) not in value (VALUE)"
        text: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_type(ThirdBlock):
        OPCODE = "&gceTestRunner::assert type of (VALUE) is ([EXPECTED])"
        value: INPUT_COMPATIBLE_T
        expected: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("EXPECTED", "expected", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("EXPECTED", "expected", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_custom_id_type(ThirdBlock):
        OPCODE = "&gceTestRunner::assert custom id of (VALUE) is (EXPECTED)"
        value: INPUT_COMPATIBLE_T
        expected: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("EXPECTED", "expected", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("EXPECTED", "expected", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_throws(ThirdBlock):
        OPCODE = "&gceTestRunner::assert throws error {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SUBSTACK", "substack", p.SRScriptInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SUBSTACK", "substack", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class assert_throws_contains(ThirdBlock):
        OPCODE = "&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}"
        msg: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("MSG", "msg", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("MSG", "msg", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class assert_does_not_throw(ThirdBlock):
        OPCODE = "&gceTestRunner::assert does not throw error {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SUBSTACK", "substack", p.SRScriptInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SUBSTACK", "substack", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class fail_test(ThirdBlock):
        OPCODE = "&gceTestRunner::fail test with message (MSG)"
        msg: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("MSG", "msg", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("MSG", "msg", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class menu_expected_type(ThirdBlock):
        OPCODE = "&gceTestRunner::#menu:expectedType"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
