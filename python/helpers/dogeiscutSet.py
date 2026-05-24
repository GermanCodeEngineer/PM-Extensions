from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutSet:

    @grepr_dataclass()
    class blank(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&dogeiscutSet::blank set", inputs={}, dropdowns={})

    @grepr_dataclass()
    class from_list(ThirdBlock):
        list: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::set from list (LIST)",
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
                opcode="&dogeiscutSet::parse (INPUT) as set",
                inputs={
                    "INPUT": ThirdInputValue.as_input(
                        self.input, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class builder_current(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::current set", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class builder(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        set: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::set builder to (SET)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class has(ThirdBlock):
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class is_subset_of(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::is (ONE) a subset of [TWO]?",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_superset_of(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::is (ONE) a superset of [TWO]?",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_disjoint_from(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::is (ONE) disjoint from [TWO]?",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class size(ThirdBlock):
        set: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::size of (SET)",
                inputs={
                    "SET": ThirdInputValue.as_input(self.set, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class add(ThirdBlock):
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class delete(ThirdBlock):
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class union(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::union (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class intersect(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::intersect (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class difference(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::difference (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class symmetric_difference(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::symmetric difference (ONE) with (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class flat(ThirdBlock):
        set: INPUT_COMPATIBLE_T
        depth: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class to_string(ThirdBlock):
        set: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class for_each_v(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&dogeiscutSet::value", inputs={}, dropdowns={})

    @grepr_dataclass()
    class for_each(ThirdBlock):
        set: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class menu_list(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::#menu:list", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutSet::#menu:stringifyFormat", inputs={}, dropdowns={}
            )
