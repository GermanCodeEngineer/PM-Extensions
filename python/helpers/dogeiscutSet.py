from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutSet:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE = "&dogeiscutSet::blank set"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class from_list(ThirdBlock):
        OPCODE = "&dogeiscutSet::set from list (LIST)"
        INPUT_SPECS = (("LIST", "list", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        list: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE = "&dogeiscutSet::parse (INPUT) as set"
        INPUT_SPECS = (("INPUT", "input", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_current(ThirdBlock):
        OPCODE = "&dogeiscutSet::current set"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE = "&dogeiscutSet::set builder {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: dogeiscutSet.builder_current(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE = "&dogeiscutSet::append (VALUE) to builder"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE = "&dogeiscutSet::set builder to (SET)"
        INPUT_SPECS = (("SET", "set", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        set: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE = "&dogeiscutSet::(SET) has (VALUE)"
        INPUT_SPECS = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_subset_of(ThirdBlock):
        OPCODE = "&dogeiscutSet::is (ONE) a subset of [TWO]?"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_superset_of(ThirdBlock):
        OPCODE = "&dogeiscutSet::is (ONE) a superset of [TWO]?"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_disjoint_from(ThirdBlock):
        OPCODE = "&dogeiscutSet::is (ONE) disjoint from [TWO]?"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class size(ThirdBlock):
        OPCODE = "&dogeiscutSet::size of (SET)"
        INPUT_SPECS = (("SET", "set", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        set: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&dogeiscutSet::add (VALUE) to (SET)"
        INPUT_SPECS = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete(ThirdBlock):
        OPCODE = "&dogeiscutSet::delete (VALUE) from (SET)"
        INPUT_SPECS = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        set: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class union(ThirdBlock):
        OPCODE = "&dogeiscutSet::union (ONE) with (TWO)"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class intersect(ThirdBlock):
        OPCODE = "&dogeiscutSet::intersect (ONE) with (TWO)"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class difference(ThirdBlock):
        OPCODE = "&dogeiscutSet::difference (ONE) with (TWO)"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class symmetric_difference(ThirdBlock):
        OPCODE = "&dogeiscutSet::symmetric difference (ONE) with (TWO)"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class flat(ThirdBlock):
        OPCODE = "&dogeiscutSet::flat (SET) with depth (DEPTH)"
        INPUT_SPECS = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        set: INPUT_COMPATIBLE_T
        depth: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&dogeiscutSet::stringify (SET) (FORMAT)"
        INPUT_SPECS = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        set: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE = "&dogeiscutSet::value"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&dogeiscutSet::for {:V:} of (SET) {SUBSTACK}"
        INPUT_SPECS = (
            ("SET", "set", p.SRBlockOnlyInputValue, None),
            ("V", "v", p.SREmbeddedBlockInputValue, lambda: dogeiscutSet.for_each_v()),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        set: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_list(ThirdBlock):
        OPCODE = "&dogeiscutSet::#menu:list"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE = "&dogeiscutSet::#menu:stringifyFormat"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
