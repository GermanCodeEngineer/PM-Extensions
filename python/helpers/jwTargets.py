from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class jwTargets:

    @staticmethod
    def this() -> p.SRBlock:
        return p.SRBlock(opcode="&jwTargets::this target", inputs={}, dropdowns={})

    @staticmethod
    def stage() -> p.SRBlock:
        return p.SRBlock(opcode="&jwTargets::stage target", inputs={}, dropdowns={})

    @staticmethod
    def from_name(sprite: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::(SPRITE) target",
            inputs={
                "SPRITE": ThirdInputValue.as_input(sprite, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def clone_origin(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::origin of (TARGET)",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def get(target: INPUT_COMPATIBLE_T, menu: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::(TARGET) (MENU)",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue),
                "MENU": ThirdInputValue.as_input(menu, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set(
        target: INPUT_COMPATIBLE_T, menu: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::set (TARGET) (MENU) to (VALUE)",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue),
                "MENU": ThirdInputValue.as_input(menu, p.SRBlockOnlyInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_clone(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::is (TARGET) a clone",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def is_touching_object(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::is (A) touching (B) {{id=jwTargets_isTouchingObject}}",
            inputs={
                "A": ThirdInputValue.as_input(a, p.SRBlockOnlyInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_var(target: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::var (NAME) of (TARGET)",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_var(
        target: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::set var (NAME) of (TARGET) to (VALUE)",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def clone_r(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::create clone of (TARGET) {{id=jwTargets_cloneR}}",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def delete_clone(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::delete clone (TARGET)",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def all() -> p.SRBlock:
        return p.SRBlock(opcode="&jwTargets::all targets", inputs={}, dropdowns={})

    @staticmethod
    def touching(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::targets touching (TARGET)",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def clones(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::clones of (TARGET)",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def array_has_target(
        array: INPUT_COMPATIBLE_T, target: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::(ARRAY) has clone of (TARGET)",
            inputs={
                "ARRAY": ThirdInputValue.as_input(array, p.SRBlockOnlyInputValue),
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_touching(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::is (A) touching (B) {{id=jwTargets_isTouching}}",
            inputs={
                "A": ThirdInputValue.as_input(a, p.SRBlockOnlyInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def clone(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::create clone of (TARGET) {{id=jwTargets_clone}}",
            inputs={
                "TARGET": ThirdInputValue.as_input(target, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def menu_sprite() -> p.SRBlock:
        return p.SRBlock(opcode="&jwTargets::#menu:sprite", inputs={}, dropdowns={})

    @staticmethod
    def menu_target_property() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::#menu:targetProperty", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_target_property_set() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::#menu:targetPropertySet", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_touching_object() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwTargets::#menu:touchingObject", inputs={}, dropdowns={}
        )
