from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class jwXML:

    @grepr_dataclass()
    class new_node(ThirdBlock):
        OPCODE = "&jwXML::new node (NAME)"
        INPUT_SPECS = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE = "&jwXML::parse (INPUT) as node"
        INPUT_SPECS = (("INPUT", "input", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class parse_multiple(ThirdBlock):
        OPCODE = "&jwXML::parse (INPUT) as nodes"
        INPUT_SPECS = (("INPUT", "input", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_name(ThirdBlock):
        OPCODE = "&jwXML::name of (NODE)"
        INPUT_SPECS = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_name(ThirdBlock):
        OPCODE = "&jwXML::set name of (NODE) to (NAME)"
        INPUT_SPECS = (
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class append_child(ThirdBlock):
        OPCODE = "&jwXML::append (CHILD) to (NODE)"
        INPUT_SPECS = (
            ("CHILD", "child", p.SRBlockAndTextInputValue, None),
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        child: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class remove_children(ThirdBlock):
        OPCODE = "&jwXML::remove children of (NODE)"
        INPUT_SPECS = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_children(ThirdBlock):
        OPCODE = "&jwXML::children of (NODE)"
        INPUT_SPECS = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_children(ThirdBlock):
        OPCODE = "&jwXML::set children of (NODE) to (CHILDREN)"
        INPUT_SPECS = (
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("CHILDREN", "children", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T
        children: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_attribute(ThirdBlock):
        OPCODE = "&jwXML::attribute (ATTRIBUTE) of (NODE)"
        INPUT_SPECS = (
            ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_attribute(ThirdBlock):
        OPCODE = "&jwXML::set attribute (ATTRIBUTE) of (NODE) to (VALUE)"
        INPUT_SPECS = (
            ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class remove_attribute(ThirdBlock):
        OPCODE = "&jwXML::remove attribute (ATTRIBUTE) of (NODE)"
        INPUT_SPECS = (
            ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class remove_attributes(ThirdBlock):
        OPCODE = "&jwXML::remove all attributes of (NODE)"
        INPUT_SPECS = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class has_attribute(ThirdBlock):
        OPCODE = "&jwXML::(NODE) has attribute (ATTRIBUTE)"
        INPUT_SPECS = (
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T
        attribute: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_attributes(ThirdBlock):
        OPCODE = "&jwXML::attributes of (NODE)"
        INPUT_SPECS = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&jwXML::stringify (NODE) (FORMAT)"
        INPUT_SPECS = (
            ("NODE", "node", p.SRBlockOnlyInputValue, None),
            ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        node: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class valid_name(ThirdBlock):
        OPCODE = "&jwXML::is (NAME) valid name"
        INPUT_SPECS = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_string_safe(ThirdBlock):
        OPCODE = "&jwXML::make (TEXT) XML safe"
        INPUT_SPECS = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class filter_array(ThirdBlock):
        OPCODE = "&jwXML::elements named (NAME) in (INPUT)"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("INPUT", "input", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        input: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE = "&jwXML::#menu:stringifyFormat"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
