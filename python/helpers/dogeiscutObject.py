from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutObject:

    class blank(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::blank object", inputs={}, dropdowns={}
            )

    class parse(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::parse (VALUE) as object",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class from_entries(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T):
            self.array = array

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::from entries (ARRAY)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class current_object(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::current object", inputs={}, dropdowns={}
            )

    class builder(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::object builder {:CURRENT_OBJECT:} {SUBSTACK}",
                inputs={
                    "CURRENT_OBJECT": ThirdInputValue.as_input(
                        ThirdInputValue(dogeiscutObject.current_object()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class builder_append(ThirdBlock):

        def __init__(self, key: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.key = key
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::append key (KEY) value (VALUE) to builder",
                inputs={
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class builder_append_empty(ThirdBlock):

        def __init__(self, key: INPUT_COMPATIBLE_T):
            self.key = key

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::append key (KEY) to builder",
                inputs={
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class builder_set(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T):
            self.object = object

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::set builder to (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class get(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, key: INPUT_COMPATIBLE_T):
            self.object = object
            self.key = key

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::get (KEY) in (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class get_path(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, array: INPUT_COMPATIBLE_T):
            self.object = object
            self.array = array

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::get path (ARRAY) in (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class has(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, key: INPUT_COMPATIBLE_T):
            self.object = object
            self.key = key

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::(OBJECT) has key (KEY)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class size(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T):
            self.object = object

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::size of (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class set(ThirdBlock):

        def __init__(
            self,
            object: INPUT_COMPATIBLE_T,
            key: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
        ):
            self.object = object
            self.key = key
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::set (KEY) in (OBJECT) to (VALUE)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class set_path(ThirdBlock):

        def __init__(
            self,
            object: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
            array: INPUT_COMPATIBLE_T,
        ):
            self.object = object
            self.value = value
            self.array = array

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::set path (ARRAY) in (OBJECT) to (VALUE)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class delete(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, key: INPUT_COMPATIBLE_T):
            self.object = object
            self.key = key

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::delete key (KEY) from (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class delete_at_path(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, array: INPUT_COMPATIBLE_T):
            self.object = object
            self.array = array

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::delete at path (ARRAY) from (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class merge(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::merge (ONE) into (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class to_string(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T):
            self.object = object
            self.format = format

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::stringify (OBJECT) (FORMAT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "FORMAT": ThirdInputValue.as_input(
                        self.format, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class keys(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T):
            self.object = object

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::keys of (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class values(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T):
            self.object = object

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::values of (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class entries(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T):
            self.object = object

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::entries of (OBJECT)",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class is_(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::does (VALUE) parse as an object?",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class for_each_k(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&dogeiscutObject::key", inputs={}, dropdowns={})

    class for_each_v(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&dogeiscutObject::value", inputs={}, dropdowns={})

    class for_each(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.object = object
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::for {:K:} {:V:} of (OBJECT) {SUBSTACK}",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockOnlyInputValue
                    ),
                    "K": ThirdInputValue.as_input(
                        ThirdInputValue(dogeiscutObject.for_each_k()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "V": ThirdInputValue.as_input(
                        ThirdInputValue(dogeiscutObject.for_each_v()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class menu_stringify_format(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::#menu:stringifyFormat",
                inputs={},
                dropdowns={},
            )
