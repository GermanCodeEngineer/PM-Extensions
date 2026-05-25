from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class looks:

    @grepr_dataclass()
    class sayforsecs(ThirdBlock):
        OPCODE = "&looks::say (MESSAGE) for (SECONDS) seconds"
        INPUT_SPECS = (
            ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        message: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class say(ThirdBlock):
        OPCODE = "&looks::say (MESSAGE)"
        INPUT_SPECS = (("MESSAGE", "message", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        message: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class thinkforsecs(ThirdBlock):
        OPCODE = "&looks::think (MESSAGE) for (SECONDS) seconds"
        INPUT_SPECS = (
            ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        message: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class think(ThirdBlock):
        OPCODE = "&looks::think (MESSAGE)"
        INPUT_SPECS = (("MESSAGE", "message", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        message: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stoptalking(ThirdBlock):
        OPCODE = "&looks::stop speaking"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class set_font(ThirdBlock):
        OPCODE = "&looks::set font to (FONT) with font size (FONT-SIZE)"
        INPUT_SPECS = (
            ("FONT", "font", p.SRBlockAndTextInputValue, None),
            ("FONT-SIZE", "font_size", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        font: INPUT_COMPATIBLE_T
        font_size: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_color(ThirdBlock):
        OPCODE = "&looks::set [PROPERTY] color to (COLOR)"
        INPUT_SPECS = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("PROPERTY", "property"),)
        color: INPUT_COMPATIBLE_T
        property: str

    @grepr_dataclass()
    class set_shape(ThirdBlock):
        OPCODE = "&looks::set text bubble [PROPERTY] to (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("PROPERTY", "property"),)
        value: INPUT_COMPATIBLE_T
        property: str

    @grepr_dataclass()
    class say_width(ThirdBlock):
        OPCODE = "&looks::bubble width"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class say_height(ThirdBlock):
        OPCODE = "&looks::bubble height"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class switchcostumeto(ThirdBlock):
        OPCODE = "&looks::switch costume to ([COSTUME])"
        INPUT_SPECS = (("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        costume: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class nextcostume(ThirdBlock):
        OPCODE = "&looks::next costume"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class getinputofcostume(ThirdBlock):
        OPCODE = "&looks::([PROPERTY]) of ([COSTUME])"
        INPUT_SPECS = (
            ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
            ("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        property: INPUT_COMPATIBLE_T
        costume: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class switchbackdropto(ThirdBlock):
        OPCODE = "&looks::switch backdrop to ([BACKDROP])"
        INPUT_SPECS = (("BACKDROP", "backdrop", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        backdrop: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class nextbackdrop(ThirdBlock):
        OPCODE = "&looks::next backdrop"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class changesizeby(ThirdBlock):
        OPCODE = "&looks::change size by (AMOUNT)"
        INPUT_SPECS = (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        amount: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class setsizeto(ThirdBlock):
        OPCODE = "&looks::set size to (SIZE)"
        INPUT_SPECS = (("SIZE", "size", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        size: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_stretch(ThirdBlock):
        OPCODE = "&looks::set stretch to x: (X) y: (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class change_stretch(ThirdBlock):
        OPCODE = "&looks:: change stretch by x: (X) y: (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stretch_get_x(ThirdBlock):
        OPCODE = "&looks::x stretch"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class stretch_get_y(ThirdBlock):
        OPCODE = "&looks::y stretch"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class changeeffectby(ThirdBlock):
        OPCODE = "&looks::change [EFFECT] effect by (AMOUNT)"
        INPUT_SPECS = (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("EFFECT", "effect"),)
        amount: INPUT_COMPATIBLE_T
        effect: str

    @grepr_dataclass()
    class seteffectto(ThirdBlock):
        OPCODE = "&looks::set [EFFECT] effect to (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("EFFECT", "effect"),)
        value: INPUT_COMPATIBLE_T
        effect: str

    @grepr_dataclass()
    class set_tint_color(ThirdBlock):
        OPCODE = "&looks::set tint color to (COLOR)"
        INPUT_SPECS = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class cleargraphiceffects(ThirdBlock):
        OPCODE = "&looks::clear graphic effects"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class get_effect_value(ThirdBlock):
        OPCODE = "&looks::[EFFECT] effect"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("EFFECT", "effect"),)
        effect: str

    @grepr_dataclass()
    class tint_color(ThirdBlock):
        OPCODE = "&looks::tint color"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class show(ThirdBlock):
        OPCODE = "&looks::show"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class hide(ThirdBlock):
        OPCODE = "&looks::hide"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class get_sprite_visible(ThirdBlock):
        OPCODE = "&looks::visible?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class change_visibility_of_sprite_show(ThirdBlock):
        OPCODE = "&looks::show ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class change_visibility_of_sprite_hide(ThirdBlock):
        OPCODE = "&looks::hide ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_other_sprite_visible(ThirdBlock):
        OPCODE = "&sounds::is ([TARGET]) visible?"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gotofrontback(ThirdBlock):
        OPCODE = "&looks::go to [LAYER] layer"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LAYER", "layer"),)
        layer: str

    @grepr_dataclass()
    class goforwardbackwardlayers(ThirdBlock):
        OPCODE = "&looks::go [DIRECTION] (LAYERS) layers"
        INPUT_SPECS = (("LAYERS", "layers", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("DIRECTION", "direction"),)
        layers: INPUT_COMPATIBLE_T
        direction: str

    @grepr_dataclass()
    class layers_set_layer(ThirdBlock):
        OPCODE = "&looks::go to layer (LAYER)"
        INPUT_SPECS = (("LAYER", "layer", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        layer: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class go_target_layer(ThirdBlock):
        OPCODE = "&looks::go [DIRECTION] ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = (("DIRECTION", "direction"),)
        target: INPUT_COMPATIBLE_T
        direction: str

    @grepr_dataclass()
    class layers_get_layer(ThirdBlock):
        OPCODE = "&looks::layer"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class costumenumbername(ThirdBlock):
        OPCODE = "&looks::costume [PROPERTY]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("PROPERTY", "property"),)
        property: str

    @grepr_dataclass()
    class backdropnumbername(ThirdBlock):
        OPCODE = "&looks::backdrop [PROPERTY]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("PROPERTY", "property"),)
        property: str

    @grepr_dataclass()
    class size(ThirdBlock):
        OPCODE = "&looks::size"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class costume(ThirdBlock):
        OPCODE = "&looks::#COSTUME MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class backdrops(ThirdBlock):
        OPCODE = "&looks::#BACKDROP MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class getinput_menu(ThirdBlock):
        OPCODE = "&looks::#COSTUME PROPERTY MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class change_visibility_of_sprite_menu(ThirdBlock):
        OPCODE = "&looks::#SHOW/HIDE SPRITE MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class get_other_sprite_visible_menu(ThirdBlock):
        OPCODE = "&looks::#IS SPRITE VISIBLE MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
