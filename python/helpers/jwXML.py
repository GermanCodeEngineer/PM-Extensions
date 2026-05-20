from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class jwXML:

    @staticmethod
    def new_node(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::new node (NAME)",
            inputs={"NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def parse(input: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::parse (INPUT) as node",
            inputs={
                "INPUT": ThirdInputValue.as_input(input, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def parse_multiple(input: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::parse (INPUT) as nodes",
            inputs={
                "INPUT": ThirdInputValue.as_input(input, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def get_name(node: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::name of (NODE)",
            inputs={"NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def set_name(node: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::set name of (NODE) to (NAME)",
            inputs={
                "NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def append_child(child: INPUT_COMPATIBLE_T, node: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::append (CHILD) to (NODE)",
            inputs={
                "CHILD": ThirdInputValue.as_input(child, p.SRBlockAndTextInputValue),
                "NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def remove_children(node: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::remove children of (NODE)",
            inputs={"NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_children(node: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::children of (NODE)",
            inputs={"NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def set_children(
        node: INPUT_COMPATIBLE_T, children: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::set children of (NODE) to (CHILDREN)",
            inputs={
                "NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue),
                "CHILDREN": ThirdInputValue.as_input(children, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_attribute(
        attribute: INPUT_COMPATIBLE_T, node: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::attribute (ATTRIBUTE) of (NODE)",
            inputs={
                "ATTRIBUTE": ThirdInputValue.as_input(
                    attribute, p.SRBlockAndTextInputValue
                ),
                "NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_attribute(
        attribute: INPUT_COMPATIBLE_T,
        node: INPUT_COMPATIBLE_T,
        value: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::set attribute (ATTRIBUTE) of (NODE) to (VALUE)",
            inputs={
                "ATTRIBUTE": ThirdInputValue.as_input(
                    attribute, p.SRBlockAndTextInputValue
                ),
                "NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def remove_attribute(
        attribute: INPUT_COMPATIBLE_T, node: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::remove attribute (ATTRIBUTE) of (NODE)",
            inputs={
                "ATTRIBUTE": ThirdInputValue.as_input(
                    attribute, p.SRBlockAndTextInputValue
                ),
                "NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def remove_attributes(node: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::remove all attributes of (NODE)",
            inputs={"NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def has_attribute(
        node: INPUT_COMPATIBLE_T, attribute: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::(NODE) has attribute (ATTRIBUTE)",
            inputs={
                "NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue),
                "ATTRIBUTE": ThirdInputValue.as_input(
                    attribute, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def get_attributes(node: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::attributes of (NODE)",
            inputs={"NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def to_string(node: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::stringify (NODE) (FORMAT)",
            inputs={
                "NODE": ThirdInputValue.as_input(node, p.SRBlockOnlyInputValue),
                "FORMAT": ThirdInputValue.as_input(format, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def valid_name(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::is (NAME) valid name",
            inputs={"NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def to_string_safe(text: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::make (TEXT) XML safe",
            inputs={"TEXT": ThirdInputValue.as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def filter_array(name: INPUT_COMPATIBLE_T, input: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::elements named (NAME) in (INPUT)",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "INPUT": ThirdInputValue.as_input(input, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_stringify_format() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwXML::#menu:stringifyFormat", inputs={}, dropdowns={}
        )
