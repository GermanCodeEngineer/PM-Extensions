from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class dogeiscutObject:

    @staticmethod
    def blank() -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::blank object", inputs={}, dropdowns={}
        )

    @staticmethod
    def parse(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::parse (VALUE) as object",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def from_entries(array: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::from entries (ARRAY)",
            inputs={
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def current_object() -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::current object", inputs={}, dropdowns={}
        )

    @staticmethod
    def builder(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::object builder {:CURRENT_OBJECT:} {SUBSTACK}",
            inputs={
                "CURRENT_OBJECT": InputValue.try_as_input(
                    InputValue(dogeiscutObject.current_object()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def builder_append(key: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::append key (KEY) value (VALUE) to builder",
            inputs={
                "KEY": InputValue.try_as_input(key, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def builder_append_empty(key: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::append key (KEY) to builder",
            inputs={"KEY": InputValue.try_as_input(key, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def builder_set(object: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::set builder to (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def get(object: INPUT_COMPATIBLE_T, key: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::get (KEY) in (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue),
                "KEY": InputValue.try_as_input(key, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_path(object: INPUT_COMPATIBLE_T, array: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::get path (ARRAY) in (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue),
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def has(object: INPUT_COMPATIBLE_T, key: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::(OBJECT) has key (KEY)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue),
                "KEY": InputValue.try_as_input(key, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def size(object: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::size of (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def set(
        object: INPUT_COMPATIBLE_T, key: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::set (KEY) in (OBJECT) to (VALUE)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue),
                "KEY": InputValue.try_as_input(key, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_path(
        object: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T, array: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::set path (ARRAY) in (OBJECT) to (VALUE)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def delete(object: INPUT_COMPATIBLE_T, key: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::delete key (KEY) from (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue),
                "KEY": InputValue.try_as_input(key, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def delete_at_path(
        object: INPUT_COMPATIBLE_T, array: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::delete at path (ARRAY) from (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue),
                "ARRAY": InputValue.try_as_input(array, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def merge(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::merge (ONE) into (TWO)",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockAndTextInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def to_string(object: INPUT_COMPATIBLE_T, format: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::stringify (OBJECT) [FORMAT]",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "FORMAT": p.SRDropdownValue(p.DropdownValueKind.STANDARD, format)
            },
        )

    @staticmethod
    def keys(object: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::keys of (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def values(object: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::values of (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def entries(object: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::entries of (OBJECT)",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def is_(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::does (VALUE) parse as an object?",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def for_each_k() -> p.SRBlock:
        return p.SRBlock(opcode="&dogeiscutObject::key", inputs={}, dropdowns={})

    @staticmethod
    def for_each_v() -> p.SRBlock:
        return p.SRBlock(opcode="&dogeiscutObject::value", inputs={}, dropdowns={})

    @staticmethod
    def for_each(object: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::for {:K:} {:V:} of (OBJECT) {SUBSTACK}",
            inputs={
                "OBJECT": InputValue.try_as_input(object, p.SRBlockAndTextInputValue),
                "K": InputValue.try_as_input(
                    InputValue(dogeiscutObject.for_each_k()),
                    p.SREmbeddedBlockInputValue,
                ),
                "V": InputValue.try_as_input(
                    InputValue(dogeiscutObject.for_each_v()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_stringify_format() -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutObject::#menu:stringifyFormat", inputs={}, dropdowns={}
        )
