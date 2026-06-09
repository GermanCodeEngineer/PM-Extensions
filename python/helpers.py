from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class BlockHelpers:

    class motion:

        @grepr_dataclass()
        class movesteps(ThirdBlock):
            OPCODE: ClassVar = "&motion::move (STEPS) steps"
            INPUT_SPECS: ClassVar = (
                ("STEPS", "steps", p.SRBlockAndTextInputValue, None),
            )
            steps: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class movebacksteps(ThirdBlock):
            OPCODE: ClassVar = "&motion::move back (STEPS) steps"
            INPUT_SPECS: ClassVar = (
                ("STEPS", "steps", p.SRBlockAndTextInputValue, None),
            )
            steps: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class moveupdownsteps(ThirdBlock):
            OPCODE: ClassVar = "&motion::move [DIRECTION] (STEPS) steps"
            INPUT_SPECS: ClassVar = (
                ("STEPS", "steps", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("DIRECTION", "direction"),)
            steps: INPUT_COMPATIBLE_T
            direction: str

        @grepr_dataclass()
        class turnright(ThirdBlock):
            OPCODE: ClassVar = "&motion::turn clockwise (DEGREES) degrees"
            INPUT_SPECS: ClassVar = (
                ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
            )
            degrees: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class turnleft(ThirdBlock):
            OPCODE: ClassVar = "&motion::turn counterclockwise (DEGREES) degrees"
            INPUT_SPECS: ClassVar = (
                ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
            )
            degrees: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class goto(ThirdBlock):
            OPCODE: ClassVar = "&motion::go to ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class gotoxy(ThirdBlock):
            OPCODE: ClassVar = "&motion::go to x: (X) y: (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class changebyxy(ThirdBlock):
            OPCODE: ClassVar = "&motion::change by x: (DX) y: (DY)"
            INPUT_SPECS: ClassVar = (
                ("DX", "dx", p.SRBlockAndTextInputValue, None),
                ("DY", "dy", p.SRBlockAndTextInputValue, None),
            )
            dx: INPUT_COMPATIBLE_T
            dy: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class glideto(ThirdBlock):
            OPCODE: ClassVar = "&motion::glide (SECONDS) secs to ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            seconds: INPUT_COMPATIBLE_T
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class glidesecstoxy(ThirdBlock):
            OPCODE: ClassVar = "&motion::glide (SECONDS) secs to x: (X) y: (Y)"
            INPUT_SPECS: ClassVar = (
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            seconds: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class pointindirection(ThirdBlock):
            OPCODE: ClassVar = "&motion::point in direction (DIRECTION)"
            INPUT_SPECS: ClassVar = (
                ("DIRECTION", "direction", p.SRBlockAndTextInputValue, None),
            )
            direction: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class pointtowards(ThirdBlock):
            OPCODE: ClassVar = "&motion::point towards ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class pointtowardsxy(ThirdBlock):
            OPCODE: ClassVar = "&motion::point towards x: (X) y: (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class turnaround(ThirdBlock):
            OPCODE: ClassVar = "&motion::turn around"

        @grepr_dataclass()
        class changexby(ThirdBlock):
            OPCODE: ClassVar = "&motion::change x by (DX)"
            INPUT_SPECS: ClassVar = (("DX", "dx", p.SRBlockAndTextInputValue, None),)
            dx: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class setx(ThirdBlock):
            OPCODE: ClassVar = "&motion::set x to (X)"
            INPUT_SPECS: ClassVar = (("X", "x", p.SRBlockAndTextInputValue, None),)
            x: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class changeyby(ThirdBlock):
            OPCODE: ClassVar = "&motion::change y by (DY)"
            INPUT_SPECS: ClassVar = (("DY", "dy", p.SRBlockAndTextInputValue, None),)
            dy: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class sety(ThirdBlock):
            OPCODE: ClassVar = "&motion::set y to (Y)"
            INPUT_SPECS: ClassVar = (("Y", "y", p.SRBlockAndTextInputValue, None),)
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class ifonedgebounce(ThirdBlock):
            OPCODE: ClassVar = "&motion::if on edge, bounce"

        @grepr_dataclass()
        class ifonspritebounce(ThirdBlock):
            OPCODE: ClassVar = "&motion::if touching ([TARGET]), bounce"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class setrotationstyle(ThirdBlock):
            OPCODE: ClassVar = "&motion::set rotation style [STYLE]"
            DROPDOWN_SPECS: ClassVar = (("STYLE", "style"),)
            style: str

        @grepr_dataclass()
        class move_sprite_to_scene_side(ThirdBlock):
            OPCODE: ClassVar = "&motion::move to stage [ZONE]"
            DROPDOWN_SPECS: ClassVar = (("ZONE", "zone"),)
            zone: str

        @grepr_dataclass()
        class xposition(ThirdBlock):
            OPCODE: ClassVar = "&motion::x position"

        @grepr_dataclass()
        class yposition(ThirdBlock):
            OPCODE: ClassVar = "&motion::y position"

        @grepr_dataclass()
        class direction(ThirdBlock):
            OPCODE: ClassVar = "&motion::direction"

        @grepr_dataclass()
        class goto_menu(ThirdBlock):
            OPCODE: ClassVar = "&motion::#REACHABLE TARGET MENU (GO)"

        @grepr_dataclass()
        class glideto_menu(ThirdBlock):
            OPCODE: ClassVar = "&motion::#REACHABLE TARGET MENU (GLIDE)"

        @grepr_dataclass()
        class pointtowards_menu(ThirdBlock):
            OPCODE: ClassVar = "&motion::#OBSERVABLE TARGET MENU"

        @grepr_dataclass()
        class turnrightaroundxy(ThirdBlock):
            OPCODE: ClassVar = "&motion::turn clockwise (DEGREES) around x: (X) y: (Y)"
            INPUT_SPECS: ClassVar = (
                ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            degrees: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class turnleftaroundxy(ThirdBlock):
            OPCODE: ClassVar = (
                "&motion::turn counterclockwise (DEGREES) around x: (X) y: (Y)"
            )
            INPUT_SPECS: ClassVar = (
                ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            degrees: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class ifonxybounce(ThirdBlock):
            OPCODE: ClassVar = "&motion::if touching x: (X) y: [Y], bounce"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

    class looks:

        @grepr_dataclass()
        class sayforsecs(ThirdBlock):
            OPCODE: ClassVar = "&looks::say (MESSAGE) for (SECONDS) seconds"
            INPUT_SPECS: ClassVar = (
                ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            )
            message: INPUT_COMPATIBLE_T
            seconds: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class say(ThirdBlock):
            OPCODE: ClassVar = "&looks::say (MESSAGE)"
            INPUT_SPECS: ClassVar = (
                ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
            )
            message: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class thinkforsecs(ThirdBlock):
            OPCODE: ClassVar = "&looks::think (MESSAGE) for (SECONDS) seconds"
            INPUT_SPECS: ClassVar = (
                ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            )
            message: INPUT_COMPATIBLE_T
            seconds: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class think(ThirdBlock):
            OPCODE: ClassVar = "&looks::think (MESSAGE)"
            INPUT_SPECS: ClassVar = (
                ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
            )
            message: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class stoptalking(ThirdBlock):
            OPCODE: ClassVar = "&looks::stop speaking"

        @grepr_dataclass()
        class set_font(ThirdBlock):
            OPCODE: ClassVar = "&looks::set font to (FONT) with font size (FONT-SIZE)"
            INPUT_SPECS: ClassVar = (
                ("FONT", "font", p.SRBlockAndTextInputValue, None),
                ("FONT-SIZE", "font_size", p.SRBlockAndTextInputValue, None),
            )
            font: INPUT_COMPATIBLE_T
            font_size: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_color(ThirdBlock):
            OPCODE: ClassVar = "&looks::set [PROPERTY] color to (COLOR)"
            INPUT_SPECS: ClassVar = (
                ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
            color: INPUT_COMPATIBLE_T
            property: str

        @grepr_dataclass()
        class set_shape(ThirdBlock):
            OPCODE: ClassVar = "&looks::set text bubble [PROPERTY] to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
            value: INPUT_COMPATIBLE_T
            property: str

        @grepr_dataclass()
        class say_width(ThirdBlock):
            OPCODE: ClassVar = "&looks::bubble width"

        @grepr_dataclass()
        class say_height(ThirdBlock):
            OPCODE: ClassVar = "&looks::bubble height"

        @grepr_dataclass()
        class switchcostumeto(ThirdBlock):
            OPCODE: ClassVar = "&looks::switch costume to ([COSTUME])"
            INPUT_SPECS: ClassVar = (
                ("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),
            )
            costume: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class nextcostume(ThirdBlock):
            OPCODE: ClassVar = "&looks::next costume"

        @grepr_dataclass()
        class getinputofcostume(ThirdBlock):
            OPCODE: ClassVar = "&looks::([PROPERTY]) of ([COSTUME])"
            INPUT_SPECS: ClassVar = (
                ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
                ("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),
            )
            property: INPUT_COMPATIBLE_T
            costume: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class switchbackdropto(ThirdBlock):
            OPCODE: ClassVar = "&looks::switch backdrop to ([BACKDROP])"
            INPUT_SPECS: ClassVar = (
                ("BACKDROP", "backdrop", p.SRBlockAndDropdownInputValue, None),
            )
            backdrop: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class nextbackdrop(ThirdBlock):
            OPCODE: ClassVar = "&looks::next backdrop"

        @grepr_dataclass()
        class changesizeby(ThirdBlock):
            OPCODE: ClassVar = "&looks::change size by (AMOUNT)"
            INPUT_SPECS: ClassVar = (
                ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
            )
            amount: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class setsizeto(ThirdBlock):
            OPCODE: ClassVar = "&looks::set size to (SIZE)"
            INPUT_SPECS: ClassVar = (
                ("SIZE", "size", p.SRBlockAndTextInputValue, None),
            )
            size: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_stretch(ThirdBlock):
            OPCODE: ClassVar = "&looks::set stretch to x: (X) y: (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class change_stretch(ThirdBlock):
            OPCODE: ClassVar = "&looks:: change stretch by x: (X) y: (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class stretch_get_x(ThirdBlock):
            OPCODE: ClassVar = "&looks::x stretch"

        @grepr_dataclass()
        class stretch_get_y(ThirdBlock):
            OPCODE: ClassVar = "&looks::y stretch"

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
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
            value: INPUT_COMPATIBLE_T
            effect: str

        @grepr_dataclass()
        class set_tint_color(ThirdBlock):
            OPCODE: ClassVar = "&looks::set tint color to (COLOR)"
            INPUT_SPECS: ClassVar = (
                ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            )
            color: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class cleargraphiceffects(ThirdBlock):
            OPCODE: ClassVar = "&looks::clear graphic effects"

        @grepr_dataclass()
        class get_effect_value(ThirdBlock):
            OPCODE: ClassVar = "&looks::[EFFECT] effect"
            DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
            effect: str

        @grepr_dataclass()
        class tint_color(ThirdBlock):
            OPCODE: ClassVar = "&looks::tint color"

        @grepr_dataclass()
        class show(ThirdBlock):
            OPCODE: ClassVar = "&looks::show"

        @grepr_dataclass()
        class hide(ThirdBlock):
            OPCODE: ClassVar = "&looks::hide"

        @grepr_dataclass()
        class get_sprite_visible(ThirdBlock):
            OPCODE: ClassVar = "&looks::visible?"

        @grepr_dataclass()
        class change_visibility_of_sprite_show(ThirdBlock):
            OPCODE: ClassVar = "&looks::show ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class change_visibility_of_sprite_hide(ThirdBlock):
            OPCODE: ClassVar = "&looks::hide ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_other_sprite_visible(ThirdBlock):
            OPCODE: ClassVar = "&sounds::is ([TARGET]) visible?"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class gotofrontback(ThirdBlock):
            OPCODE: ClassVar = "&looks::go to [LAYER] layer"
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
            INPUT_SPECS: ClassVar = (
                ("LAYER", "layer", p.SRBlockAndTextInputValue, None),
            )
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

        @grepr_dataclass()
        class costumenumbername(ThirdBlock):
            OPCODE: ClassVar = "&looks::costume [PROPERTY]"
            DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
            property: str

        @grepr_dataclass()
        class backdropnumbername(ThirdBlock):
            OPCODE: ClassVar = "&looks::backdrop [PROPERTY]"
            DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
            property: str

        @grepr_dataclass()
        class size(ThirdBlock):
            OPCODE: ClassVar = "&looks::size"

        @grepr_dataclass()
        class costume(ThirdBlock):
            OPCODE: ClassVar = "&looks::#COSTUME MENU"

        @grepr_dataclass()
        class backdrops(ThirdBlock):
            OPCODE: ClassVar = "&looks::#BACKDROP MENU"

        @grepr_dataclass()
        class getinput_menu(ThirdBlock):
            OPCODE: ClassVar = "&looks::#COSTUME PROPERTY MENU"

        @grepr_dataclass()
        class change_visibility_of_sprite_menu(ThirdBlock):
            OPCODE: ClassVar = "&looks::#SHOW/HIDE SPRITE MENU"

        @grepr_dataclass()
        class get_other_sprite_visible_menu(ThirdBlock):
            OPCODE: ClassVar = "&looks::#IS SPRITE VISIBLE MENU"

    class sound:

        @grepr_dataclass()
        class playuntildone(ThirdBlock):
            OPCODE: ClassVar = "&sound::play sound ([SOUND]) until done"
            INPUT_SPECS: ClassVar = (
                ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            )
            sound: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class play_at_seconds_until_done(ThirdBlock):
            OPCODE: ClassVar = (
                "&sound::play sound ([SOUND]) starting at (SECONDS) seconds until done"
            )
            INPUT_SPECS: ClassVar = (
                ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            )
            sound: INPUT_COMPATIBLE_T
            seconds: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class play(ThirdBlock):
            OPCODE: ClassVar = "&sound::start sound ([SOUND])"
            INPUT_SPECS: ClassVar = (
                ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            )
            sound: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class play_at_seconds(ThirdBlock):
            OPCODE: ClassVar = "&sound::start sound ([SOUND]) at (SECONDS) seconds"
            INPUT_SPECS: ClassVar = (
                ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            )
            sound: INPUT_COMPATIBLE_T
            seconds: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class stop(ThirdBlock):
            OPCODE: ClassVar = "&sound::stop sound ([SOUND])"
            INPUT_SPECS: ClassVar = (
                ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            )
            sound: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class playallsounds(ThirdBlock):
            OPCODE: ClassVar = "&sound::play all sounds"

        @grepr_dataclass()
        class stopallsounds(ThirdBlock):
            OPCODE: ClassVar = "&sound::stop all sounds"

        @grepr_dataclass()
        class set_stop_fadeout_to(ThirdBlock):
            OPCODE: ClassVar = "&sound::set fadeout to (SECONDS) seconds on ([SOUND])"
            INPUT_SPECS: ClassVar = (
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            )
            seconds: INPUT_COMPATIBLE_T
            sound: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_sound_playing(ThirdBlock):
            OPCODE: ClassVar = "&sound::is ([SOUND]) playing?"
            INPUT_SPECS: ClassVar = (
                ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            )
            sound: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_length(ThirdBlock):
            OPCODE: ClassVar = "&sound::length of ([SOUND])?"
            INPUT_SPECS: ClassVar = (
                ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            )
            sound: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class changeeffectby(ThirdBlock):
            OPCODE: ClassVar = "&sound::change [EFFECT] sound effect by (AMOUNT)"
            INPUT_SPECS: ClassVar = (
                ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
            amount: INPUT_COMPATIBLE_T
            effect: str

        @grepr_dataclass()
        class seteffectto(ThirdBlock):
            OPCODE: ClassVar = "&sound::set [EFFECT] sound effect to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
            value: INPUT_COMPATIBLE_T
            effect: str

        @grepr_dataclass()
        class cleareffects(ThirdBlock):
            OPCODE: ClassVar = "&sound::clear sound effects"

        @grepr_dataclass()
        class get_effect_value(ThirdBlock):
            OPCODE: ClassVar = "&sounds::[EFFECT] effect"
            DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
            effect: str

        @grepr_dataclass()
        class changevolumeby(ThirdBlock):
            OPCODE: ClassVar = "&sound::change volume by (AMOUNT)"
            INPUT_SPECS: ClassVar = (
                ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
            )
            amount: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class setvolumeto(ThirdBlock):
            OPCODE: ClassVar = "&sound::set volume to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class volume(ThirdBlock):
            OPCODE: ClassVar = "&sound::volume"

        @grepr_dataclass()
        class sounds_menu(ThirdBlock):
            OPCODE: ClassVar = "&sound::#SOUND MENU"

    class event:

        @grepr_dataclass()
        class whenflagclicked(ThirdBlock):
            OPCODE: ClassVar = "&events::when green flag clicked"

        @grepr_dataclass()
        class whenstopclicked(ThirdBlock):
            OPCODE: ClassVar = "&events::when stop clicked"

        @grepr_dataclass()
        class always(ThirdBlock):
            OPCODE: ClassVar = "&events::always"

        @grepr_dataclass()
        class whenanything(ThirdBlock):
            OPCODE: ClassVar = "&events::when <CONDITION>"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class whenkeypressed(ThirdBlock):
            OPCODE: ClassVar = "&events::when [KEY] key pressed"
            DROPDOWN_SPECS: ClassVar = (("KEY", "key"),)
            key: str

        @grepr_dataclass()
        class whenkeyhit(ThirdBlock):
            OPCODE: ClassVar = "&events::when [KEY] key hit"
            DROPDOWN_SPECS: ClassVar = (("KEY", "key"),)
            key: str

        @grepr_dataclass()
        class whenmousescrolled(ThirdBlock):
            OPCODE: ClassVar = "&events::when mouse is scrolled [DIRECTION]"
            DROPDOWN_SPECS: ClassVar = (("DIRECTION", "direction"),)
            direction: str

        @grepr_dataclass()
        class whenthisspriteclicked(ThirdBlock):
            OPCODE: ClassVar = "&events::when this sprite clicked"

        @grepr_dataclass()
        class whenstageclicked(ThirdBlock):
            OPCODE: ClassVar = "&events::when stage clicked"

        @grepr_dataclass()
        class whenbackdropswitchesto(ThirdBlock):
            OPCODE: ClassVar = "&events::when backdrop switches to [BACKDROP]"
            DROPDOWN_SPECS: ClassVar = (("BACKDROP", "backdrop"),)
            backdrop: str

        @grepr_dataclass()
        class whengreaterthan(ThirdBlock):
            OPCODE: ClassVar = "&events::when [OPTION] > (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("OPTION", "option"),)
            value: INPUT_COMPATIBLE_T
            option: str

        @grepr_dataclass()
        class whenbroadcastreceived(ThirdBlock):
            OPCODE: ClassVar = "&events::when I receive [MESSAGE]"
            DROPDOWN_SPECS: ClassVar = (("MESSAGE", "message"),)
            message: str

        @grepr_dataclass()
        class broadcast(ThirdBlock):
            OPCODE: ClassVar = "&events::broadcast ([MESSAGE])"
            INPUT_SPECS: ClassVar = (
                ("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),
            )
            message: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class broadcastandwait(ThirdBlock):
            OPCODE: ClassVar = "&events::broadcast ([MESSAGE]) and wait"
            INPUT_SPECS: ClassVar = (
                ("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),
            )
            message: INPUT_COMPATIBLE_T

    class control:

        @grepr_dataclass()
        class wait(ThirdBlock):
            OPCODE: ClassVar = "&control::wait (SECONDS) seconds"
            INPUT_SPECS: ClassVar = (
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            )
            seconds: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class waitsecondsoruntil(ThirdBlock):
            OPCODE: ClassVar = "&control::wait (SECONDS) seconds or until <CONDITION>"
            INPUT_SPECS: ClassVar = (
                ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            )
            seconds: INPUT_COMPATIBLE_T
            condition: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class repeat(ThirdBlock):
            OPCODE: ClassVar = "&control::repeat (TIMES) {BODY}"
            INPUT_SPECS: ClassVar = (
                ("TIMES", "times", p.SRBlockAndTextInputValue, None),
                ("BODY", "body", p.SRScriptInputValue, None),
            )
            times: INPUT_COMPATIBLE_T
            body: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class forever(ThirdBlock):
            OPCODE: ClassVar = "&control::forever {BODY}"
            INPUT_SPECS: ClassVar = (("BODY", "body", p.SRScriptInputValue, None),)
            body: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class for_each(ThirdBlock):
            OPCODE: ClassVar = "&control::for each [VARIABLE] in (RANGE) {BODY}"
            INPUT_SPECS: ClassVar = (
                ("RANGE", "range", p.SRBlockAndTextInputValue, None),
                ("BODY", "body", p.SRScriptInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
            range: INPUT_COMPATIBLE_T
            body: INPUT_COMPATIBLE_T
            variable: str

        @grepr_dataclass()
        class exit_loop(ThirdBlock):
            OPCODE: ClassVar = "&control::escape loop"

        @grepr_dataclass()
        class continue_loop(ThirdBlock):
            OPCODE: ClassVar = "&control::continue loop"

        @grepr_dataclass()
        class switch(ThirdBlock):
            OPCODE: ClassVar = "&control::switch (CONDITION) {CASES}"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
                ("CASES", "cases", p.SRScriptInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            cases: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class switch_default(ThirdBlock):
            OPCODE: ClassVar = "&control::switch (CONDITION) {CASES} default {DEFAULT}"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockOnlyInputValue, None),
                ("CASES", "cases", p.SRScriptInputValue, None),
                ("DEFAULT", "default", p.SRScriptInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            cases: INPUT_COMPATIBLE_T
            default: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class exit_case(ThirdBlock):
            OPCODE: ClassVar = "&control::exit case"

        @grepr_dataclass()
        class case_next(ThirdBlock):
            OPCODE: ClassVar = "&control::run next case when (CONDITION)"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndTextInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class case(ThirdBlock):
            OPCODE: ClassVar = "&control::case (CONDITION) {BODY}"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndTextInputValue, None),
                ("BODY", "body", p.SRScriptInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            body: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class if_(ThirdBlock):
            OPCODE: ClassVar = "&control::if <CONDITION> then {THEN}"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ("THEN", "then", p.SRScriptInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            then: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class if_else(ThirdBlock):
            OPCODE: ClassVar = "&control::if <CONDITION> then {THEN} else {ELSE}"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ("THEN", "then", p.SRScriptInputValue, None),
                ("ELSE", "else_", p.SRScriptInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            then: INPUT_COMPATIBLE_T
            else_: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class if_return_else_return(ThirdBlock):
            OPCODE: ClassVar = (
                "&control::if <CONDITION> then (TRUEVALUE) else (FALSEVALUE)"
            )
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ("TRUEVALUE", "truevalue", p.SRBlockAndTextInputValue, None),
                ("FALSEVALUE", "falsevalue", p.SRBlockAndTextInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            truevalue: INPUT_COMPATIBLE_T
            falsevalue: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class wait_until(ThirdBlock):
            OPCODE: ClassVar = "&control::wait until <CONDITION>"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class repeat_until(ThirdBlock):
            OPCODE: ClassVar = "&control::repeat until <CONDITION> {BODY}"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ("BODY", "body", p.SRScriptInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            body: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class while_(ThirdBlock):
            OPCODE: ClassVar = "&control::while <CONDITION> {BODY}"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ("BODY", "body", p.SRScriptInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            body: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class all_at_once(ThirdBlock):
            OPCODE: ClassVar = "&control::all at once {BODY}"
            INPUT_SPECS: ClassVar = (("BODY", "body", p.SRScriptInputValue, None),)
            body: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class run_as_sprite(ThirdBlock):
            OPCODE: ClassVar = "&control::as ([TARGET]) {BODY}"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
                ("BODY", "body", p.SRScriptInputValue, None),
            )
            target: INPUT_COMPATIBLE_T
            body: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class try_catch(ThirdBlock):
            OPCODE: ClassVar = "&control::try to do {TRY} if a block errors {IFERROR}"
            INPUT_SPECS: ClassVar = (
                ("TRY", "try_", p.SRScriptInputValue, None),
                ("IFERROR", "iferror", p.SRScriptInputValue, None),
            )
            try_: INPUT_COMPATIBLE_T
            iferror: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class throw_error(ThirdBlock):
            OPCODE: ClassVar = "&control::throw error (ERROR)"
            INPUT_SPECS: ClassVar = (
                ("ERROR", "error", p.SRBlockAndTextInputValue, None),
            )
            error: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class error(ThirdBlock):
            OPCODE: ClassVar = "&control::error"

        @grepr_dataclass()
        class back_to_green_flag(ThirdBlock):
            OPCODE: ClassVar = "&control::run flag"

        @grepr_dataclass()
        class stop_sprite(ThirdBlock):
            OPCODE: ClassVar = "&control::stop sprite ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class stop(ThirdBlock):
            OPCODE: ClassVar = "&control::stop script [TARGET]"
            DROPDOWN_SPECS: ClassVar = (("TARGET", "target"),)
            target: str

        @grepr_dataclass()
        class start_as_clone(ThirdBlock):
            OPCODE: ClassVar = "&control::when I start as a clone"

        @grepr_dataclass()
        class create_clone_of(ThirdBlock):
            OPCODE: ClassVar = "&control::create clone of ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete_clones_of(ThirdBlock):
            OPCODE: ClassVar = "&control::delete clones of ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete_this_clone(ThirdBlock):
            OPCODE: ClassVar = "&control::delete this clone"

        @grepr_dataclass()
        class is_clone(ThirdBlock):
            OPCODE: ClassVar = "&control::is clone?"

        @grepr_dataclass()
        class stop_sprite_menu(ThirdBlock):
            OPCODE: ClassVar = "&control::#STOP SPRITE MENU"

        @grepr_dataclass()
        class create_clone_of_menu(ThirdBlock):
            OPCODE: ClassVar = "&control::#CLONE TARGET MENU"

        @grepr_dataclass()
        class run_as_sprite_menu(ThirdBlock):
            OPCODE: ClassVar = "&control::#RUN AS SPRITE MENU"

        @grepr_dataclass()
        class expandable_if(ThirdBlock):
            OPCODE: ClassVar = "&control::{{EXPANDABLE IF-THEN-ELSE CHAIN}}"

        @grepr_dataclass()
        class repeat_for_seconds(ThirdBlock):
            OPCODE: ClassVar = "&control::repeat for (TIMES) seconds {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("TIMES", "times", p.SRBlockAndTextInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            times: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class inline_stack_output(ThirdBlock):
            OPCODE: ClassVar = "&control::inline block {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class waittick(ThirdBlock):
            OPCODE: ClassVar = "&control::wait until next tick"

        @grepr_dataclass()
        class get_counter(ThirdBlock):
            OPCODE: ClassVar = "&control::counter"

        @grepr_dataclass()
        class incr_counter(ThirdBlock):
            OPCODE: ClassVar = "&control::increment counter"

        @grepr_dataclass()
        class decr_counter(ThirdBlock):
            OPCODE: ClassVar = "&control::decrement counter"

        @grepr_dataclass()
        class set_counter(ThirdBlock):
            OPCODE: ClassVar = "&control::set counter to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class clear_counter(ThirdBlock):
            OPCODE: ClassVar = "&control::clear counter"

    class sensing:

        @grepr_dataclass()
        class touchingobject(ThirdBlock):
            OPCODE: ClassVar = "&sensing::touching ([OBJECT]) ?"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
            )
            object: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class objecttouchingobject(ThirdBlock):
            OPCODE: ClassVar = "&sensing::([OBJECT]) touching ([SPRITE]) ?"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
                ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            sprite: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class objecttouchingclonesprite(ThirdBlock):
            OPCODE: ClassVar = "&sensing::([OBJECT]) touching clone of ([SPRITE]) ?"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
                ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            sprite: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class touchingcolor(ThirdBlock):
            OPCODE: ClassVar = "&sensing::touching color (COLOR) ?"
            INPUT_SPECS: ClassVar = (
                ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            )
            color: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class coloristouchingcolor(ThirdBlock):
            OPCODE: ClassVar = "&sensing::color (COLOR1) is touching color (COLOR2) ?"
            INPUT_SPECS: ClassVar = (
                ("COLOR1", "color1", p.SRBlockAndTextInputValue, None),
                ("COLOR2", "color2", p.SRBlockAndTextInputValue, None),
            )
            color1: INPUT_COMPATIBLE_T
            color2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class getxyoftouchingsprite(ThirdBlock):
            OPCODE: ClassVar = "&sensing::[COORDINATE] of touching ([OBJECT]) point"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("COORDINATE", "coordinate"),)
            object: INPUT_COMPATIBLE_T
            coordinate: str

        @grepr_dataclass()
        class distanceto(ThirdBlock):
            OPCODE: ClassVar = "&sensing::distance to ([OBJECT])"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
            )
            object: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class distance_to(ThirdBlock):
            OPCODE: ClassVar = "&sensing::distance from (X1) (Y1) to (X2) (Y2)"
            INPUT_SPECS: ClassVar = (
                ("X1", "x1", p.SRBlockAndTextInputValue, None),
                ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                ("X2", "x2", p.SRBlockAndTextInputValue, None),
                ("Y2", "y2", p.SRBlockAndTextInputValue, None),
            )
            x1: INPUT_COMPATIBLE_T
            y1: INPUT_COMPATIBLE_T
            x2: INPUT_COMPATIBLE_T
            y2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class direction_to(ThirdBlock):
            OPCODE: ClassVar = "&sensing::direction to (X1) (Y1) from (X2) (Y2)"
            INPUT_SPECS: ClassVar = (
                ("X1", "x1", p.SRBlockAndTextInputValue, None),
                ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                ("X2", "x2", p.SRBlockAndTextInputValue, None),
                ("Y2", "y2", p.SRBlockAndTextInputValue, None),
            )
            x1: INPUT_COMPATIBLE_T
            y1: INPUT_COMPATIBLE_T
            x2: INPUT_COMPATIBLE_T
            y2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class askandwait(ThirdBlock):
            OPCODE: ClassVar = "&sensing::ask (QUESTION) and wait"
            INPUT_SPECS: ClassVar = (
                ("QUESTION", "question", p.SRBlockAndTextInputValue, None),
            )
            question: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class answer(ThirdBlock):
            OPCODE: ClassVar = "&sensing::answer"

        @grepr_dataclass()
        class thing_is_text(ThirdBlock):
            OPCODE: ClassVar = "&sensing::(STRING) is text?"
            INPUT_SPECS: ClassVar = (
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class thing_is_number(ThirdBlock):
            OPCODE: ClassVar = "&sensing::(STRING) is number?"
            INPUT_SPECS: ClassVar = (
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class keypressed(ThirdBlock):
            OPCODE: ClassVar = "&sensing::key ([KEY]) pressed?"
            INPUT_SPECS: ClassVar = (
                ("KEY", "key", p.SRBlockAndDropdownInputValue, None),
            )
            key: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class keyhit(ThirdBlock):
            OPCODE: ClassVar = "&sensing::key ([KEY]) hit?"
            INPUT_SPECS: ClassVar = (
                ("KEY", "key", p.SRBlockAndDropdownInputValue, None),
            )
            key: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class mousescrolling(ThirdBlock):
            OPCODE: ClassVar = "&sensing::is mouse scrolling ([DIRECTION]) ?"
            INPUT_SPECS: ClassVar = (
                ("DIRECTION", "direction", p.SRBlockAndDropdownInputValue, None),
            )
            direction: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class mousedown(ThirdBlock):
            OPCODE: ClassVar = "&sensing::mouse down?"

        @grepr_dataclass()
        class mouseclicked(ThirdBlock):
            OPCODE: ClassVar = "&sensing::mouse clicked?"

        @grepr_dataclass()
        class mousex(ThirdBlock):
            OPCODE: ClassVar = "&sensing::mouse x"

        @grepr_dataclass()
        class mousey(ThirdBlock):
            OPCODE: ClassVar = "&sensing::mouse y"

        @grepr_dataclass()
        class setclipboard(ThirdBlock):
            OPCODE: ClassVar = "&sensing::add (TEXT) to clipboard"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class getclipboard(ThirdBlock):
            OPCODE: ClassVar = "&sensing::clipboard item"

        @grepr_dataclass()
        class setdragmode(ThirdBlock):
            OPCODE: ClassVar = "&sensing::set drag mode [MODE]"
            DROPDOWN_SPECS: ClassVar = (("MODE", "mode"),)
            mode: str

        @grepr_dataclass()
        class getdragmode(ThirdBlock):
            OPCODE: ClassVar = "&sensing::draggable?"

        @grepr_dataclass()
        class loudness(ThirdBlock):
            OPCODE: ClassVar = "&sensing::loudness"

        @grepr_dataclass()
        class loud(ThirdBlock):
            OPCODE: ClassVar = "&sensing::loud?"

        @grepr_dataclass()
        class resettimer(ThirdBlock):
            OPCODE: ClassVar = "&sensing::reset timer"

        @grepr_dataclass()
        class timer(ThirdBlock):
            OPCODE: ClassVar = "&sensing::timer"

        @grepr_dataclass()
        class set_of(ThirdBlock):
            OPCODE: ClassVar = "&sensing::set [PROPERTY] of ([TARGET]) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
            value: INPUT_COMPATIBLE_T
            target: INPUT_COMPATIBLE_T
            property: str

        @grepr_dataclass()
        class of(ThirdBlock):
            OPCODE: ClassVar = "&sensing::[PROPERTY] of ([TARGET])"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
            target: INPUT_COMPATIBLE_T
            property: str

        @grepr_dataclass()
        class current(ThirdBlock):
            OPCODE: ClassVar = "&sensing::current [PROPERTY]"
            DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
            property: str

        @grepr_dataclass()
        class dayssince2000(ThirdBlock):
            OPCODE: ClassVar = "&sensing::days since 2000"

        @grepr_dataclass()
        class mobile(ThirdBlock):
            OPCODE: ClassVar = "&sensing::mobile?"

        @grepr_dataclass()
        class fingerdown(ThirdBlock):
            OPCODE: ClassVar = "&sensing::finger ([INDEX]) down?"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndDropdownInputValue, None),
            )
            index: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class fingertapped(ThirdBlock):
            OPCODE: ClassVar = "&sensing::finger ([INDEX]) tapped?"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndDropdownInputValue, None),
            )
            index: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class fingerx(ThirdBlock):
            OPCODE: ClassVar = "&sensing::finger ([INDEX]) x"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndDropdownInputValue, None),
            )
            index: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class fingery(ThirdBlock):
            OPCODE: ClassVar = "&sensing::finger ([INDEX]) y"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndDropdownInputValue, None),
            )
            index: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class username(ThirdBlock):
            OPCODE: ClassVar = "&sensing::username"

        @grepr_dataclass()
        class loggedin(ThirdBlock):
            OPCODE: ClassVar = "&sensing::logged in?"

        @grepr_dataclass()
        class touchingobjectmenu(ThirdBlock):
            OPCODE: ClassVar = "&sensing::#TOUCHING OBJECT MENU"

        @grepr_dataclass()
        class fulltouchingobjectmenu(ThirdBlock):
            OPCODE: ClassVar = "&sensing::#FULL TOUCHING OBJECT MENU"

        @grepr_dataclass()
        class touchingobjectmenusprites(ThirdBlock):
            OPCODE: ClassVar = "&sensing::#TOUCHING OBJECT MENU SPRITES"

        @grepr_dataclass()
        class distancetomenu(ThirdBlock):
            OPCODE: ClassVar = "&sensing::#DISTANCE TO MENU"

        @grepr_dataclass()
        class keyoptions(ThirdBlock):
            OPCODE: ClassVar = "&sensing::#KEY MENU"

        @grepr_dataclass()
        class scrolldirections(ThirdBlock):
            OPCODE: ClassVar = "&sensing::#SCROLL DIRECTION MENU"

        @grepr_dataclass()
        class of_object_menu(ThirdBlock):
            OPCODE: ClassVar = "&sensing::#OJBECT PROPERTY MENU"

        @grepr_dataclass()
        class fingeroptions(ThirdBlock):
            OPCODE: ClassVar = "&sensing::#FINGER INDEX MENU"

        @grepr_dataclass()
        class thing_has_number(ThirdBlock):
            OPCODE: ClassVar = "&sensing::(TEXT1) has number?"
            INPUT_SPECS: ClassVar = (
                ("TEXT1", "text1", p.SRBlockAndTextInputValue, None),
            )
            text1: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_upper_case(ThirdBlock):
            OPCODE: ClassVar = "&sensing::is character (text) uppercase?"
            INPUT_SPECS: ClassVar = (
                ("text", "text", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class regextest(ThirdBlock):
            OPCODE: ClassVar = "&sensing::test regex (reg) (regrule) with text (text)"
            INPUT_SPECS: ClassVar = (
                ("text", "text", p.SRBlockAndTextInputValue, None),
                ("reg", "reg", p.SRBlockAndTextInputValue, None),
                ("regrule", "regrule", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            reg: INPUT_COMPATIBLE_T
            regrule: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class getspritewithattrib(ThirdBlock):
            OPCODE: ClassVar = "&sensing::get sprite with (var) set to (val)"
            INPUT_SPECS: ClassVar = (
                ("var", "var", p.SRBlockAndTextInputValue, None),
                ("val", "val", p.SRBlockAndTextInputValue, None),
            )
            var: INPUT_COMPATIBLE_T
            val: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class getoperatingsystem(ThirdBlock):
            OPCODE: ClassVar = "&sensing::operating system"

        @grepr_dataclass()
        class getbrowser(ThirdBlock):
            OPCODE: ClassVar = "&sensing::browser"

        @grepr_dataclass()
        class geturl(ThirdBlock):
            OPCODE: ClassVar = "&sensing::url"

    class operator:

        @grepr_dataclass()
        class add(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) + (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class subtract(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) - (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class multiply(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) * (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class divide(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) / (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class power(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) ^ (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class adv_math_expanded(ThirdBlock):
            OPCODE: ClassVar = (
                "&operators::(OPERAND1) * (OPERAND2) [OPERATION] (OPERAND3)"
            )
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
                ("OPERAND3", "operand3", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("OPERATION", "operation"),)
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T
            operand3: INPUT_COMPATIBLE_T
            operation: str

        @grepr_dataclass()
        class adv_math(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) [OPERATION] (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("OPERATION", "operation"),)
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T
            operation: str

        @grepr_dataclass()
        class random(ThirdBlock):
            OPCODE: ClassVar = "&operators::pick random (OPERAND1) to (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class constrainnumber(ThirdBlock):
            OPCODE: ClassVar = "&operators::constrain (NUM) min (MIN) max (MAX)"
            INPUT_SPECS: ClassVar = (
                ("NUM", "num", p.SRBlockAndTextInputValue, None),
                ("MIN", "min", p.SRBlockAndTextInputValue, None),
                ("MAX", "max", p.SRBlockAndTextInputValue, None),
            )
            num: INPUT_COMPATIBLE_T
            min: INPUT_COMPATIBLE_T
            max: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class lerp_func(ThirdBlock):
            OPCODE: ClassVar = (
                "&operators::interpolate (OPERAND1) to (OPERAND2) by (WEIGHT)"
            )
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
                ("WEIGHT", "weight", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T
            weight: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class gt(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) > (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class gtorequal(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) >= (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class lt(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) < (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class ltorequal(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) <= (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class equals(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) = (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class notequal(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) != (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class true_boolean(ThirdBlock):
            OPCODE: ClassVar = "&operators::true"

        @grepr_dataclass()
        class false_boolean(ThirdBlock):
            OPCODE: ClassVar = "&operators::false"

        @grepr_dataclass()
        class and_(ThirdBlock):
            OPCODE: ClassVar = "&operators::<OPERAND1> and <OPERAND2>"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class or_(ThirdBlock):
            OPCODE: ClassVar = "&operators::<OPERAND1> or <OPERAND2>"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class not_(ThirdBlock):
            OPCODE: ClassVar = "&operators::not <OPERAND>"
            INPUT_SPECS: ClassVar = (
                ("OPERAND", "operand", p.SRBlockAndBoolInputValue, None),
            )
            operand: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class new_line(ThirdBlock):
            OPCODE: ClassVar = "&operators::new line"

        @grepr_dataclass()
        class tab_character(ThirdBlock):
            OPCODE: ClassVar = "&operators::tab character"

        @grepr_dataclass()
        class join(ThirdBlock):
            OPCODE: ClassVar = "&operators::join (STRING1) (STRING2)"
            INPUT_SPECS: ClassVar = (
                ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            )
            string1: INPUT_COMPATIBLE_T
            string2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class join3(ThirdBlock):
            OPCODE: ClassVar = "&operators::join (STRING1) (STRING2) (STRING3)"
            INPUT_SPECS: ClassVar = (
                ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
            )
            string1: INPUT_COMPATIBLE_T
            string2: INPUT_COMPATIBLE_T
            string3: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class index_of_text_in_text(ThirdBlock):
            OPCODE: ClassVar = "&operators::index of (SUBSTRING) in (TEXT)"
            INPUT_SPECS: ClassVar = (
                ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            substring: INPUT_COMPATIBLE_T
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class last_index_of_text_in_text(ThirdBlock):
            OPCODE: ClassVar = "&operators::last index of (SUBSTRING) in (TEXT)"
            INPUT_SPECS: ClassVar = (
                ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            substring: INPUT_COMPATIBLE_T
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class letter_of(ThirdBlock):
            OPCODE: ClassVar = "&operators::letter (LETTER) of (STRING)"
            INPUT_SPECS: ClassVar = (
                ("LETTER", "letter", p.SRBlockAndTextInputValue, None),
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            letter: INPUT_COMPATIBLE_T
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_letters_from_index_to_index_in_text(ThirdBlock):
            OPCODE: ClassVar = "&operators::letters from (START) to (STOP) in (TEXT)"
            INPUT_SPECS: ClassVar = (
                ("START", "start", p.SRBlockAndTextInputValue, None),
                ("STOP", "stop", p.SRBlockAndTextInputValue, None),
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            start: INPUT_COMPATIBLE_T
            stop: INPUT_COMPATIBLE_T
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class length(ThirdBlock):
            OPCODE: ClassVar = "&operators::length of (TEXT)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class contains(ThirdBlock):
            OPCODE: ClassVar = "&operators::(TEXT) contains (SUBSTRING) ?"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            substring: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class text_starts_or_ends_with(ThirdBlock):
            OPCODE: ClassVar = "&operators::(TEXT) [OPERATION] with (SUBSTRING) ?"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("OPERATION", "operation"),)
            text: INPUT_COMPATIBLE_T
            substring: INPUT_COMPATIBLE_T
            operation: str

        @grepr_dataclass()
        class replace_all(ThirdBlock):
            OPCODE: ClassVar = (
                "&operators::in (TEXT) replace all (OLDVALUE) with (NEWVALUE)"
            )
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("OLDVALUE", "oldvalue", p.SRBlockAndTextInputValue, None),
                ("NEWVALUE", "newvalue", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            oldvalue: INPUT_COMPATIBLE_T
            newvalue: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class replace_first(ThirdBlock):
            OPCODE: ClassVar = (
                "&operators::in (TEXT) replace first (OLDVALUE) with (NEWVALUE)"
            )
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("OLDVALUE", "oldvalue", p.SRBlockAndTextInputValue, None),
                ("NEWVALUE", "newvalue", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            oldvalue: INPUT_COMPATIBLE_T
            newvalue: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class regexmatch(ThirdBlock):
            OPCODE: ClassVar = "&operators::match (TEXT) with regex (REGEX) (MODIFIER)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("REGEX", "regex", p.SRBlockAndTextInputValue, None),
                ("MODIFIER", "modifier", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            regex: INPUT_COMPATIBLE_T
            modifier: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_upper_lower_case(ThirdBlock):
            OPCODE: ClassVar = "&operators::(TEXT) to [CASE]"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("CASE", "case"),)
            text: INPUT_COMPATIBLE_T
            case: str

        @grepr_dataclass()
        class mod(ThirdBlock):
            OPCODE: ClassVar = "&operators::(OPERAND1) mod (OPERAND2)"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class round(ThirdBlock):
            OPCODE: ClassVar = "&operators::round (NUM)"
            INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
            num: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class mathop(ThirdBlock):
            OPCODE: ClassVar = "&operators::[OPERATION] of (NUM)"
            INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
            DROPDOWN_SPECS: ClassVar = (("OPERATION", "operation"),)
            num: INPUT_COMPATIBLE_T
            operation: str

        @grepr_dataclass()
        class stringify(ThirdBlock):
            OPCODE: ClassVar = "&operators::(VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class boolify(ThirdBlock):
            OPCODE: ClassVar = "&operators::(VALUE) as a boolean"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class expandable_math(ThirdBlock):
            OPCODE: ClassVar = "&operators::{{EXPANDABLE MATH CHAIN}}"

        @grepr_dataclass()
        class expandable_bool(ThirdBlock):
            OPCODE: ClassVar = "&operators::{{EXPANDABLE BOOL CHAIN}}"

        @grepr_dataclass()
        class expandable_compare(ThirdBlock):
            OPCODE: ClassVar = "&operators::{{EXPANDABLE COMPARE CHAIN}}"

        @grepr_dataclass()
        class expandablejoininputs(ThirdBlock):
            OPCODE: ClassVar = "&operators::{{EXPANDABLE JOIN CHAIN}}"

        @grepr_dataclass()
        class nand(ThirdBlock):
            OPCODE: ClassVar = "&operator::<OPERAND1> nand <OPERAND2>"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class nor(ThirdBlock):
            OPCODE: ClassVar = "&operator::<OPERAND1> nor <OPERAND2>"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class xor(ThirdBlock):
            OPCODE: ClassVar = "&operator::<OPERAND1> xor <OPERAND2>"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class xnor(ThirdBlock):
            OPCODE: ClassVar = "&operator::<OPERAND1> xnor <OPERAND2>"
            INPUT_SPECS: ClassVar = (
                ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
                ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
            )
            operand1: INPUT_COMPATIBLE_T
            operand2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class random_boolean(ThirdBlock):
            OPCODE: ClassVar = "&operator::random"

        @grepr_dataclass()
        class count_appear_times(ThirdBlock):
            OPCODE: ClassVar = "&operator::amount of times (TEXT1) appears in (TEXT2)"
            INPUT_SPECS: ClassVar = (
                ("TEXT1", "text1", p.SRBlockAndTextInputValue, None),
                ("TEXT2", "text2", p.SRBlockAndTextInputValue, None),
            )
            text1: INPUT_COMPATIBLE_T
            text2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class read_line_in_multiline_text(ThirdBlock):
            OPCODE: ClassVar = "&operator::read line (LINE) in (TEXT)"
            INPUT_SPECS: ClassVar = (
                ("LINE", "line", p.SRBlockAndTextInputValue, None),
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            line: INPUT_COMPATIBLE_T
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class text_includes_letter_from(ThirdBlock):
            OPCODE: ClassVar = "&operator::(TEXT1) includes a letter from (TEXT2) ?"
            INPUT_SPECS: ClassVar = (
                ("TEXT1", "text1", p.SRBlockAndTextInputValue, None),
                ("TEXT2", "text2", p.SRBlockAndTextInputValue, None),
            )
            text1: INPUT_COMPATIBLE_T
            text2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class character_to_code(ThirdBlock):
            OPCODE: ClassVar = "&operator::character (ONE) to id"
            INPUT_SPECS: ClassVar = (("ONE", "one", p.SRBlockAndTextInputValue, None),)
            one: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class code_to_character(ThirdBlock):
            OPCODE: ClassVar = "&operator::id (ONE) to character"
            INPUT_SPECS: ClassVar = (("ONE", "one", p.SRBlockAndTextInputValue, None),)
            one: INPUT_COMPATIBLE_T

    class data:

        @grepr_dataclass()
        class setvariableto(ThirdBlock):
            OPCODE: ClassVar = "&variables::set [VARIABLE] to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
            value: INPUT_COMPATIBLE_T
            variable: str

        @grepr_dataclass()
        class changevariableby(ThirdBlock):
            OPCODE: ClassVar = "&variables::change [VARIABLE] by (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
            value: INPUT_COMPATIBLE_T
            variable: str

        @grepr_dataclass()
        class showvariable(ThirdBlock):
            OPCODE: ClassVar = "&variables::show variable [VARIABLE]"
            DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
            variable: str

        @grepr_dataclass()
        class hidevariable(ThirdBlock):
            OPCODE: ClassVar = "&variables::hide variable [VARIABLE]"
            DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
            variable: str

        @grepr_dataclass()
        class variable(ThirdBlock):
            OPCODE: ClassVar = "&variables::value of [VARIABLE]"
            DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
            variable: str

        @grepr_dataclass()
        class addtolist(ThirdBlock):
            OPCODE: ClassVar = "&lists::add (ITEM) to [LIST]"
            INPUT_SPECS: ClassVar = (
                ("ITEM", "item", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            item: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class deleteoflist(ThirdBlock):
            OPCODE: ClassVar = "&lists::delete (INDEX) of [LIST]"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            index: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class deletealloflist(ThirdBlock):
            OPCODE: ClassVar = "&lists::delete all of [LIST]"
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            list: str

        @grepr_dataclass()
        class shiftlist(ThirdBlock):
            OPCODE: ClassVar = "&lists::shift [LIST] by (INDEX)"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            index: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class insertatlist(ThirdBlock):
            OPCODE: ClassVar = "&lists::insert (ITEM) at (INDEX) of [LIST]"
            INPUT_SPECS: ClassVar = (
                ("ITEM", "item", p.SRBlockAndTextInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            item: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class replaceitemoflist(ThirdBlock):
            OPCODE: ClassVar = "&lists::replace item (INDEX) of [LIST] with (ITEM)"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ("ITEM", "item", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            index: INPUT_COMPATIBLE_T
            item: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class listforeachitem(ThirdBlock):
            OPCODE: ClassVar = "&lists::For each item [VARIABLE] in [LIST] {BODY}"
            INPUT_SPECS: ClassVar = (("BODY", "body", p.SRScriptInputValue, None),)
            DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"), ("LIST", "list"))
            body: INPUT_COMPATIBLE_T
            variable: str
            list: str

        @grepr_dataclass()
        class listforeachnum(ThirdBlock):
            OPCODE: ClassVar = "&lists::For each item # [VARIABLE] in [LIST] {BODY}}"
            INPUT_SPECS: ClassVar = (("BODY", "body", p.SRScriptInputValue, None),)
            DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"), ("LIST", "list"))
            body: INPUT_COMPATIBLE_T
            variable: str
            list: str

        @grepr_dataclass()
        class itemoflist(ThirdBlock):
            OPCODE: ClassVar = "&lists::item (INDEX) of [LIST]"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            index: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class itemnumoflist(ThirdBlock):
            OPCODE: ClassVar = "&lists::item # of (ITEM) in [LIST]"
            INPUT_SPECS: ClassVar = (
                ("ITEM", "item", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            item: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class amountinlist(ThirdBlock):
            OPCODE: ClassVar = "&lists::amount of (VALUE) of [LIST]"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            value: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class lengthoflist(ThirdBlock):
            OPCODE: ClassVar = "&lists::length of [LIST]"
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            list: str

        @grepr_dataclass()
        class listcontainsitem(ThirdBlock):
            OPCODE: ClassVar = "&lists::[LIST] contains (ITEM) ?"
            INPUT_SPECS: ClassVar = (
                ("ITEM", "item", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            item: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class itemexistslist(ThirdBlock):
            OPCODE: ClassVar = "&lists::item (INDEX) exists in [LIST] ?"
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            index: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class listisempty(ThirdBlock):
            OPCODE: ClassVar = "&lists::is [LIST] empty?"
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            list: str

        @grepr_dataclass()
        class reverselist(ThirdBlock):
            OPCODE: ClassVar = "&lists::reverse [LIST]"
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            list: str

        @grepr_dataclass()
        class filterlist(ThirdBlock):
            OPCODE: ClassVar = "&lists::filter [LIST] by (INDEX) (ITEM) <KEEP>"
            INPUT_SPECS: ClassVar = (
                (
                    "INDEX",
                    "index",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.data.filterlistindex(),
                ),
                (
                    "ITEM",
                    "item",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.data.filterlistitem(),
                ),
                ("KEEP", "keep", p.SRBlockAndBoolInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            keep: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class arraylist(ThirdBlock):
            OPCODE: ClassVar = "&lists::set [LIST] to array (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            value: INPUT_COMPATIBLE_T
            list: str

        @grepr_dataclass()
        class listarray(ThirdBlock):
            OPCODE: ClassVar = "&lists::get list [LIST] as an array"
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            list: str

        @grepr_dataclass()
        class showlist(ThirdBlock):
            OPCODE: ClassVar = "&lists::show list [LIST]"
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            list: str

        @grepr_dataclass()
        class hidelist(ThirdBlock):
            OPCODE: ClassVar = "&lists::hide list [LIST]"
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            list: str

        @grepr_dataclass()
        class listcontents(ThirdBlock):
            OPCODE: ClassVar = "&variables::value of [LIST]"
            DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
            list: str

        @grepr_dataclass()
        class filterlistindex(ThirdBlock):
            OPCODE: ClassVar = "&lists::{{FILTER INDEX}}"

        @grepr_dataclass()
        class filterlistitem(ThirdBlock):
            OPCODE: ClassVar = "&lists::{{FILTER ITEM}}"

    class procedures:

        @grepr_dataclass()
        class definition(ThirdBlock):
            OPCODE: ClassVar = "&customblocks::define custom block"

        @grepr_dataclass()
        class definition_return(ThirdBlock):
            OPCODE: ClassVar = "&customblocks::define custom block reporter"

        @grepr_dataclass()
        class prototype(ThirdBlock):
            OPCODE: ClassVar = "&customblocks::#CUSTOM BLOCK PROTOTYPE"

        @grepr_dataclass()
        class call(ThirdBlock):
            OPCODE: ClassVar = "&customblocks::call custom block"

        @grepr_dataclass()
        class return_(ThirdBlock):
            OPCODE: ClassVar = "&customblocks::return (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set(ThirdBlock):
            OPCODE: ClassVar = "&customblocks::set (PARAM) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("PARAM", "param", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            param: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

    class argument:

        @grepr_dataclass()
        class reporter_string_number(ThirdBlock):
            OPCODE: ClassVar = "&customblocks::custom block text arg [ARGUMENT]"

        @grepr_dataclass()
        class reporter_boolean(ThirdBlock):
            OPCODE: ClassVar = "&customblocks::custom block boolean arg [ARGUMENT]"

    class checkbox:
        pass

    class polygon:
        pass

    class note:
        pass

    class pmControlsExpansion:

        @grepr_dataclass()
        class as_new_broadcast(ThirdBlock):
            OPCODE: ClassVar = "&pmControlsExpansion::new thread {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class restart_from_the_top(ThirdBlock):
            OPCODE: ClassVar = "&pmControlsExpansion::restart from the top"

        @grepr_dataclass()
        class as_new_broadcast_args(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmControlsExpansion::new thread with data (DATA) {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("DATA", "data", p.SRBlockAndTextInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            data: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class as_new_broadcast_arg_block(ThirdBlock):
            OPCODE: ClassVar = "&pmControlsExpansion::thread data"

        @grepr_dataclass()
        class if_else_if(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2}"
            )
            INPUT_SPECS: ClassVar = (
                ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
                ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
            )
            condition1: INPUT_COMPATIBLE_T
            condition2: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T
            substack2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class if_else_if_else(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2} else {SUBSTACK3}"
            )
            INPUT_SPECS: ClassVar = (
                ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
                ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
                ("SUBSTACK3", "substack3", p.SRScriptInputValue, None),
            )
            condition1: INPUT_COMPATIBLE_T
            condition2: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T
            substack2: INPUT_COMPATIBLE_T
            substack3: INPUT_COMPATIBLE_T

    class pmEventsExpansion:

        @grepr_dataclass()
        class every_other_frame(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::every other frame"

        @grepr_dataclass()
        class neverr(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::never"

        @grepr_dataclass()
        class when_sprite_clicked(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::when [SPRITE] clicked"
            DROPDOWN_SPECS: ClassVar = (("SPRITE", "sprite"),)
            sprite: str

        @grepr_dataclass()
        class send_with_data(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmEventsExpansion::broadcast (BROADCAST) with data (DATA)"
            )
            INPUT_SPECS: ClassVar = (
                ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
                ("DATA", "data", p.SRBlockAndTextInputValue, None),
            )
            broadcast: INPUT_COMPATIBLE_T
            data: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class received_data(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmEventsExpansion::when I receive [BROADCAST] with data"
            )
            DROPDOWN_SPECS: ClassVar = (("BROADCAST", "broadcast"),)
            broadcast: str

        @grepr_dataclass()
        class is_broadcast_received(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::is message (BROADCAST) received?"
            INPUT_SPECS: ClassVar = (
                ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
            )
            broadcast: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class recieved_data_reporter(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::recieved data"

        @grepr_dataclass()
        class broadcast_to_sprite(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::broadcast (BROADCAST) to [SPRITE]"
            INPUT_SPECS: ClassVar = (
                ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("SPRITE", "sprite"),)
            broadcast: INPUT_COMPATIBLE_T
            sprite: str

        @grepr_dataclass()
        class broadcast_function(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::broadcast (BROADCAST) and wait"
            INPUT_SPECS: ClassVar = (
                ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
            )
            broadcast: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class return_from_broadcast_func(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::return (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class broadcast_thread_count(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmEventsExpansion::broadcast (BROADCAST) and get # of blocks started"
            )
            INPUT_SPECS: ClassVar = (
                ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
            )
            broadcast: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class broadcast_function_args(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmEventsExpansion::broadcast (BROADCAST) with data (ARGS) and wait"
            )
            INPUT_SPECS: ClassVar = (
                ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
                ("ARGS", "args", p.SRBlockAndTextInputValue, None),
            )
            broadcast: INPUT_COMPATIBLE_T
            args: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_sprite_name(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::#menu:spriteName"

        @grepr_dataclass()
        class menu_broadcast_menu(ThirdBlock):
            OPCODE: ClassVar = "&pmEventsExpansion::#menu:broadcastMenu"

    class pmMotionExpansion:

        @grepr_dataclass()
        class rotation_style(ThirdBlock):
            OPCODE: ClassVar = "&pmMotionExpansion::rotation style"

        @grepr_dataclass()
        class fence(ThirdBlock):
            OPCODE: ClassVar = "&pmMotionExpansion::manually fence"

        @grepr_dataclass()
        class steptowards(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmMotionExpansion::move (STEPS) steps towards x: (X) y: (Y)"
            )
            INPUT_SPECS: ClassVar = (
                ("STEPS", "steps", p.SRBlockAndTextInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            steps: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class tweentowards(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmMotionExpansion::move [PERCENT]% of the way to x: (X) y: (Y)"
            )
            INPUT_SPECS: ClassVar = (
                ("PERCENT", "percent", p.SRBlockAndTextInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            percent: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class touchingxy(ThirdBlock):
            OPCODE: ClassVar = "&pmMotionExpansion::touching x: (X) y: [Y]?"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class touchingrect(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmMotionExpansion::touching rectangle x1: (X1) y1: (Y1) x2: (X2) y2: [Y2]?"
            )
            INPUT_SPECS: ClassVar = (
                ("X1", "x1", p.SRBlockAndTextInputValue, None),
                ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                ("X2", "x2", p.SRBlockAndTextInputValue, None),
                ("Y2", "y2", p.SRBlockAndTextInputValue, None),
            )
            x1: INPUT_COMPATIBLE_T
            y1: INPUT_COMPATIBLE_T
            x2: INPUT_COMPATIBLE_T
            y2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_home(ThirdBlock):
            OPCODE: ClassVar = "&pmMotionExpansion::set my home"

        @grepr_dataclass()
        class goto_home(ThirdBlock):
            OPCODE: ClassVar = "&pmMotionExpansion::go to home"

    class pmOperatorsExpansion:

        @grepr_dataclass()
        class shift_left(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) << (num2)"
            INPUT_SPECS: ClassVar = (
                ("num1", "num1", p.SRBlockAndTextInputValue, None),
                ("num2", "num2", p.SRBlockAndTextInputValue, None),
            )
            num1: INPUT_COMPATIBLE_T
            num2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class shift_right(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) >> (num2)"
            INPUT_SPECS: ClassVar = (
                ("num1", "num1", p.SRBlockAndTextInputValue, None),
                ("num2", "num2", p.SRBlockAndTextInputValue, None),
            )
            num1: INPUT_COMPATIBLE_T
            num2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class binnary_and(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) & (num2)"
            INPUT_SPECS: ClassVar = (
                ("num1", "num1", p.SRBlockAndTextInputValue, None),
                ("num2", "num2", p.SRBlockAndTextInputValue, None),
            )
            num1: INPUT_COMPATIBLE_T
            num2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class binnary_or(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) | (num2)"
            INPUT_SPECS: ClassVar = (
                ("num1", "num1", p.SRBlockAndTextInputValue, None),
                ("num2", "num2", p.SRBlockAndTextInputValue, None),
            )
            num1: INPUT_COMPATIBLE_T
            num2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class binnary_xor(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) ^ (num2)"
            INPUT_SPECS: ClassVar = (
                ("num1", "num1", p.SRBlockAndTextInputValue, None),
                ("num2", "num2", p.SRBlockAndTextInputValue, None),
            )
            num1: INPUT_COMPATIBLE_T
            num2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class binnary_not(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::~ (num1)"
            INPUT_SPECS: ClassVar = (
                ("num1", "num1", p.SRBlockAndTextInputValue, None),
            )
            num1: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class or_if_falsey(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::(ONE) or else (TWO)"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockAndTextInputValue, None),
                ("TWO", "two", p.SRBlockAndTextInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class if_is_truthy(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::if <ONE> is true then (TWO)"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockAndBoolInputValue, None),
                ("TWO", "two", p.SRBlockAndTextInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_number_multiple_of(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) multiple of [MULTIPLE]?"
            INPUT_SPECS: ClassVar = (
                ("NUM", "num", p.SRBlockAndTextInputValue, None),
                ("MULTIPLE", "multiple", p.SRBlockAndTextInputValue, None),
            )
            num: INPUT_COMPATIBLE_T
            multiple: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_integer(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) an integer?"
            INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
            num: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_prime(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) a prime number?"
            INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
            num: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_even(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) even?"
            INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
            num: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class between_numbers(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmOperatorsExpansion::is (NUM) between (MIN) and [MAX]?"
            )
            INPUT_SPECS: ClassVar = (
                ("NUM", "num", p.SRBlockAndTextInputValue, None),
                ("MIN", "min", p.SRBlockAndTextInputValue, None),
                ("MAX", "max", p.SRBlockAndTextInputValue, None),
            )
            num: INPUT_COMPATIBLE_T
            min: INPUT_COMPATIBLE_T
            max: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class evaluate_math(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::answer to (EQUATION)"
            INPUT_SPECS: ClassVar = (
                ("EQUATION", "equation", p.SRBlockAndTextInputValue, None),
            )
            equation: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class part_of_ratio(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::([PART]) part of ratio (RATIO)"
            INPUT_SPECS: ClassVar = (
                ("PART", "part", p.SRBlockAndDropdownInputValue, None),
                ("RATIO", "ratio", p.SRBlockAndTextInputValue, None),
            )
            part: INPUT_COMPATIBLE_T
            ratio: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class simplify_ratio(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::simplify ratio (RATIO)"
            INPUT_SPECS: ClassVar = (
                ("RATIO", "ratio", p.SRBlockAndTextInputValue, None),
            )
            ratio: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class pi(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::π"

        @grepr_dataclass()
        class euler(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::e"

        @grepr_dataclass()
        class infinity(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::∞"

        @grepr_dataclass()
        class truncate_number(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::truncate number (NUM)"
            INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
            num: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class atan2(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::atan2 of x (X) y (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class reverse_chars(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::reverse (TEXT)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class shuffle_chars(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::shuffle (TEXT)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class text_after(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::text after (TEXT) in (BASE)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("BASE", "base", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            base: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class text_before(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::text before (TEXT) in (BASE)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("BASE", "base", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            base: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class exactly_equal(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::(ONE) exactly equals [TWO]?"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockAndTextInputValue, None),
                ("TWO", "two", p.SRBlockAndTextInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_replacer(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmOperatorsExpansion::set replacer (REPLACER) to (TEXT)"
            )
            INPUT_SPECS: ClassVar = (
                ("REPLACER", "replacer", p.SRBlockAndTextInputValue, None),
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            replacer: INPUT_COMPATIBLE_T
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class reset_replacers(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::reset replacers"

        @grepr_dataclass()
        class apply_replacers(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::apply replacers to (TEXT)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class speed_to_pitch(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::speed (SPEED) to pitch"
            INPUT_SPECS: ClassVar = (
                ("SPEED", "speed", p.SRBlockAndTextInputValue, None),
            )
            speed: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class pitch_to_speed(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::pitch (PITCH) to speed"
            INPUT_SPECS: ClassVar = (
                ("PITCH", "pitch", p.SRBlockAndTextInputValue, None),
            )
            pitch: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class join4(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4)"
            )
            INPUT_SPECS: ClassVar = (
                ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
            )
            string1: INPUT_COMPATIBLE_T
            string2: INPUT_COMPATIBLE_T
            string3: INPUT_COMPATIBLE_T
            string4: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class join5(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5)"
            )
            INPUT_SPECS: ClassVar = (
                ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
            )
            string1: INPUT_COMPATIBLE_T
            string2: INPUT_COMPATIBLE_T
            string3: INPUT_COMPATIBLE_T
            string4: INPUT_COMPATIBLE_T
            string5: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class join6(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6)"
            )
            INPUT_SPECS: ClassVar = (
                ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
            )
            string1: INPUT_COMPATIBLE_T
            string2: INPUT_COMPATIBLE_T
            string3: INPUT_COMPATIBLE_T
            string4: INPUT_COMPATIBLE_T
            string5: INPUT_COMPATIBLE_T
            string6: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class join7(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7)"
            )
            INPUT_SPECS: ClassVar = (
                ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
            )
            string1: INPUT_COMPATIBLE_T
            string2: INPUT_COMPATIBLE_T
            string3: INPUT_COMPATIBLE_T
            string4: INPUT_COMPATIBLE_T
            string5: INPUT_COMPATIBLE_T
            string6: INPUT_COMPATIBLE_T
            string7: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class join8(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8)"
            )
            INPUT_SPECS: ClassVar = (
                ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
                ("STRING8", "string8", p.SRBlockAndTextInputValue, None),
            )
            string1: INPUT_COMPATIBLE_T
            string2: INPUT_COMPATIBLE_T
            string3: INPUT_COMPATIBLE_T
            string4: INPUT_COMPATIBLE_T
            string5: INPUT_COMPATIBLE_T
            string6: INPUT_COMPATIBLE_T
            string7: INPUT_COMPATIBLE_T
            string8: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class join9(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8) (STRING9)"
            )
            INPUT_SPECS: ClassVar = (
                ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
                ("STRING8", "string8", p.SRBlockAndTextInputValue, None),
                ("STRING9", "string9", p.SRBlockAndTextInputValue, None),
            )
            string1: INPUT_COMPATIBLE_T
            string2: INPUT_COMPATIBLE_T
            string3: INPUT_COMPATIBLE_T
            string4: INPUT_COMPATIBLE_T
            string5: INPUT_COMPATIBLE_T
            string6: INPUT_COMPATIBLE_T
            string7: INPUT_COMPATIBLE_T
            string8: INPUT_COMPATIBLE_T
            string9: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_part(ThirdBlock):
            OPCODE: ClassVar = "&pmOperatorsExpansion::#menu:part"

    class pmSensingExpansion:

        @grepr_dataclass()
        class battery_percentage(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::battery percentage"

        @grepr_dataclass()
        class battery_charging(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::is device charging?"

        @grepr_dataclass()
        class vibrate_device(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::vibrate"

        @grepr_dataclass()
        class browser_language(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::preferred language"

        @grepr_dataclass()
        class url_options(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::url ([OPTIONS])"
            INPUT_SPECS: ClassVar = (
                ("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),
            )
            options: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class url_options_of(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::([OPTIONS]) of url (URL)"
            INPUT_SPECS: ClassVar = (
                ("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),
                ("URL", "url", p.SRBlockAndTextInputValue, None),
            )
            options: INPUT_COMPATIBLE_T
            url: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_username(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::set username to (NAME)"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_url_end(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::set url path to (PATH)"
            INPUT_SPECS: ClassVar = (
                ("PATH", "path", p.SRBlockAndTextInputValue, None),
            )
            path: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class query_param_of_url(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmSensingExpansion::query parameter (PARAM) of url (URL)"
            )
            INPUT_SPECS: ClassVar = (
                ("PARAM", "param", p.SRBlockAndTextInputValue, None),
                ("URL", "url", p.SRBlockAndTextInputValue, None),
            )
            param: INPUT_COMPATIBLE_T
            url: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class packaged(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::project packaged?"

        @grepr_dataclass()
        class sprite_name(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::sprite name"

        @grepr_dataclass()
        class framed(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::project in iframe?"

        @grepr_dataclass()
        class current_millisecond(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::current millisecond"

        @grepr_dataclass()
        class delta_time(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::delta time"

        @grepr_dataclass()
        class pick_color(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::grab color at x: (X) y: (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class max_sprite_layers(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::max sprite layers"

        @grepr_dataclass()
        class average_loudness(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::average loudness"

        @grepr_dataclass()
        class scrolling_distance(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::scrolling distance"

        @grepr_dataclass()
        class set_scrolling_distance(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::set scrolling distance to (AMOUNT)"
            INPUT_SPECS: ClassVar = (
                ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
            )
            amount: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class change_scrolling_distance_by(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmSensingExpansion::change scrolling distance by (AMOUNT)"
            )
            INPUT_SPECS: ClassVar = (
                ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
            )
            amount: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class current_key_pressed(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::current key pressed"

        @grepr_dataclass()
        class get_last_key_pressed(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::last key pressed"

        @grepr_dataclass()
        class get_button_is_down(ThirdBlock):
            OPCODE: ClassVar = (
                "&pmSensingExpansion::([MOUSE_BUTTON]) mouse button down?"
            )
            INPUT_SPECS: ClassVar = (
                ("MOUSE_BUTTON", "mouse_button", p.SRBlockAndDropdownInputValue, None),
            )
            mouse_button: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class changed(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::(ONE) changed?"
            INPUT_SPECS: ClassVar = (("ONE", "one", p.SRBlockOnlyInputValue, None),)
            one: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class amount_of_time_key_has_been_held(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::seconds since holding ([KEY])"
            INPUT_SPECS: ClassVar = (
                ("KEY", "key", p.SRBlockAndDropdownInputValue, None),
            )
            key: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_key(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::#menu:key"

        @grepr_dataclass()
        class menu_mouse_button(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::#menu:mouseButton"

        @grepr_dataclass()
        class menu_url_sections(ThirdBlock):
            OPCODE: ClassVar = "&pmSensingExpansion::#menu:urlSections"

    class gceOOP:

        @grepr_dataclass()
        class temp_block(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::temp block with (INSTANCE) end"
            INPUT_SPECS: ClassVar = (
                ("INSTANCE", "instance", p.SRBlockOnlyInputValue, None),
            )
            instance: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class temp_block2(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::temp command with (A) and (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockOnlyInputValue, None),
                ("B", "b", p.SRBlockOnlyInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_class_at(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.current_class(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_subclass_at(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.current_class(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            superclass: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_class_named(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.current_class(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_subclass_named(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.current_class(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            superclass: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class on_class(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.current_class(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            class_: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class current_class(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::current class"

        @grepr_dataclass()
        class is_subclass(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?"
            INPUT_SPECS: ClassVar = (
                ("SUBCLASS", "subclass", p.SRBlockAndTextInputValue, None),
                ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
            )
            subclass: INPUT_COMPATIBLE_T
            superclass: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_superclass(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::get superclass of (CLASS)"
            INPUT_SPECS: ClassVar = (
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            )
            class_: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_instance_method(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.self_value(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_special_method(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                (
                    "SPECIAL_METHOD",
                    "special_method",
                    p.SRBlockAndDropdownInputValue,
                    None,
                ),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.self_value(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            special_method: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class self_value(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::self"

        @grepr_dataclass()
        class call_super_method(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::call super method (NAME) with positional args (POSARGS)"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            posargs: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class call_super_init_method(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::call super init method with positional args (POSARGS)"
            )
            INPUT_SPECS: ClassVar = (
                ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
            )
            posargs: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_getter(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.self_value(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_setter(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                (
                    "SHADOW1",
                    "shadow1",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.self_value(),
                ),
                (
                    "SHADOW2",
                    "shadow2",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.define_setter_value(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_operator_method(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                (
                    "OPERATOR_KIND",
                    "operator_kind",
                    p.SRBlockAndDropdownInputValue,
                    None,
                ),
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.gceOOP.operator_operator_value(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            operator_kind: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class operator_operator_value(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"
            )

        @grepr_dataclass()
        class set_class_variable(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::on (CLASS) set class var (NAME) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            class_: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_class_variable(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::on (CLASS) get class var (NAME)"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            class_: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete_class_variable(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::on (CLASS) delete class var (NAME)"
            INPUT_SPECS: ClassVar = (
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            class_: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_static_method(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::define static method (NAME) {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class property_names_of_class(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::([PROPERTY]) names of class (CLASS)"
            INPUT_SPECS: ClassVar = (
                ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            )
            property: INPUT_COMPATIBLE_T
            class_: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_instance(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::create instance of class (CLASS) with positional args (POSARGS)"
            )
            INPUT_SPECS: ClassVar = (
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
            )
            class_: INPUT_COMPATIBLE_T
            posargs: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_instance(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?"
            )
            INPUT_SPECS: ClassVar = (
                (
                    "POTENTIAL_INSTANCE",
                    "potential_instance",
                    p.SRBlockAndTextInputValue,
                    None,
                ),
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            )
            potential_instance: INPUT_COMPATIBLE_T
            class_: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_class_of_instance(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::get class of (INSTANCE)"
            INPUT_SPECS: ClassVar = (
                ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
            )
            instance: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_attribute(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            instance: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_attribute(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::on (INSTANCE) get attribute (NAME)"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            instance: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_all_attributes(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::all attributes of (INSTANCE)"
            INPUT_SPECS: ClassVar = (
                ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
            )
            instance: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class call_method(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)"
            )
            INPUT_SPECS: ClassVar = (
                ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
            )
            instance: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T
            posargs: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class call_static_method(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)"
            )
            INPUT_SPECS: ClassVar = (
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
            )
            class_: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T
            posargs: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_static_method_func(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceOOP::get static method (NAME) of (CLASS) as function"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            class_: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_setter_value(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::operator value {{id=gceOOP_defineSetterValue}}"

        @grepr_dataclass()
        class menu_class_property(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::#menu:classProperty"

        @grepr_dataclass()
        class menu_operator_method(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::#menu:operatorMethod"

        @grepr_dataclass()
        class menu_special_method(ThirdBlock):
            OPCODE: ClassVar = "&gceOOP::#menu:specialMethod"

    class gceFuncsScopes:

        @grepr_dataclass()
        class set_scope_var(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceFuncsScopes::set var (NAME) to (VALUE) in current scope"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_scope_var(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::get var (NAME)"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class scope_var_exists(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::var (NAME) exists in [KIND]?"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            kind: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete_scope_var(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::delete var (NAME) in current scope"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class all_variables(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::all variables in ([KIND])"
            INPUT_SPECS: ClassVar = (
                ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
            )
            kind: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_var_scope(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::create local variable scope {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class run_with_separate_globals(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::run with separate globals {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class bind_var_to_scope(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceFuncsScopes::bind ([KIND]) variable (NAME) to current scope"
            )
            INPUT_SPECS: ClassVar = (
                ("KIND", "kind", p.SRBlockAndDropdownInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            kind: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class configure_next_function_args(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceFuncsScopes::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)"
            )
            INPUT_SPECS: ClassVar = (
                ("ARGNAMES", "argnames", p.SRBlockAndTextInputValue, None),
                ("ARGDEFAULTS", "argdefaults", p.SRBlockAndTextInputValue, None),
            )
            argnames: INPUT_COMPATIBLE_T
            argdefaults: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_function_at(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceFuncsScopes::create function at var (NAME) {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_function_named(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceFuncsScopes::create function named (NAME) {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class return_value(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::return (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class call_function(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceFuncsScopes::call function (FUNC) with positional args (POSARGS)"
            )
            INPUT_SPECS: ClassVar = (
                ("FUNC", "func", p.SRBlockAndTextInputValue, None),
                ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
            )
            func: INPUT_COMPATIBLE_T
            posargs: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class object_as_string(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::(VALUE) as string"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class typeof_value(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::typeof (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class typeof_value_is_menu(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::typeof (VALUE) is ([TYPE]) ?"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            )
            value: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class typeof_value_selection(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::([TYPE])"
            INPUT_SPECS: ClassVar = (
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            )
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class check_identity(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::(VALUE1) is (VALUE2) ?"
            INPUT_SPECS: ClassVar = (
                ("VALUE1", "value1", p.SRBlockAndTextInputValue, None),
                ("VALUE2", "value2", p.SRBlockAndTextInputValue, None),
            )
            value1: INPUT_COMPATIBLE_T
            value2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class nothing(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::Nothing"

        @grepr_dataclass()
        class execute_expression(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::execute expression (EXPR)"
            INPUT_SPECS: ClassVar = (
                ("EXPR", "expr", p.SRBlockAndTextInputValue, None),
            )
            expr: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_variable_available_kind(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::#menu:variableAvailableKind"

        @grepr_dataclass()
        class menu_bind_var_origin_kind(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::#menu:bindVarOriginKind"

        @grepr_dataclass()
        class menu_typeof_menu(ThirdBlock):
            OPCODE: ClassVar = "&gceFuncsScopes::#menu:typeofMenu"

    class gceTestRunner:

        @grepr_dataclass()
        class test_scope(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::test scope named (NAME) {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert <CONDITION>"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_not(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert not <CONDITION>"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_msg(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert <CONDITION> message (MSG)"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ("MSG", "msg", p.SRBlockAndTextInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            msg: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_not_msg(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert not <CONDITION> message (MSG)"
            INPUT_SPECS: ClassVar = (
                ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
                ("MSG", "msg", p.SRBlockAndTextInputValue, None),
            )
            condition: INPUT_COMPATIBLE_T
            msg: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_strict_equal(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert typed equality (A) = (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_strict_not_equal(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert typed inequality (A) != (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_unstrict_equal(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert string equality (A) = (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_unstrict_not_equal(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert string inequality (A) != (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_text_in_value(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert text (TEXT) in value (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_text_not_in_value(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert text (TEXT) not in value (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_type(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert type of (VALUE) is ([EXPECTED])"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("EXPECTED", "expected", p.SRBlockAndDropdownInputValue, None),
            )
            value: INPUT_COMPATIBLE_T
            expected: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_custom_id_type(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceTestRunner::assert custom id of (VALUE) is (EXPECTED)"
            )
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("EXPECTED", "expected", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T
            expected: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_throws(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert throws error {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_throws_contains(ThirdBlock):
            OPCODE: ClassVar = (
                "&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("MSG", "msg", p.SRBlockAndTextInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            msg: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class assert_does_not_throw(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::assert does not throw error {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class fail_test(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::fail test with message (MSG)"
            INPUT_SPECS: ClassVar = (("MSG", "msg", p.SRBlockAndTextInputValue, None),)
            msg: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_expected_type(ThirdBlock):
            OPCODE: ClassVar = "&gceTestRunner::#menu:expectedType"

    class agBuffer:

        @grepr_dataclass()
        class new_buffer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::create new array buffer of size (LENGTH)"
            INPUT_SPECS: ClassVar = (
                ("LENGTH", "length", p.SRBlockAndTextInputValue, None),
            )
            length: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class buffer_of(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::parse (VALUE) as array buffer"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class from_url(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::get array buffer from url (URL)"
            INPUT_SPECS: ClassVar = (("URL", "url", p.SRBlockAndTextInputValue, None),)
            url: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class from_base64(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::array buffer from base64 (BASE64)"
            INPUT_SPECS: ClassVar = (
                ("BASE64", "base64", p.SRBlockAndTextInputValue, None),
            )
            base64: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class from_string(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::array buffer from string (STRING)"
            INPUT_SPECS: ClassVar = (
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_current(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::current buffer"

        @grepr_dataclass()
        class builder(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::array buffer builder {:CURRENT:} {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                (
                    "CURRENT",
                    "current",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.agBuffer.builder_current(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_append(ThirdBlock):
            OPCODE: ClassVar = (
                "&agBuffer::append ([TYPE]) value (VALUE) <ENDIAN> to builder"
            )
            INPUT_SPECS: ClassVar = (
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
            )
            type: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T
            endian: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_append_buffer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::append buffer (VALUE) to builder"
            INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockOnlyInputValue, None),)
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_set(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::set builder to (BUFFER)"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_value(ThirdBlock):
            OPCODE: ClassVar = (
                "&agBuffer::read ([TYPE]) value of (BUFFER) at (INDEX) <ENDIAN>"
            )
            INPUT_SPECS: ClassVar = (
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
            )
            type: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T
            buffer: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T
            endian: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_value(ThirdBlock):
            OPCODE: ClassVar = (
                "&agBuffer::write ([TYPE]) value (VALUE) to (BUFFER) at (INDEX) <ENDIAN>"
            )
            INPUT_SPECS: ClassVar = (
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
            )
            type: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T
            buffer: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T
            endian: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class write_sub_buffer(ThirdBlock):
            OPCODE: ClassVar = (
                "&agBuffer::write sub-buffer (SUBBUFFER) to (BUFFER) at (INDEX)"
            )
            INPUT_SPECS: ClassVar = (
                ("SUBBUFFER", "subbuffer", p.SRBlockOnlyInputValue, None),
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            subbuffer: INPUT_COMPATIBLE_T
            buffer: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_buffer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::(VALUE) is array buffer?"
            INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockOnlyInputValue, None),)
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_size(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::byte length of buffer (BUFFER)"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_array(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::convert (BUFFER) to array"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_typed_array(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::convert (BUFFER) to ([TYPE]) typed array"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class buffer_to_string(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::array buffer (BUFFER) to string"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_base64(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::array buffer (BUFFER) to base64"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_data_url(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::array buffer (BUFFER) to data:url"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class read_null_terminated_string(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::read string at (INDEX) of (BUFFER)"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class write_null_terminated_string(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::write string (STRING) at (INDEX) of (BUFFER)"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class items_of(ThirdBlock):
            OPCODE: ClassVar = (
                "&agBuffer::get bytes (MIN) to (MAX) from (BUFFER) as new buffer"
            )
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("MIN", "min", p.SRBlockAndTextInputValue, None),
                ("MAX", "max", p.SRBlockAndTextInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T
            min: INPUT_COMPATIBLE_T
            max: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class resize(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::resize (BUFFER) to (SIZE) bytes as new"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("SIZE", "size", p.SRBlockAndTextInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T
            size: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class resize_inst(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::resize (BUFFER) to (SIZE) bytes"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("SIZE", "size", p.SRBlockAndTextInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T
            size: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class copy(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::copy (BUFFER)"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class reverse(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::reverse (BUFFER)"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class reverse_r(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::reverse (BUFFER) as new"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class stringify(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::stringify (BUFFER) [MODE]"
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("MODE", "mode"),)
            buffer: INPUT_COMPATIBLE_T
            mode: str

        @grepr_dataclass()
        class for_each_v(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::byte"

        @grepr_dataclass()
        class for_each_i(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::index"

        @grepr_dataclass()
        class for_each(ThirdBlock):
            OPCODE: ClassVar = (
                "&agBuffer::for each [INDEX], {:BYTE:} of (BUFFER) {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                (
                    "INDEX",
                    "index",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.agBuffer.for_each_i(),
                ),
                (
                    "BYTE",
                    "byte",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.agBuffer.for_each_v(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            buffer: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class size_of_type(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::size of ([TYPE])"
            INPUT_SPECS: ClassVar = (
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            )
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class cast(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::cast (VALUE) to ([TYPE])"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            )
            value: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class create_pointer(ThirdBlock):
            OPCODE: ClassVar = (
                "&agBuffer::create ([TYPE]) pointer for (BUFFER) at (INDEX) <ENDIAN>"
            )
            INPUT_SPECS: ClassVar = (
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
                ("BUFFER", "buffer", p.SRBlockOnlyInputValue, None),
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
            )
            index: INPUT_COMPATIBLE_T
            endian: INPUT_COMPATIBLE_T
            buffer: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_pointer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::set value of pointer (PTR) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            ptr: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_pointer_index(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::set address of pointer (PTR) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            ptr: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_pointer_endian(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::set endian of pointer (PTR) to <VALUE>"
            INPUT_SPECS: ClassVar = (
                ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
            )
            ptr: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_pointer_type(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::set type of pointer (PTR) to ([VALUE])"
            INPUT_SPECS: ClassVar = (
                ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndDropdownInputValue, None),
            )
            ptr: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_pointer_buffer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::set buffer of pointer (PTR) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockOnlyInputValue, None),
            )
            ptr: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_pointer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::get value of pointer (PTR)"
            INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
            ptr: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_pointer_index(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::get address of pointer (PTR)"
            INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
            ptr: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_pointer_type(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::get type of pointer (PTR)"
            INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
            ptr: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_pointer_endian(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::is pointer (PTR) little-endian?"
            INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
            ptr: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_pointer_buffer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::get array buffer of pointer (PTR)"
            INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
            ptr: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_pointer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::is pointer [PTR]?"
            INPUT_SPECS: ClassVar = (("PTR", "ptr", p.SRBlockOnlyInputValue, None),)
            ptr: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class copy_pointer(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::copy pointer (PTR)"
            INPUT_SPECS: ClassVar = (
                ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
            )
            ptr: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T
            endian: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class pointer_as_type(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::(PTR) as ([TYPE]) pointer <ENDIAN>"
            INPUT_SPECS: ClassVar = (
                ("PTR", "ptr", p.SRBlockOnlyInputValue, None),
                ("TYPE", "type", p.SRBlockAndDropdownInputValue, None),
                ("ENDIAN", "endian", p.SRBlockAndBoolInputValue, None),
            )
            ptr: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T
            endian: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class max_reporter_lines(ThirdBlock):
            OPCODE: ClassVar = (
                "&agBuffer::(only visual) set max lines shown in reporter output to (LINES)"
            )
            INPUT_SPECS: ClassVar = (
                ("LINES", "lines", p.SRBlockAndTextInputValue, None),
            )
            lines: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class error_handling(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::set disable error prevention to <VALUE>"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_datatypes(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::#menu:DATATYPES"

        @grepr_dataclass()
        class menu_pointer_types(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::#menu:POINTER_TYPES"

        @grepr_dataclass()
        class menu_stringifymode(ThirdBlock):
            OPCODE: ClassVar = "&agBuffer::#menu:STRINGIFYMODE"

    class ddeDateFormat:

        @grepr_dataclass()
        class current_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::current date"

        @grepr_dataclass()
        class create_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::new date from (string)"
            INPUT_SPECS: ClassVar = (
                ("string", "string", p.SRBlockAndTextInputValue, None),
            )
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class format_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::format date (date) as (format)"
            INPUT_SPECS: ClassVar = (
                ("date", "date", p.SRBlockAndTextInputValue, None),
                ("format", "format", p.SRBlockAndTextInputValue, None),
            )
            date: INPUT_COMPATIBLE_T
            format: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class locale_format_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::format date (date) to ([type]) locale"
            INPUT_SPECS: ClassVar = (
                ("date", "date", p.SRBlockAndTextInputValue, None),
                ("type", "type", p.SRBlockAndDropdownInputValue, None),
            )
            date: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class compare_date(ThirdBlock):
            OPCODE: ClassVar = (
                "&ddeDateFormat::is date (date1) ([operation]) date [date2]?"
            )
            INPUT_SPECS: ClassVar = (
                ("date1", "date1", p.SRBlockAndTextInputValue, None),
                ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
                ("date2", "date2", p.SRBlockAndTextInputValue, None),
            )
            date1: INPUT_COMPATIBLE_T
            operation: INPUT_COMPATIBLE_T
            date2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_valid(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::is date (date) valid?"
            INPUT_SPECS: ClassVar = (
                ("date", "date", p.SRBlockAndTextInputValue, None),
            )
            date: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_date_part(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::get ([part]) of (date)"
            INPUT_SPECS: ClassVar = (
                ("part", "part", p.SRBlockAndDropdownInputValue, None),
                ("date", "date", p.SRBlockAndTextInputValue, None),
            )
            part: INPUT_COMPATIBLE_T
            date: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class add_time(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::add (amount) ([unit]) to (date)"
            INPUT_SPECS: ClassVar = (
                ("amount", "amount", p.SRBlockAndTextInputValue, None),
                ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                ("date", "date", p.SRBlockAndTextInputValue, None),
            )
            amount: INPUT_COMPATIBLE_T
            unit: INPUT_COMPATIBLE_T
            date: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class diff_date(ThirdBlock):
            OPCODE: ClassVar = (
                "&ddeDateFormat::difference between (date1) and (date2) in ([unit])"
            )
            INPUT_SPECS: ClassVar = (
                ("date1", "date1", p.SRBlockAndTextInputValue, None),
                ("date2", "date2", p.SRBlockAndTextInputValue, None),
                ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
            )
            date1: INPUT_COMPATIBLE_T
            date2: INPUT_COMPATIBLE_T
            unit: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_compare_operations(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::#menu:compareOperations"

        @grepr_dataclass()
        class menu_date_parts(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::#menu:dateParts"

        @grepr_dataclass()
        class menu_time_units(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::#menu:timeUnits"

        @grepr_dataclass()
        class menu_locale_length(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormat::#menu:localeLength"

    class ddeDateFormatV2:

        @grepr_dataclass()
        class current_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::current date"

        @grepr_dataclass()
        class create_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::new date from (string)"
            INPUT_SPECS: ClassVar = (
                ("string", "string", p.SRBlockAndTextInputValue, None),
            )
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class format_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::format (date) as (format)"
            INPUT_SPECS: ClassVar = (
                ("date", "date", p.SRBlockOnlyInputValue, None),
                ("format", "format", p.SRBlockAndTextInputValue, None),
            )
            date: INPUT_COMPATIBLE_T
            format: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class locale_format_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::format (date) as ([type]) locale"
            INPUT_SPECS: ClassVar = (
                ("date", "date", p.SRBlockOnlyInputValue, None),
                ("type", "type", p.SRBlockAndDropdownInputValue, None),
            )
            date: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class extra_format_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::format (date) as ([type])"
            INPUT_SPECS: ClassVar = (
                ("date", "date", p.SRBlockOnlyInputValue, None),
                ("type", "type", p.SRBlockAndDropdownInputValue, None),
            )
            date: INPUT_COMPATIBLE_T
            type: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iso_format_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::format (date) as ISO string"
            INPUT_SPECS: ClassVar = (("date", "date", p.SRBlockOnlyInputValue, None),)
            date: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_valid(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::is (date) valid?"
            INPUT_SPECS: ClassVar = (("date", "date", p.SRBlockOnlyInputValue, None),)
            date: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class compare_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::is (date1) ([operation]) [date2]?"
            INPUT_SPECS: ClassVar = (
                ("date1", "date1", p.SRBlockOnlyInputValue, None),
                ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
                ("date2", "date2", p.SRBlockOnlyInputValue, None),
            )
            date1: INPUT_COMPATIBLE_T
            operation: INPUT_COMPATIBLE_T
            date2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class check_date_property(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::is (date) [property]?"
            INPUT_SPECS: ClassVar = (
                ("date", "date", p.SRBlockOnlyInputValue, None),
                ("property", "property", p.SRBlockAndDropdownInputValue, None),
            )
            date: INPUT_COMPATIBLE_T
            property: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class diff_date(ThirdBlock):
            OPCODE: ClassVar = (
                "&ddeDateFormatV2::get ([unit]) between (date1) and (date2)"
            )
            INPUT_SPECS: ClassVar = (
                ("date1", "date1", p.SRBlockOnlyInputValue, None),
                ("date2", "date2", p.SRBlockOnlyInputValue, None),
                ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
            )
            date1: INPUT_COMPATIBLE_T
            date2: INPUT_COMPATIBLE_T
            unit: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_date_part(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::get UTC ([part]) of (date)"
            INPUT_SPECS: ClassVar = (
                ("part", "part", p.SRBlockAndDropdownInputValue, None),
                ("date", "date", p.SRBlockOnlyInputValue, None),
            )
            part: INPUT_COMPATIBLE_T
            date: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_date_part_new(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::get ([part]) of (date)"
            INPUT_SPECS: ClassVar = (
                ("part", "part", p.SRBlockAndDropdownInputValue, None),
                ("date", "date", p.SRBlockOnlyInputValue, None),
            )
            part: INPUT_COMPATIBLE_T
            date: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_date_part(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::set ([part]) of (date) to (value)"
            INPUT_SPECS: ClassVar = (
                ("part", "part", p.SRBlockAndDropdownInputValue, None),
                ("date", "date", p.SRBlockOnlyInputValue, None),
                ("value", "value", p.SRBlockAndTextInputValue, None),
            )
            part: INPUT_COMPATIBLE_T
            date: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class add_time(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::add (amount) ([unit]) to (date)"
            INPUT_SPECS: ClassVar = (
                ("amount", "amount", p.SRBlockAndTextInputValue, None),
                ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                ("date", "date", p.SRBlockOnlyInputValue, None),
            )
            amount: INPUT_COMPATIBLE_T
            unit: INPUT_COMPATIBLE_T
            date: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class round_date(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::round (date) to nearest ([unit])"
            INPUT_SPECS: ClassVar = (
                ("date", "date", p.SRBlockOnlyInputValue, None),
                ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
            )
            date: INPUT_COMPATIBLE_T
            unit: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_compare_operations(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::#menu:compareOperations"

        @grepr_dataclass()
        class menu_date_parts(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::#menu:dateParts"

        @grepr_dataclass()
        class menu_time_units(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::#menu:timeUnits"

        @grepr_dataclass()
        class menu_locale_length(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::#menu:localeLength"

        @grepr_dataclass()
        class menu_date_properties(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::#menu:dateProperties"

        @grepr_dataclass()
        class menu_extra_formats(ThirdBlock):
            OPCODE: ClassVar = "&ddeDateFormatV2::#menu:extraFormats"

    class divAlgEffects:

        @grepr_dataclass()
        class eff_perform_ret(ThirdBlock):
            OPCODE: ClassVar = (
                "&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerformRet}}"
            )
            INPUT_SPECS: ClassVar = (
                ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                ("DATA", "data", p.SRBlockAndTextInputValue, None),
            )
            eff: INPUT_COMPATIBLE_T
            data: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eff_handle(ThirdBlock):
            OPCODE: ClassVar = (
                "&divAlgEffects::handle in {SUBSTACK} effects {SUBSTACK2}"
            )
            INPUT_SPECS: ClassVar = (
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T
            substack2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eff_handler_case(ThirdBlock):
            OPCODE: ClassVar = "&divAlgEffects::effect (EFF) with {:DATA:} {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                (
                    "DATA",
                    "data",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divAlgEffects.eff_data(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            eff: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eff_recurse_handler(ThirdBlock):
            OPCODE: ClassVar = "&divAlgEffects::recursively handle {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eff_resume_ret(ThirdBlock):
            OPCODE: ClassVar = (
                "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeRet}}"
            )
            INPUT_SPECS: ClassVar = (
                ("DATA", "data", p.SRBlockAndTextInputValue, None),
            )
            data: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eff_resume_tail(ThirdBlock):
            OPCODE: ClassVar = (
                "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeTail}}"
            )
            INPUT_SPECS: ClassVar = (
                ("DATA", "data", p.SRBlockAndTextInputValue, None),
            )
            data: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eff_data(ThirdBlock):
            OPCODE: ClassVar = "&divAlgEffects::data"

        @grepr_dataclass()
        class eff_continuation(ThirdBlock):
            OPCODE: ClassVar = "&divAlgEffects::continuation"

        @grepr_dataclass()
        class eff_cont_has_resumed(ThirdBlock):
            OPCODE: ClassVar = "&divAlgEffects::has (CONT) resumed?"
            INPUT_SPECS: ClassVar = (
                ("CONT", "cont", p.SRBlockAndTextInputValue, None),
            )
            cont: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eff_perform(ThirdBlock):
            OPCODE: ClassVar = (
                "&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerform}}"
            )
            INPUT_SPECS: ClassVar = (
                ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                ("DATA", "data", p.SRBlockAndTextInputValue, None),
            )
            eff: INPUT_COMPATIBLE_T
            data: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eff_resume(ThirdBlock):
            OPCODE: ClassVar = (
                "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResume}}"
            )
            INPUT_SPECS: ClassVar = (
                ("DATA", "data", p.SRBlockAndTextInputValue, None),
            )
            data: INPUT_COMPATIBLE_T

    class divIterator:

        @grepr_dataclass()
        class iter_item(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::item"

        @grepr_dataclass()
        class iter_acc(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::acc"

        @grepr_dataclass()
        class iter_advance(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::advance (ITER)"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            iter: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_next(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::next item from (ITER)"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            iter: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_is_iter(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::is (THING) an iterator?"
            INPUT_SPECS: ClassVar = (
                ("THING", "thing", p.SRBlockAndTextInputValue, None),
            )
            thing: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_done(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) is done?"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            iter: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_clone(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::clone (ITER)"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            iter: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_clonable(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) is clonable?"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            iter: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_branch(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::branch (ITER) into (NUM) branches"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                ("NUM", "num", p.SRBlockAndTextInputValue, None),
            )
            iter: INPUT_COMPATIBLE_T
            num: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_term_for_each(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::for {:I:} of (ITER) {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                (
                    "I",
                    "i",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_item(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            iter: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_range(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::range from (START) to (END)"
            INPUT_SPECS: ClassVar = (
                ("START", "start", p.SRBlockAndTextInputValue, None),
                ("END", "end", p.SRBlockAndTextInputValue, None),
            )
            start: INPUT_COMPATIBLE_T
            end: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_iter_over(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::iter over (VAL)"
            INPUT_SPECS: ClassVar = (("VAL", "val", p.SRBlockAndTextInputValue, None),)
            val: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_builder(ThirdBlock):
            OPCODE: ClassVar = (
                "&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("STATE", "state", p.SRBlockAndTextInputValue, None),
                (
                    "S",
                    "s",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_builder_get_state(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            state: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_builder_get_state(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::state"

        @grepr_dataclass()
        class iter_builder_set_state(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::set state to (STATE)"
            INPUT_SPECS: ClassVar = (
                ("STATE", "state", p.SRBlockAndTextInputValue, None),
            )
            state: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_builder_item(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::return item (ITEM)"
            INPUT_SPECS: ClassVar = (
                ("ITEM", "item", p.SRBlockAndTextInputValue, None),
            )
            item: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_builder_done(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::finish iterator"

        @grepr_dataclass()
        class iter_adapter_map(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) then map {:I:} (MAP)"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                (
                    "I",
                    "i",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_item(),
                ),
                ("MAP", "map", p.SRBlockAndTextInputValue, None),
            )
            iter: INPUT_COMPATIBLE_T
            map: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_keep(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) then keep {:I:} if <PRED>"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                (
                    "I",
                    "i",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_item(),
                ),
                ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
            )
            iter: INPUT_COMPATIBLE_T
            pred: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_enum(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) then enumerate items"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            iter: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_cycle(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) then cycle items"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            iter: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_take(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) then take (COUNT) items"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                ("COUNT", "count", p.SRBlockAndTextInputValue, None),
            )
            iter: INPUT_COMPATIBLE_T
            count: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_skip(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) then skip (COUNT) items"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                ("COUNT", "count", p.SRBlockAndTextInputValue, None),
            )
            iter: INPUT_COMPATIBLE_T
            count: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_step_by(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) then step by (STEP) items"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                ("STEP", "step", p.SRBlockAndTextInputValue, None),
            )
            iter: INPUT_COMPATIBLE_T
            step: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_chain(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER1) then chain with (ITER2)"
            INPUT_SPECS: ClassVar = (
                ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
            )
            iter1: INPUT_COMPATIBLE_T
            iter2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_zip(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER1) then zip with (ITER2)"
            INPUT_SPECS: ClassVar = (
                ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
            )
            iter1: INPUT_COMPATIBLE_T
            iter2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_cross(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER1) then cross with (ITER2)"
            INPUT_SPECS: ClassVar = (
                ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
            )
            iter1: INPUT_COMPATIBLE_T
            iter2: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_adapter_inspect(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) then inspect {:I:} {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                (
                    "I",
                    "i",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_item(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            iter: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_collect_to(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) finally collect to [TYPE]"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            DROPDOWN_SPECS: ClassVar = (("TYPE", "type"),)
            iter: INPUT_COMPATIBLE_T
            type: str

        @grepr_dataclass()
        class iter_term_count(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) finally count items"
            INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
            iter: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_term_fold(ThirdBlock):
            OPCODE: ClassVar = (
                "&divIterator::(ITER) finally reduce (INIT) with {:A:} {:I:} (FOLD)"
            )
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                ("INIT", "init", p.SRBlockAndTextInputValue, None),
                ("FOLD", "fold", p.SRBlockAndTextInputValue, None),
                (
                    "A",
                    "a",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_acc(),
                ),
                (
                    "I",
                    "i",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_item(),
                ),
            )
            iter: INPUT_COMPATIBLE_T
            init: INPUT_COMPATIBLE_T
            fold: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_term_any(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) finally any {:I:} <PRED>"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
                (
                    "I",
                    "i",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_item(),
                ),
            )
            iter: INPUT_COMPATIBLE_T
            pred: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class iter_term_all(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::(ITER) finally all {:I:} <PRED>"
            INPUT_SPECS: ClassVar = (
                ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
                (
                    "I",
                    "i",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.divIterator.iter_item(),
                ),
            )
            iter: INPUT_COMPATIBLE_T
            pred: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_from_iter(ThirdBlock):
            OPCODE: ClassVar = "&divIterator::#menu:fromIter"

    class dogeiscutObject:

        @grepr_dataclass()
        class blank(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::blank object"

        @grepr_dataclass()
        class parse(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::parse (VALUE) as object"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class from_entries(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::from entries (ARRAY)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class current_object(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::current object"

        @grepr_dataclass()
        class builder(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutObject::object builder {:CURRENT_OBJECT:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                (
                    "CURRENT_OBJECT",
                    "current_object",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.dogeiscutObject.current_object(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_append(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutObject::append key (KEY) value (VALUE) to builder"
            )
            INPUT_SPECS: ClassVar = (
                ("KEY", "key", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            key: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_append_empty(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::append key (KEY) to builder"
            INPUT_SPECS: ClassVar = (("KEY", "key", p.SRBlockAndTextInputValue, None),)
            key: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_set(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::set builder to (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            )
            object: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::get (KEY) in (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                ("KEY", "key", p.SRBlockAndTextInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            key: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_path(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::get path (ARRAY) in (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            array: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class has(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::(OBJECT) has key (KEY)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                ("KEY", "key", p.SRBlockAndTextInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            key: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class size(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::size of (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            )
            object: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::set (KEY) in (OBJECT) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                ("KEY", "key", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            key: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_path(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutObject::set path (ARRAY) in (OBJECT) to (VALUE)"
            )
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T
            array: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::delete key (KEY) from (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                ("KEY", "key", p.SRBlockAndTextInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            key: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete_at_path(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::delete at path (ARRAY) from (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                ("ARRAY", "array", p.SRBlockAndTextInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            array: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class merge(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::merge (ONE) into (TWO)"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_string(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::stringify (OBJECT) (FORMAT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            format: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class keys(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::keys of (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            )
            object: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class values(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::values of (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            )
            object: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class entries(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::entries of (OBJECT)"
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
            )
            object: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::does (VALUE) parse as an object?"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class for_each_k(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::key"

        @grepr_dataclass()
        class for_each_v(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::value"

        @grepr_dataclass()
        class for_each(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutObject::for {:K:} {:V:} of (OBJECT) {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("OBJECT", "object", p.SRBlockOnlyInputValue, None),
                (
                    "K",
                    "k",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.dogeiscutObject.for_each_k(),
                ),
                (
                    "V",
                    "v",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.dogeiscutObject.for_each_v(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            object: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_stringify_format(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutObject::#menu:stringifyFormat"

    class dogeiscutRegularExpressions:

        @grepr_dataclass()
        class regex(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)"
            )
            INPUT_SPECS: ClassVar = (
                ("PATTERN", "pattern", p.SRBlockAndTextInputValue, None),
                ("FLAGS", "flags", p.SRBlockAndTextInputValue, None),
            )
            pattern: INPUT_COMPATIBLE_T
            flags: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class escape(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutRegularExpressions::escape (STRING) for regex"
            INPUT_SPECS: ClassVar = (
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class source_of(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutRegularExpressions::source of (REGEX)"
            INPUT_SPECS: ClassVar = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
            regex: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class flags_of(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutRegularExpressions::flags of (REGEX)"
            INPUT_SPECS: ClassVar = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
            regex: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class test(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutRegularExpressions::test (STRING) for (REGEX)"
            INPUT_SPECS: ClassVar = (
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            )
            string: INPUT_COMPATIBLE_T
            regex: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class search(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutRegularExpressions::search (STRING) with (REGEX)"
            )
            INPUT_SPECS: ClassVar = (
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            )
            string: INPUT_COMPATIBLE_T
            regex: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class replace(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutRegularExpressions::replace (REGEX) in (A) with (B)"
            )
            INPUT_SPECS: ClassVar = (
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            regex: INPUT_COMPATIBLE_T
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class replace_all(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutRegularExpressions::replace all (REGEX) in (A) with (B)"
            )
            INPUT_SPECS: ClassVar = (
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            regex: INPUT_COMPATIBLE_T
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class split(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutRegularExpressions::split (STRING) by (REGEX)"
            INPUT_SPECS: ClassVar = (
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
            )
            string: INPUT_COMPATIBLE_T
            regex: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class match(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutRegularExpressions::match (REGEX) with (STRING)"
            )
            INPUT_SPECS: ClassVar = (
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            regex: INPUT_COMPATIBLE_T
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class match_all(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutRegularExpressions::match all (REGEX) with (STRING)"
            )
            INPUT_SPECS: ClassVar = (
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            regex: INPUT_COMPATIBLE_T
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class exec(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutRegularExpressions::execute (REGEX) on (STRING)"
            )
            INPUT_SPECS: ClassVar = (
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
            )
            regex: INPUT_COMPATIBLE_T
            string: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_last_index(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutRegularExpressions::get last index of (REGEX)"
            INPUT_SPECS: ClassVar = (("REGEX", "regex", p.SRBlockOnlyInputValue, None),)
            regex: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_last_index(ThirdBlock):
            OPCODE: ClassVar = (
                "&dogeiscutRegularExpressions::set last index of (REGEX) to (INDEX)"
            )
            INPUT_SPECS: ClassVar = (
                ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            regex: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T

    class dogeiscutSet:

        @grepr_dataclass()
        class blank(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::blank set"

        @grepr_dataclass()
        class from_list(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::set from list (LIST)"
            INPUT_SPECS: ClassVar = (("LIST", "list", p.SRBlockOnlyInputValue, None),)
            list: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class parse(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::parse (INPUT) as set"
            INPUT_SPECS: ClassVar = (
                ("INPUT", "input", p.SRBlockAndTextInputValue, None),
            )
            input: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_current(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::current set"

        @grepr_dataclass()
        class builder(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::set builder {:SHADOW:} {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.dogeiscutSet.builder_current(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_append(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::append (VALUE) to builder"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_set(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::set builder to (SET)"
            INPUT_SPECS: ClassVar = (("SET", "set", p.SRBlockOnlyInputValue, None),)
            set: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class has(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::(SET) has (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("SET", "set", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            set: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_subset_of(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::is (ONE) a subset of [TWO]?"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_superset_of(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::is (ONE) a superset of [TWO]?"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_disjoint_from(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::is (ONE) disjoint from [TWO]?"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class size(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::size of (SET)"
            INPUT_SPECS: ClassVar = (("SET", "set", p.SRBlockOnlyInputValue, None),)
            set: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class add(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::add (VALUE) to (SET)"
            INPUT_SPECS: ClassVar = (
                ("SET", "set", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            set: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::delete (VALUE) from (SET)"
            INPUT_SPECS: ClassVar = (
                ("SET", "set", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            set: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class union(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::union (ONE) with (TWO)"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class intersect(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::intersect (ONE) with (TWO)"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class difference(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::difference (ONE) with (TWO)"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class symmetric_difference(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::symmetric difference (ONE) with (TWO)"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class flat(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::flat (SET) with depth (DEPTH)"
            INPUT_SPECS: ClassVar = (
                ("SET", "set", p.SRBlockOnlyInputValue, None),
                ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
            )
            set: INPUT_COMPATIBLE_T
            depth: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_string(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::stringify (SET) (FORMAT)"
            INPUT_SPECS: ClassVar = (
                ("SET", "set", p.SRBlockOnlyInputValue, None),
                ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
            )
            set: INPUT_COMPATIBLE_T
            format: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class for_each_v(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::value"

        @grepr_dataclass()
        class for_each(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::for {:V:} of (SET) {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("SET", "set", p.SRBlockOnlyInputValue, None),
                (
                    "V",
                    "v",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.dogeiscutSet.for_each_v(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            set: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_list(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::#menu:list"

        @grepr_dataclass()
        class menu_stringify_format(ThirdBlock):
            OPCODE: ClassVar = "&dogeiscutSet::#menu:stringifyFormat"

    class fruitsPaintUtils:

        @grepr_dataclass()
        class mix_colours(ThirdBlock):
            OPCODE: ClassVar = (
                "&fruitsPaintUtils::mix colours (COLOUR_NAME1) and (COLOUR_NAME2) and return the [MIX_OPTIONS]"
            )
            INPUT_SPECS: ClassVar = (
                ("COLOUR_NAME1", "colour_name1", p.SRBlockAndTextInputValue, None),
                ("COLOUR_NAME2", "colour_name2", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("MIX_OPTIONS", "mix_options"),)
            colour_name1: INPUT_COMPATIBLE_T
            colour_name2: INPUT_COMPATIBLE_T
            mix_options: str

        @grepr_dataclass()
        class get_colour(ThirdBlock):
            OPCODE: ClassVar = (
                "&fruitsPaintUtils::get colour from colour name (COLOUR_NAME)"
            )
            INPUT_SPECS: ClassVar = (
                ("COLOUR_NAME", "colour_name", p.SRBlockAndTextInputValue, None),
            )
            colour_name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_mix_options(ThirdBlock):
            OPCODE: ClassVar = "&fruitsPaintUtils::#menu:MIX_OPTIONS"

    class jwArray:

        @grepr_dataclass()
        class blank(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::blank array"

        @grepr_dataclass()
        class blank_length(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::blank array of length (LENGTH)"
            INPUT_SPECS: ClassVar = (
                ("LENGTH", "length", p.SRBlockAndTextInputValue, None),
            )
            length: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class from_list(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::array from list (LIST)"
            INPUT_SPECS: ClassVar = (("LIST", "list", p.SRBlockOnlyInputValue, None),)
            list: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class parse(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::parse (INPUT) as array"
            INPUT_SPECS: ClassVar = (
                ("INPUT", "input", p.SRBlockAndTextInputValue, None),
            )
            input: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class split(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::split (STRING) by (DIVIDER)"
            INPUT_SPECS: ClassVar = (
                ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
            )
            string: INPUT_COMPATIBLE_T
            divider: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::array builder {:SHADOW:} {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                (
                    "SHADOW",
                    "shadow",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.jwArray.builder_current(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_current(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::current array"

        @grepr_dataclass()
        class builder_append(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::append (VALUE) to builder"
            INPUT_SPECS: ClassVar = (
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class builder_set(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::set builder to (ARRAY)"
            INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
            array: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::get (INDEX) in (ARRAY)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class items(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::items (X) to (Y) in (ARRAY)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class index(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::index of (VALUE) in (ARRAY)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class has(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::(ARRAY) has (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class length(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::length of (ARRAY)"
            INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
            array: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::set (INDEX) in (ARRAY) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class append(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::append (VALUE) to (ARRAY)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class concat(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::merge (ONE) with (TWO)"
            INPUT_SPECS: ClassVar = (
                ("ONE", "one", p.SRBlockOnlyInputValue, None),
                ("TWO", "two", p.SRBlockOnlyInputValue, None),
            )
            one: INPUT_COMPATIBLE_T
            two: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class fill(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::fill (ARRAY) with (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class reverse(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::reverse (ARRAY)"
            INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
            array: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class splice(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::splice (ARRAY) at (INDEX) with (ITEMS) items"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ("ITEMS", "items", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            index: INPUT_COMPATIBLE_T
            items: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class repeat(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::repeat (ARRAY) (TIMES) times"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("TIMES", "times", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            times: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class flat(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::flat (ARRAY) with depth (DEPTH)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("DEPTH", "depth", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            depth: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_string(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::stringify (ARRAY) (FORMAT)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            format: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class join(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::join (ARRAY) with (DIVIDER)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("DIVIDER", "divider", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            divider: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class sum(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::sum of (ARRAY)"
            INPUT_SPECS: ClassVar = (("ARRAY", "array", p.SRBlockOnlyInputValue, None),)
            array: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class for_each_i(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::index"

        @grepr_dataclass()
        class for_each_v(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::value"

        @grepr_dataclass()
        class for_each(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::for {:I:} {:V:} of (ARRAY) {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("I", "i", p.SREmbeddedBlockInputValue, lambda: h.jwArray.for_each_i()),
                ("V", "v", p.SREmbeddedBlockInputValue, lambda: h.jwArray.for_each_v()),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class basic_sort(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::sort (ARRAY) {:I:} {:V:} > (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("I", "i", p.SREmbeddedBlockInputValue, lambda: h.jwArray.for_each_i()),
                ("V", "v", p.SREmbeddedBlockInputValue, lambda: h.jwArray.for_each_v()),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_list(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::#menu:list"

        @grepr_dataclass()
        class menu_stringify_format(ThirdBlock):
            OPCODE: ClassVar = "&jwArray::#menu:stringifyFormat"

    class jwColor:

        @grepr_dataclass()
        class new_color(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::new color (COLOR)"
            INPUT_SPECS: ClassVar = (
                ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            )
            color: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class from_rgb(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::from RGB (R) (G) (B)"
            INPUT_SPECS: ClassVar = (
                ("R", "r", p.SRBlockAndTextInputValue, None),
                ("G", "g", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            r: INPUT_COMPATIBLE_T
            g: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class from_hsv(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::from HSV (H) (S) (V)"
            INPUT_SPECS: ClassVar = (
                ("H", "h", p.SRBlockAndTextInputValue, None),
                ("S", "s", p.SRBlockAndTextInputValue, None),
                ("V", "v", p.SRBlockAndTextInputValue, None),
            )
            h: INPUT_COMPATIBLE_T
            s: INPUT_COMPATIBLE_T
            v: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class from_hex(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::from hex (HEX)"
            INPUT_SPECS: ClassVar = (("HEX", "hex", p.SRBlockAndTextInputValue, None),)
            hex: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class add(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::(A) + (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class sub(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::(A) - (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class mul(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::(A) * (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class interpolate(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::interpolate (A) to (B) by (I) using (OPTION)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
                ("I", "i", p.SRBlockAndTextInputValue, None),
                ("OPTION", "option", p.SRBlockOnlyInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T
            i: INPUT_COMPATIBLE_T
            option: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::get (OPTION) (COLOR)"
            INPUT_SPECS: ClassVar = (
                ("COLOR", "color", p.SRBlockAndTextInputValue, None),
                ("OPTION", "option", p.SRBlockOnlyInputValue, None),
            )
            color: INPUT_COMPATIBLE_T
            option: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::set (OPTION) (COLOR) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("COLOR", "color", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ("OPTION", "option", p.SRBlockOnlyInputValue, None),
            )
            color: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T
            option: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_decimal(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::(COLOR) to decimal"
            INPUT_SPECS: ClassVar = (
                ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            )
            color: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_hex(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::(COLOR) to hexadecimal"
            INPUT_SPECS: ClassVar = (
                ("COLOR", "color", p.SRBlockAndTextInputValue, None),
            )
            color: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_interpolate_option(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::#menu:interpolateOption"

        @grepr_dataclass()
        class menu_prop_option(ThirdBlock):
            OPCODE: ClassVar = "&jwColor::#menu:propOption"

    class jwDate:

        @grepr_dataclass()
        class now(ThirdBlock):
            OPCODE: ClassVar = "&jwDate::now"

        @grepr_dataclass()
        class epoch(ThirdBlock):
            OPCODE: ClassVar = "&jwDate::unix epoch"

        @grepr_dataclass()
        class parse(ThirdBlock):
            OPCODE: ClassVar = "&jwDate::parse (INPUT)"
            INPUT_SPECS: ClassVar = (("INPUT", "input", p.SRBlockOnlyInputValue, None),)
            input: INPUT_COMPATIBLE_T

    class jwLambda:

        @grepr_dataclass()
        class arg(ThirdBlock):
            OPCODE: ClassVar = "&jwLambda::argument"

        @grepr_dataclass()
        class new_lambda(ThirdBlock):
            OPCODE: ClassVar = "&jwLambda::new lambda {:ARG:} {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("ARG", "arg", p.SREmbeddedBlockInputValue, lambda: h.jwLambda.arg()),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class raw_lambda_input(ThirdBlock):
            OPCODE: ClassVar = "&jwLambda::(FIELD)"
            INPUT_SPECS: ClassVar = (("FIELD", "field", p.SRBlockOnlyInputValue, None),)
            field: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class raw_lambda(ThirdBlock):
            OPCODE: ClassVar = "&jwLambda::new lambda {:RAW:}"
            INPUT_SPECS: ClassVar = (
                (
                    "RAW",
                    "raw",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.jwLambda.raw_lambda_input(),
                ),
            )

        @grepr_dataclass()
        class execute_r(ThirdBlock):
            OPCODE: ClassVar = (
                "&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_executeR}}"
            )
            INPUT_SPECS: ClassVar = (
                ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
                ("ARG", "arg", p.SRBlockAndTextInputValue, None),
            )
            lambda_: INPUT_COMPATIBLE_T
            arg: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class this(ThirdBlock):
            OPCODE: ClassVar = "&jwLambda::this lambda"

        @grepr_dataclass()
        class times_executed(ThirdBlock):
            OPCODE: ClassVar = "&jwLambda::times (LAMBDA) executed"
            INPUT_SPECS: ClassVar = (
                ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
            )
            lambda_: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class execute(ThirdBlock):
            OPCODE: ClassVar = (
                "&jwLambda::execute (LAMBDA) with (ARG) {{id=jwLambda_execute}}"
            )
            INPUT_SPECS: ClassVar = (
                ("LAMBDA", "lambda_", p.SRBlockOnlyInputValue, None),
                ("ARG", "arg", p.SRBlockAndTextInputValue, None),
            )
            lambda_: INPUT_COMPATIBLE_T
            arg: INPUT_COMPATIBLE_T

    class jwNum:

        @grepr_dataclass()
        class add(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) + (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class sub(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) - (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class mul(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) * (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class div(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) / (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class pow(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) ^ (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class fact(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::[A]!"
            INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
            a: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class eq(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) = (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class gt(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) > (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class gte(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) >= (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class lt(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) < (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class lte(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) <= (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class root(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::root (A) (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class ssqrt(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::square super-root (A)"
            INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
            a: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class log(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::log (A) (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class slog(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::super log (A) (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class mod(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) % (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class round(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::([A]) (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndDropdownInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_integer(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::is (A) an integer?"
            INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
            a: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class hyper(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) hyper (B) (C)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
                ("C", "c", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T
            c: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class arrow(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) arrow (B) (C)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
                ("C", "c", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T
            c: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class reverse_arrow(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(C) reverse arrow (B) (A)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
                ("C", "c", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T
            c: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class expansion(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) expansion (B)"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_string(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) to string"
            INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
            a: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_string_d(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) to string with (B) decimal places"
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockAndTextInputValue, None),
                ("B", "b", p.SRBlockAndTextInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_hyper_e(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::(A) to hyper E"
            INPUT_SPECS: ClassVar = (("A", "a", p.SRBlockAndTextInputValue, None),)
            a: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_round(ThirdBlock):
            OPCODE: ClassVar = "&jwNum::#menu:round"

    class jwTargets:

        @grepr_dataclass()
        class this(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::this target"

        @grepr_dataclass()
        class stage(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::stage target"

        @grepr_dataclass()
        class from_name(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::(SPRITE) target"
            INPUT_SPECS: ClassVar = (
                ("SPRITE", "sprite", p.SRBlockOnlyInputValue, None),
            )
            sprite: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class clone_origin(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::origin of (TARGET)"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::(TARGET) (MENU)"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                ("MENU", "menu", p.SRBlockOnlyInputValue, None),
            )
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
            target: INPUT_COMPATIBLE_T
            menu: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_clone(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::is (TARGET) a clone"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            )
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
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_var(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::var (NAME) of (TARGET)"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
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
            target: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class clone_r(ThirdBlock):
            OPCODE: ClassVar = (
                "&jwTargets::create clone of (TARGET) {{id=jwTargets_cloneR}}"
            )
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete_clone(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::delete clone (TARGET)"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class all(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::all targets"

        @grepr_dataclass()
        class touching(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::targets touching (TARGET)"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class clones(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::clones of (TARGET)"
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class array_has_target(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::(ARRAY) has clone of (TARGET)"
            INPUT_SPECS: ClassVar = (
                ("ARRAY", "array", p.SRBlockOnlyInputValue, None),
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            )
            array: INPUT_COMPATIBLE_T
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class is_touching(ThirdBlock):
            OPCODE: ClassVar = (
                "&jwTargets::is (A) touching (B) {{id=jwTargets_isTouching}}"
            )
            INPUT_SPECS: ClassVar = (
                ("A", "a", p.SRBlockOnlyInputValue, None),
                ("B", "b", p.SRBlockOnlyInputValue, None),
            )
            a: INPUT_COMPATIBLE_T
            b: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class clone(ThirdBlock):
            OPCODE: ClassVar = (
                "&jwTargets::create clone of (TARGET) {{id=jwTargets_clone}}"
            )
            INPUT_SPECS: ClassVar = (
                ("TARGET", "target", p.SRBlockOnlyInputValue, None),
            )
            target: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_sprite(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::#menu:sprite"

        @grepr_dataclass()
        class menu_target_property(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::#menu:targetProperty"

        @grepr_dataclass()
        class menu_target_property_set(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::#menu:targetPropertySet"

        @grepr_dataclass()
        class menu_touching_object(ThirdBlock):
            OPCODE: ClassVar = "&jwTargets::#menu:touchingObject"

    class jwVector:

        @grepr_dataclass()
        class new_vector(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::new vector x: (X) y: (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class new_vector_from_magnitude(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::new vector magnitude: (X) angle: (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class vector_x(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(VECTOR) x"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class vector_y(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(VECTOR) y"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class add(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(X) + (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockOnlyInputValue, None),
                ("Y", "y", p.SRBlockOnlyInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class subtract(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(X) - (Y)"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockOnlyInputValue, None),
                ("Y", "y", p.SRBlockOnlyInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class multiply_b(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(X) * (Y) {{id=jwVector_multiplyB}}"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockOnlyInputValue, None),
                ("Y", "y", p.SRBlockOnlyInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class divide_b(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(X) / (Y) {{id=jwVector_divideB}}"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockOnlyInputValue, None),
                ("Y", "y", p.SRBlockOnlyInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class magnitude(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::magnitude of (VECTOR)"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class angle(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::angle of (VECTOR)"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class normalize(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::normalize (VECTOR)"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class absolute(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::absolute (VECTOR)"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class rotate(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::rotate (VECTOR) by (ANGLE)"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
                ("ANGLE", "angle", p.SRBlockAndTextInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T
            angle: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class round(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(ROUNDING) of (VECTOR)"
            INPUT_SPECS: ClassVar = (
                ("ROUNDING", "rounding", p.SRBlockOnlyInputValue, None),
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            rounding: INPUT_COMPATIBLE_T
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_pos(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::position"

        @grepr_dataclass()
        class set_pos(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::set position to (VECTOR)"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_stretch(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::stretch"

        @grepr_dataclass()
        class set_stretch(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::set stretch to (VECTOR)"
            INPUT_SPECS: ClassVar = (
                ("VECTOR", "vector", p.SRBlockOnlyInputValue, None),
            )
            vector: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_mouse(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::mouse position"

        @grepr_dataclass()
        class divide_a(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(X) / (Y) {{id=jwVector_divideA}}"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockOnlyInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class multiply_a(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::(X) * (Y) {{id=jwVector_multiplyA}}"
            INPUT_SPECS: ClassVar = (
                ("X", "x", p.SRBlockOnlyInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_rounding_functions(ThirdBlock):
            OPCODE: ClassVar = "&jwVector::#menu:roundingFunctions"

    class jwXML:

        @grepr_dataclass()
        class new_node(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::new node (NAME)"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class parse(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::parse (INPUT) as node"
            INPUT_SPECS: ClassVar = (
                ("INPUT", "input", p.SRBlockAndTextInputValue, None),
            )
            input: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class parse_multiple(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::parse (INPUT) as nodes"
            INPUT_SPECS: ClassVar = (
                ("INPUT", "input", p.SRBlockAndTextInputValue, None),
            )
            input: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_name(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::name of (NODE)"
            INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
            node: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_name(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::set name of (NODE) to (NAME)"
            INPUT_SPECS: ClassVar = (
                ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            node: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class append_child(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::append (CHILD) to (NODE)"
            INPUT_SPECS: ClassVar = (
                ("CHILD", "child", p.SRBlockAndTextInputValue, None),
                ("NODE", "node", p.SRBlockOnlyInputValue, None),
            )
            child: INPUT_COMPATIBLE_T
            node: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class remove_children(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::remove children of (NODE)"
            INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
            node: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_children(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::children of (NODE)"
            INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
            node: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_children(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::set children of (NODE) to (CHILDREN)"
            INPUT_SPECS: ClassVar = (
                ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ("CHILDREN", "children", p.SRBlockOnlyInputValue, None),
            )
            node: INPUT_COMPATIBLE_T
            children: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_attribute(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::attribute (ATTRIBUTE) of (NODE)"
            INPUT_SPECS: ClassVar = (
                ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                ("NODE", "node", p.SRBlockOnlyInputValue, None),
            )
            attribute: INPUT_COMPATIBLE_T
            node: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class set_attribute(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::set attribute (ATTRIBUTE) of (NODE) to (VALUE)"
            INPUT_SPECS: ClassVar = (
                ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            attribute: INPUT_COMPATIBLE_T
            node: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class remove_attribute(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::remove attribute (ATTRIBUTE) of (NODE)"
            INPUT_SPECS: ClassVar = (
                ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
                ("NODE", "node", p.SRBlockOnlyInputValue, None),
            )
            attribute: INPUT_COMPATIBLE_T
            node: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class remove_attributes(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::remove all attributes of (NODE)"
            INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
            node: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class has_attribute(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::(NODE) has attribute (ATTRIBUTE)"
            INPUT_SPECS: ClassVar = (
                ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ("ATTRIBUTE", "attribute", p.SRBlockAndTextInputValue, None),
            )
            node: INPUT_COMPATIBLE_T
            attribute: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_attributes(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::attributes of (NODE)"
            INPUT_SPECS: ClassVar = (("NODE", "node", p.SRBlockOnlyInputValue, None),)
            node: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_string(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::stringify (NODE) (FORMAT)"
            INPUT_SPECS: ClassVar = (
                ("NODE", "node", p.SRBlockOnlyInputValue, None),
                ("FORMAT", "format", p.SRBlockOnlyInputValue, None),
            )
            node: INPUT_COMPATIBLE_T
            format: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class valid_name(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::is (NAME) valid name"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class to_string_safe(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::make (TEXT) XML safe"
            INPUT_SPECS: ClassVar = (
                ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            )
            text: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class filter_array(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::elements named (NAME) in (INPUT)"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ("INPUT", "input", p.SRBlockOnlyInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            input: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class menu_stringify_format(ThirdBlock):
            OPCODE: ClassVar = "&jwXML::#menu:stringifyFormat"

    class newCanvas:

        @grepr_dataclass()
        class canvas_getter(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::[canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class set_size(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::set width: (width) height: (height) of [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("width", "width", p.SRBlockAndTextInputValue, None),
                ("height", "height", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class set_property(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set [prop] of [canvas] to"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"), ("prop", "prop"))
            canvas: str
            prop: str

        @grepr_dataclass()
        class get_property(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::get [prop] of [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"), ("prop", "prop"))
            canvas: str
            prop: str

        @grepr_dataclass()
        class dash(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set line dash to (dashing) in [canvas]"
            INPUT_SPECS: ClassVar = (
                ("dashing", "dashing", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            dashing: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class clear_canvas(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::clear canvas [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class clear_aria(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::clear area at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                ("width", "width", p.SRBlockAndTextInputValue, None),
                ("height", "height", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class draw_text(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::draw text (text) at (x) (y) onto [canvas]"
            INPUT_SPECS: ClassVar = (
                ("text", "text", p.SRBlockAndTextInputValue, None),
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            text: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class draw_text_with_cap(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::draw text (text) at (x) (y) with size cap (cap) onto [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("text", "text", p.SRBlockAndTextInputValue, None),
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                ("cap", "cap", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            text: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            cap: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class outline_text(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::draw text outline for (text) at (x) (y) onto [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("text", "text", p.SRBlockAndTextInputValue, None),
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            text: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class outline_text_with_cap(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::draw text outline for (text) at (x) (y) with size cap (cap) onto [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("text", "text", p.SRBlockAndTextInputValue, None),
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                ("cap", "cap", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            text: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            cap: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class draw_rect(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::draw rectangle at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                ("width", "width", p.SRBlockAndTextInputValue, None),
                ("height", "height", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class outline_rect(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::draw rectangle outline at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                ("width", "width", p.SRBlockAndTextInputValue, None),
                ("height", "height", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class preload_uri_image(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::preload image (URI) as (NAME)"
            INPUT_SPECS: ClassVar = (
                ("URI", "uri", p.SRBlockAndTextInputValue, None),
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            uri: INPUT_COMPATIBLE_T
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class unload_uri_image(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::unload image (NAME)"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_width_of_preloaded(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::get width of (name)"
            INPUT_SPECS: ClassVar = (
                ("name", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class get_height_of_preloaded(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::get height of (name)"
            INPUT_SPECS: ClassVar = (
                ("name", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class draw_uri_image(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::draw image (URI) at x:[X] y:[Y] onto canvas [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("URI", "uri", p.SRBlockAndTextInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            uri: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class draw_uri_image_whr(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] pointed at: (ROTATE) onto canvas [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("URI", "uri", p.SRBlockAndTextInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
                ("WIDTH", "width", p.SRBlockAndTextInputValue, None),
                ("HEIGHT", "height", p.SRBlockAndTextInputValue, None),
                ("ROTATE", "rotate", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            uri: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            rotate: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class draw_uri_image_whcx1_y1_x2_y2_r(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] cropping from x:[CROPX] y:[CROPY] width:[CROPW] height:[CROPH] pointed at: (ROTATE) onto canvas [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("URI", "uri", p.SRBlockAndTextInputValue, None),
                ("X", "x", p.SRBlockAndTextInputValue, None),
                ("Y", "y", p.SRBlockAndTextInputValue, None),
                ("WIDTH", "width", p.SRBlockAndTextInputValue, None),
                ("HEIGHT", "height", p.SRBlockAndTextInputValue, None),
                ("CROPX", "cropx", p.SRBlockAndTextInputValue, None),
                ("CROPY", "cropy", p.SRBlockAndTextInputValue, None),
                ("CROPW", "cropw", p.SRBlockAndTextInputValue, None),
                ("CROPH", "croph", p.SRBlockAndTextInputValue, None),
                ("ROTATE", "rotate", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            uri: INPUT_COMPATIBLE_T
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            cropx: INPUT_COMPATIBLE_T
            cropy: INPUT_COMPATIBLE_T
            cropw: INPUT_COMPATIBLE_T
            croph: INPUT_COMPATIBLE_T
            rotate: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class begin_path(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::begin path drawing on [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class move_to(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::move pen to x:[x] y:[y] on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class line_to(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::add line going to x:[x] y:[y] on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class arc_to(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::add arc going to x:[x] y:[y] on [canvas] with control points {:controlPoints:} and radius (radius)"
            )
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                (
                    "controlPoints",
                    "control_points",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.newCanvas.param(),
                ),
                ("radius", "radius", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            radius: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class add_rect(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::add a rectangle at x:[x] y:[y] with width:[width] height:[height] to [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                ("width", "width", p.SRBlockAndTextInputValue, None),
                ("height", "height", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class add_ellipse(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::add a ellipse at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                ("width", "width", p.SRBlockAndTextInputValue, None),
                ("height", "height", p.SRBlockAndTextInputValue, None),
                ("dir", "dir", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            dir: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class add_ellipse_start_stop(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::add a ellipse with starting rotation (start) and ending rotation (end) at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
                ("width", "width", p.SRBlockAndTextInputValue, None),
                ("height", "height", p.SRBlockAndTextInputValue, None),
                ("start", "start", p.SRBlockAndTextInputValue, None),
                ("end", "end", p.SRBlockAndTextInputValue, None),
                ("dir", "dir", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            width: INPUT_COMPATIBLE_T
            height: INPUT_COMPATIBLE_T
            start: INPUT_COMPATIBLE_T
            end: INPUT_COMPATIBLE_T
            dir: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class close_path(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::attempt to close any open path in [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class stroke(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::draw outline for current path in [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class fill(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::draw fill for current path in [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class save_transform(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::save [canvas]'s transform"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class restore_transform(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::reset to [canvas]'s saved transform"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class turn_rotation_left(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::turn left (degrees) in [canvas]"
            INPUT_SPECS: ClassVar = (
                ("degrees", "degrees", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            degrees: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class turn_rotation_right(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::turn right (degrees) in [canvas]"
            INPUT_SPECS: ClassVar = (
                ("degrees", "degrees", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            degrees: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class set_rotation(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set rotation to (degrees) in [canvas]"
            INPUT_SPECS: ClassVar = (
                ("degrees", "degrees", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            degrees: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class set_translate_xy(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set translation X: (x) Y: (y) on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class change_translate_xy(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::change translation X: (x) Y: (y) on [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("x", "x", p.SRBlockAndTextInputValue, None),
                ("y", "y", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            x: INPUT_COMPATIBLE_T
            y: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class change_translate_x(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::change X translation by (amount) on [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("amount", "amount", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            amount: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class set_translate_x(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set X scaler to (amount) on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("amount", "amount", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            amount: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class change_translate_y(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::change Y translation by (amount) on [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("amount", "amount", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            amount: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class set_translate_y(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set Y translation by (amount) on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("amount", "amount", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            amount: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class change_scale_xy(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::change XY scaler by [percent]% on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("percent", "percent", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            percent: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class set_scale_xy(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set XY scaler to [percent]% on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("percent", "percent", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            percent: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class change_scale_x(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::change X scaler by [percent]% on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("percent", "percent", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            percent: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class set_scale_x(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set X scaler to [percent]% on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("percent", "percent", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            percent: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class change_scale_y(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::change Y scaler by [percent]% on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("percent", "percent", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            percent: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class set_scale_y(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set Y scaler to [percent]% on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("percent", "percent", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            percent: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class reset_transform(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::clear transform in [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class load_transform(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set new transform (transform) on [canvas]"
            INPUT_SPECS: ClassVar = (
                ("transform", "transform", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            transform: INPUT_COMPATIBLE_T
            canvas: str

        @grepr_dataclass()
        class get_transform(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::get current transform in [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class put_onto_sprite(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::set this sprites costume to [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class get_data_uri(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::get data URL of [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class get_width_of_canvas(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::get width of [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class get_height_of_canvas(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::get height of [canvas]"
            DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
            canvas: str

        @grepr_dataclass()
        class get_drawn_width_of_text(ThirdBlock):
            OPCODE: ClassVar = (
                "&newCanvas::get [dimension] of text (text) when drawn to [canvas]"
            )
            INPUT_SPECS: ClassVar = (
                ("text", "text", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (
                ("dimension", "dimension"),
                ("canvas", "canvas"),
            )
            text: INPUT_COMPATIBLE_T
            dimension: str
            canvas: str

        @grepr_dataclass()
        class menu_text_dimension(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::#menu:textDimension"

        @grepr_dataclass()
        class menu_canvas(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::#menu:canvas"

        @grepr_dataclass()
        class menu_canvas_props(ThirdBlock):
            OPCODE: ClassVar = "&newCanvas::#menu:canvasProps"

    class steve0greatnesstimers:

        @grepr_dataclass()
        class getter(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::[TIMER]"
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
            timer: str

        @grepr_dataclass()
        class elapsed(ThirdBlock):
            OPCODE: ClassVar = (
                "&steve0greatnesstimers::time elapsed for [TIMER] in [UNITS]"
            )
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"), ("UNITS", "units"))
            timer: str
            units: str

        @grepr_dataclass()
        class pause(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::pause [TIMER]"
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
            timer: str

        @grepr_dataclass()
        class toggle(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::toggle [TIMER]"
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
            timer: str

        @grepr_dataclass()
        class unpause(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::start [TIMER]"
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
            timer: str

        @grepr_dataclass()
        class is_paused(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::is [TIMER] paused?"
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
            timer: str

        @grepr_dataclass()
        class restart(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::restart [TIMER]"
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
            timer: str

        @grepr_dataclass()
        class stop(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::stop [TIMER]"
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
            timer: str

        @grepr_dataclass()
        class add(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::add (TIME) [UNITS] to [TIMER]"
            INPUT_SPECS: ClassVar = (
                ("TIME", "time", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("UNITS", "units"), ("TIMER", "timer"))
            time: INPUT_COMPATIBLE_T
            units: str
            timer: str

        @grepr_dataclass()
        class whengt(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::when [TIMER] > (TIME) [UNITS]"
            INPUT_SPECS: ClassVar = (
                ("TIME", "time", p.SRBlockAndTextInputValue, None),
            )
            DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"), ("UNITS", "units"))
            time: INPUT_COMPATIBLE_T
            timer: str
            units: str

        @grepr_dataclass()
        class menu_timers(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::#menu:TIMERS"

        @grepr_dataclass()
        class menu_units_get(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::#menu:UNITS_GET"

        @grepr_dataclass()
        class menu_units_set(ThirdBlock):
            OPCODE: ClassVar = "&steve0greatnesstimers::#menu:UNITS_SET"

    class jwProto:

        @grepr_dataclass()
        class label_function(ThirdBlock):
            OPCODE: ClassVar = "&jwProto::// (LABEL) {SUBSTACK}"
            INPUT_SPECS: ClassVar = (
                ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            label: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class label_command(ThirdBlock):
            OPCODE: ClassVar = "&jwProto::// (LABEL) {{id=jwProto_labelCommand}}"
            INPUT_SPECS: ClassVar = (
                ("LABEL", "label", p.SRBlockAndTextInputValue, None),
            )
            label: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class label_reporter(ThirdBlock):
            OPCODE: ClassVar = "&jwProto::(VALUE) // (LABEL)"
            INPUT_SPECS: ClassVar = (
                ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            )
            label: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class label_boolean(ThirdBlock):
            OPCODE: ClassVar = "&jwProto::<VALUE> // (LABEL)"
            INPUT_SPECS: ClassVar = (
                ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
            )
            label: INPUT_COMPATIBLE_T
            value: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class placeholder_reporter(ThirdBlock):
            OPCODE: ClassVar = "&jwProto::... {{id=jwProto_placeholderReporter}}"

        @grepr_dataclass()
        class placeholder_boolean(ThirdBlock):
            OPCODE: ClassVar = "&jwProto::... {{id=jwProto_placeholderBoolean}}"

        @grepr_dataclass()
        class label_hat(ThirdBlock):
            OPCODE: ClassVar = "&jwProto::// (LABEL) {{id=jwProto_labelHat}}"
            INPUT_SPECS: ClassVar = (
                ("LABEL", "label", p.SRBlockAndTextInputValue, None),
            )
            label: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class placeholder_command(ThirdBlock):
            OPCODE: ClassVar = "&jwProto::... {{id=jwProto_placeholderCommand}}"

    class SPjavascriptV2:

        @grepr_dataclass()
        class code_input(ThirdBlock):
            OPCODE: ClassVar = "&SPjavascriptV2::(CODE)"
            INPUT_SPECS: ClassVar = (("CODE", "code", p.SRBlockOnlyInputValue, None),)
            code: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class argument_report(ThirdBlock):
            OPCODE: ClassVar = "&SPjavascriptV2::data"

        @grepr_dataclass()
        class return_data(ThirdBlock):
            OPCODE: ClassVar = "&SPjavascriptV2::return (DATA)"
            INPUT_SPECS: ClassVar = (
                ("DATA", "data", p.SRBlockAndTextInputValue, None),
            )
            data: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class js_reporter(ThirdBlock):
            OPCODE: ClassVar = (
                "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsReporter}}"
            )
            INPUT_SPECS: ClassVar = (
                ("CODE", "code", p.SRBlockAndTextInputValue, None),
            )
            code: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class js_boolean(ThirdBlock):
            OPCODE: ClassVar = (
                "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsBoolean}}"
            )
            INPUT_SPECS: ClassVar = (
                ("CODE", "code", p.SRBlockAndTextInputValue, None),
            )
            code: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class js_reporter_binded(ThirdBlock):
            OPCODE: ClassVar = (
                "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsReporterBinded}}"
            )
            INPUT_SPECS: ClassVar = (
                (
                    "CODE",
                    "code",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.SPjavascriptV2.code_input(),
                ),
                ("ARGS", "args", p.SRBlockAndTextInputValue, None),
            )
            args: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class js_boolean_binded(ThirdBlock):
            OPCODE: ClassVar = (
                "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsBooleanBinded}}"
            )
            INPUT_SPECS: ClassVar = (
                (
                    "CODE",
                    "code",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.SPjavascriptV2.code_input(),
                ),
                ("ARGS", "args", p.SRBlockAndTextInputValue, None),
            )
            args: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_global_func(ThirdBlock):
            OPCODE: ClassVar = (
                "&SPjavascriptV2::create global function named (NAME) with code {:CODE:}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                (
                    "CODE",
                    "code",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.SPjavascriptV2.code_input(),
                ),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class define_scratch_code(ThirdBlock):
            OPCODE: ClassVar = (
                "&SPjavascriptV2::create local function named (NAME) with code {:CODE:} {SUBSTACK}"
            )
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
                (
                    "CODE",
                    "code",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.SPjavascriptV2.argument_report(),
                ),
                ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            )
            name: INPUT_COMPATIBLE_T
            substack: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class delete_global_func(ThirdBlock):
            OPCODE: ClassVar = "&SPjavascriptV2::delete global function (NAME)"
            INPUT_SPECS: ClassVar = (
                ("NAME", "name", p.SRBlockAndTextInputValue, None),
            )
            name: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class js_command_binded(ThirdBlock):
            OPCODE: ClassVar = (
                "&SPjavascriptV2::run {:CODE:} with data (ARGS) {{id=SPjavascriptV2_jsCommandBinded}}"
            )
            INPUT_SPECS: ClassVar = (
                (
                    "CODE",
                    "code",
                    p.SREmbeddedBlockInputValue,
                    lambda: h.SPjavascriptV2.code_input(),
                ),
                ("ARGS", "args", p.SRBlockAndTextInputValue, None),
            )
            args: INPUT_COMPATIBLE_T

        @grepr_dataclass()
        class js_command(ThirdBlock):
            OPCODE: ClassVar = (
                "&SPjavascriptV2::run (CODE) {{id=SPjavascriptV2_jsCommand}}"
            )
            INPUT_SPECS: ClassVar = (
                ("CODE", "code", p.SRBlockAndTextInputValue, None),
            )
            code: INPUT_COMPATIBLE_T


h = BlockHelpers
