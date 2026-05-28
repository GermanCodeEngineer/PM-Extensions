from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class dogeiscutRegularExpressions:

    @grepr_dataclass()
    class regex(ThirdBlock):
        OPCODE: ClassVar = (
            "&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)"
        )
        INPUT_SPECS: ClassVar = (
            ("PATTERN", "pattern", p.SRBlockAndTextInputValue, None),
            ("FLAGS", "flags", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        pattern: INPUT_COMPATIBLE_T
        flags: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class escape(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::escape (STRING) for regex"
        INPUT_SPECS: ClassVar = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class source_of(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::source of (REGEX)"
        INPUT_SPECS: ClassVar = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class flags_of(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::flags of (REGEX)"
        INPUT_SPECS: ClassVar = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class test(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::test (STRING) for (REGEX)"
        INPUT_SPECS: ClassVar = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class search(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::search (STRING) with (REGEX)"
        INPUT_SPECS: ClassVar = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class replace(ThirdBlock):
        OPCODE: ClassVar = (
            "&dogeiscutRegularExpressions::replace (REGEX) in (A) with (B)"
        )
        INPUT_SPECS: ClassVar = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class replace_all(ThirdBlock):
        OPCODE: ClassVar = (
            "&dogeiscutRegularExpressions::replace all (REGEX) in (A) with (B)"
        )
        INPUT_SPECS: ClassVar = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class split(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::split (STRING) by (REGEX)"
        INPUT_SPECS: ClassVar = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class match(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::match (REGEX) with (STRING)"
        INPUT_SPECS: ClassVar = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class match_all(ThirdBlock):
        OPCODE: ClassVar = (
            "&dogeiscutRegularExpressions::match all (REGEX) with (STRING)"
        )
        INPUT_SPECS: ClassVar = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class exec(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::execute (REGEX) on (STRING)"
        INPUT_SPECS: ClassVar = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_last_index(ThirdBlock):
        OPCODE: ClassVar = "&dogeiscutRegularExpressions::get last index of (REGEX)"
        INPUT_SPECS: ClassVar = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_last_index(ThirdBlock):
        OPCODE: ClassVar = (
            "&dogeiscutRegularExpressions::set last index of (REGEX) to (INDEX)"
        )
        INPUT_SPECS: ClassVar = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        regex: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
