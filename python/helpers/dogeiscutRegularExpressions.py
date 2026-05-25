from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutRegularExpressions:

    @grepr_dataclass()
    class regex(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)"
        INPUT_SPECS = (
            ("PATTERN", "pattern", p.SRBlockAndTextInputValue, None),
            ("FLAGS", "flags", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        pattern: INPUT_COMPATIBLE_T
        flags: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class escape(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::escape (STRING) for regex"
        INPUT_SPECS = (("STRING", "string", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class source_of(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::source of (REGEX)"
        INPUT_SPECS = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class flags_of(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::flags of (REGEX)"
        INPUT_SPECS = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class test(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::test (STRING) for (REGEX)"
        INPUT_SPECS = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class search(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::search (STRING) with (REGEX)"
        INPUT_SPECS = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class replace(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::replace (REGEX) in (A) with (B)"
        INPUT_SPECS = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class replace_all(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::replace all (REGEX) in (A) with (B)"
        INPUT_SPECS = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class split(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::split (STRING) by (REGEX)"
        INPUT_SPECS = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class match(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::match (REGEX) with (STRING)"
        INPUT_SPECS = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class match_all(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::match all (REGEX) with (STRING)"
        INPUT_SPECS = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class exec(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::execute (REGEX) on (STRING)"
        INPUT_SPECS = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_last_index(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::get last index of (REGEX)"
        INPUT_SPECS = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_last_index(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::set last index of (REGEX) to (INDEX)"
        INPUT_SPECS = (
            ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        regex: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
