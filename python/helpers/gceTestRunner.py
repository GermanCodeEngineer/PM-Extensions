from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class gceTestRunner:

    @grepr_dataclass()
    class test_scope(ThirdBlock):
        OPCODE = "&gceTestRunner::test scope named (NAME) {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_(ThirdBlock):
        OPCODE = "&gceTestRunner::assert <CONDITION>"
        INPUT_SPECS = (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),)
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_not(ThirdBlock):
        OPCODE = "&gceTestRunner::assert not <CONDITION>"
        INPUT_SPECS = (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),)
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_msg(ThirdBlock):
        OPCODE = "&gceTestRunner::assert <CONDITION> message (MSG)"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("MSG", "msg", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        msg: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_not_msg(ThirdBlock):
        OPCODE = "&gceTestRunner::assert not <CONDITION> message (MSG)"
        INPUT_SPECS = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            ("MSG", "msg", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T
        msg: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_strict_equal(ThirdBlock):
        OPCODE = "&gceTestRunner::assert typed equality (A) = (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_strict_not_equal(ThirdBlock):
        OPCODE = "&gceTestRunner::assert typed inequality (A) != (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_unstrict_equal(ThirdBlock):
        OPCODE = "&gceTestRunner::assert string equality (A) = (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_unstrict_not_equal(ThirdBlock):
        OPCODE = "&gceTestRunner::assert string inequality (A) != (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockAndTextInputValue, None),
            ("B", "b", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_text_in_value(ThirdBlock):
        OPCODE = "&gceTestRunner::assert text (TEXT) in value (VALUE)"
        INPUT_SPECS = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_text_not_in_value(ThirdBlock):
        OPCODE = "&gceTestRunner::assert text (TEXT) not in value (VALUE)"
        INPUT_SPECS = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_type(ThirdBlock):
        OPCODE = "&gceTestRunner::assert type of (VALUE) is ([EXPECTED])"
        INPUT_SPECS = (
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("EXPECTED", "expected", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T
        expected: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_custom_id_type(ThirdBlock):
        OPCODE = "&gceTestRunner::assert custom id of (VALUE) is (EXPECTED)"
        INPUT_SPECS = (
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("EXPECTED", "expected", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T
        expected: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_throws(ThirdBlock):
        OPCODE = "&gceTestRunner::assert throws error {SUBSTACK}"
        INPUT_SPECS = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_throws_contains(ThirdBlock):
        OPCODE = "&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}"
        INPUT_SPECS = (
            ("MSG", "msg", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        msg: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class assert_does_not_throw(ThirdBlock):
        OPCODE = "&gceTestRunner::assert does not throw error {SUBSTACK}"
        INPUT_SPECS = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fail_test(ThirdBlock):
        OPCODE = "&gceTestRunner::fail test with message (MSG)"
        INPUT_SPECS = (("MSG", "msg", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        msg: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_expected_type(ThirdBlock):
        OPCODE = "&gceTestRunner::#menu:expectedType"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
