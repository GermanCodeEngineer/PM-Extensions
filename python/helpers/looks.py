from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class looks:

    @grepr_dataclass()
    class sayforsecs(ThirdBlock):
        message: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::say (MESSAGE) for (SECONDS) seconds",
                inputs={
                    "MESSAGE": ThirdInputValue.as_input(
                        self.message, p.SRBlockAndTextInputValue
                    ),
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class say(ThirdBlock):
        message: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::say (MESSAGE)",
                inputs={
                    "MESSAGE": ThirdInputValue.as_input(
                        self.message, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class thinkforsecs(ThirdBlock):
        message: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::think (MESSAGE) for (SECONDS) seconds",
                inputs={
                    "MESSAGE": ThirdInputValue.as_input(
                        self.message, p.SRBlockAndTextInputValue
                    ),
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class think(ThirdBlock):
        message: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::think (MESSAGE)",
                inputs={
                    "MESSAGE": ThirdInputValue.as_input(
                        self.message, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class stoptalking(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::stop speaking", inputs={}, dropdowns={})

    @grepr_dataclass()
    class set_font(ThirdBlock):
        font: INPUT_COMPATIBLE_T
        font_size: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::set font to (FONT) with font size (FONT-SIZE)",
                inputs={
                    "FONT": ThirdInputValue.as_input(
                        self.font, p.SRBlockAndTextInputValue
                    ),
                    "FONT-SIZE": ThirdInputValue.as_input(
                        self.font_size, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_color(ThirdBlock):
        color: INPUT_COMPATIBLE_T
        property: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::set [PROPERTY] color to (COLOR)",
                inputs={
                    "COLOR": ThirdInputValue.as_input(
                        self.color, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "PROPERTY": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.property
                    )
                },
            )

    @grepr_dataclass()
    class set_shape(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        property: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::set text bubble [PROPERTY] to (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "PROPERTY": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.property
                    )
                },
            )

    @grepr_dataclass()
    class say_width(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::bubble width", inputs={}, dropdowns={})

    @grepr_dataclass()
    class say_height(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::bubble height", inputs={}, dropdowns={})

    @grepr_dataclass()
    class switchcostumeto(ThirdBlock):
        costume: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::switch costume to ([COSTUME])",
                inputs={
                    "COSTUME": ThirdInputValue.as_input(
                        self.costume, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class nextcostume(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::next costume", inputs={}, dropdowns={})

    @grepr_dataclass()
    class getinputofcostume(ThirdBlock):
        property: INPUT_COMPATIBLE_T
        costume: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::([PROPERTY]) of ([COSTUME])",
                inputs={
                    "PROPERTY": ThirdInputValue.as_input(
                        self.property, p.SRBlockAndDropdownInputValue
                    ),
                    "COSTUME": ThirdInputValue.as_input(
                        self.costume, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class switchbackdropto(ThirdBlock):
        backdrop: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::switch backdrop to ([BACKDROP])",
                inputs={
                    "BACKDROP": ThirdInputValue.as_input(
                        self.backdrop, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class nextbackdrop(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::next backdrop", inputs={}, dropdowns={})

    @grepr_dataclass()
    class changesizeby(ThirdBlock):
        amount: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::change size by (AMOUNT)",
                inputs={
                    "AMOUNT": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class setsizeto(ThirdBlock):
        size: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::set size to (SIZE)",
                inputs={
                    "SIZE": ThirdInputValue.as_input(
                        self.size, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_stretch(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::set stretch to x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class change_stretch(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks:: change stretch by x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class stretch_get_x(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::x stretch", inputs={}, dropdowns={})

    @grepr_dataclass()
    class stretch_get_y(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::y stretch", inputs={}, dropdowns={})

    @grepr_dataclass()
    class changeeffectby(ThirdBlock):
        amount: INPUT_COMPATIBLE_T
        effect: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::change [EFFECT] effect by (AMOUNT)",
                inputs={
                    "AMOUNT": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "EFFECT": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.effect
                    )
                },
            )

    @grepr_dataclass()
    class seteffectto(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        effect: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::set [EFFECT] effect to (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "EFFECT": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.effect
                    )
                },
            )

    @grepr_dataclass()
    class set_tint_color(ThirdBlock):
        color: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::set tint color to (COLOR)",
                inputs={
                    "COLOR": ThirdInputValue.as_input(
                        self.color, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class cleargraphiceffects(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::clear graphic effects", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class get_effect_value(ThirdBlock):
        effect: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::[EFFECT] effect",
                inputs={},
                dropdowns={
                    "EFFECT": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.effect
                    )
                },
            )

    @grepr_dataclass()
    class tint_color(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::tint color", inputs={}, dropdowns={})

    @grepr_dataclass()
    class show(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::show", inputs={}, dropdowns={})

    @grepr_dataclass()
    class hide(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::hide", inputs={}, dropdowns={})

    @grepr_dataclass()
    class get_sprite_visible(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::visible?", inputs={}, dropdowns={})

    @grepr_dataclass()
    class change_visibility_of_sprite_show(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::show ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class change_visibility_of_sprite_hide(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::hide ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_other_sprite_visible(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sounds::is ([TARGET]) visible?",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class gotofrontback(ThirdBlock):
        layer: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::go to [LAYER] layer",
                inputs={},
                dropdowns={
                    "LAYER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.layer)
                },
            )

    @grepr_dataclass()
    class goforwardbackwardlayers(ThirdBlock):
        layers: INPUT_COMPATIBLE_T
        direction: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::go [DIRECTION] (LAYERS) layers",
                inputs={
                    "LAYERS": ThirdInputValue.as_input(
                        self.layers, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "DIRECTION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.direction
                    )
                },
            )

    @grepr_dataclass()
    class layers_set_layer(ThirdBlock):
        layer: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::go to layer (LAYER)",
                inputs={
                    "LAYER": ThirdInputValue.as_input(
                        self.layer, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class go_target_layer(ThirdBlock):
        target: INPUT_COMPATIBLE_T
        direction: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::go [DIRECTION] ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={
                    "DIRECTION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.direction
                    )
                },
            )

    @grepr_dataclass()
    class layers_get_layer(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::layer", inputs={}, dropdowns={})

    @grepr_dataclass()
    class costumenumbername(ThirdBlock):
        property: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::costume [PROPERTY]",
                inputs={},
                dropdowns={
                    "PROPERTY": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.property
                    )
                },
            )

    @grepr_dataclass()
    class backdropnumbername(ThirdBlock):
        property: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::backdrop [PROPERTY]",
                inputs={},
                dropdowns={
                    "PROPERTY": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.property
                    )
                },
            )

    @grepr_dataclass()
    class size(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::size", inputs={}, dropdowns={})

    @grepr_dataclass()
    class costume(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::#COSTUME MENU", inputs={}, dropdowns={})

    @grepr_dataclass()
    class backdrops(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::#BACKDROP MENU", inputs={}, dropdowns={})

    @grepr_dataclass()
    class getinput_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::#COSTUME PROPERTY MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class change_visibility_of_sprite_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::#SHOW/HIDE SPRITE MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class get_other_sprite_visible_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::#IS SPRITE VISIBLE MENU", inputs={}, dropdowns={}
            )
