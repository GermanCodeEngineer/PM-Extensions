from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class agBuffer:

    @grepr_dataclass()
    class new_buffer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::create new array buffer of size (LENGTH)"
        INPUT_SPECS: ClassVar = (
            ("LENGTH", "length", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        length: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class buffer_of(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::parse (VALUE) as array buffer"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_url(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::get array buffer from url (URL)"
        INPUT_SPECS: ClassVar = (("URL", "url", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        url: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_base64(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::array buffer from base64 (BASE64)"
        INPUT_SPECS: ClassVar = (
            ("BASE64", "base64", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        base64: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_string(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::array buffer from string (STRING)"
        INPUT_SPECS: ClassVar = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_current(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::current buffer"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::array buffer builder {:CURRENT:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            (
                "CURRENT",
                "current",
                p.SREmbeddedBlockInputValue,
                lambda: agBuffer.builder_current(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE: ClassVar = (
            "&agBuffer::append ([TYPE]) value (VALUE) <ENDIAN> to builder"
        )
        INPUT_SPECS: ClassVar = (
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append_buffer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::append buffer (VALUE) to builder"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::set builder to (BUFFER)"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_value(ThirdBlock):
        OPCODE: ClassVar = (
            "&agBuffer::read ([TYPE]) value of (BUFFER) at (INDEX) <ENDIAN>"
        )
        INPUT_SPECS: ClassVar = (
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_value(ThirdBlock):
        OPCODE: ClassVar = (
            "&agBuffer::write ([TYPE]) value (VALUE) to (BUFFER) at (INDEX) <ENDIAN>"
        )
        INPUT_SPECS: ClassVar = (
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class write_sub_buffer(ThirdBlock):
        OPCODE: ClassVar = (
            "&agBuffer::write sub-buffer (SUBBUFFER) to (BUFFER) at (INDEX)"
        )
        INPUT_SPECS: ClassVar = (
            ("SUBBUFFER", "subbuffer", p.SRBlockOnlyInputValue, None),
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        subbuffer: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_buffer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::(VALUE) is array buffer?"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_size(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::byte length of buffer (BUFFER)"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_array(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::convert (BUFFER) to array"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_typed_array(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::convert (BUFFER) to ([TYPE]) typed array"
        INPUT_SPECS: ClassVar = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class buffer_to_string(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::array buffer (BUFFER) to string"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_base64(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::array buffer (BUFFER) to base64"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_data_url(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::array buffer (BUFFER) to data:url"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class read_null_terminated_string(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::read string at (INDEX) of (BUFFER)"
        INPUT_SPECS: ClassVar = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class write_null_terminated_string(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::write string (STRING) at (INDEX) of (BUFFER)"
        INPUT_SPECS: ClassVar = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class items_of(ThirdBlock):
        OPCODE: ClassVar = (
            "&agBuffer::get bytes (MIN) to (MAX) from (BUFFER) as new buffer"
        )
        INPUT_SPECS: ClassVar = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("MIN", "min", p.SRBlockAndTextInputValue, None),
            ("MAX", "max", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T
        min: INPUT_COMPATIBLE_T
        max: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class resize(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::resize (BUFFER) to (SIZE) bytes as new"
        INPUT_SPECS: ClassVar = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("SIZE", "size", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T
        size: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class resize_inst(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::resize (BUFFER) to (SIZE) bytes"
        INPUT_SPECS: ClassVar = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("SIZE", "size", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T
        size: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class copy(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::copy (BUFFER)"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::reverse (BUFFER)"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse_r(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::reverse (BUFFER) as new"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stringify(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::stringify (BUFFER) [MODE]"
        INPUT_SPECS: ClassVar = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("MODE", "mode"),)
        buffer: INPUT_COMPATIBLE_T
        mode: str

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::byte"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class for_each_i(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::index"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE: ClassVar = (
            "&agBuffer::for each [INDEX], {:BYTE:} of (BUFFER) {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            (
                "INDEX",
                "index",
                p.SREmbeddedBlockInputValue,
                lambda: agBuffer.for_each_i(),
            ),
            (
                "BYTE",
                "byte",
                p.SREmbeddedBlockInputValue,
                lambda: agBuffer.for_each_v(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        buffer: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class size_of_type(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::size of ([TYPE])"
        INPUT_SPECS: ClassVar = (
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class cast(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::cast (VALUE) to ([TYPE])"
        INPUT_SPECS: ClassVar = (
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_pointer(ThirdBlock):
        OPCODE: ClassVar = (
            "&agBuffer::create ([TYPE]) pointer for (BUFFER) at (INDEX) <ENDIAN>"
        )
        INPUT_SPECS: ClassVar = (
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::set value of pointer (PTR) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer_index(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::set address of pointer (PTR) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer_endian(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::set endian of pointer (PTR) to <VALUE>"
        INPUT_SPECS: ClassVar = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer_type(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::set type of pointer (PTR) to ([VALUE])"
        INPUT_SPECS: ClassVar = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer_buffer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::set buffer of pointer (PTR) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::get value of pointer (PTR)"
        INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer_index(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::get address of pointer (PTR)"
        INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer_type(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::get type of pointer (PTR)"
        INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer_endian(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::is pointer (PTR) little-endian?"
        INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer_buffer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::get array buffer of pointer (PTR)"
        INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_pointer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::is pointer [PTR]?"
        INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class copy_pointer(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::copy pointer (PTR)"
        INPUT_SPECS: ClassVar = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pointer_as_type(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::(PTR) as ([TYPE]) pointer <ENDIAN>"
        INPUT_SPECS: ClassVar = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        ptr: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class max_reporter_lines(ThirdBlock):
        OPCODE: ClassVar = (
            "&agBuffer::(only visual) set max lines shown in reporter output to (LINES)"
        )
        INPUT_SPECS: ClassVar = (("LINES", "lines", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        lines: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class error_handling(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::set disable error prevention to <VALUE>"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndBoolInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_datatypes(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::#menu:DATATYPES"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_pointer_types(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::#menu:POINTER_TYPES"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_stringifymode(ThirdBlock):
        OPCODE: ClassVar = "&agBuffer::#menu:STRINGIFYMODE"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
