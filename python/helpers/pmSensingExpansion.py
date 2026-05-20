from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmSensingExpansion:

    class battery_percentage(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::battery percentage",
                inputs={},
                dropdowns={},
            )

    class battery_charging(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::is device charging?",
                inputs={},
                dropdowns={},
            )

    class vibrate_device(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::vibrate", inputs={}, dropdowns={}
            )

    class browser_language(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::preferred language",
                inputs={},
                dropdowns={},
            )

    class url_options(ThirdBlock):

        def __init__(self, options: INPUT_COMPATIBLE_T):
            self.options = options

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

    class url_options_of(ThirdBlock):

        def __init__(self, options: INPUT_COMPATIBLE_T, url: INPUT_COMPATIBLE_T):
            self.options = options
            self.url = url

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

    class set_username(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T):
            self.name = name

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

    class set_url_end(ThirdBlock):

        def __init__(self, path: INPUT_COMPATIBLE_T):
            self.path = path

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

    class query_param_of_url(ThirdBlock):

        def __init__(self, param: INPUT_COMPATIBLE_T, url: INPUT_COMPATIBLE_T):
            self.param = param
            self.url = url

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

    class packaged(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::project packaged?", inputs={}, dropdowns={}
            )

    class sprite_name(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::sprite name", inputs={}, dropdowns={}
            )

    class framed(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::project in iframe?",
                inputs={},
                dropdowns={},
            )

    class current_millisecond(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::current millisecond",
                inputs={},
                dropdowns={},
            )

    class delta_time(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::delta time", inputs={}, dropdowns={}
            )

    class pick_color(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::grab color at x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class max_sprite_layers(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::max sprite layers", inputs={}, dropdowns={}
            )

    class average_loudness(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::average loudness", inputs={}, dropdowns={}
            )

    class scrolling_distance(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::scrolling distance",
                inputs={},
                dropdowns={},
            )

    class set_scrolling_distance(ThirdBlock):

        def __init__(self, amount: INPUT_COMPATIBLE_T):
            self.amount = amount

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

    class change_scrolling_distance_by(ThirdBlock):

        def __init__(self, amount: INPUT_COMPATIBLE_T):
            self.amount = amount

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

    class current_key_pressed(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::current key pressed",
                inputs={},
                dropdowns={},
            )

    class get_last_key_pressed(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::last key pressed", inputs={}, dropdowns={}
            )

    class get_button_is_down(ThirdBlock):

        def __init__(self, mouse_button: INPUT_COMPATIBLE_T):
            self.mouse_button = mouse_button

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

    class changed(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T):
            self.one = one

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::(ONE) changed?",
                inputs={
                    "ONE": ThirdInputValue.as_input(self.one, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class amount_of_time_key_has_been_held(ThirdBlock):

        def __init__(self, key: INPUT_COMPATIBLE_T):
            self.key = key

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

    class menu_key(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::#menu:key", inputs={}, dropdowns={}
            )

    class menu_mouse_button(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::#menu:mouseButton", inputs={}, dropdowns={}
            )

    class menu_url_sections(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmSensingExpansion::#menu:urlSections", inputs={}, dropdowns={}
            )
