from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class data:

    @grepr_dataclass()
    class setvariableto(ThirdBlock):
        OPCODE = "&variables::set [VARIABLE] to (VALUE)"
        value: INPUT_COMPATIBLE_T
        variable: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("VARIABLE", "variable"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("VARIABLE", "variable"),),
            )

    @grepr_dataclass()
    class changevariableby(ThirdBlock):
        OPCODE = "&variables::change [VARIABLE] by (VALUE)"
        value: INPUT_COMPATIBLE_T
        variable: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("VARIABLE", "variable"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("VARIABLE", "variable"),),
            )

    @grepr_dataclass()
    class showvariable(ThirdBlock):
        OPCODE = "&variables::show variable [VARIABLE]"
        variable: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("VARIABLE", "variable"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("VARIABLE", "variable"),))

    @grepr_dataclass()
    class hidevariable(ThirdBlock):
        OPCODE = "&variables::hide variable [VARIABLE]"
        variable: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("VARIABLE", "variable"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("VARIABLE", "variable"),))

    @grepr_dataclass()
    class variable(ThirdBlock):
        OPCODE = "&variables::value of [VARIABLE]"
        variable: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("VARIABLE", "variable"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("VARIABLE", "variable"),))

    @grepr_dataclass()
    class addtolist(ThirdBlock):
        OPCODE = "&lists::add (ITEM) to [LIST]"
        item: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITEM", "item", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("ITEM", "item", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class deleteoflist(ThirdBlock):
        OPCODE = "&lists::delete (INDEX) of [LIST]"
        index: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INDEX", "index", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INDEX", "index", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class deletealloflist(ThirdBlock):
        OPCODE = "&lists::delete all of [LIST]"
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LIST", "list"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LIST", "list"),))

    @grepr_dataclass()
    class shiftlist(ThirdBlock):
        OPCODE = "&lists::shift [LIST] by (INDEX)"
        index: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INDEX", "index", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INDEX", "index", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class insertatlist(ThirdBlock):
        OPCODE = "&lists::insert (ITEM) at (INDEX) of [LIST]"
        item: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITEM", "item", p.SRBlockAndTextInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITEM", "item", p.SRBlockAndTextInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class replaceitemoflist(ThirdBlock):
        OPCODE = "&lists::replace item (INDEX) of [LIST] with (ITEM)"
        index: INPUT_COMPATIBLE_T
        item: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ITEM", "item", p.SRBlockAndTextInputValue, None),
                ),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                    ("ITEM", "item", p.SRBlockAndTextInputValue, None),
                ),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class listforeachitem(ThirdBlock):
        OPCODE = "&lists::For each item [VARIABLE] in [LIST] {BODY}"
        body: INPUT_COMPATIBLE_T
        variable: str
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BODY", "body", p.SRScriptInputValue, None),),
                (("VARIABLE", "variable"), ("LIST", "list")),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BODY", "body", p.SRScriptInputValue, None),),
                (("VARIABLE", "variable"), ("LIST", "list")),
            )

    @grepr_dataclass()
    class listforeachnum(ThirdBlock):
        OPCODE = "&lists::For each item # [VARIABLE] in [LIST] {BODY}}"
        body: INPUT_COMPATIBLE_T
        variable: str
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BODY", "body", p.SRScriptInputValue, None),),
                (("VARIABLE", "variable"), ("LIST", "list")),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BODY", "body", p.SRScriptInputValue, None),),
                (("VARIABLE", "variable"), ("LIST", "list")),
            )

    @grepr_dataclass()
    class itemoflist(ThirdBlock):
        OPCODE = "&lists::item (INDEX) of [LIST]"
        index: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INDEX", "index", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INDEX", "index", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class itemnumoflist(ThirdBlock):
        OPCODE = "&lists::item # of (ITEM) in [LIST]"
        item: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITEM", "item", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("ITEM", "item", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class amountinlist(ThirdBlock):
        OPCODE = "&lists::amount of (VALUE) of [LIST]"
        value: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class lengthoflist(ThirdBlock):
        OPCODE = "&lists::length of [LIST]"
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LIST", "list"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LIST", "list"),))

    @grepr_dataclass()
    class listcontainsitem(ThirdBlock):
        OPCODE = "&lists::[LIST] contains (ITEM) ?"
        item: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITEM", "item", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("ITEM", "item", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class itemexistslist(ThirdBlock):
        OPCODE = "&lists::item (INDEX) exists in [LIST] ?"
        index: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INDEX", "index", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INDEX", "index", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class listisempty(ThirdBlock):
        OPCODE = "&lists::is [LIST] empty?"
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LIST", "list"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LIST", "list"),))

    @grepr_dataclass()
    class reverselist(ThirdBlock):
        OPCODE = "&lists::reverse [LIST]"
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LIST", "list"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LIST", "list"),))

    @grepr_dataclass()
    class filterlist(ThirdBlock):
        OPCODE = "&lists::filter [LIST] by (INDEX) (ITEM) <KEEP>"
        keep: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "INDEX",
                        "index",
                        p.SREmbeddedBlockInputValue,
                        data.filterlistindex,
                    ),
                    ("ITEM", "item", p.SREmbeddedBlockInputValue, data.filterlistitem),
                    ("KEEP", "keep", p.SRBlockAndBoolInputValue, None),
                ),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "INDEX",
                        "index",
                        p.SREmbeddedBlockInputValue,
                        data.filterlistindex,
                    ),
                    ("ITEM", "item", p.SREmbeddedBlockInputValue, data.filterlistitem),
                    ("KEEP", "keep", p.SRBlockAndBoolInputValue, None),
                ),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class arraylist(ThirdBlock):
        OPCODE = "&lists::set [LIST] to array (VALUE)"
        value: INPUT_COMPATIBLE_T
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("LIST", "list"),),
            )

    @grepr_dataclass()
    class listarray(ThirdBlock):
        OPCODE = "&lists::get list [LIST] as an array"
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LIST", "list"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LIST", "list"),))

    @grepr_dataclass()
    class showlist(ThirdBlock):
        OPCODE = "&lists::show list [LIST]"
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LIST", "list"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LIST", "list"),))

    @grepr_dataclass()
    class hidelist(ThirdBlock):
        OPCODE = "&lists::hide list [LIST]"
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LIST", "list"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LIST", "list"),))

    @grepr_dataclass()
    class listcontents(ThirdBlock):
        OPCODE = "&variables::value of [LIST]"
        list: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LIST", "list"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LIST", "list"),))

    @grepr_dataclass()
    class filterlistindex(ThirdBlock):
        OPCODE = "&lists::{{FILTER INDEX}}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class filterlistitem(ThirdBlock):
        OPCODE = "&lists::{{FILTER ITEM}}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
