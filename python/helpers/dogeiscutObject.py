from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutObject:

    @grepr_dataclass()
    class blank(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::blank object", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class parse(ThirdBlock):
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class from_entries(ThirdBlock):
        array: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class current_object(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::current object", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class builder(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class builder_append(ThirdBlock):
        key: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class builder_append_empty(ThirdBlock):
        key: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class builder_set(ThirdBlock):
        object: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class get(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class get_path(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class has(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class size(ThirdBlock):
        object: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class set(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class set_path(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class delete(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        key: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class delete_at_path(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        array: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class merge(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::merge (ONE) into (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue),
                    "TWO": ThirdInputValue.as_input(self.two, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class to_string(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class keys(ThirdBlock):
        object: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class values(ThirdBlock):
        object: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class entries(ThirdBlock):
        object: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class is_(ThirdBlock):
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class for_each_k(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&dogeiscutObject::key", inputs={}, dropdowns={})

    @grepr_dataclass()
    class for_each_v(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&dogeiscutObject::value", inputs={}, dropdowns={})

    @grepr_dataclass()
    class for_each(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutObject::#menu:stringifyFormat",
                inputs={},
                dropdowns={},
            )
