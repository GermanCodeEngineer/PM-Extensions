from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class looks:

    @staticmethod
    def sayforsecs(
        message: INPUT_COMPATIBLE_T, seconds: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::say (MESSAGE) for (SECONDS) seconds",
            inputs={
                "MESSAGE": InputValue.try_as_input(message, p.SRBlockAndTextInputValue),
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def say(message: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::say (MESSAGE)",
            inputs={
                "MESSAGE": InputValue.try_as_input(message, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def thinkforsecs(
        message: INPUT_COMPATIBLE_T, seconds: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::think (MESSAGE) for (SECONDS) seconds",
            inputs={
                "MESSAGE": InputValue.try_as_input(message, p.SRBlockAndTextInputValue),
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def think(message: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::think (MESSAGE)",
            inputs={
                "MESSAGE": InputValue.try_as_input(message, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def stoptalking() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::stop speaking", inputs={}, dropdowns={})

    @staticmethod
    def set_font(font: INPUT_COMPATIBLE_T, font_size: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::set font to (FONT) with font size (FONT-SIZE)",
            inputs={
                "FONT": InputValue.try_as_input(font, p.SRBlockAndTextInputValue),
                "FONT-SIZE": InputValue.try_as_input(
                    font_size, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def set_color(color: INPUT_COMPATIBLE_T, property: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::set [PROPERTY] color to (COLOR)",
            inputs={
                "COLOR": InputValue.try_as_input(color, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "PROPERTY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, property)
            },
        )

    @staticmethod
    def set_shape(value: INPUT_COMPATIBLE_T, property: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::set text bubble [PROPERTY] to (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "PROPERTY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, property)
            },
        )

    @staticmethod
    def say_width() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::bubble width", inputs={}, dropdowns={})

    @staticmethod
    def say_height() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::bubble height", inputs={}, dropdowns={})

    @staticmethod
    def switchcostumeto(costume: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::switch costume to ([COSTUME])",
            inputs={
                "COSTUME": InputValue.try_as_input(
                    costume, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def nextcostume() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::next costume", inputs={}, dropdowns={})

    @staticmethod
    def getinputofcostume(
        property: INPUT_COMPATIBLE_T, costume: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::([PROPERTY]) of ([COSTUME])",
            inputs={
                "PROPERTY": InputValue.try_as_input(
                    property, p.SRBlockAndDropdownInputValue
                ),
                "COSTUME": InputValue.try_as_input(
                    costume, p.SRBlockAndDropdownInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def switchbackdropto(backdrop: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::switch backdrop to ([BACKDROP])",
            inputs={
                "BACKDROP": InputValue.try_as_input(
                    backdrop, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def nextbackdrop() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::next backdrop", inputs={}, dropdowns={})

    @staticmethod
    def changesizeby(amount: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::change size by (AMOUNT)",
            inputs={
                "AMOUNT": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def setsizeto(size: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::set size to (SIZE)",
            inputs={"SIZE": InputValue.try_as_input(size, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def set_stretch(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::set stretch to x: (X) y: (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def change_stretch(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks:: change stretch by x: (X) y: (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def stretch_get_x() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::x stretch", inputs={}, dropdowns={})

    @staticmethod
    def stretch_get_y() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::y stretch", inputs={}, dropdowns={})

    @staticmethod
    def changeeffectby(amount: INPUT_COMPATIBLE_T, effect: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::change [EFFECT] effect by (AMOUNT)",
            inputs={
                "AMOUNT": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "EFFECT": p.SRDropdownValue(p.DropdownValueKind.STANDARD, effect)
            },
        )

    @staticmethod
    def seteffectto(value: INPUT_COMPATIBLE_T, effect: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::set [EFFECT] effect to (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "EFFECT": p.SRDropdownValue(p.DropdownValueKind.STANDARD, effect)
            },
        )

    @staticmethod
    def set_tint_color(color: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::set tint color to (COLOR)",
            inputs={
                "COLOR": InputValue.try_as_input(color, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def cleargraphiceffects() -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::clear graphic effects", inputs={}, dropdowns={}
        )

    @staticmethod
    def get_effect_value(effect: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::[EFFECT] effect",
            inputs={},
            dropdowns={
                "EFFECT": p.SRDropdownValue(p.DropdownValueKind.STANDARD, effect)
            },
        )

    @staticmethod
    def tint_color() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::tint color", inputs={}, dropdowns={})

    @staticmethod
    def show() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::show", inputs={}, dropdowns={})

    @staticmethod
    def hide() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::hide", inputs={}, dropdowns={})

    @staticmethod
    def get_sprite_visible() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::visible?", inputs={}, dropdowns={})

    @staticmethod
    def change_visibility_of_sprite_show(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::show ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def change_visibility_of_sprite_hide(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::hide ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def get_other_sprite_visible(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sounds::is ([TARGET]) visible?",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def gotofrontback(layer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::go to [LAYER] layer",
            inputs={},
            dropdowns={"LAYER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, layer)},
        )

    @staticmethod
    def goforwardbackwardlayers(
        layers: INPUT_COMPATIBLE_T, direction: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::go [DIRECTION] (LAYERS) layers",
            inputs={
                "LAYERS": InputValue.try_as_input(layers, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "DIRECTION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, direction)
            },
        )

    @staticmethod
    def layers_set_layer(layer: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::go to layer (LAYER)",
            inputs={
                "LAYER": InputValue.try_as_input(layer, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def go_target_layer(target: INPUT_COMPATIBLE_T, direction: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::go [DIRECTION] ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={
                "DIRECTION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, direction)
            },
        )

    @staticmethod
    def layers_get_layer() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::layer", inputs={}, dropdowns={})

    @staticmethod
    def costumenumbername(property: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::costume [PROPERTY]",
            inputs={},
            dropdowns={
                "PROPERTY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, property)
            },
        )

    @staticmethod
    def backdropnumbername(property: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::backdrop [PROPERTY]",
            inputs={},
            dropdowns={
                "PROPERTY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, property)
            },
        )

    @staticmethod
    def size() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::size", inputs={}, dropdowns={})

    @staticmethod
    def costume() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::#COSTUME MENU", inputs={}, dropdowns={})

    @staticmethod
    def backdrops() -> p.SRBlock:
        return p.SRBlock(opcode="&looks::#BACKDROP MENU", inputs={}, dropdowns={})

    @staticmethod
    def getinput_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::#COSTUME PROPERTY MENU", inputs={}, dropdowns={}
        )

    @staticmethod
    def change_visibility_of_sprite_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::#SHOW/HIDE SPRITE MENU", inputs={}, dropdowns={}
        )

    @staticmethod
    def get_other_sprite_visible_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&looks::#IS SPRITE VISIBLE MENU", inputs={}, dropdowns={}
        )
