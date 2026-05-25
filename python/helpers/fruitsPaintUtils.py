from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class fruitsPaintUtils:

    @grepr_dataclass()
    class mix_colours(ThirdBlock):
        OPCODE = "&fruitsPaintUtils::mix colours (COLOUR_NAME1) and (COLOUR_NAME2) and return the [MIX_OPTIONS]"
        colour_name1: INPUT_COMPATIBLE_T
        colour_name2: INPUT_COMPATIBLE_T
        mix_options: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("COLOUR_NAME1", "colour_name1", p.SRBlockAndTextInputValue, None),
                    ("COLOUR_NAME2", "colour_name2", p.SRBlockAndTextInputValue, None),
                ),
                (("MIX_OPTIONS", "mix_options"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("COLOUR_NAME1", "colour_name1", p.SRBlockAndTextInputValue, None),
                    ("COLOUR_NAME2", "colour_name2", p.SRBlockAndTextInputValue, None),
                ),
                (("MIX_OPTIONS", "mix_options"),),
            )

    @grepr_dataclass()
    class get_colour(ThirdBlock):
        OPCODE = "&fruitsPaintUtils::get colour from colour name (COLOUR_NAME)"
        colour_name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("COLOUR_NAME", "colour_name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("COLOUR_NAME", "colour_name", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class menu_mix_options(ThirdBlock):
        OPCODE = "&fruitsPaintUtils::#menu:MIX_OPTIONS"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
