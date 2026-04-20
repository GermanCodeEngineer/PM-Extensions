from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class fruitsPaintUtils:

    @staticmethod
    def mix_colours(
        colour_name1: INPUT_COMPATIBLE_T,
        colour_name2: INPUT_COMPATIBLE_T,
        mix_options: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&fruitsPaintUtils::mix colours (COLOUR_NAME1) and (COLOUR_NAME2) and return the [MIX_OPTIONS]",
            inputs={
                "COLOUR_NAME1": InputValue.try_as_input(
                    colour_name1, p.SRBlockAndTextInputValue
                ),
                "COLOUR_NAME2": InputValue.try_as_input(
                    colour_name2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={
                "MIX_OPTIONS": p.SRDropdownValue(
                    p.DropdownValueKind.STANDARD, mix_options
                )
            },
        )

    @staticmethod
    def get_colour(colour_name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&fruitsPaintUtils::get colour from colour name (COLOUR_NAME)",
            inputs={
                "COLOUR_NAME": InputValue.try_as_input(
                    colour_name, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def menu_mix_options() -> p.SRBlock:
        return p.SRBlock(
            opcode="&fruitsPaintUtils::#menu:MIX_OPTIONS", inputs={}, dropdowns={}
        )
