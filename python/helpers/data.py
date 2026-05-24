from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class data:

    @grepr_dataclass()
    class setvariableto(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        variable: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::set [VARIABLE] to (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    @grepr_dataclass()
    class changevariableby(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        variable: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::change [VARIABLE] by (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    @grepr_dataclass()
    class showvariable(ThirdBlock):
        variable: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::show variable [VARIABLE]",
                inputs={},
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    @grepr_dataclass()
    class hidevariable(ThirdBlock):
        variable: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::hide variable [VARIABLE]",
                inputs={},
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    @grepr_dataclass()
    class variable(ThirdBlock):
        variable: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::value of [VARIABLE]",
                inputs={},
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    @grepr_dataclass()
    class addtolist(ThirdBlock):
        item: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::add (ITEM) to [LIST]",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class deleteoflist(ThirdBlock):
        index: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::delete (INDEX) of [LIST]",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class deletealloflist(ThirdBlock):
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::delete all of [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class shiftlist(ThirdBlock):
        index: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::shift [LIST] by (INDEX)",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class insertatlist(ThirdBlock):
        item: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::insert (ITEM) at (INDEX) of [LIST]",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class replaceitemoflist(ThirdBlock):
        index: INPUT_COMPATIBLE_T
        item: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::replace item (INDEX) of [LIST] with (ITEM)",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class listforeachitem(ThirdBlock):
        body: INPUT_COMPATIBLE_T
        variable: str
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::For each item [VARIABLE] in [LIST] {BODY}",
                inputs={
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue)
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    ),
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list),
                },
            )

    @grepr_dataclass()
    class listforeachnum(ThirdBlock):
        body: INPUT_COMPATIBLE_T
        variable: str
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::For each item # [VARIABLE] in [LIST] {BODY}}",
                inputs={
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue)
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    ),
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list),
                },
            )

    @grepr_dataclass()
    class itemoflist(ThirdBlock):
        index: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::item (INDEX) of [LIST]",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class itemnumoflist(ThirdBlock):
        item: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::item # of (ITEM) in [LIST]",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class amountinlist(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::amount of (VALUE) of [LIST]",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class lengthoflist(ThirdBlock):
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::length of [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class listcontainsitem(ThirdBlock):
        item: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::[LIST] contains (ITEM) ?",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class itemexistslist(ThirdBlock):
        index: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::item (INDEX) exists in [LIST] ?",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class listisempty(ThirdBlock):
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::is [LIST] empty?",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class reverselist(ThirdBlock):
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::reverse [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class filterlist(ThirdBlock):
        keep: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::filter [LIST] by (INDEX) (ITEM) <KEEP>",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        ThirdInputValue(data.filterlistindex()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "ITEM": ThirdInputValue.as_input(
                        ThirdInputValue(data.filterlistitem()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "KEEP": ThirdInputValue.as_input(
                        self.keep, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class arraylist(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::set [LIST] to array (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class listarray(ThirdBlock):
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::get list [LIST] as an array",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class showlist(ThirdBlock):
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::show list [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class hidelist(ThirdBlock):
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::hide list [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class listcontents(ThirdBlock):
        list: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::value of [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    @grepr_dataclass()
    class filterlistindex(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&lists::{{FILTER INDEX}}", inputs={}, dropdowns={})

    @grepr_dataclass()
    class filterlistitem(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&lists::{{FILTER ITEM}}", inputs={}, dropdowns={})
