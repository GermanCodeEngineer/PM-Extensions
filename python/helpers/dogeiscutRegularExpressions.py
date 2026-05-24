from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutRegularExpressions:

    @grepr_dataclass()
    class regex(ThirdBlock):
        pattern: INPUT_COMPATIBLE_T
        flags: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)",
                inputs={
                    "PATTERN": ThirdInputValue.as_input(
                        self.pattern, p.SRBlockAndTextInputValue
                    ),
                    "FLAGS": ThirdInputValue.as_input(
                        self.flags, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class escape(ThirdBlock):
        string: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::escape (STRING) for regex",
                inputs={
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class source_of(ThirdBlock):
        regex: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::source of (REGEX)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class flags_of(ThirdBlock):
        regex: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::flags of (REGEX)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class test(ThirdBlock):
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::test (STRING) for (REGEX)",
                inputs={
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class search(ThirdBlock):
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::search (STRING) with (REGEX)",
                inputs={
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class replace(ThirdBlock):
        regex: INPUT_COMPATIBLE_T
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::replace (REGEX) in (A) with (B)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class replace_all(ThirdBlock):
        regex: INPUT_COMPATIBLE_T
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::replace all (REGEX) in (A) with (B)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class split(ThirdBlock):
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::split (STRING) by (REGEX)",
                inputs={
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class match(ThirdBlock):
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::match (REGEX) with (STRING)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class match_all(ThirdBlock):
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::match all (REGEX) with (STRING)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class exec(ThirdBlock):
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::execute (REGEX) on (STRING)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_last_index(ThirdBlock):
        regex: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::get last index of (REGEX)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_last_index(ThirdBlock):
        regex: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&dogeiscutRegularExpressions::set last index of (REGEX) to (INDEX)",
                inputs={
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockOnlyInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )
