from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwArray:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE = "&jwArray::blank array"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class blank_length(ThirdBlock):
        OPCODE = "&jwArray::blank array of length (LENGTH)"
        INPUT_SPECS = (("LENGTH", "length", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        length: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_list(ThirdBlock):
        OPCODE = "&jwArray::array from list (LIST)"
        INPUT_SPECS = (("LIST", "list", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        list: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE = "&jwArray::parse (INPUT) as array"
        INPUT_SPECS = (("INPUT", "input", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class split(ThirdBlock):
        OPCODE = "&jwArray::split (STRING) by (DIVIDER)"
        INPUT_SPECS = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
            ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T
        divider: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE = "&jwArray::array builder {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, jwArray.builder_current),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_current(ThirdBlock):
        OPCODE = "&jwArray::current array"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE = "&jwArray::append (VALUE) to builder"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE = "&jwArray::set builder to (ARRAY)"
        INPUT_SPECS = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE = "&jwArray::get (INDEX) in (ARRAY)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class items(ThirdBlock):
        OPCODE = "&jwArray::items (X) to (Y) in (ARRAY)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class index(ThirdBlock):
        OPCODE = "&jwArray::index of (VALUE) in (ARRAY)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE = "&jwArray::(ARRAY) has (VALUE)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class length(ThirdBlock):
        OPCODE = "&jwArray::length of (ARRAY)"
        INPUT_SPECS = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&jwArray::set (INDEX) in (ARRAY) to (VALUE)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class append(ThirdBlock):
        OPCODE = "&jwArray::append (VALUE) to (ARRAY)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class concat(ThirdBlock):
        OPCODE = "&jwArray::merge (ONE) with (TWO)"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fill(ThirdBlock):
        OPCODE = "&jwArray::fill (ARRAY) with (VALUE)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse(ThirdBlock):
        OPCODE = "&jwArray::reverse (ARRAY)"
        INPUT_SPECS = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class splice(ThirdBlock):
        OPCODE = "&jwArray::splice (ARRAY) at (INDEX) with (ITEMS) items"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ITEMS", "items", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        items: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class repeat(ThirdBlock):
        OPCODE = "&jwArray::repeat (ARRAY) (TIMES) times"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("TIMES", "times", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        times: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class flat(ThirdBlock):
        OPCODE = "&jwArray::flat (ARRAY) with depth (DEPTH)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        depth: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&jwArray::stringify (ARRAY) (FORMAT)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join(ThirdBlock):
        OPCODE = "&jwArray::join (ARRAY) with (DIVIDER)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        divider: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class sum(ThirdBlock):
        OPCODE = "&jwArray::sum of (ARRAY)"
        INPUT_SPECS = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class for_each_i(ThirdBlock):
        OPCODE = "&jwArray::index"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE = "&jwArray::value"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&jwArray::for {:I:} {:V:} of (ARRAY) {SUBSTACK}"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, jwArray.for_each_i),
            ("V", "v", p.SREmbeddedBlockInputValue, jwArray.for_each_v),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class basic_sort(ThirdBlock):
        OPCODE = "&jwArray::sort (ARRAY) {:I:} {:V:} > (VALUE)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, jwArray.for_each_i),
            ("V", "v", p.SREmbeddedBlockInputValue, jwArray.for_each_v),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_list(ThirdBlock):
        OPCODE = "&jwArray::#menu:list"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE = "&jwArray::#menu:stringifyFormat"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
