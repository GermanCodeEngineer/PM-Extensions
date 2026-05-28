from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class dogeiscutSet:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::blank set"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class from_list(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::set from list (LIST)"
        INPUT_SPECS: ClassVar = (("LIST", "list", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        list: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::parse (INPUT) as set"
        INPUT_SPECS: ClassVar = (("INPUT", "input", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_current(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::current set"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::set builder {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: dogeiscutSet.builder_current(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::append (VALUE) to builder"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::set builder to (SET)"
        INPUT_SPECS: ClassVar = (("SET", "set", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        set: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::(SET) has (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_subset_of(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::is (ONE) a subset of [TWO]?"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_superset_of(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::is (ONE) a superset of [TWO]?"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_disjoint_from(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::is (ONE) disjoint from [TWO]?"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class size(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::size of (SET)"
        INPUT_SPECS: ClassVar = (("SET", "set", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        set: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::add (VALUE) to (SET)"
        INPUT_SPECS: ClassVar = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::delete (VALUE) from (SET)"
        INPUT_SPECS: ClassVar = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class union(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::union (ONE) with (TWO)"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class intersect(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::intersect (ONE) with (TWO)"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class difference(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::difference (ONE) with (TWO)"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class symmetric_difference(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::symmetric difference (ONE) with (TWO)"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class flat(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::flat (SET) with depth (DEPTH)"
        INPUT_SPECS: ClassVar = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        set: INPUT_COMPATIBLE_T
        depth: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::stringify (SET) (FORMAT)"
        INPUT_SPECS: ClassVar = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        set: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::value"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::for {:V:} of (SET) {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("V", "v", p.SREmbeddedBlockInputValue, lambda: dogeiscutSet.for_each_v()),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        set: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_list(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::#menu:list"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutSet::#menu:stringifyFormat"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
