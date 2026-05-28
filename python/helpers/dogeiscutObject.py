from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class dogeiscutObject:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::blank object"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::parse (VALUE) as object"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_entries(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::from entries (ARRAY)"
        INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class current_object(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::current object"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE: ClassVar = (
            "&dogeiscutObject::object builder {:CURRENT_OBJECT:} {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            (
                "CURRENT_OBJECT",
                "current_object",
                p.SREmbeddedBlockInputValue,
                lambda: dogeiscutObject.current_object(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::append key (KEY) value (VALUE) to builder"
        INPUT_SPECS: ClassVar = (
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        key: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append_empty(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::append key (KEY) to builder"
        INPUT_SPECS: ClassVar = (("KEY", "key", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::set builder to (OBJECT)"
        INPUT_SPECS: ClassVar = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::get (KEY) in (OBJECT)"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_path(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::get path (ARRAY) in (OBJECT)"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::(OBJECT) has key (KEY)"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class size(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::size of (OBJECT)"
        INPUT_SPECS: ClassVar = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::set (KEY) in (OBJECT) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_path(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::set path (ARRAY) in (OBJECT) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::delete key (KEY) from (OBJECT)"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_at_path(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::delete at path (ARRAY) from (OBJECT)"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class merge(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::merge (ONE) into (TWO)"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::stringify (OBJECT) (FORMAT)"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class keys(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::keys of (OBJECT)"
        INPUT_SPECS: ClassVar = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class values(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::values of (OBJECT)"
        INPUT_SPECS: ClassVar = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class entries(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::entries of (OBJECT)"
        INPUT_SPECS: ClassVar = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::does (VALUE) parse as an object?"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class for_each_k(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::key"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::value"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::for {:K:} {:V:} of (OBJECT) {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            (
                "K",
                "k",
                p.SREmbeddedBlockInputValue,
                lambda: dogeiscutObject.for_each_k(),
            ),
            (
                "V",
                "v",
                p.SREmbeddedBlockInputValue,
                lambda: dogeiscutObject.for_each_v(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutObject::#menu:stringifyFormat"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
