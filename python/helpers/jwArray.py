from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwArray:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::blank array"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class blank_length(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::blank array of length (LENGTH)"
        INPUT_SPECS: ClassVar = (
            ("LENGTH", "length", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        length: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_list(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::array from list (LIST)"
        INPUT_SPECS: ClassVar = (("LIST", "list", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        list: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::parse (INPUT) as array"
        INPUT_SPECS: ClassVar = (("INPUT", "input", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class split(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::split (STRING) by (DIVIDER)"
        INPUT_SPECS: ClassVar = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
            ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T
        divider: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::array builder {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: jwArray.builder_current(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_current(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::current array"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::append (VALUE) to builder"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::set builder to (ARRAY)"
        INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::get (INDEX) in (ARRAY)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class items(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::items (X) to (Y) in (ARRAY)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class index(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::index of (VALUE) in (ARRAY)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::(ARRAY) has (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class length(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::length of (ARRAY)"
        INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::set (INDEX) in (ARRAY) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class append(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::append (VALUE) to (ARRAY)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class concat(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::merge (ONE) with (TWO)"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fill(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::fill (ARRAY) with (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::reverse (ARRAY)"
        INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class splice(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::splice (ARRAY) at (INDEX) with (ITEMS) items"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ITEMS", "items", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        items: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class repeat(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::repeat (ARRAY) (TIMES) times"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("TIMES", "times", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        times: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class flat(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::flat (ARRAY) with depth (DEPTH)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        depth: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::stringify (ARRAY) (FORMAT)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::join (ARRAY) with (DIVIDER)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        divider: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class sum(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::sum of (ARRAY)"
        INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class for_each_i(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::index"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::value"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::for {:I:} {:V:} of (ARRAY) {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: jwArray.for_each_i()),
            ("V", "v", p.SREmbeddedBlockInputValue, lambda: jwArray.for_each_v()),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class basic_sort(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::sort (ARRAY) {:I:} {:V:} > (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: jwArray.for_each_i()),
            ("V", "v", p.SREmbeddedBlockInputValue, lambda: jwArray.for_each_v()),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_list(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::#menu:list"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE: ClassVar = "&jwArray::#menu:stringifyFormat"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
