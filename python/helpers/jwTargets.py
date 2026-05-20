from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwTargets:

    class this(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwTargets::this target", inputs={}, dropdowns={})

    class stage(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwTargets::stage target", inputs={}, dropdowns={})

    class from_name(ThirdBlock):

        def __init__(self, sprite: INPUT_COMPATIBLE_T):
            self.sprite = sprite

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

    class clone_origin(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class get(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T, menu: INPUT_COMPATIBLE_T):
            self.target = target
            self.menu = menu

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

    class set(ThirdBlock):

        def __init__(
            self,
            target: INPUT_COMPATIBLE_T,
            menu: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
        ):
            self.target = target
            self.menu = menu
            self.value = value

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

    class is_clone(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class is_touching_object(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::is (A) touching (B) {{id=jwTargets_isTouchingObject}}",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockOnlyInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class get_var(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T):
            self.target = target
            self.name = name

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

    class set_var(ThirdBlock):

        def __init__(
            self,
            target: INPUT_COMPATIBLE_T,
            name: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
        ):
            self.target = target
            self.name = name
            self.value = value

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

    class clone_r(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class delete_clone(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class all(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwTargets::all targets", inputs={}, dropdowns={})

    class touching(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class clones(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class array_has_target(ThirdBlock):

        def __init__(self, array: INPUT_COMPATIBLE_T, target: INPUT_COMPATIBLE_T):
            self.array = array
            self.target = target

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

    class is_touching(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::is (A) touching (B) {{id=jwTargets_isTouching}}",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockOnlyInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class clone(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class menu_sprite(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwTargets::#menu:sprite", inputs={}, dropdowns={})

    class menu_target_property(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::#menu:targetProperty", inputs={}, dropdowns={}
            )

    class menu_target_property_set(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::#menu:targetPropertySet", inputs={}, dropdowns={}
            )

    class menu_touching_object(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwTargets::#menu:touchingObject", inputs={}, dropdowns={}
            )
