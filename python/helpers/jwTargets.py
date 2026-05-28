from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwTargets:

    @grepr_dataclass()
    class this(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::this target"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class stage(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::stage target"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class from_name(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::(SPRITE) target"
        INPUT_SPECS: ClassVar = (("SPRITE", "sprite", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        sprite: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clone_origin(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::origin of (TARGET)"
        INPUT_SPECS: ClassVar = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::(TARGET) (MENU)"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            ("MENU", "menu", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T
        menu: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::set (TARGET) (MENU) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            ("MENU", "menu", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T
        menu: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_clone(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::is (TARGET) a clone"
        INPUT_SPECS: ClassVar = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_touching_object(ThirdBlock):
        OPCODE: ClassVar = (
            "&jwTargets::is (A) touching (B) {{id=jwTargets_isTouchingObject}}"
        )
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockOnlyInputValue, None),
            ("B", "b", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_var(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::var (NAME) of (TARGET)"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_var(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::set var (NAME) of (TARGET) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clone_r(ThirdBlock):
        OPCODE: ClassVar = (
            "&jwTargets::create clone of (TARGET) {{id=jwTargets_cloneR}}"
        )
        INPUT_SPECS: ClassVar = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_clone(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::delete clone (TARGET)"
        INPUT_SPECS: ClassVar = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class all(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::all targets"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class touching(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::targets touching (TARGET)"
        INPUT_SPECS: ClassVar = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clones(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::clones of (TARGET)"
        INPUT_SPECS: ClassVar = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class array_has_target(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::(ARRAY) has clone of (TARGET)"
        INPUT_SPECS: ClassVar = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        array: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_touching(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::is (A) touching (B) {{id=jwTargets_isTouching}}"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockOnlyInputValue, None),
            ("B", "b", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clone(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::create clone of (TARGET) {{id=jwTargets_clone}}"
        INPUT_SPECS: ClassVar = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_sprite(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::#menu:sprite"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_target_property(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::#menu:targetProperty"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_target_property_set(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::#menu:targetPropertySet"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_touching_object(ThirdBlock):
        OPCODE: ClassVar = "&jwTargets::#menu:touchingObject"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
