from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutSet:

    class blank(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&dogeiscutSet::blank set", inputs={}, dropdowns={})

    class from_list(ThirdBlock):

        def __init__(self, list: INPUT_COMPATIBLE_T):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::set from list (LIST)",
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
                opcode="&dogeiscutSet::parse (INPUT) as set",
                inputs={
                    "INPUT": ThirdInputValue.as_input(
                        self.input, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class builder_current(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::current set", inputs={}, dropdowns={}
            )

    class builder(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::set builder {:SHADOW:} {SUBSTACK}",
                inputs={
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(dogeiscutSet.builder_current()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class builder_append(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::append (VALUE) to builder",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class builder_set(ThirdBlock):

        def __init__(self, set: INPUT_COMPATIBLE_T):
            self.set = set

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::set builder to (SET)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class has(ThirdBlock):

        def __init__(self, set: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.set = set
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::(SET) has (VALUE)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class is_subset_of(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::is (ONE) a subset of [TWO]?",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class is_superset_of(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::is (ONE) a superset of [TWO]?",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class is_disjoint_from(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::is (ONE) disjoint from [TWO]?",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class size(ThirdBlock):

        def __init__(self, set: INPUT_COMPATIBLE_T):
            self.set = set

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::size of (SET)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class add(ThirdBlock):

        def __init__(self, set: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.set = set
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::add (VALUE) to (SET)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class delete(ThirdBlock):

        def __init__(self, set: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.set = set
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::delete (VALUE) from (SET)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class union(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::union (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class intersect(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::intersect (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class difference(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::difference (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class symmetric_difference(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::symmetric difference (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class flat(ThirdBlock):

        def __init__(self, set: INPUT_COMPATIBLE_T, depth: INPUT_COMPATIBLE_T):
            self.set = set
            self.depth = depth

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::flat (SET) with depth (DEPTH)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue),
                    "DEPTH": ThirdInputValue.as_input(
                        self.depth, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class to_string(ThirdBlock):

        def __init__(self, set: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T):
            self.set = set
            self.format = format

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::stringify (SET) (FORMAT)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue),
                    "FORMAT": ThirdInputValue.as_input(
                        self.format, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class for_each_v(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&dogeiscutSet::value", inputs={}, dropdowns={})

    class for_each(ThirdBlock):

        def __init__(self, set: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.set = set
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::for {:V:} of (SET) {SUBSTACK}",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue),
                    "V": ThirdInputValue.as_input(
                        ThirdInputValue(dogeiscutSet.for_each_v()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class menu_list(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::#menu:list", inputs={}, dropdowns={}
            )

    class menu_stringify_format(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::#menu:stringifyFormat", inputs={}, dropdowns={}
            )
