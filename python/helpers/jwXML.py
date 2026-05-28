from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwXML:

    @grepr_dataclass()
    class new_node(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::new node (NAME)"
        INPUT_SPECS: ClassVar = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::parse (INPUT) as node"
        INPUT_SPECS: ClassVar = (("INPUT", "input", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class parse_multiple(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::parse (INPUT) as nodes"
        INPUT_SPECS: ClassVar = (("INPUT", "input", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_name(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::name of (NODE)"
        INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_name(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::set name of (NODE) to (NAME)"
        INPUT_SPECS: ClassVar = (
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class append_child(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::append (CHILD) to (NODE)"
        INPUT_SPECS: ClassVar = (
            ("CHILD", "child", p.SRBlockAndTextInputValue, None),
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        child: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class remove_children(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::remove children of (NODE)"
        INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_children(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::children of (NODE)"
        INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_children(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::set children of (NODE) to (CHILDREN)"
        INPUT_SPECS: ClassVar = (
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("CHILDREN", "children", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T
        children: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_attribute(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::attribute (ATTRIBUTE) of (NODE)"
        INPUT_SPECS: ClassVar = (
            ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_attribute(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::set attribute (ATTRIBUTE) of (NODE) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class remove_attribute(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::remove attribute (ATTRIBUTE) of (NODE)"
        INPUT_SPECS: ClassVar = (
            ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class remove_attributes(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::remove all attributes of (NODE)"
        INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class has_attribute(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::(NODE) has attribute (ATTRIBUTE)"
        INPUT_SPECS: ClassVar = (
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T
        attribute: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_attributes(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::attributes of (NODE)"
        INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::stringify (NODE) (FORMAT)"
        INPUT_SPECS: ClassVar = (
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        node: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class valid_name(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::is (NAME) valid name"
        INPUT_SPECS: ClassVar = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string_safe(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::make (TEXT) XML safe"
        INPUT_SPECS: ClassVar = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class filter_array(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::elements named (NAME) in (INPUT)"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("INPUT", "input", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE: ClassVar = "&jwXML::#menu:stringifyFormat"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
