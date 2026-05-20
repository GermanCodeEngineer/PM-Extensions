from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class agBuffer:

    class new_buffer(ThirdBlock):

        def __init__(self, length: INPUT_COMPATIBLE_T):
            self.length = length

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::create new array buffer of size (LENGTH)",
                inputs={
                    "LENGTH": ThirdInputValue.as_input(
                        self.length, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class buffer_of(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::parse (VALUE) as array buffer",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class from_url(ThirdBlock):

        def __init__(self, url: INPUT_COMPATIBLE_T):
            self.url = url

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::get array buffer from url (URL)",
                inputs={
                    "URL": ThirdInputValue.as_input(
                        self.url, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class from_base64(ThirdBlock):

        def __init__(self, base64: INPUT_COMPATIBLE_T):
            self.base64 = base64

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::array buffer from base64 (BASE64)",
                inputs={
                    "BASE64": ThirdInputValue.as_input(
                        self.base64, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class from_string(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T):
            self.string = string

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::array buffer from string (STRING)",
                inputs={
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class builder_current(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::current buffer", inputs={}, dropdowns={}
            )

    class builder(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::array buffer builder {:CURRENT:} {SUBSTACK}",
                inputs={
                    "CURRENT": ThirdInputValue.as_input(
                        ThirdInputValue(agBuffer.builder_current()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class builder_append(ThirdBlock):

        def __init__(
            self,
            type: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
            endian: INPUT_COMPATIBLE_T,
        ):
            self.type = type
            self.value = value
            self.endian = endian

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::append ([TYPE]) value (VALUE) <ENDIAN> to builder",
                inputs={
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "ENDIAN": ThirdInputValue.as_input(
                        self.endian, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    class builder_append_buffer(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::append buffer (VALUE) to builder",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class builder_set(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::set builder to (BUFFER)",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class get_value(ThirdBlock):

        def __init__(
            self,
            type: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
            buffer: INPUT_COMPATIBLE_T,
            index: INPUT_COMPATIBLE_T,
            endian: INPUT_COMPATIBLE_T,
        ):
            self.type = type
            self.value = value
            self.buffer = buffer
            self.index = index
            self.endian = endian

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::read ([TYPE]) value of (BUFFER) at (INDEX) <ENDIAN>",
                inputs={
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                    "ENDIAN": ThirdInputValue.as_input(
                        self.endian, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    class set_value(ThirdBlock):

        def __init__(
            self,
            type: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
            buffer: INPUT_COMPATIBLE_T,
            index: INPUT_COMPATIBLE_T,
            endian: INPUT_COMPATIBLE_T,
        ):
            self.type = type
            self.value = value
            self.buffer = buffer
            self.index = index
            self.endian = endian

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::write ([TYPE]) value (VALUE) to (BUFFER) at (INDEX) <ENDIAN>",
                inputs={
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                    "ENDIAN": ThirdInputValue.as_input(
                        self.endian, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    class write_sub_buffer(ThirdBlock):

        def __init__(
            self,
            subbuffer: INPUT_COMPATIBLE_T,
            buffer: INPUT_COMPATIBLE_T,
            index: INPUT_COMPATIBLE_T,
        ):
            self.subbuffer = subbuffer
            self.buffer = buffer
            self.index = index

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::write sub-buffer (SUBBUFFER) to (BUFFER) at (INDEX)",
                inputs={
                    "SUBBUFFER": ThirdInputValue.as_input(
                        self.subbuffer, p.SRBlockOnlyInputValue
                    ),
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class is_buffer(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::(VALUE) is array buffer?",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class get_size(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::byte length of buffer (BUFFER)",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class to_array(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::convert (BUFFER) to array",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class to_typed_array(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T):
            self.buffer = buffer
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::convert (BUFFER) to ([TYPE]) typed array",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class buffer_to_string(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::array buffer (BUFFER) to string",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class to_base64(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::array buffer (BUFFER) to base64",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class to_data_url(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::array buffer (BUFFER) to data:url",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class read_null_terminated_string(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T):
            self.buffer = buffer
            self.index = index

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::read string at (INDEX) of (BUFFER)",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class write_null_terminated_string(ThirdBlock):

        def __init__(
            self,
            buffer: INPUT_COMPATIBLE_T,
            index: INPUT_COMPATIBLE_T,
            string: INPUT_COMPATIBLE_T,
        ):
            self.buffer = buffer
            self.index = index
            self.string = string

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::write string (STRING) at (INDEX) of (BUFFER)",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class items_of(ThirdBlock):

        def __init__(
            self,
            buffer: INPUT_COMPATIBLE_T,
            min: INPUT_COMPATIBLE_T,
            max: INPUT_COMPATIBLE_T,
        ):
            self.buffer = buffer
            self.min = min
            self.max = max

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::get bytes (MIN) to (MAX) from (BUFFER) as new buffer",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "MIN": ThirdInputValue.as_input(
                        self.min, p.SRBlockAndTextInputValue
                    ),
                    "MAX": ThirdInputValue.as_input(
                        self.max, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class resize(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T, size: INPUT_COMPATIBLE_T):
            self.buffer = buffer
            self.size = size

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::resize (BUFFER) to (SIZE) bytes as new",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "SIZE": ThirdInputValue.as_input(
                        self.size, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class resize_inst(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T, size: INPUT_COMPATIBLE_T):
            self.buffer = buffer
            self.size = size

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::resize (BUFFER) to (SIZE) bytes",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "SIZE": ThirdInputValue.as_input(
                        self.size, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class copy(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::copy (BUFFER)",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class reverse(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::reverse (BUFFER)",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class reverse_r(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T):
            self.buffer = buffer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::reverse (BUFFER) as new",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class stringify(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T, mode: str):
            self.buffer = buffer
            self.mode = mode

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::stringify (BUFFER) [MODE]",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={
                    "MODE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.mode)
                },
            )

    class for_each_v(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&agBuffer::byte", inputs={}, dropdowns={})

    class for_each_i(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&agBuffer::index", inputs={}, dropdowns={})

    class for_each(ThirdBlock):

        def __init__(self, buffer: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.buffer = buffer
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::for each [INDEX], {:BYTE:} of (BUFFER) {SUBSTACK}",
                inputs={
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        ThirdInputValue(agBuffer.for_each_i()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "BYTE": ThirdInputValue.as_input(
                        ThirdInputValue(agBuffer.for_each_v()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class size_of_type(ThirdBlock):

        def __init__(self, type: INPUT_COMPATIBLE_T):
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::size of ([TYPE])",
                inputs={
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    class cast(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T):
            self.value = value
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::cast (VALUE) to ([TYPE])",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class create_pointer(ThirdBlock):

        def __init__(
            self,
            index: INPUT_COMPATIBLE_T,
            endian: INPUT_COMPATIBLE_T,
            buffer: INPUT_COMPATIBLE_T,
            type: INPUT_COMPATIBLE_T,
        ):
            self.index = index
            self.endian = endian
            self.buffer = buffer
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::create ([TYPE]) pointer for (BUFFER) at (INDEX) <ENDIAN>",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                    "ENDIAN": ThirdInputValue.as_input(
                        self.endian, p.SRBlockAndBoolInputValue
                    ),
                    "BUFFER": ThirdInputValue.as_input(
                        self.buffer, p.SRBlockOnlyInputValue
                    ),
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class set_pointer(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.ptr = ptr
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::set value of pointer (PTR) to (VALUE)",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class set_pointer_index(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.ptr = ptr
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::set address of pointer (PTR) to (VALUE)",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class set_pointer_endian(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.ptr = ptr
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::set endian of pointer (PTR) to <VALUE>",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    class set_pointer_type(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.ptr = ptr
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::set type of pointer (PTR) to ([VALUE])",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class set_pointer_buffer(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.ptr = ptr
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::set buffer of pointer (PTR) to (VALUE)",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class get_pointer(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T):
            self.ptr = ptr

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::get value of pointer (PTR)",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class get_pointer_index(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T):
            self.ptr = ptr

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::get address of pointer (PTR)",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class get_pointer_type(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T):
            self.ptr = ptr

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::get type of pointer (PTR)",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class get_pointer_endian(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T):
            self.ptr = ptr

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::is pointer (PTR) little-endian?",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class get_pointer_buffer(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T):
            self.ptr = ptr

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::get array buffer of pointer (PTR)",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class is_pointer(ThirdBlock):

        def __init__(self, ptr: INPUT_COMPATIBLE_T):
            self.ptr = ptr

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::is pointer [PTR]?",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class copy_pointer(ThirdBlock):

        def __init__(
            self,
            ptr: INPUT_COMPATIBLE_T,
            type: INPUT_COMPATIBLE_T,
            endian: INPUT_COMPATIBLE_T,
        ):
            self.ptr = ptr
            self.type = type
            self.endian = endian

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::copy pointer (PTR)",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue),
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                    "ENDIAN": ThirdInputValue.as_input(
                        self.endian, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    class pointer_as_type(ThirdBlock):

        def __init__(
            self,
            ptr: INPUT_COMPATIBLE_T,
            type: INPUT_COMPATIBLE_T,
            endian: INPUT_COMPATIBLE_T,
        ):
            self.ptr = ptr
            self.type = type
            self.endian = endian

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::(PTR) as ([TYPE]) pointer <ENDIAN>",
                inputs={
                    "PTR": ThirdInputValue.as_input(self.ptr, p.SRBlockOnlyInputValue),
                    "TYPE": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                    "ENDIAN": ThirdInputValue.as_input(
                        self.endian, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    class max_reporter_lines(ThirdBlock):

        def __init__(self, lines: INPUT_COMPATIBLE_T):
            self.lines = lines

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::(only visual) set max lines shown in reporter output to (LINES)",
                inputs={
                    "LINES": ThirdInputValue.as_input(
                        self.lines, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class error_handling(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::set disable error prevention to <VALUE>",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndBoolInputValue
                    )
                },
                dropdowns={},
            )

    class menu_datatypes(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::#menu:DATATYPES", inputs={}, dropdowns={}
            )

    class menu_pointer_types(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::#menu:POINTER_TYPES", inputs={}, dropdowns={}
            )

    class menu_stringifymode(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&agBuffer::#menu:STRINGIFYMODE", inputs={}, dropdowns={}
            )
