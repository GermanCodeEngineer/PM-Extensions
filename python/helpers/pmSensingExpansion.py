from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class pmSensingExpansion:

    @grepr_dataclass()
    class battery_percentage(ThirdBlock):
        OPCODE = "&pmSensingExpansion::battery percentage"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class battery_charging(ThirdBlock):
        OPCODE = "&pmSensingExpansion::is device charging?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class vibrate_device(ThirdBlock):
        OPCODE = "&pmSensingExpansion::vibrate"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class browser_language(ThirdBlock):
        OPCODE = "&pmSensingExpansion::preferred language"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class url_options(ThirdBlock):
        OPCODE = "&pmSensingExpansion::url ([OPTIONS])"
        options: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class url_options_of(ThirdBlock):
        OPCODE = "&pmSensingExpansion::([OPTIONS]) of url (URL)"
        options: INPUT_COMPATIBLE_T
        url: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),
                    ("URL", "url", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),
                    ("URL", "url", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_username(ThirdBlock):
        OPCODE = "&pmSensingExpansion::set username to (NAME)"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NAME", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NAME", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class set_url_end(ThirdBlock):
        OPCODE = "&pmSensingExpansion::set url path to (PATH)"
        path: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("PATH", "path", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("PATH", "path", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class query_param_of_url(ThirdBlock):
        OPCODE = "&pmSensingExpansion::query parameter (PARAM) of url (URL)"
        param: INPUT_COMPATIBLE_T
        url: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PARAM", "param", p.SRBlockAndTextInputValue, None),
                    ("URL", "url", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PARAM", "param", p.SRBlockAndTextInputValue, None),
                    ("URL", "url", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class packaged(ThirdBlock):
        OPCODE = "&pmSensingExpansion::project packaged?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class sprite_name(ThirdBlock):
        OPCODE = "&pmSensingExpansion::sprite name"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class framed(ThirdBlock):
        OPCODE = "&pmSensingExpansion::project in iframe?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class current_millisecond(ThirdBlock):
        OPCODE = "&pmSensingExpansion::current millisecond"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class delta_time(ThirdBlock):
        OPCODE = "&pmSensingExpansion::delta time"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class pick_color(ThirdBlock):
        OPCODE = "&pmSensingExpansion::grab color at x: (X) y: (Y)"
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
    class max_sprite_layers(ThirdBlock):
        OPCODE = "&pmSensingExpansion::max sprite layers"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class average_loudness(ThirdBlock):
        OPCODE = "&pmSensingExpansion::average loudness"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class scrolling_distance(ThirdBlock):
        OPCODE = "&pmSensingExpansion::scrolling distance"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class set_scrolling_distance(ThirdBlock):
        OPCODE = "&pmSensingExpansion::set scrolling distance to (AMOUNT)"
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
    class change_scrolling_distance_by(ThirdBlock):
        OPCODE = "&pmSensingExpansion::change scrolling distance by (AMOUNT)"
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
    class current_key_pressed(ThirdBlock):
        OPCODE = "&pmSensingExpansion::current key pressed"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class get_last_key_pressed(ThirdBlock):
        OPCODE = "&pmSensingExpansion::last key pressed"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class get_button_is_down(ThirdBlock):
        OPCODE = "&pmSensingExpansion::([MOUSE_BUTTON]) mouse button down?"
        mouse_button: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "MOUSE_BUTTON",
                        "mouse_button",
                        p.SRBlockAndDropdownInputValue,
                        None,
                    ),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "MOUSE_BUTTON",
                        "mouse_button",
                        p.SRBlockAndDropdownInputValue,
                        None,
                    ),
                ),
                (),
            )

    @grepr_dataclass()
    class changed(ThirdBlock):
        OPCODE = "&pmSensingExpansion::(ONE) changed?"
        one: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("ONE", "one", p.SRBlockOnlyInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ONE", "one", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class amount_of_time_key_has_been_held(ThirdBlock):
        OPCODE = "&pmSensingExpansion::seconds since holding ([KEY])"
        key: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("KEY", "key", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("KEY", "key", p.SRBlockAndDropdownInputValue, None),), ()
            )

    @grepr_dataclass()
    class menu_key(ThirdBlock):
        OPCODE = "&pmSensingExpansion::#menu:key"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_mouse_button(ThirdBlock):
        OPCODE = "&pmSensingExpansion::#menu:mouseButton"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_url_sections(ThirdBlock):
        OPCODE = "&pmSensingExpansion::#menu:urlSections"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
