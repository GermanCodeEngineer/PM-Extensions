from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutObject:

    @grepr_dataclass()
    class blank(ThirdBlock):
        OPCODE = "&dogeiscutObject::blank object"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE = "&dogeiscutObject::parse (VALUE) as object"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_entries(ThirdBlock):
        OPCODE = "&dogeiscutObject::from entries (ARRAY)"
        INPUT_SPECS = (("ARRAY", "array", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class current_object(ThirdBlock):
        OPCODE = "&dogeiscutObject::current object"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE = "&dogeiscutObject::object builder {:CURRENT_OBJECT:} {SUBSTACK}"
        INPUT_SPECS = (
            (
                "CURRENT_OBJECT",
                "current_object",
                p.SREmbeddedBlockInputValue,
                lambda: dogeiscutObject.current_object(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE = "&dogeiscutObject::append key (KEY) value (VALUE) to builder"
        INPUT_SPECS = (
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        key: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append_empty(ThirdBlock):
        OPCODE = "&dogeiscutObject::append key (KEY) to builder"
        INPUT_SPECS = (("KEY", "key", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE = "&dogeiscutObject::set builder to (OBJECT)"
        INPUT_SPECS = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE = "&dogeiscutObject::get (KEY) in (OBJECT)"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_path(ThirdBlock):
        OPCODE = "&dogeiscutObject::get path (ARRAY) in (OBJECT)"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class has(ThirdBlock):
        OPCODE = "&dogeiscutObject::(OBJECT) has key (KEY)"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class size(ThirdBlock):
        OPCODE = "&dogeiscutObject::size of (OBJECT)"
        INPUT_SPECS = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&dogeiscutObject::set (KEY) in (OBJECT) to (VALUE)"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_path(ThirdBlock):
        OPCODE = "&dogeiscutObject::set path (ARRAY) in (OBJECT) to (VALUE)"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete(ThirdBlock):
        OPCODE = "&dogeiscutObject::delete key (KEY) from (OBJECT)"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("KEY", "key", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_at_path(ThirdBlock):
        OPCODE = "&dogeiscutObject::delete at path (ARRAY) from (OBJECT)"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class merge(ThirdBlock):
        OPCODE = "&dogeiscutObject::merge (ONE) into (TWO)"
        INPUT_SPECS = (
            ("ONE", "one", p.SRBlockOnlyInputValue, None),
            ("TWO", "two", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&dogeiscutObject::stringify (OBJECT) (FORMAT)"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class keys(ThirdBlock):
        OPCODE = "&dogeiscutObject::keys of (OBJECT)"
        INPUT_SPECS = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class values(ThirdBlock):
        OPCODE = "&dogeiscutObject::values of (OBJECT)"
        INPUT_SPECS = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class entries(ThirdBlock):
        OPCODE = "&dogeiscutObject::entries of (OBJECT)"
        INPUT_SPECS = (("OBJECT", "object", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_(ThirdBlock):
        OPCODE = "&dogeiscutObject::does (VALUE) parse as an object?"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class for_each_k(ThirdBlock):
        OPCODE = "&dogeiscutObject::key"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE = "&dogeiscutObject::value"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&dogeiscutObject::for {:K:} {:V:} of (OBJECT) {SUBSTACK}"
        INPUT_SPECS = (
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
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE = "&dogeiscutObject::#menu:stringifyFormat"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
