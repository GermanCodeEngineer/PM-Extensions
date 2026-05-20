from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwNum:

    class add(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) + (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class sub(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) - (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class mul(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) * (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class div(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) / (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class pow(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) ^ (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class fact(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T):
            self.a = a

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::[A]!",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class eq(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) = (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class gt(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) > (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class gte(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) >= (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class lt(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) < (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class lte(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) <= (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class root(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::root (A) (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class ssqrt(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T):
            self.a = a

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::square super-root (A)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class log(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::log (A) (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class slog(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::super log (A) (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class mod(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) % (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class round(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::([A]) (B)",
                inputs={
                    "A": ThirdInputValue.as_input(
                        self.a, p.SRBlockAndDropdownInputValue
                    ),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class is_integer(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T):
            self.a = a

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::is (A) an integer?",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class hyper(ThirdBlock):

        def __init__(
            self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T, c: INPUT_COMPATIBLE_T
        ):
            self.a = a
            self.b = b
            self.c = c

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) hyper (B) (C)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                    "C": ThirdInputValue.as_input(self.c, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class arrow(ThirdBlock):

        def __init__(
            self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T, c: INPUT_COMPATIBLE_T
        ):
            self.a = a
            self.b = b
            self.c = c

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) arrow (B) (C)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                    "C": ThirdInputValue.as_input(self.c, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class reverse_arrow(ThirdBlock):

        def __init__(
            self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T, c: INPUT_COMPATIBLE_T
        ):
            self.a = a
            self.b = b
            self.c = c

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(C) reverse arrow (B) (A)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                    "C": ThirdInputValue.as_input(self.c, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class expansion(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) expansion (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class to_string(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T):
            self.a = a

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) to string",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class to_string_d(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) to string with (B) decimal places",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class to_hyper_e(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T):
            self.a = a

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) to hyper E",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class menu_round(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwNum::#menu:round", inputs={}, dropdowns={})
