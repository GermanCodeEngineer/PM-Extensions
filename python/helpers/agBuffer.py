from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class agBuffer:

    @staticmethod
    def new_buffer(length: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::create new array buffer of size (LENGTH)",
            inputs={
                "LENGTH": InputValue.try_as_input(length, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def buffer_of(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::parse (VALUE) as array buffer",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def from_url(url: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::get array buffer from url (URL)",
            inputs={"URL": InputValue.try_as_input(url, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def from_base64(base64: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::array buffer from base64 (BASE64)",
            inputs={
                "BASE64": InputValue.try_as_input(base64, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def from_string(string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::array buffer from string (STRING)",
            inputs={
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def builder_current() -> p.SRBlock:
        return p.SRBlock(opcode="&agBuffer::current buffer", inputs={}, dropdowns={})

    @staticmethod
    def builder(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::array buffer builder {:CURRENT:} {SUBSTACK}",
            inputs={
                "CURRENT": InputValue.try_as_input(
                    InputValue(agBuffer.builder_current()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def builder_append(
        type: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T, endian: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::append ([TYPE]) value (VALUE) <ENDIAN> to builder",
            inputs={
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
                "ENDIAN": InputValue.try_as_input(endian, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def builder_append_buffer(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::append buffer (VALUE) to builder",
            inputs={"VALUE": InputValue.try_as_input(value, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def builder_set(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::set builder to (BUFFER)",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_value(
        type: INPUT_COMPATIBLE_T,
        value: INPUT_COMPATIBLE_T,
        buffer: INPUT_COMPATIBLE_T,
        index: INPUT_COMPATIBLE_T,
        endian: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::read ([TYPE]) value of (BUFFER) at (INDEX) <ENDIAN>",
            inputs={
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
                "ENDIAN": InputValue.try_as_input(endian, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_value(
        type: INPUT_COMPATIBLE_T,
        value: INPUT_COMPATIBLE_T,
        buffer: INPUT_COMPATIBLE_T,
        index: INPUT_COMPATIBLE_T,
        endian: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::write ([TYPE]) value (VALUE) to (BUFFER) at (INDEX) <ENDIAN>",
            inputs={
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
                "ENDIAN": InputValue.try_as_input(endian, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def write_sub_buffer(
        subbuffer: INPUT_COMPATIBLE_T,
        buffer: INPUT_COMPATIBLE_T,
        index: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::write sub-buffer (SUBBUFFER) to (BUFFER) at (INDEX)",
            inputs={
                "SUBBUFFER": InputValue.try_as_input(
                    subbuffer, p.SRBlockOnlyInputValue
                ),
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_buffer(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::(VALUE) is array buffer?",
            inputs={"VALUE": InputValue.try_as_input(value, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_size(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::byte length of buffer (BUFFER)",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def to_array(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::convert (BUFFER) to array",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def buffer_to_string(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::array buffer (BUFFER) to string",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def to_base64(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::array buffer (BUFFER) to base64",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def to_data_url(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::array buffer (BUFFER) to data:url",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def read_null_terminated_string(
        buffer: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::read string at (INDEX) of (BUFFER)",
            inputs={
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def write_null_terminated_string(
        buffer: INPUT_COMPATIBLE_T,
        index: INPUT_COMPATIBLE_T,
        string: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::write string (STRING) at (INDEX) of (BUFFER)",
            inputs={
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def items_of(
        buffer: INPUT_COMPATIBLE_T, min: INPUT_COMPATIBLE_T, max: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::get bytes (MIN) to (MAX) from (BUFFER) as new buffer",
            inputs={
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "MIN": InputValue.try_as_input(min, p.SRBlockAndTextInputValue),
                "MAX": InputValue.try_as_input(max, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def resize(buffer: INPUT_COMPATIBLE_T, size: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::resize (BUFFER) to (SIZE) bytes",
            inputs={
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "SIZE": InputValue.try_as_input(size, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def copy(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::copy (BUFFER)",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def reverse(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::reverse (BUFFER)",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def reverse_r(buffer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::reverse (BUFFER) as new",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def stringify(buffer: INPUT_COMPATIBLE_T, mode: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::stringify (BUFFER) [MODE]",
            inputs={"BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue)},
            dropdowns={"MODE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, mode)},
        )

    @staticmethod
    def for_each_v() -> p.SRBlock:
        return p.SRBlock(opcode="&agBuffer::byte", inputs={}, dropdowns={})

    @staticmethod
    def for_each_i() -> p.SRBlock:
        return p.SRBlock(opcode="&agBuffer::index", inputs={}, dropdowns={})

    @staticmethod
    def for_each(buffer: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::for each [INDEX], {:BYTE:} of (BUFFER) {SUBSTACK}",
            inputs={
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "INDEX": InputValue.try_as_input(
                    InputValue(agBuffer.for_each_i()), p.SREmbeddedBlockInputValue
                ),
                "BYTE": InputValue.try_as_input(
                    InputValue(agBuffer.for_each_v()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def size_of_type(type: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::size of ([TYPE])",
            inputs={
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def cast(value: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::cast (VALUE) to ([TYPE])",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_pointer(
        index: INPUT_COMPATIBLE_T,
        endian: INPUT_COMPATIBLE_T,
        buffer: INPUT_COMPATIBLE_T,
        type: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::create ([TYPE]) pointer for (BUFFER) at (INDEX) <ENDIAN>",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
                "ENDIAN": InputValue.try_as_input(endian, p.SRBlockAndBoolInputValue),
                "BUFFER": InputValue.try_as_input(buffer, p.SRBlockOnlyInputValue),
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_pointer(ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::set value of pointer (PTR) to (VALUE)",
            inputs={
                "PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_pointer_index(
        ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::set address of pointer (PTR) to (VALUE)",
            inputs={
                "PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_pointer_endian(
        ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::set endian of pointer (PTR) to <VALUE>",
            inputs={
                "PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_pointer_type(
        ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::set type of pointer (PTR) to ([VALUE])",
            inputs={
                "PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_pointer_buffer(
        ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::set buffer of pointer (PTR) to (VALUE)",
            inputs={
                "PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_pointer(ptr: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::get value of pointer (PTR)",
            inputs={"PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_pointer_index(ptr: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::get address of pointer (PTR)",
            inputs={"PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_pointer_type(ptr: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::get type of pointer (PTR)",
            inputs={"PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_pointer_endian(ptr: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::is pointer (PTR) little-endian?",
            inputs={"PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_pointer_buffer(ptr: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::get array buffer of pointer (PTR)",
            inputs={"PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def is_pointer(ptr: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::is pointer [VALUE]?",
            inputs={"PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def copy_pointer(
        ptr: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T, endian: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::copy pointer (PTR)",
            inputs={
                "PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue),
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
                "ENDIAN": InputValue.try_as_input(endian, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def pointer_as_type(
        ptr: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T, endian: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::(PTR) as ([TYPE]) pointer <ENDIAN>",
            inputs={
                "PTR": InputValue.try_as_input(ptr, p.SRBlockOnlyInputValue),
                "TYPE": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
                "ENDIAN": InputValue.try_as_input(endian, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def max_reporter_lines(lines: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::(only visual) set max lines shown in reporter output to (LINES)",
            inputs={
                "LINES": InputValue.try_as_input(lines, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def error_handling(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::set disable error prevention to <VALUE>",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndBoolInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def menu_datatypes() -> p.SRBlock:
        return p.SRBlock(opcode="&agBuffer::#menu:DATATYPES", inputs={}, dropdowns={})

    @staticmethod
    def menu_pointer_types() -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::#menu:POINTER_TYPES", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_stringifymode() -> p.SRBlock:
        return p.SRBlock(
            opcode="&agBuffer::#menu:STRINGIFYMODE", inputs={}, dropdowns={}
        )
