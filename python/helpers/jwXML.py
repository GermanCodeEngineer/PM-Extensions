from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class jwXML:

    @grepr_dataclass()
    class new_node(ThirdBlock):
        OPCODE = "&jwXML::new node (NAME)"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NAME", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NAME", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE = "&jwXML::parse (INPUT) as node"
        input: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INPUT", "input", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("INPUT", "input", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class parse_multiple(ThirdBlock):
        OPCODE = "&jwXML::parse (INPUT) as nodes"
        input: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INPUT", "input", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("INPUT", "input", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_name(ThirdBlock):
        OPCODE = "&jwXML::name of (NODE)"
        node: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NODE", "node", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NODE", "node", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class set_name(ThirdBlock):
        OPCODE = "&jwXML::set name of (NODE) to (NAME)"
        node: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class append_child(ThirdBlock):
        OPCODE = "&jwXML::append (CHILD) to (NODE)"
        child: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CHILD", "child", p.SRBlockAndTextInputValue, None),
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CHILD", "child", p.SRBlockAndTextInputValue, None),
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class remove_children(ThirdBlock):
        OPCODE = "&jwXML::remove children of (NODE)"
        node: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NODE", "node", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NODE", "node", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_children(ThirdBlock):
        OPCODE = "&jwXML::children of (NODE)"
        node: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NODE", "node", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NODE", "node", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class set_children(ThirdBlock):
        OPCODE = "&jwXML::set children of (NODE) to (CHILDREN)"
        node: INPUT_COMPATIBLE_T
        children: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("CHILDREN", "children", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("CHILDREN", "children", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_attribute(ThirdBlock):
        OPCODE = "&jwXML::attribute (ATTRIBUTE) of (NODE)"
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_attribute(ThirdBlock):
        OPCODE = "&jwXML::set attribute (ATTRIBUTE) of (NODE) to (VALUE)"
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class remove_attribute(ThirdBlock):
        OPCODE = "&jwXML::remove attribute (ATTRIBUTE) of (NODE)"
        attribute: INPUT_COMPATIBLE_T
        node: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class remove_attributes(ThirdBlock):
        OPCODE = "&jwXML::remove all attributes of (NODE)"
        node: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NODE", "node", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NODE", "node", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class has_attribute(ThirdBlock):
        OPCODE = "&jwXML::(NODE) has attribute (ATTRIBUTE)"
        node: INPUT_COMPATIBLE_T
        attribute: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_attributes(ThirdBlock):
        OPCODE = "&jwXML::attributes of (NODE)"
        node: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NODE", "node", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NODE", "node", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class to_string(ThirdBlock):
        OPCODE = "&jwXML::stringify (NODE) (FORMAT)"
        node: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NODE", "node", p.SRBlockOnlyInputValue, None),
                    ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class valid_name(ThirdBlock):
        OPCODE = "&jwXML::is (NAME) valid name"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NAME", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NAME", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class to_string_safe(ThirdBlock):
        OPCODE = "&jwXML::make (TEXT) XML safe"
        text: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TEXT", "text", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TEXT", "text", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class filter_array(ThirdBlock):
        OPCODE = "&jwXML::elements named (NAME) in (INPUT)"
        name: INPUT_COMPATIBLE_T
        input: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("INPUT", "input", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("INPUT", "input", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_stringify_format(ThirdBlock):
        OPCODE = "&jwXML::#menu:stringifyFormat"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
