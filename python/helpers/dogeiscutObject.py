from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class dogeiscutObject:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE = "&dogeiscutObject::blank object"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE = "&dogeiscutObject::parse (VALUE) as object"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class from_entries(ThirdBlock):
        OPCODE = "&dogeiscutObject::from entries (ARRAY)"
        array: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ARRAY", "array", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ARRAY", "array", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class current_object(ThirdBlock):
        OPCODE = "&dogeiscutObject::current object"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE = "&dogeiscutObject::object builder {:CURRENT_OBJECT:} {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "CURRENT_OBJECT",
                        "current_object",
                        p.SREmbeddedBlockInputValue,
                        dogeiscutObject.current_object,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "CURRENT_OBJECT",
                        "current_object",
                        p.SREmbeddedBlockInputValue,
                        dogeiscutObject.current_object,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE = "&dogeiscutObject::append key (KEY) value (VALUE) to builder"
        key: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class builder_append_empty(ThirdBlock):
        OPCODE = "&dogeiscutObject::append key (KEY) to builder"
        key: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("KEY", "key", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("KEY", "key", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE = "&dogeiscutObject::set builder to (OBJECT)"
        object: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OBJECT", "object", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("OBJECT", "object", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE = "&dogeiscutObject::get (KEY) in (OBJECT)"
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_path(ThirdBlock):
        OPCODE = "&dogeiscutObject::get path (ARRAY) in (OBJECT)"
        object: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE = "&dogeiscutObject::(OBJECT) has key (KEY)"
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class size(ThirdBlock):
        OPCODE = "&dogeiscutObject::size of (OBJECT)"
        object: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OBJECT", "object", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("OBJECT", "object", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&dogeiscutObject::set (KEY) in (OBJECT) to (VALUE)"
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_path(ThirdBlock):
        OPCODE = "&dogeiscutObject::set path (ARRAY) in (OBJECT) to (VALUE)"
        object: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class delete(ThirdBlock):
        OPCODE = "&dogeiscutObject::delete key (KEY) from (OBJECT)"
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("KEY", "key", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class delete_at_path(ThirdBlock):
        OPCODE = "&dogeiscutObject::delete at path (ARRAY) from (OBJECT)"
        object: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class merge(ThirdBlock):
        OPCODE = "&dogeiscutObject::merge (ONE) into (TWO)"
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ONE", "one", p.SRBlockOnlyInputValue, None),
                    ("TWO", "two", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ONE", "one", p.SRBlockOnlyInputValue, None),
                    ("TWO", "two", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&dogeiscutObject::stringify (OBJECT) (FORMAT)"
        object: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class keys(ThirdBlock):
        OPCODE = "&dogeiscutObject::keys of (OBJECT)"
        object: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OBJECT", "object", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("OBJECT", "object", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class values(ThirdBlock):
        OPCODE = "&dogeiscutObject::values of (OBJECT)"
        object: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OBJECT", "object", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("OBJECT", "object", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class entries(ThirdBlock):
        OPCODE = "&dogeiscutObject::entries of (OBJECT)"
        object: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OBJECT", "object", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("OBJECT", "object", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class is_(ThirdBlock):
        OPCODE = "&dogeiscutObject::does (VALUE) parse as an object?"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class for_each_k(ThirdBlock):
        OPCODE = "&dogeiscutObject::key"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE = "&dogeiscutObject::value"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&dogeiscutObject::for {:K:} {:V:} of (OBJECT) {SUBSTACK}"
        object: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("K", "k", p.SREmbeddedBlockInputValue, dogeiscutObject.for_each_k),
                    ("V", "v", p.SREmbeddedBlockInputValue, dogeiscutObject.for_each_v),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                    ("K", "k", p.SREmbeddedBlockInputValue, dogeiscutObject.for_each_k),
                    ("V", "v", p.SREmbeddedBlockInputValue, dogeiscutObject.for_each_v),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE = "&dogeiscutObject::#menu:stringifyFormat"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
