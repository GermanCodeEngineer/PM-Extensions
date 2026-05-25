from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class jwTargets:

    @grepr_dataclass()
    class this(ThirdBlock):
        OPCODE = "&jwTargets::this target"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class stage(ThirdBlock):
        OPCODE = "&jwTargets::stage target"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class from_name(ThirdBlock):
        OPCODE = "&jwTargets::(SPRITE) target"
        INPUT_SPECS = (("SPRITE", "sprite", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        sprite: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clone_origin(ThirdBlock):
        OPCODE = "&jwTargets::origin of (TARGET)"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get(ThirdBlock):
        OPCODE = "&jwTargets::(TARGET) (MENU)"
        INPUT_SPECS = (
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            ("MENU", "menu", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T
        menu: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&jwTargets::set (TARGET) (MENU) to (VALUE)"
        INPUT_SPECS = (
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            ("MENU", "menu", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T
        menu: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_clone(ThirdBlock):
        OPCODE = "&jwTargets::is (TARGET) a clone"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_touching_object(ThirdBlock):
        OPCODE = "&jwTargets::is (A) touching (B) {{id=jwTargets_isTouchingObject}}"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockOnlyInputValue, None),
            ("B", "b", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_var(ThirdBlock):
        OPCODE = "&jwTargets::var (NAME) of (TARGET)"
        INPUT_SPECS = (
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_var(ThirdBlock):
        OPCODE = "&jwTargets::set var (NAME) of (TARGET) to (VALUE)"
        INPUT_SPECS = (
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clone_r(ThirdBlock):
        OPCODE = "&jwTargets::create clone of (TARGET) {{id=jwTargets_cloneR}}"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_clone(ThirdBlock):
        OPCODE = "&jwTargets::delete clone (TARGET)"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class all(ThirdBlock):
        OPCODE = "&jwTargets::all targets"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class touching(ThirdBlock):
        OPCODE = "&jwTargets::targets touching (TARGET)"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clones(ThirdBlock):
        OPCODE = "&jwTargets::clones of (TARGET)"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class array_has_target(ThirdBlock):
        OPCODE = "&jwTargets::(ARRAY) has clone of (TARGET)"
        INPUT_SPECS = (
            ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
            ("TARGET", "target", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        array: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_touching(ThirdBlock):
        OPCODE = "&jwTargets::is (A) touching (B) {{id=jwTargets_isTouching}}"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockOnlyInputValue, None),
            ("B", "b", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class clone(ThirdBlock):
        OPCODE = "&jwTargets::create clone of (TARGET) {{id=jwTargets_clone}}"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_sprite(ThirdBlock):
        OPCODE = "&jwTargets::#menu:sprite"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_target_property(ThirdBlock):
        OPCODE = "&jwTargets::#menu:targetProperty"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_target_property_set(ThirdBlock):
        OPCODE = "&jwTargets::#menu:targetPropertySet"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_touching_object(ThirdBlock):
        OPCODE = "&jwTargets::#menu:touchingObject"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
