from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class jwArray:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE = "&jwArray::blank array"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class blank_length(ThirdBlock):
        OPCODE = "&jwArray::blank array of length (LENGTH)"
        length: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LENGTH", "length", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("LENGTH", "length", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class from_list(ThirdBlock):
        OPCODE = "&jwArray::array from list (LIST)"
        list: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LIST", "list", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("LIST", "list", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE = "&jwArray::parse (INPUT) as array"
        input: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INPUT", "input", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("INPUT", "input", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class split(ThirdBlock):
        OPCODE = "&jwArray::split (STRING) by (DIVIDER)"
        string: INPUT_COMPATIBLE_T
        divider: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                    ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                    ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE = "&jwArray::array builder {:SHADOW:} {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        jwArray.builder_current,
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
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        jwArray.builder_current,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class builder_current(ThirdBlock):
        OPCODE = "&jwArray::current array"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE = "&jwArray::append (VALUE) to builder"
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
    class builder_set(ThirdBlock):
        OPCODE = "&jwArray::set builder to (ARRAY)"
        array: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ARRAY", "array", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ARRAY", "array", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE = "&jwArray::get (INDEX) in (ARRAY)"
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class items(ThirdBlock):
        OPCODE = "&jwArray::items (X) to (Y) in (ARRAY)"
        array: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class index(ThirdBlock):
        OPCODE = "&jwArray::index of (VALUE) in (ARRAY)"
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE = "&jwArray::(ARRAY) has (VALUE)"
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class length(ThirdBlock):
        OPCODE = "&jwArray::length of (ARRAY)"
        array: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ARRAY", "array", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ARRAY", "array", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&jwArray::set (INDEX) in (ARRAY) to (VALUE)"
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class append(ThirdBlock):
        OPCODE = "&jwArray::append (VALUE) to (ARRAY)"
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class concat(ThirdBlock):
        OPCODE = "&jwArray::merge (ONE) with (TWO)"
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
    class fill(ThirdBlock):
        OPCODE = "&jwArray::fill (ARRAY) with (VALUE)"
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class reverse(ThirdBlock):
        OPCODE = "&jwArray::reverse (ARRAY)"
        array: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ARRAY", "array", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ARRAY", "array", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class splice(ThirdBlock):
        OPCODE = "&jwArray::splice (ARRAY) at (INDEX) with (ITEMS) items"
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        items: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ITEMS", "items", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ITEMS", "items", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class repeat(ThirdBlock):
        OPCODE = "&jwArray::repeat (ARRAY) (TIMES) times"
        array: INPUT_COMPATIBLE_T
        times: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("TIMES", "times", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("TIMES", "times", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class flat(ThirdBlock):
        OPCODE = "&jwArray::flat (ARRAY) with depth (DEPTH)"
        array: INPUT_COMPATIBLE_T
        depth: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&jwArray::stringify (ARRAY) (FORMAT)"
        array: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class join(ThirdBlock):
        OPCODE = "&jwArray::join (ARRAY) with (DIVIDER)"
        array: INPUT_COMPATIBLE_T
        divider: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class sum(ThirdBlock):
        OPCODE = "&jwArray::sum of (ARRAY)"
        array: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ARRAY", "array", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ARRAY", "array", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class for_each_i(ThirdBlock):
        OPCODE = "&jwArray::index"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE = "&jwArray::value"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&jwArray::for {:I:} {:V:} of (ARRAY) {SUBSTACK}"
        array: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, jwArray.for_each_i),
                    ("V", "v", p.SREmbeddedBlockInputValue, jwArray.for_each_v),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, jwArray.for_each_i),
                    ("V", "v", p.SREmbeddedBlockInputValue, jwArray.for_each_v),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class basic_sort(ThirdBlock):
        OPCODE = "&jwArray::sort (ARRAY) {:I:} {:V:} > (VALUE)"
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, jwArray.for_each_i),
                    ("V", "v", p.SREmbeddedBlockInputValue, jwArray.for_each_v),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, jwArray.for_each_i),
                    ("V", "v", p.SREmbeddedBlockInputValue, jwArray.for_each_v),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_list(ThirdBlock):
        OPCODE = "&jwArray::#menu:list"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE = "&jwArray::#menu:stringifyFormat"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
