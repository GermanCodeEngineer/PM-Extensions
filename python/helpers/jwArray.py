from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwArray:

    class blank(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::blank array", inputs={}, dropdowns={})

    class blank_length(ThirdBlock):

        def __init__(self, length: INPUT_COMPATIBLE_T):
            self.length = length

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::blank array of length (LENGTH)",
                inputs={
                    "LENGTH": ThirdInputValue.as_input(
                        self.length, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class from_list(ThirdBlock):

        def __init__(self, list: INPUT_COMPATIBLE_T):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::array from list (LIST)",
                inputs={
                    "LIST": ThirdInputValue.as_input(self.list, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class parse(ThirdBlock):

        def __init__(self, input: INPUT_COMPATIBLE_T):
            self.input = input

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::parse (INPUT) as array",
                inputs={
                    "INPUT": ThirdInputValue.as_input(
                        self.input, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class split(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T, divider: INPUT_COMPATIBLE_T):
            self.string = string
            self.divider = divider

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::split (STRING) by (DIVIDER)",
                inputs={
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                    "DIVIDER": ThirdInputValue.as_input(
                        self.divider, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class builder(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::array builder {:SHADOW:} {SUBSTACK}",
                inputs={
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(jwArray.builder_current()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class builder_current(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::current array", inputs={}, dropdowns={})

    class builder_append(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::append (VALUE) to builder",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class builder_set(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T):
            self.array = array

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::set builder to (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class get(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T):
            self.array = array
            self.index = index

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::get (INDEX) in (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class items(ThirdBlock):

        def __init__(
            self,
            array: INPUT_COMPATIBLE_T,
            x: INPUT_COMPATIBLE_T,
            y: INPUT_COMPATIBLE_T,
        ):
            self.array = array
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::items (X) to (Y) in (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class index(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.array = array
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::index of (VALUE) in (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class has(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.array = array
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::(ARRAY) has (VALUE)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class length(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T):
            self.array = array

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::length of (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class set(ThirdBlock):

        def __init__(
            self,
            array: INPUT_COMPATIBLE_T,
            index: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
        ):
            self.array = array
            self.index = index
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::set (INDEX) in (ARRAY) to (VALUE)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class append(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.array = array
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::append (VALUE) to (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class concat(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::merge (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class fill(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.array = array
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::fill (ARRAY) with (VALUE)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class reverse(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T):
            self.array = array

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::reverse (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class splice(ThirdBlock):

        def __init__(
            self,
            array: INPUT_COMPATIBLE_T,
            index: INPUT_COMPATIBLE_T,
            items: INPUT_COMPATIBLE_T,
        ):
            self.array = array
            self.index = index
            self.items = items

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::splice (ARRAY) at (INDEX) with (ITEMS) items",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                    "ITEMS": ThirdInputValue.as_input(
                        self.items, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class repeat(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, times: INPUT_COMPATIBLE_T):
            self.array = array
            self.times = times

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::repeat (ARRAY) (TIMES) times",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "TIMES": ThirdInputValue.as_input(
                        self.times, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class flat(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, depth: INPUT_COMPATIBLE_T):
            self.array = array
            self.depth = depth

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::flat (ARRAY) with depth (DEPTH)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "DEPTH": ThirdInputValue.as_input(
                        self.depth, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class to_string(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T):
            self.array = array
            self.format = format

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::stringify (ARRAY) (FORMAT)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "FORMAT": ThirdInputValue.as_input(
                        self.format, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class join(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, divider: INPUT_COMPATIBLE_T):
            self.array = array
            self.divider = divider

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::join (ARRAY) with (DIVIDER)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "DIVIDER": ThirdInputValue.as_input(
                        self.divider, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class sum(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T):
            self.array = array

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::sum of (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class for_each_i(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::index", inputs={}, dropdowns={})

    class for_each_v(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::value", inputs={}, dropdowns={})

    class for_each(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.array = array
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::for {:I:} {:V:} of (ARRAY) {SUBSTACK}",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(jwArray.for_each_i()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "V": ThirdInputValue.as_input(
                        ThirdInputValue(jwArray.for_each_v()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class basic_sort(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.array = array
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::sort (ARRAY) {:I:} {:V:} > (VALUE)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(jwArray.for_each_i()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "V": ThirdInputValue.as_input(
                        ThirdInputValue(jwArray.for_each_v()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class menu_list(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::#menu:list", inputs={}, dropdowns={})

    class menu_stringify_format(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::#menu:stringifyFormat", inputs={}, dropdowns={}
            )
