from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class dogeiscutRegularExpressions:

    class regex(ThirdBlock):

        def __init__(self, pattern: INPUT_COMPATIBLE_T, flags: INPUT_COMPATIBLE_T):
            self.pattern = pattern
            self.flags = flags

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

    class escape(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T):
            self.string = string

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

    class source_of(ThirdBlock):

        def __init__(self, regex: INPUT_COMPATIBLE_T):
            self.regex = regex

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

    class flags_of(ThirdBlock):

        def __init__(self, regex: INPUT_COMPATIBLE_T):
            self.regex = regex

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

    class test(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T):
            self.string = string
            self.regex = regex

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

    class search(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T):
            self.string = string
            self.regex = regex

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

    class replace(ThirdBlock):

        def __init__(
            self,
            regex: INPUT_COMPATIBLE_T,
            a: INPUT_COMPATIBLE_T,
            b: INPUT_COMPATIBLE_T,
        ):
            self.regex = regex
            self.a = a
            self.b = b

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

    class replace_all(ThirdBlock):

        def __init__(
            self,
            regex: INPUT_COMPATIBLE_T,
            a: INPUT_COMPATIBLE_T,
            b: INPUT_COMPATIBLE_T,
        ):
            self.regex = regex
            self.a = a
            self.b = b

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

    class split(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T):
            self.string = string
            self.regex = regex

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

    class match(ThirdBlock):

        def __init__(self, regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T):
            self.regex = regex
            self.string = string

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

    class match_all(ThirdBlock):

        def __init__(self, regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T):
            self.regex = regex
            self.string = string

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

    class exec(ThirdBlock):

        def __init__(self, regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T):
            self.regex = regex
            self.string = string

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

    class get_last_index(ThirdBlock):

        def __init__(self, regex: INPUT_COMPATIBLE_T):
            self.regex = regex

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

    class set_last_index(ThirdBlock):

        def __init__(self, regex: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T):
            self.regex = regex
            self.index = index

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
