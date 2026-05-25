from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class agBuffer:

    @grepr_dataclass()
    class new_buffer(ThirdBlock):
        OPCODE = "&agBuffer::create new array buffer of size (LENGTH)"
        length: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LENGTH", "length", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("LENGTH", "length", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class buffer_of(ThirdBlock):
        OPCODE = "&agBuffer::parse (VALUE) as array buffer"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class from_url(ThirdBlock):
        OPCODE = "&agBuffer::get array buffer from url (URL)"
        url: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("URL", "url", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("URL", "url", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class from_base64(ThirdBlock):
        OPCODE = "&agBuffer::array buffer from base64 (BASE64)"
        base64: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BASE64", "base64", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BASE64", "base64", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class from_string(ThirdBlock):
        OPCODE = "&agBuffer::array buffer from string (STRING)"
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("STRING", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("STRING", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class builder_current(ThirdBlock):
        OPCODE = "&agBuffer::current buffer"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class builder(ThirdBlock):
        OPCODE = "&agBuffer::array buffer builder {:CURRENT:} {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "CURRENT",
                        "current",
                        p.SREmbeddedBlockInputValue,
                        agBuffer.builder_current,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "CURRENT",
                        "current",
                        p.SREmbeddedBlockInputValue,
                        agBuffer.builder_current,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        OPCODE = "&agBuffer::append ([TYPE]) value (VALUE) <ENDIAN> to builder"
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class builder_append_buffer(ThirdBlock):
        OPCODE = "&agBuffer::append buffer (VALUE) to builder"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        OPCODE = "&agBuffer::set builder to (BUFFER)"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_value(ThirdBlock):
        OPCODE = "&agBuffer::read ([TYPE]) value of (BUFFER) at (INDEX) <ENDIAN>"
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_value(ThirdBlock):
        OPCODE = (
            "&agBuffer::write ([TYPE]) value (VALUE) to (BUFFER) at (INDEX) <ENDIAN>"
        )
        type: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class write_sub_buffer(ThirdBlock):
        OPCODE = "&agBuffer::write sub-buffer (SUBBUFFER) to (BUFFER) at (INDEX)"
        subbuffer: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SUBBUFFER", "subbuffer", p.SRBlockOnlyInputValue, None),
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SUBBUFFER", "subbuffer", p.SRBlockOnlyInputValue, None),
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_buffer(ThirdBlock):
        OPCODE = "&agBuffer::(VALUE) is array buffer?"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_size(ThirdBlock):
        OPCODE = "&agBuffer::byte length of buffer (BUFFER)"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class to_array(ThirdBlock):
        OPCODE = "&agBuffer::convert (BUFFER) to array"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class to_typed_array(ThirdBlock):
        OPCODE = "&agBuffer::convert (BUFFER) to ([TYPE]) typed array"
        buffer: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class buffer_to_string(ThirdBlock):
        OPCODE = "&agBuffer::array buffer (BUFFER) to string"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class to_base64(ThirdBlock):
        OPCODE = "&agBuffer::array buffer (BUFFER) to base64"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class to_data_url(ThirdBlock):
        OPCODE = "&agBuffer::array buffer (BUFFER) to data:url"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class read_null_terminated_string(ThirdBlock):
        OPCODE = "&agBuffer::read string at (INDEX) of (BUFFER)"
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class write_null_terminated_string(ThirdBlock):
        OPCODE = "&agBuffer::write string (STRING) at (INDEX) of (BUFFER)"
        buffer: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class items_of(ThirdBlock):
        OPCODE = "&agBuffer::get bytes (MIN) to (MAX) from (BUFFER) as new buffer"
        buffer: INPUT_COMPATIBLE_T
        min: INPUT_COMPATIBLE_T
        max: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("MIN", "min", p.SRBlockAndTextInputValue, None),
                    ("MAX", "max", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("MIN", "min", p.SRBlockAndTextInputValue, None),
                    ("MAX", "max", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class resize(ThirdBlock):
        OPCODE = "&agBuffer::resize (BUFFER) to (SIZE) bytes as new"
        buffer: INPUT_COMPATIBLE_T
        size: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("SIZE", "size", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("SIZE", "size", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class resize_inst(ThirdBlock):
        OPCODE = "&agBuffer::resize (BUFFER) to (SIZE) bytes"
        buffer: INPUT_COMPATIBLE_T
        size: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("SIZE", "size", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("SIZE", "size", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class copy(ThirdBlock):
        OPCODE = "&agBuffer::copy (BUFFER)"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class reverse(ThirdBlock):
        OPCODE = "&agBuffer::reverse (BUFFER)"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class reverse_r(ThirdBlock):
        OPCODE = "&agBuffer::reverse (BUFFER) as new"
        buffer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class stringify(ThirdBlock):
        OPCODE = "&agBuffer::stringify (BUFFER) [MODE]"
        buffer: INPUT_COMPATIBLE_T
        mode: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (("MODE", "mode"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),),
                (("MODE", "mode"),),
            )

    @grepr_dataclass()
    class for_each_v(ThirdBlock):
        OPCODE = "&agBuffer::byte"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class for_each_i(ThirdBlock):
        OPCODE = "&agBuffer::index"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class for_each(ThirdBlock):
        OPCODE = "&agBuffer::for each [INDEX], {:BYTE:} of (BUFFER) {SUBSTACK}"
        buffer: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    (
                        "INDEX",
                        "index",
                        p.SREmbeddedBlockInputValue,
                        agBuffer.for_each_i,
                    ),
                    ("BYTE", "byte", p.SREmbeddedBlockInputValue, agBuffer.for_each_v),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    (
                        "INDEX",
                        "index",
                        p.SREmbeddedBlockInputValue,
                        agBuffer.for_each_i,
                    ),
                    ("BYTE", "byte", p.SREmbeddedBlockInputValue, agBuffer.for_each_v),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class size_of_type(ThirdBlock):
        OPCODE = "&agBuffer::size of ([TYPE])"
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TYPE", "type", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TYPE", "type", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class cast(ThirdBlock):
        OPCODE = "&agBuffer::cast (VALUE) to ([TYPE])"
        value: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class create_pointer(ThirdBlock):
        OPCODE = "&agBuffer::create ([TYPE]) pointer for (BUFFER) at (INDEX) <ENDIAN>"
        index: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T
        buffer: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                    ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_pointer(ThirdBlock):
        OPCODE = "&agBuffer::set value of pointer (PTR) to (VALUE)"
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_pointer_index(ThirdBlock):
        OPCODE = "&agBuffer::set address of pointer (PTR) to (VALUE)"
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_pointer_endian(ThirdBlock):
        OPCODE = "&agBuffer::set endian of pointer (PTR) to <VALUE>"
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_pointer_type(ThirdBlock):
        OPCODE = "&agBuffer::set type of pointer (PTR) to ([VALUE])"
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_pointer_buffer(ThirdBlock):
        OPCODE = "&agBuffer::set buffer of pointer (PTR) to (VALUE)"
        ptr: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_pointer(ThirdBlock):
        OPCODE = "&agBuffer::get value of pointer (PTR)"
        ptr: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_pointer_index(ThirdBlock):
        OPCODE = "&agBuffer::get address of pointer (PTR)"
        ptr: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_pointer_type(ThirdBlock):
        OPCODE = "&agBuffer::get type of pointer (PTR)"
        ptr: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_pointer_endian(ThirdBlock):
        OPCODE = "&agBuffer::is pointer (PTR) little-endian?"
        ptr: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_pointer_buffer(ThirdBlock):
        OPCODE = "&agBuffer::get array buffer of pointer (PTR)"
        ptr: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class is_pointer(ThirdBlock):
        OPCODE = "&agBuffer::is pointer [PTR]?"
        ptr: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("PTR", "ptr", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class copy_pointer(ThirdBlock):
        OPCODE = "&agBuffer::copy pointer (PTR)"
        ptr: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class pointer_as_type(ThirdBlock):
        OPCODE = "&agBuffer::(PTR) as ([TYPE]) pointer <ENDIAN>"
        ptr: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T
        endian: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                    ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                    ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class max_reporter_lines(ThirdBlock):
        OPCODE = (
            "&agBuffer::(only visual) set max lines shown in reporter output to (LINES)"
        )
        lines: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LINES", "lines", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("LINES", "lines", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class error_handling(ThirdBlock):
        OPCODE = "&agBuffer::set disable error prevention to <VALUE>"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndBoolInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndBoolInputValue, None),), ()
            )

    @grepr_dataclass()
    class menu_datatypes(ThirdBlock):
        OPCODE = "&agBuffer::#menu:DATATYPES"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_pointer_types(ThirdBlock):
        OPCODE = "&agBuffer::#menu:POINTER_TYPES"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_stringifymode(ThirdBlock):
        OPCODE = "&agBuffer::#menu:STRINGIFYMODE"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
