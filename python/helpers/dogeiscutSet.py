from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class dogeiscutSet:

    @staticmethod
    def blank() -> p.SRBlock:
        return p.SRBlock(opcode="&dogeiscutSet::blank set", inputs={}, dropdowns={})

    @staticmethod
    def from_list(list: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::set from list (LIST)",
            inputs={"LIST": InputValue.try_as_input(list, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def parse(input: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::parse (INPUT) as set",
            inputs={
                "INPUT": InputValue.try_as_input(input, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def builder_current() -> p.SRBlock:
        return p.SRBlock(opcode="&dogeiscutSet::current set", inputs={}, dropdowns={})

    @staticmethod
    def builder(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::set builder {:SHADOW:} {SUBSTACK}",
            inputs={
                "SHADOW": InputValue.try_as_input(
                    InputValue(dogeiscutSet.builder_current()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def builder_append(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::append (VALUE) to builder",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def builder_set(set: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::set builder to (SET)",
            inputs={"SET": InputValue.try_as_input(set, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def has(set: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::(SET) has (VALUE)",
            inputs={
                "SET": InputValue.try_as_input(set, p.SRBlockOnlyInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_subset_of(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::is (ONE) a subset of [TWO]?",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockOnlyInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_superset_of(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::is (ONE) a superset of [TWO]?",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockOnlyInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_disjoint_from(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::is (ONE) disjoint from [TWO]?",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockOnlyInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def size(set: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::size of (SET)",
            inputs={"SET": InputValue.try_as_input(set, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def add(set: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::add (VALUE) to (SET)",
            inputs={
                "SET": InputValue.try_as_input(set, p.SRBlockOnlyInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def delete(set: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::delete (VALUE) from (SET)",
            inputs={
                "SET": InputValue.try_as_input(set, p.SRBlockOnlyInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def union(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::union (ONE) with (TWO)",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockOnlyInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def intersect(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::intersect (ONE) with (TWO)",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockOnlyInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def difference(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::difference (ONE) with (TWO)",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockOnlyInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def symmetric_difference(
        one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::symmetric difference (ONE) with (TWO)",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockOnlyInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def flat(set: INPUT_COMPATIBLE_T, depth: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::flat (SET) with depth (DEPTH)",
            inputs={
                "SET": InputValue.try_as_input(set, p.SRBlockOnlyInputValue),
                "DEPTH": InputValue.try_as_input(depth, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def to_string(set: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::stringify (SET) (FORMAT)",
            inputs={
                "SET": InputValue.try_as_input(set, p.SRBlockOnlyInputValue),
                "FORMAT": InputValue.try_as_input(format, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def for_each_v() -> p.SRBlock:
        return p.SRBlock(opcode="&dogeiscutSet::value", inputs={}, dropdowns={})

    @staticmethod
    def for_each(set: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::for {:V:} of (SET) {SUBSTACK}",
            inputs={
                "SET": InputValue.try_as_input(set, p.SRBlockOnlyInputValue),
                "V": InputValue.try_as_input(
                    InputValue(dogeiscutSet.for_each_v()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_list() -> p.SRBlock:
        return p.SRBlock(opcode="&dogeiscutSet::#menu:list", inputs={}, dropdowns={})

    @staticmethod
    def menu_stringify_format() -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutSet::#menu:stringifyFormat", inputs={}, dropdowns={}
        )
