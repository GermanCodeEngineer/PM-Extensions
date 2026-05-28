from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class fruitsPaintUtils:

    @grepr_dataclass()
    class mix_colours(ThirdBlock):
        OPCODE: ClassVar = (
            "&fruitsPaintUtils::mix colours (COLOUR_NAME1) and (COLOUR_NAME2) and return the [MIX_OPTIONS]"
        )
        INPUT_SPECS: ClassVar = (
            ("COLOUR_NAME1", "colour_name1", p.SRBlockAndTextInputValue, None),
            ("COLOUR_NAME2", "colour_name2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("MIX_OPTIONS", "mix_options"),)
        colour_name1: INPUT_COMPATIBLE_T
        colour_name2: INPUT_COMPATIBLE_T
        mix_options: str

    @grepr_dataclass()
    class get_colour(ThirdBlock):
        OPCODE: ClassVar = (
            "&fruitsPaintUtils::get colour from colour name (COLOUR_NAME)"
        )
        INPUT_SPECS: ClassVar = (
            ("COLOUR_NAME", "colour_name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        colour_name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_mix_options(ThirdBlock):
        OPCODE: ClassVar = "&fruitsPaintUtils::#menu:MIX_OPTIONS"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
