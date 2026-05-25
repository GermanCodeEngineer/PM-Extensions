from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class looks:

    @grepr_dataclass()
    class sayforsecs(ThirdBlock):
        OPCODE = "&looks::say (MESSAGE) for (SECONDS) seconds"
        message: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class say(ThirdBlock):
        OPCODE = "&looks::say (MESSAGE)"
        message: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("MESSAGE", "message", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("MESSAGE", "message", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class thinkforsecs(ThirdBlock):
        OPCODE = "&looks::think (MESSAGE) for (SECONDS) seconds"
        message: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("MESSAGE", "message", p.SRBlockAndTextInputValue, None),
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class think(ThirdBlock):
        OPCODE = "&looks::think (MESSAGE)"
        message: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("MESSAGE", "message", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("MESSAGE", "message", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class stoptalking(ThirdBlock):
        OPCODE = "&looks::stop speaking"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class set_font(ThirdBlock):
        OPCODE = "&looks::set font to (FONT) with font size (FONT-SIZE)"
        font: INPUT_COMPATIBLE_T
        font_size: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("FONT", "font", p.SRBlockAndTextInputValue, None),
                    ("FONT-SIZE", "font_size", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("FONT", "font", p.SRBlockAndTextInputValue, None),
                    ("FONT-SIZE", "font_size", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_color(ThirdBlock):
        OPCODE = "&looks::set [PROPERTY] color to (COLOR)"
        color: INPUT_COMPATIBLE_T
        property: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("COLOR", "color", p.SRBlockAndTextInputValue, None),),
                (("PROPERTY", "property"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("COLOR", "color", p.SRBlockAndTextInputValue, None),),
                (("PROPERTY", "property"),),
            )

    @grepr_dataclass()
    class set_shape(ThirdBlock):
        OPCODE = "&looks::set text bubble [PROPERTY] to (VALUE)"
        value: INPUT_COMPATIBLE_T
        property: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("PROPERTY", "property"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("PROPERTY", "property"),),
            )

    @grepr_dataclass()
    class say_width(ThirdBlock):
        OPCODE = "&looks::bubble width"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class say_height(ThirdBlock):
        OPCODE = "&looks::bubble height"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class switchcostumeto(ThirdBlock):
        OPCODE = "&looks::switch costume to ([COSTUME])"
        costume: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class nextcostume(ThirdBlock):
        OPCODE = "&looks::next costume"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class getinputofcostume(ThirdBlock):
        OPCODE = "&looks::([PROPERTY]) of ([COSTUME])"
        property: INPUT_COMPATIBLE_T
        costume: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
                    ("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
                    ("COSTUME", "costume", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class switchbackdropto(ThirdBlock):
        OPCODE = "&looks::switch backdrop to ([BACKDROP])"
        backdrop: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BACKDROP", "backdrop", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BACKDROP", "backdrop", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class nextbackdrop(ThirdBlock):
        OPCODE = "&looks::next backdrop"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class changesizeby(ThirdBlock):
        OPCODE = "&looks::change size by (AMOUNT)"
        amount: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class setsizeto(ThirdBlock):
        OPCODE = "&looks::set size to (SIZE)"
        size: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SIZE", "size", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SIZE", "size", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class set_stretch(ThirdBlock):
        OPCODE = "&looks::set stretch to x: (X) y: (Y)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class change_stretch(ThirdBlock):
        OPCODE = "&looks:: change stretch by x: (X) y: (Y)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class stretch_get_x(ThirdBlock):
        OPCODE = "&looks::x stretch"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class stretch_get_y(ThirdBlock):
        OPCODE = "&looks::y stretch"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class changeeffectby(ThirdBlock):
        OPCODE = "&looks::change [EFFECT] effect by (AMOUNT)"
        amount: INPUT_COMPATIBLE_T
        effect: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),),
                (("EFFECT", "effect"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),),
                (("EFFECT", "effect"),),
            )

    @grepr_dataclass()
    class seteffectto(ThirdBlock):
        OPCODE = "&looks::set [EFFECT] effect to (VALUE)"
        value: INPUT_COMPATIBLE_T
        effect: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("EFFECT", "effect"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("EFFECT", "effect"),),
            )

    @grepr_dataclass()
    class set_tint_color(ThirdBlock):
        OPCODE = "&looks::set tint color to (COLOR)"
        color: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("COLOR", "color", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("COLOR", "color", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class cleargraphiceffects(ThirdBlock):
        OPCODE = "&looks::clear graphic effects"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class get_effect_value(ThirdBlock):
        OPCODE = "&looks::[EFFECT] effect"
        effect: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("EFFECT", "effect"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("EFFECT", "effect"),))

    @grepr_dataclass()
    class tint_color(ThirdBlock):
        OPCODE = "&looks::tint color"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class show(ThirdBlock):
        OPCODE = "&looks::show"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class hide(ThirdBlock):
        OPCODE = "&looks::hide"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class get_sprite_visible(ThirdBlock):
        OPCODE = "&looks::visible?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class change_visibility_of_sprite_show(ThirdBlock):
        OPCODE = "&looks::show ([TARGET])"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class change_visibility_of_sprite_hide(ThirdBlock):
        OPCODE = "&looks::hide ([TARGET])"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class get_other_sprite_visible(ThirdBlock):
        OPCODE = "&sounds::is ([TARGET]) visible?"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class gotofrontback(ThirdBlock):
        OPCODE = "&looks::go to [LAYER] layer"
        layer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("LAYER", "layer"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("LAYER", "layer"),))

    @grepr_dataclass()
    class goforwardbackwardlayers(ThirdBlock):
        OPCODE = "&looks::go [DIRECTION] (LAYERS) layers"
        layers: INPUT_COMPATIBLE_T
        direction: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LAYERS", "layers", p.SRBlockAndTextInputValue, None),),
                (("DIRECTION", "direction"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("LAYERS", "layers", p.SRBlockAndTextInputValue, None),),
                (("DIRECTION", "direction"),),
            )

    @grepr_dataclass()
    class layers_set_layer(ThirdBlock):
        OPCODE = "&looks::go to layer (LAYER)"
        layer: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LAYER", "layer", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("LAYER", "layer", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class go_target_layer(ThirdBlock):
        OPCODE = "&looks::go [DIRECTION] ([TARGET])"
        target: INPUT_COMPATIBLE_T
        direction: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (("DIRECTION", "direction"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (("DIRECTION", "direction"),),
            )

    @grepr_dataclass()
    class layers_get_layer(ThirdBlock):
        OPCODE = "&looks::layer"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class costumenumbername(ThirdBlock):
        OPCODE = "&looks::costume [PROPERTY]"
        property: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("PROPERTY", "property"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("PROPERTY", "property"),))

    @grepr_dataclass()
    class backdropnumbername(ThirdBlock):
        OPCODE = "&looks::backdrop [PROPERTY]"
        property: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("PROPERTY", "property"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("PROPERTY", "property"),))

    @grepr_dataclass()
    class size(ThirdBlock):
        OPCODE = "&looks::size"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class costume(ThirdBlock):
        OPCODE = "&looks::#COSTUME MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class backdrops(ThirdBlock):
        OPCODE = "&looks::#BACKDROP MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class getinput_menu(ThirdBlock):
        OPCODE = "&looks::#COSTUME PROPERTY MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class change_visibility_of_sprite_menu(ThirdBlock):
        OPCODE = "&looks::#SHOW/HIDE SPRITE MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class get_other_sprite_visible_menu(ThirdBlock):
        OPCODE = "&looks::#IS SPRITE VISIBLE MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
