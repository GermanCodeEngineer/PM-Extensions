from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class dogeiscutSet:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE = "&dogeiscutSet::blank set"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class from_list(ThirdBlock):
        OPCODE = "&dogeiscutSet::set from list (LIST)"
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
        OPCODE = "&dogeiscutSet::parse (INPUT) as set"
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
    class builder_current(ThirdBlock):
        OPCODE = "&dogeiscutSet::current set"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE = "&dogeiscutSet::set builder {:SHADOW:} {SUBSTACK}"
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
                        dogeiscutSet.builder_current,
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
                        dogeiscutSet.builder_current,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE = "&dogeiscutSet::append (VALUE) to builder"
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
        OPCODE = "&dogeiscutSet::set builder to (SET)"
        set: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("SET", "set", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SET", "set", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE = "&dogeiscutSet::(SET) has (VALUE)"
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_subset_of(ThirdBlock):
        OPCODE = "&dogeiscutSet::is (ONE) a subset of [TWO]?"
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
    class is_superset_of(ThirdBlock):
        OPCODE = "&dogeiscutSet::is (ONE) a superset of [TWO]?"
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
    class is_disjoint_from(ThirdBlock):
        OPCODE = "&dogeiscutSet::is (ONE) disjoint from [TWO]?"
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
    class size(ThirdBlock):
        OPCODE = "&dogeiscutSet::size of (SET)"
        set: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("SET", "set", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SET", "set", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&dogeiscutSet::add (VALUE) to (SET)"
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class delete(ThirdBlock):
        OPCODE = "&dogeiscutSet::delete (VALUE) from (SET)"
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class union(ThirdBlock):
        OPCODE = "&dogeiscutSet::union (ONE) with (TWO)"
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
    class intersect(ThirdBlock):
        OPCODE = "&dogeiscutSet::intersect (ONE) with (TWO)"
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
    class difference(ThirdBlock):
        OPCODE = "&dogeiscutSet::difference (ONE) with (TWO)"
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
    class symmetric_difference(ThirdBlock):
        OPCODE = "&dogeiscutSet::symmetric difference (ONE) with (TWO)"
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
    class flat(ThirdBlock):
        OPCODE = "&dogeiscutSet::flat (SET) with depth (DEPTH)"
        set: INPUT_COMPATIBLE_T
        depth: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&dogeiscutSet::stringify (SET) (FORMAT)"
        set: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE = "&dogeiscutSet::value"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&dogeiscutSet::for {:V:} of (SET) {SUBSTACK}"
        set: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("V", "v", p.SREmbeddedBlockInputValue, dogeiscutSet.for_each_v),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SET", "set", p.SRBlockOnlyInputValue, None),
                    ("V", "v", p.SREmbeddedBlockInputValue, dogeiscutSet.for_each_v),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_list(ThirdBlock):
        OPCODE = "&dogeiscutSet::#menu:list"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE = "&dogeiscutSet::#menu:stringifyFormat"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
