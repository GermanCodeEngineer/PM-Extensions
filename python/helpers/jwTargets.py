from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwTargets:

    @grepr_dataclass()
    class this(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwTargets::this target", inputs={}, dropdowns={})

    @grepr_dataclass()
    class stage(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwTargets::stage target", inputs={}, dropdowns={})

    @grepr_dataclass()
    class from_name(ThirdBlock):
        sprite: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::(SPRITE) target",
                inputs={
                    "SPRITE": ThirdInputValue.as_input(
                        self.sprite, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class clone_origin(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::origin of (TARGET)",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get(ThirdBlock):
        target: INPUT_COMPATIBLE_T
        menu: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::(TARGET) (MENU)",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    ),
                    "MENU": ThirdInputValue.as_input(
                        self.menu, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set(ThirdBlock):
        target: INPUT_COMPATIBLE_T
        menu: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::set (TARGET) (MENU) to (VALUE)",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    ),
                    "MENU": ThirdInputValue.as_input(
                        self.menu, p.SRBlockOnlyInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_clone(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::is (TARGET) a clone",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_touching_object(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::is (A) touching (B) {{id=jwTargets_isTouchingObject}}",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockOnlyInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_var(ThirdBlock):
        target: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::var (NAME) of (TARGET)",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_var(ThirdBlock):
        target: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::set var (NAME) of (TARGET) to (VALUE)",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class clone_r(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::create clone of (TARGET) {{id=jwTargets_cloneR}}",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class delete_clone(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::delete clone (TARGET)",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class all(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwTargets::all targets", inputs={}, dropdowns={})

    @grepr_dataclass()
    class touching(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::targets touching (TARGET)",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class clones(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::clones of (TARGET)",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class array_has_target(ThirdBlock):
        array: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::(ARRAY) has clone of (TARGET)",
                inputs={
                    "ARRAY": ThirdInputValue.as_input(
                        self.array, p.SRBlockOnlyInputValue
                    ),
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_touching(ThirdBlock):
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::is (A) touching (B) {{id=jwTargets_isTouching}}",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockOnlyInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class clone(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::create clone of (TARGET) {{id=jwTargets_clone}}",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_sprite(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwTargets::#menu:sprite", inputs={}, dropdowns={})

    @grepr_dataclass()
    class menu_target_property(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::#menu:targetProperty", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_target_property_set(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::#menu:targetPropertySet", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_touching_object(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::#menu:touchingObject", inputs={}, dropdowns={}
            )
