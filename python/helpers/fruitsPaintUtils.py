from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class fruitsPaintUtils:

    @grepr_dataclass()
    class mix_colours(ThirdBlock):
        colour_name1: INPUT_COMPATIBLE_T
        colour_name2: INPUT_COMPATIBLE_T
        mix_options: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&fruitsPaintUtils::mix colours (COLOUR_NAME1) and (COLOUR_NAME2) and return the [MIX_OPTIONS]",
                inputs={
                    "COLOUR_NAME1": ThirdInputValue.as_input(
                        self.colour_name1, p.SRBlockAndTextInputValue
                    ),
                    "COLOUR_NAME2": ThirdInputValue.as_input(
                        self.colour_name2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "MIX_OPTIONS": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.mix_options
                    )
                },
            )

    @grepr_dataclass()
    class get_colour(ThirdBlock):
        colour_name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&fruitsPaintUtils::get colour from colour name (COLOUR_NAME)",
                inputs={
                    "COLOUR_NAME": ThirdInputValue.as_input(
                        self.colour_name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_mix_options(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&fruitsPaintUtils::#menu:MIX_OPTIONS", inputs={}, dropdowns={}
            )
