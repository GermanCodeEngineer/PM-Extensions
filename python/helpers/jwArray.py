from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwArray:

    @grepr_dataclass()
    class blank(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::blank array", inputs={}, dropdowns={})

    @grepr_dataclass()
    class blank_length(ThirdBlock):
        length: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class from_list(ThirdBlock):
        list: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::array from list (LIST)",
                inputs={
                    "LIST": ThirdInputValue.as_input(self.list, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class parse(ThirdBlock):
        input: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class split(ThirdBlock):
        string: INPUT_COMPATIBLE_T
        divider: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class builder(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class builder_current(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::current array", inputs={}, dropdowns={})

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        array: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class get(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class items(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class index(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class has(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class length(ThirdBlock):
        array: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class set(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class append(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class concat(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::merge (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class fill(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class reverse(ThirdBlock):
        array: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class splice(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        items: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class repeat(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        times: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class flat(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        depth: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class to_string(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class join(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        divider: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class sum(ThirdBlock):
        array: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class for_each_i(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::index", inputs={}, dropdowns={})

    @grepr_dataclass()
    class for_each_v(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::value", inputs={}, dropdowns={})

    @grepr_dataclass()
    class for_each(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class basic_sort(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class menu_list(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwArray::#menu:list", inputs={}, dropdowns={})

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwArray::#menu:stringifyFormat", inputs={}, dropdowns={}
            )
