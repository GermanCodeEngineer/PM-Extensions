from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class looks:

    @grepr_dataclass()
    class sayforsecs(ThirdBlock):
        OPCODE: ClassVar = "&looks::say (MESSAGE) for (SECONDS) seconds"
        INPUT_SPECS: ClassVar = (
            ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        message: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class say(ThirdBlock):
        OPCODE: ClassVar = "&looks::say (MESSAGE)"
        INPUT_SPECS: ClassVar = (
            ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        message: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class thinkforsecs(ThirdBlock):
        OPCODE: ClassVar = "&looks::think (MESSAGE) for (SECONDS) seconds"
        INPUT_SPECS: ClassVar = (
            ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        message: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class think(ThirdBlock):
        OPCODE: ClassVar = "&looks::think (MESSAGE)"
        INPUT_SPECS: ClassVar = (
            ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        message: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stoptalking(ThirdBlock):
        OPCODE: ClassVar = "&looks::stop speaking"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class set_font(ThirdBlock):
        OPCODE: ClassVar = "&looks::set font to (FONT) with font size (FONT-SIZE)"
        INPUT_SPECS: ClassVar = (
            ("FONT", "font", p.SRBlockAndTextInputValue, None),
            ("FONT-SIZE", "font_size", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        font: INPUT_COMPATIBLE_T
        font_size: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_color(ThirdBlock):
        OPCODE: ClassVar = "&looks::set [PROPERTY] color to (COLOR)"
        INPUT_SPECS: ClassVar = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
        color: INPUT_COMPATIBLE_T
        property: str

    @grepr_dataclass()
    class set_shape(ThirdBlock):
        OPCODE: ClassVar = "&looks::set text bubble [PROPERTY] to (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
        value: INPUT_COMPATIBLE_T
        property: str

    @grepr_dataclass()
    class say_width(ThirdBlock):
        OPCODE: ClassVar = "&looks::bubble width"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class say_height(ThirdBlock):
        OPCODE: ClassVar = "&looks::bubble height"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class switchcostumeto(ThirdBlock):
        OPCODE: ClassVar = "&looks::switch costume to ([COSTUME])"
        INPUT_SPECS: ClassVar = (
            ("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        costume: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class nextcostume(ThirdBlock):
        OPCODE: ClassVar = "&looks::next costume"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class getinputofcostume(ThirdBlock):
        OPCODE: ClassVar = "&looks::([PROPERTY]) of ([COSTUME])"
        INPUT_SPECS: ClassVar = (
            ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
            ("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        property: INPUT_COMPATIBLE_T
        costume: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class switchbackdropto(ThirdBlock):
        OPCODE: ClassVar = "&looks::switch backdrop to ([BACKDROP])"
        INPUT_SPECS: ClassVar = (
            ("BACKDROP", "backdrop", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        backdrop: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class nextbackdrop(ThirdBlock):
        OPCODE: ClassVar = "&looks::next backdrop"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class changesizeby(ThirdBlock):
        OPCODE: ClassVar = "&looks::change size by (AMOUNT)"
        INPUT_SPECS: ClassVar = (
            ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        amount: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class setsizeto(ThirdBlock):
        OPCODE: ClassVar = "&looks::set size to (SIZE)"
        INPUT_SPECS: ClassVar = (("SIZE", "size", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        size: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_stretch(ThirdBlock):
        OPCODE: ClassVar = "&looks::set stretch to x: (X) y: (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class change_stretch(ThirdBlock):
        OPCODE: ClassVar = "&looks:: change stretch by x: (X) y: (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stretch_get_x(ThirdBlock):
        OPCODE: ClassVar = "&looks::x stretch"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class stretch_get_y(ThirdBlock):
        OPCODE: ClassVar = "&looks::y stretch"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class changeeffectby(ThirdBlock):
        OPCODE: ClassVar = "&looks::change [EFFECT] effect by (AMOUNT)"
        INPUT_SPECS: ClassVar = (
            ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
        amount: INPUT_COMPATIBLE_T
        effect: str

    @grepr_dataclass()
    class seteffectto(ThirdBlock):
        OPCODE: ClassVar = "&looks::set [EFFECT] effect to (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
        value: INPUT_COMPATIBLE_T
        effect: str

    @grepr_dataclass()
    class set_tint_color(ThirdBlock):
        OPCODE: ClassVar = "&looks::set tint color to (COLOR)"
        INPUT_SPECS: ClassVar = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class cleargraphiceffects(ThirdBlock):
        OPCODE: ClassVar = "&looks::clear graphic effects"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class get_effect_value(ThirdBlock):
        OPCODE: ClassVar = "&looks::[EFFECT] effect"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
        effect: str

    @grepr_dataclass()
    class tint_color(ThirdBlock):
        OPCODE: ClassVar = "&looks::tint color"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class show(ThirdBlock):
        OPCODE: ClassVar = "&looks::show"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class hide(ThirdBlock):
        OPCODE: ClassVar = "&looks::hide"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class get_sprite_visible(ThirdBlock):
        OPCODE: ClassVar = "&looks::visible?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class change_visibility_of_sprite_show(ThirdBlock):
        OPCODE: ClassVar = "&looks::show ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class change_visibility_of_sprite_hide(ThirdBlock):
        OPCODE: ClassVar = "&looks::hide ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_other_sprite_visible(ThirdBlock):
        OPCODE: ClassVar = "&sounds::is ([TARGET]) visible?"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gotofrontback(ThirdBlock):
        OPCODE: ClassVar = "&looks::go to [LAYER] layer"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LAYER", "layer"),)
        layer: str

    @grepr_dataclass()
    class goforwardbackwardlayers(ThirdBlock):
        OPCODE: ClassVar = "&looks::go [DIRECTION] (LAYERS) layers"
        INPUT_SPECS: ClassVar = (
            ("LAYERS", "layers", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("DIRECTION", "direction"),)
        layers: INPUT_COMPATIBLE_T
        direction: str

    @grepr_dataclass()
    class layers_set_layer(ThirdBlock):
        OPCODE: ClassVar = "&looks::go to layer (LAYER)"
        INPUT_SPECS: ClassVar = (("LAYER", "layer", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        layer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class go_target_layer(ThirdBlock):
        OPCODE: ClassVar = "&looks::go [DIRECTION] ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("DIRECTION", "direction"),)
        target: INPUT_COMPATIBLE_T
        direction: str

    @grepr_dataclass()
    class layers_get_layer(ThirdBlock):
        OPCODE: ClassVar = "&looks::layer"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class costumenumbername(ThirdBlock):
        OPCODE: ClassVar = "&looks::costume [PROPERTY]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
        property: str

    @grepr_dataclass()
    class backdropnumbername(ThirdBlock):
        OPCODE: ClassVar = "&looks::backdrop [PROPERTY]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
        property: str

    @grepr_dataclass()
    class size(ThirdBlock):
        OPCODE: ClassVar = "&looks::size"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class costume(ThirdBlock):
        OPCODE: ClassVar = "&looks::#COSTUME MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class backdrops(ThirdBlock):
        OPCODE: ClassVar = "&looks::#BACKDROP MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class getinput_menu(ThirdBlock):
        OPCODE: ClassVar = "&looks::#COSTUME PROPERTY MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class change_visibility_of_sprite_menu(ThirdBlock):
        OPCODE: ClassVar = "&looks::#SHOW/HIDE SPRITE MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class get_other_sprite_visible_menu(ThirdBlock):
        OPCODE: ClassVar = "&looks::#IS SPRITE VISIBLE MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
