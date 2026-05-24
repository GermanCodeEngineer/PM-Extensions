from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwNum:

    @grepr_dataclass()
    class add(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) + (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class sub(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) - (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class mul(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) * (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class div(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) / (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class pow(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) ^ (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class fact(ThirdBlock):
        a: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::[A]!",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eq(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) = (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class gt(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) > (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class gte(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) >= (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class lt(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) < (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class lte(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) <= (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class root(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::root (A) (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class ssqrt(ThirdBlock):
        a: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::square super-root (A)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class log(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::log (A) (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class slog(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::super log (A) (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class mod(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) % (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class round(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class is_integer(ThirdBlock):
        a: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::is (A) an integer?",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class hyper(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class arrow(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class reverse_arrow(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T
        c: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class expansion(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) expansion (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class to_string(ThirdBlock):
        a: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) to string",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class to_string_d(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) to string with (B) decimal places",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class to_hyper_e(ThirdBlock):
        a: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwNum::(A) to hyper E",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_round(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwNum::#menu:round", inputs={}, dropdowns={})
