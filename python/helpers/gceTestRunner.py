from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class gceTestRunner:

    @grepr_dataclass()
    class test_scope(ThirdBlock):
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_(ThirdBlock):
        condition: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert <CONDITION>",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_not(ThirdBlock):
        condition: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert not <CONDITION>",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_msg(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        msg: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert <CONDITION> message (MSG)",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "MSG": ThirdInputValue.as_input(
                        self.msg, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_not_msg(ThirdBlock):
        condition: INPUT_COMPATIBLE_T
        msg: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert not <CONDITION> message (MSG)",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "MSG": ThirdInputValue.as_input(
                        self.msg, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_strict_equal(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert typed equality (A) = (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_strict_not_equal(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert typed inequality (A) != (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_unstrict_equal(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert string equality (A) = (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_unstrict_not_equal(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert string inequality (A) != (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_text_in_value(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_text_not_in_value(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_type(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        expected: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert type of (VALUE) is ([EXPECTED])",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "EXPECTED": ThirdInputValue.as_input(
                        self.expected, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_custom_id_type(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        expected: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert custom id of (VALUE) is (EXPECTED)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "EXPECTED": ThirdInputValue.as_input(
                        self.expected, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_throws(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert throws error {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_throws_contains(ThirdBlock):
        msg: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}",
                inputs={
                    "MSG": ThirdInputValue.as_input(
                        self.msg, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class assert_does_not_throw(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert does not throw error {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class fail_test(ThirdBlock):
        msg: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::fail test with message (MSG)",
                inputs={
                    "MSG": ThirdInputValue.as_input(
                        self.msg, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_expected_type(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::#menu:expectedType", inputs={}, dropdowns={}
            )
