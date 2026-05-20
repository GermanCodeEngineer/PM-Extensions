from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwXML:

    class new_node(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T):
            self.name = name

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

    class parse(ThirdBlock):

        def __init__(self, input: INPUT_COMPATIBLE_T):
            self.input = input

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

    class parse_multiple(ThirdBlock):

        def __init__(self, input: INPUT_COMPATIBLE_T):
            self.input = input

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

    class get_name(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T):
            self.node = node

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::name of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class set_name(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T):
            self.node = node
            self.name = name

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

    class append_child(ThirdBlock):

        def __init__(self, child: INPUT_COMPATIBLE_T, node: INPUT_COMPATIBLE_T):
            self.child = child
            self.node = node

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

    class remove_children(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T):
            self.node = node

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::remove children of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class get_children(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T):
            self.node = node

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::children of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class set_children(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T, children: INPUT_COMPATIBLE_T):
            self.node = node
            self.children = children

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

    class get_attribute(ThirdBlock):

        def __init__(self, attribute: INPUT_COMPATIBLE_T, node: INPUT_COMPATIBLE_T):
            self.attribute = attribute
            self.node = node

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

    class set_attribute(ThirdBlock):

        def __init__(
            self,
            attribute: INPUT_COMPATIBLE_T,
            node: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
        ):
            self.attribute = attribute
            self.node = node
            self.value = value

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

    class remove_attribute(ThirdBlock):

        def __init__(self, attribute: INPUT_COMPATIBLE_T, node: INPUT_COMPATIBLE_T):
            self.attribute = attribute
            self.node = node

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

    class remove_attributes(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T):
            self.node = node

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::remove all attributes of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class has_attribute(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T, attribute: INPUT_COMPATIBLE_T):
            self.node = node
            self.attribute = attribute

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

    class get_attributes(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T):
            self.node = node

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::attributes of (NODE)",
                inputs={
                    "NODE": ThirdInputValue.as_input(self.node, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class to_string(ThirdBlock):

        def __init__(self, node: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T):
            self.node = node
            self.format = format

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

    class valid_name(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T):
            self.name = name

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

    class to_string_safe(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T):
            self.text = text

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

    class filter_array(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, input: INPUT_COMPATIBLE_T):
            self.name = name
            self.input = input

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

    class menu_stringify_format(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwXML::#menu:stringifyFormat", inputs={}, dropdowns={}
            )
