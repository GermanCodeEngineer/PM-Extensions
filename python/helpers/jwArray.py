from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class jwArray:

    @staticmethod
    def blank() -> p.SRBlock:
        return p.SRBlock(opcode="&jwArray::blank array", inputs={}, dropdowns={})

    @staticmethod
    def blank_length(length: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::blank array of length (LENGTH)",
            inputs={
                "LENGTH": InputValue.try_as_input(length, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def from_list(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::array from list [LIST]",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def parse(input: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::parse (INPUT) as array",
            inputs={
                "INPUT": InputValue.try_as_input(input, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def split(string: INPUT_COMPATIBLE_T, divider: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::split (STRING) by (DIVIDER)",
            inputs={
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
                "DIVIDER": InputValue.try_as_input(divider, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def builder(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::array builder {:SHADOW:} {SUBSTACK}",
            inputs={
                "SHADOW": InputValue.try_as_input(
                    InputValue(jwArray.builder_current()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def builder_current() -> p.SRBlock:
        return p.SRBlock(opcode="&jwArray::current array", inputs={}, dropdowns={})

    @staticmethod
    def builder_append(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::append (VALUE) to builder",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def builder_set(array: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::set builder to (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def get(array: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::get (INDEX) in (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def items(
        array: INPUT_COMPATIBLE_T, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::items (X) to (Y) in (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def index(array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::index of (VALUE) in (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def has(array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::(ARRAY) has (VALUE)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def length(array: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::length of (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def set(
        array: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::set (INDEX) in (ARRAY) to (VALUE)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def append(array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::append (VALUE) to (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def concat(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::merge (ONE) with (TWO)",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockAndTextInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def fill(array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::fill (ARRAY) with (VALUE)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def reverse(array: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::reverse (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def splice(
        array: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T, items: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::splice (ARRAY) at (INDEX) with (ITEMS) items",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
                "ITEMS": InputValue.try_as_input(items, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def repeat(array: INPUT_COMPATIBLE_T, times: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::repeat (ARRAY) (TIMES) times",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "TIMES": InputValue.try_as_input(times, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def flat(array: INPUT_COMPATIBLE_T, depth: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::flat (ARRAY) with depth (DEPTH)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "DEPTH": InputValue.try_as_input(depth, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def to_string(array: INPUT_COMPATIBLE_T, format: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::stringify (ARRAY) [FORMAT]",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "FORMAT": p.SRDropdownValue(p.DropdownValueKind.STANDARD, format)
            },
        )

    @staticmethod
    def join(array: INPUT_COMPATIBLE_T, divider: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::join (ARRAY) with (DIVIDER)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "DIVIDER": InputValue.try_as_input(divider, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def sum(array: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::sum of (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def for_each_i() -> p.SRBlock:
        return p.SRBlock(opcode="&jwArray::index", inputs={}, dropdowns={})

    @staticmethod
    def for_each_v() -> p.SRBlock:
        return p.SRBlock(opcode="&jwArray::value", inputs={}, dropdowns={})

    @staticmethod
    def for_each(array: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::for {:I:} {:V:} of (ARRAY) {SUBSTACK}",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "I": InputValue.try_as_input(
                    InputValue(jwArray.for_each_i()), p.SREmbeddedBlockInputValue
                ),
                "V": InputValue.try_as_input(
                    InputValue(jwArray.for_each_v()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def basic_sort(array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::sort (ARRAY) {:I:} {:V:} > (VALUE)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
                "I": InputValue.try_as_input(
                    InputValue(jwArray.for_each_i()), p.SREmbeddedBlockInputValue
                ),
                "V": InputValue.try_as_input(
                    InputValue(jwArray.for_each_v()), p.SREmbeddedBlockInputValue
                ),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_list() -> p.SRBlock:
        return p.SRBlock(opcode="&jwArray::#menu:list", inputs={}, dropdowns={})

    @staticmethod
    def menu_stringify_format() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwArray::#menu:stringifyFormat", inputs={}, dropdowns={}
        )
