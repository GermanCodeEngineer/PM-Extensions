from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class agBuffer:

    @grepr_dataclass()
    class new_buffer(ThirdBlock):
        OPCODE = "&agBuffer::create new array buffer of size (LENGTH)"
        INPUT_SPECS = (("LENGTH", "length", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        length: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class buffer_of(ThirdBlock):
        OPCODE = "&agBuffer::parse (VALUE) as array buffer"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_url(ThirdBlock):
        OPCODE = "&agBuffer::get array buffer from url (URL)"
        INPUT_SPECS = (("URL", "url", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        url: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_base64(ThirdBlock):
        OPCODE = "&agBuffer::array buffer from base64 (BASE64)"
        INPUT_SPECS = (("BASE64", "base64", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        base64: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class from_string(ThirdBlock):
        OPCODE = "&agBuffer::array buffer from string (STRING)"
        INPUT_SPECS = (("STRING", "string", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_current(ThirdBlock):
        OPCODE = "&agBuffer::current buffer"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE = "&agBuffer::array buffer builder {:CURRENT:} {SUBSTACK}"
        INPUT_SPECS = (
            (
                "CURRENT",
                "current",
                p.SREmbeddedBlockInputValue,
                lambda: agBuffer.builder_current(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE = "&agBuffer::append ([TYPE]) value (VALUE) <ENDIAN> to builder"
        INPUT_SPECS = (
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_append_buffer(ThirdBlock):
        OPCODE = "&agBuffer::append buffer (VALUE) to builder"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE = "&agBuffer::set builder to (BUFFER)"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_value(ThirdBlock):
        OPCODE = "&agBuffer::read ([TYPE]) value of (BUFFER) at (INDEX) <ENDIAN>"
        INPUT_SPECS = (
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_value(ThirdBlock):
        OPCODE = (
            "&agBuffer::write ([TYPE]) value (VALUE) to (BUFFER) at (INDEX) <ENDIAN>"
        )
        INPUT_SPECS = (
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class write_sub_buffer(ThirdBlock):
        OPCODE = "&agBuffer::write sub-buffer (SUBBUFFER) to (BUFFER) at (INDEX)"
        INPUT_SPECS = (
            ("SUBBUFFER", "subbuffer", p.SRBlockOnlyInputValue, None),
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        subbuffer: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_buffer(ThirdBlock):
        OPCODE = "&agBuffer::(VALUE) is array buffer?"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_size(ThirdBlock):
        OPCODE = "&agBuffer::byte length of buffer (BUFFER)"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_array(ThirdBlock):
        OPCODE = "&agBuffer::convert (BUFFER) to array"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_typed_array(ThirdBlock):
        OPCODE = "&agBuffer::convert (BUFFER) to ([TYPE]) typed array"
        INPUT_SPECS = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class buffer_to_string(ThirdBlock):
        OPCODE = "&agBuffer::array buffer (BUFFER) to string"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_base64(ThirdBlock):
        OPCODE = "&agBuffer::array buffer (BUFFER) to base64"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_data_url(ThirdBlock):
        OPCODE = "&agBuffer::array buffer (BUFFER) to data:url"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class read_null_terminated_string(ThirdBlock):
        OPCODE = "&agBuffer::read string at (INDEX) of (BUFFER)"
        INPUT_SPECS = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class write_null_terminated_string(ThirdBlock):
        OPCODE = "&agBuffer::write string (STRING) at (INDEX) of (BUFFER)"
        INPUT_SPECS = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class items_of(ThirdBlock):
        OPCODE = "&agBuffer::get bytes (MIN) to (MAX) from (BUFFER) as new buffer"
        INPUT_SPECS = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("MIN", "min", p.SRBlockAndTextInputValue, None),
            ("MAX", "max", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T
        min: INPUT_COMPATIBLE_T
        max: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class resize(ThirdBlock):
        OPCODE = "&agBuffer::resize (BUFFER) to (SIZE) bytes as new"
        INPUT_SPECS = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("SIZE", "size", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T
        size: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class resize_inst(ThirdBlock):
        OPCODE = "&agBuffer::resize (BUFFER) to (SIZE) bytes"
        INPUT_SPECS = (
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("SIZE", "size", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T
        size: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class copy(ThirdBlock):
        OPCODE = "&agBuffer::copy (BUFFER)"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse(ThirdBlock):
        OPCODE = "&agBuffer::reverse (BUFFER)"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse_r(ThirdBlock):
        OPCODE = "&agBuffer::reverse (BUFFER) as new"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stringify(ThirdBlock):
        OPCODE = "&agBuffer::stringify (BUFFER) [MODE]"
        INPUT_SPECS = (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = (("MODE", "mode"),)
        buffer: INPUT_COMPATIBLE_T
        mode: str

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE = "&agBuffer::byte"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class for_each_i(ThirdBlock):
        OPCODE = "&agBuffer::index"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&agBuffer::for each [INDEX], {:BYTE:} of (BUFFER) {SUBSTACK}"
        INPUT_SPECS = (
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
        DROPDOWN_SPECS = ()
        buffer: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class size_of_type(ThirdBlock):
        OPCODE = "&agBuffer::size of ([TYPE])"
        INPUT_SPECS = (("TYPE", "type", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class cast(ThirdBlock):
        OPCODE = "&agBuffer::cast (VALUE) to ([TYPE])"
        INPUT_SPECS = (
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_pointer(ThirdBlock):
        OPCODE = "&agBuffer::create ([TYPE]) pointer for (BUFFER) at (INDEX) <ENDIAN>"
        INPUT_SPECS = (
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
            ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer(ThirdBlock):
        OPCODE = "&agBuffer::set value of pointer (PTR) to (VALUE)"
        INPUT_SPECS = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer_index(ThirdBlock):
        OPCODE = "&agBuffer::set address of pointer (PTR) to (VALUE)"
        INPUT_SPECS = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer_endian(ThirdBlock):
        OPCODE = "&agBuffer::set endian of pointer (PTR) to <VALUE>"
        INPUT_SPECS = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer_type(ThirdBlock):
        OPCODE = "&agBuffer::set type of pointer (PTR) to ([VALUE])"
        INPUT_SPECS = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_pointer_buffer(ThirdBlock):
        OPCODE = "&agBuffer::set buffer of pointer (PTR) to (VALUE)"
        INPUT_SPECS = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer(ThirdBlock):
        OPCODE = "&agBuffer::get value of pointer (PTR)"
        INPUT_SPECS = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer_index(ThirdBlock):
        OPCODE = "&agBuffer::get address of pointer (PTR)"
        INPUT_SPECS = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer_type(ThirdBlock):
        OPCODE = "&agBuffer::get type of pointer (PTR)"
        INPUT_SPECS = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer_endian(ThirdBlock):
        OPCODE = "&agBuffer::is pointer (PTR) little-endian?"
        INPUT_SPECS = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_pointer_buffer(ThirdBlock):
        OPCODE = "&agBuffer::get array buffer of pointer (PTR)"
        INPUT_SPECS = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_pointer(ThirdBlock):
        OPCODE = "&agBuffer::is pointer [PTR]?"
        INPUT_SPECS = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class copy_pointer(ThirdBlock):
        OPCODE = "&agBuffer::copy pointer (PTR)"
        INPUT_SPECS = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pointer_as_type(ThirdBlock):
        OPCODE = "&agBuffer::(PTR) as ([TYPE]) pointer <ENDIAN>"
        INPUT_SPECS = (
            ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
            ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        ptr: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class max_reporter_lines(ThirdBlock):
        OPCODE = (
            "&agBuffer::(only visual) set max lines shown in reporter output to (LINES)"
        )
        INPUT_SPECS = (("LINES", "lines", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        lines: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class error_handling(ThirdBlock):
        OPCODE = "&agBuffer::set disable error prevention to <VALUE>"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndBoolInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_datatypes(ThirdBlock):
        OPCODE = "&agBuffer::#menu:DATATYPES"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_pointer_types(ThirdBlock):
        OPCODE = "&agBuffer::#menu:POINTER_TYPES"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_stringifymode(ThirdBlock):
        OPCODE = "&agBuffer::#menu:STRINGIFYMODE"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
