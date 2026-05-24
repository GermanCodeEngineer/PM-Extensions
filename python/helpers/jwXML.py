from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwXML:

    @grepr_dataclass()
    class new_node(ThirdBlock):
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::new node (NAME)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class parse(ThirdBlock):
        input: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::parse (INPUT) as node",
                inputs={
                    "INPUT": ThirdInputValue.as_input(
                        self.input, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class parse_multiple(ThirdBlock):
        input: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::parse (INPUT) as nodes",
                inputs={
                    "INPUT": ThirdInputValue.as_input(
                        self.input, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_name(ThirdBlock):
        node: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::name of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_name(ThirdBlock):
        node: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::set name of (NODE) to (NAME)",
                inputs={
                    "NODE": ThirdInputValue.as_input(
                        self.node, p.SRBlockOnlyInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class append_child(ThirdBlock):
        child: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::append (CHILD) to (NODE)",
                inputs={
                    "CHILD": ThirdInputValue.as_input(
                        self.child, p.SRBlockAndTextInputValue
                    ),
                    "NODE": ThirdInputValue.as_input(
                        self.node, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class remove_children(ThirdBlock):
        node: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::remove children of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_children(ThirdBlock):
        node: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::children of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_children(ThirdBlock):
        node: INPUT_COMPATIBLE_T
        children: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::set children of (NODE) to (CHILDREN)",
                inputs={
                    "NODE": ThirdInputValue.as_input(
                        self.node, p.SRBlockOnlyInputValue
                    ),
                    "CHILDREN": ThirdInputValue.as_input(
                        self.children, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_attribute(ThirdBlock):
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::attribute (ATTRIBUTE) of (NODE)",
                inputs={
                    "ATTRIBUTE": ThirdInputValue.as_input(
                        self.attribute, p.SRBlockAndTextInputValue
                    ),
                    "NODE": ThirdInputValue.as_input(
                        self.node, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_attribute(ThirdBlock):
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::set attribute (ATTRIBUTE) of (NODE) to (VALUE)",
                inputs={
                    "ATTRIBUTE": ThirdInputValue.as_input(
                        self.attribute, p.SRBlockAndTextInputValue
                    ),
                    "NODE": ThirdInputValue.as_input(
                        self.node, p.SRBlockOnlyInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class remove_attribute(ThirdBlock):
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::remove attribute (ATTRIBUTE) of (NODE)",
                inputs={
                    "ATTRIBUTE": ThirdInputValue.as_input(
                        self.attribute, p.SRBlockAndTextInputValue
                    ),
                    "NODE": ThirdInputValue.as_input(
                        self.node, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class remove_attributes(ThirdBlock):
        node: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::remove all attributes of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class has_attribute(ThirdBlock):
        node: INPUT_COMPATIBLE_T
        attribute: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::(NODE) has attribute (ATTRIBUTE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(
                        self.node, p.SRBlockOnlyInputValue
                    ),
                    "ATTRIBUTE": ThirdInputValue.as_input(
                        self.attribute, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_attributes(ThirdBlock):
        node: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::attributes of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class to_string(ThirdBlock):
        node: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::stringify (NODE) (FORMAT)",
                inputs={
                    "NODE": ThirdInputValue.as_input(
                        self.node, p.SRBlockOnlyInputValue
                    ),
                    "FORMAT": ThirdInputValue.as_input(
                        self.format, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class valid_name(ThirdBlock):
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::is (NAME) valid name",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class to_string_safe(ThirdBlock):
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::make (TEXT) XML safe",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class filter_array(ThirdBlock):
        name: INPUT_COMPATIBLE_T
        input: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::elements named (NAME) in (INPUT)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "INPUT": ThirdInputValue.as_input(
                        self.input, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::#menu:stringifyFormat", inputs={}, dropdowns={}
            )
