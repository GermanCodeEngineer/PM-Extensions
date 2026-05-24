from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmSensingExpansion:

    @grepr_dataclass()
    class battery_percentage(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::battery percentage",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class battery_charging(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::is device charging?",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class vibrate_device(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::vibrate", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class browser_language(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::preferred language",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class url_options(ThirdBlock):
        options: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::url ([OPTIONS])",
                inputs={
                    "OPTIONS": ThirdInputValue.as_input(
                        self.options, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class url_options_of(ThirdBlock):
        options: INPUT_COMPATIBLE_T
        url: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::([OPTIONS]) of url (URL)",
                inputs={
                    "OPTIONS": ThirdInputValue.as_input(
                        self.options, p.SRBlockAndDropdownInputValue
                    ),
                    "URL": ThirdInputValue.as_input(
                        self.url, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_username(ThirdBlock):
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::set username to (NAME)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_url_end(ThirdBlock):
        path: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::set url path to (PATH)",
                inputs={
                    "PATH": ThirdInputValue.as_input(
                        self.path, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class query_param_of_url(ThirdBlock):
        param: INPUT_COMPATIBLE_T
        url: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::query parameter (PARAM) of url (URL)",
                inputs={
                    "PARAM": ThirdInputValue.as_input(
                        self.param, p.SRBlockAndTextInputValue
                    ),
                    "URL": ThirdInputValue.as_input(
                        self.url, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class packaged(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::project packaged?", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class sprite_name(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::sprite name", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class framed(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::project in iframe?",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class current_millisecond(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::current millisecond",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class delta_time(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::delta time", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class pick_color(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::grab color at x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class max_sprite_layers(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::max sprite layers", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class average_loudness(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::average loudness", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class scrolling_distance(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::scrolling distance",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class set_scrolling_distance(ThirdBlock):
        amount: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::set scrolling distance to (AMOUNT)",
                inputs={
                    "AMOUNT": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class change_scrolling_distance_by(ThirdBlock):
        amount: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::change scrolling distance by (AMOUNT)",
                inputs={
                    "AMOUNT": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class current_key_pressed(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::current key pressed",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class get_last_key_pressed(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::last key pressed", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class get_button_is_down(ThirdBlock):
        mouse_button: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::([MOUSE_BUTTON]) mouse button down?",
                inputs={
                    "MOUSE_BUTTON": ThirdInputValue.as_input(
                        self.mouse_button, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class changed(ThirdBlock):
        one: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::(ONE) changed?",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class amount_of_time_key_has_been_held(ThirdBlock):
        key: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::seconds since holding ([KEY])",
                inputs={
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_key(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::#menu:key", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_mouse_button(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::#menu:mouseButton", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_url_sections(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::#menu:urlSections", inputs={}, dropdowns={}
            )
