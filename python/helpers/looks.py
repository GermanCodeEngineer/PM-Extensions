from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class looks:

    class sayforsecs(ThirdBlock):

        def __init__(self, message: INPUT_COMPATIBLE_T, seconds: INPUT_COMPATIBLE_T):
            self.message = message
            self.seconds = seconds

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

    class say(ThirdBlock):

        def __init__(self, message: INPUT_COMPATIBLE_T):
            self.message = message

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

    class thinkforsecs(ThirdBlock):

        def __init__(self, message: INPUT_COMPATIBLE_T, seconds: INPUT_COMPATIBLE_T):
            self.message = message
            self.seconds = seconds

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

    class think(ThirdBlock):

        def __init__(self, message: INPUT_COMPATIBLE_T):
            self.message = message

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

    class stoptalking(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::stop speaking", inputs={}, dropdowns={})

    class set_font(ThirdBlock):

        def __init__(self, font: INPUT_COMPATIBLE_T, font_size: INPUT_COMPATIBLE_T):
            self.font = font
            self.font_size = font_size

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

    class set_color(ThirdBlock):

        def __init__(self, color: INPUT_COMPATIBLE_T, property: str):
            self.color = color
            self.property = property

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

    class set_shape(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, property: str):
            self.value = value
            self.property = property

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

    class say_width(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::bubble width", inputs={}, dropdowns={})

    class say_height(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::bubble height", inputs={}, dropdowns={})

    class switchcostumeto(ThirdBlock):

        def __init__(self, costume: INPUT_COMPATIBLE_T):
            self.costume = costume

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

    class nextcostume(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::next costume", inputs={}, dropdowns={})

    class getinputofcostume(ThirdBlock):

        def __init__(self, property: INPUT_COMPATIBLE_T, costume: INPUT_COMPATIBLE_T):
            self.property = property
            self.costume = costume

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

    class switchbackdropto(ThirdBlock):

        def __init__(self, backdrop: INPUT_COMPATIBLE_T):
            self.backdrop = backdrop

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

    class nextbackdrop(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::next backdrop", inputs={}, dropdowns={})

    class changesizeby(ThirdBlock):

        def __init__(self, amount: INPUT_COMPATIBLE_T):
            self.amount = amount

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

    class setsizeto(ThirdBlock):

        def __init__(self, size: INPUT_COMPATIBLE_T):
            self.size = size

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

    class set_stretch(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::set stretch to x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class change_stretch(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks:: change stretch by x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class stretch_get_x(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::x stretch", inputs={}, dropdowns={})

    class stretch_get_y(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::y stretch", inputs={}, dropdowns={})

    class changeeffectby(ThirdBlock):

        def __init__(self, amount: INPUT_COMPATIBLE_T, effect: str):
            self.amount = amount
            self.effect = effect

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

    class seteffectto(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, effect: str):
            self.value = value
            self.effect = effect

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

    class set_tint_color(ThirdBlock):

        def __init__(self, color: INPUT_COMPATIBLE_T):
            self.color = color

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

    class cleargraphiceffects(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::clear graphic effects", inputs={}, dropdowns={}
            )

    class get_effect_value(ThirdBlock):

        def __init__(self, effect: str):
            self.effect = effect

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

    class tint_color(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::tint color", inputs={}, dropdowns={})

    class show(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::show", inputs={}, dropdowns={})

    class hide(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::hide", inputs={}, dropdowns={})

    class get_sprite_visible(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::visible?", inputs={}, dropdowns={})

    class change_visibility_of_sprite_show(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class change_visibility_of_sprite_hide(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class get_other_sprite_visible(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class gotofrontback(ThirdBlock):

        def __init__(self, layer: str):
            self.layer = layer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::go to [LAYER] layer",
                inputs={},
                dropdowns={
                    "LAYER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.layer)
                },
            )

    class goforwardbackwardlayers(ThirdBlock):

        def __init__(self, layers: INPUT_COMPATIBLE_T, direction: str):
            self.layers = layers
            self.direction = direction

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

    class layers_set_layer(ThirdBlock):

        def __init__(self, layer: INPUT_COMPATIBLE_T):
            self.layer = layer

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

    class go_target_layer(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T, direction: str):
            self.target = target
            self.direction = direction

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

    class layers_get_layer(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::layer", inputs={}, dropdowns={})

    class costumenumbername(ThirdBlock):

        def __init__(self, property: str):
            self.property = property

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

    class backdropnumbername(ThirdBlock):

        def __init__(self, property: str):
            self.property = property

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

    class size(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::size", inputs={}, dropdowns={})

    class costume(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::#COSTUME MENU", inputs={}, dropdowns={})

    class backdrops(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&looks::#BACKDROP MENU", inputs={}, dropdowns={})

    class getinput_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::#COSTUME PROPERTY MENU", inputs={}, dropdowns={}
            )

    class change_visibility_of_sprite_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::#SHOW/HIDE SPRITE MENU", inputs={}, dropdowns={}
            )

    class get_other_sprite_visible_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&looks::#IS SPRITE VISIBLE MENU", inputs={}, dropdowns={}
            )
