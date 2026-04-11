from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class pmSensingExpansion:

    @staticmethod
    def battery_percentage() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::battery percentage", inputs={}, dropdowns={}
        )

    @staticmethod
    def battery_charging() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::is device charging?", inputs={}, dropdowns={}
        )

    @staticmethod
    def vibrate_device() -> p.SRBlock:
        return p.SRBlock(opcode="&pmSensingExpansion::vibrate", inputs={}, dropdowns={})

    @staticmethod
    def browser_language() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::preferred language", inputs={}, dropdowns={}
        )

    @staticmethod
    def url_options(options: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::url ([OPTIONS])",
            inputs={
                "OPTIONS": InputValue.try_as_input(
                    options, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def url_options_of(
        options: INPUT_COMPATIBLE_T, url: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::([OPTIONS]) of url (URL)",
            inputs={
                "OPTIONS": InputValue.try_as_input(
                    options, p.SRBlockAndDropdownInputValue
                ),
                "URL": InputValue.try_as_input(url, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_username(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::set username to (NAME)",
            inputs={"NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def set_url_end(path: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::set url path to (PATH)",
            inputs={"PATH": InputValue.try_as_input(path, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def query_param_of_url(
        param: INPUT_COMPATIBLE_T, url: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::query parameter (PARAM) of url (URL)",
            inputs={
                "PARAM": InputValue.try_as_input(param, p.SRBlockAndTextInputValue),
                "URL": InputValue.try_as_input(url, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def packaged() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::project packaged?", inputs={}, dropdowns={}
        )

    @staticmethod
    def sprite_name() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::sprite name", inputs={}, dropdowns={}
        )

    @staticmethod
    def framed() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::project in iframe?", inputs={}, dropdowns={}
        )

    @staticmethod
    def current_millisecond() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::current millisecond", inputs={}, dropdowns={}
        )

    @staticmethod
    def delta_time() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::delta time", inputs={}, dropdowns={}
        )

    @staticmethod
    def pick_color(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::grab color at x: (X) y: (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def max_sprite_layers() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::max sprite layers", inputs={}, dropdowns={}
        )

    @staticmethod
    def average_loudness() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::average loudness", inputs={}, dropdowns={}
        )

    @staticmethod
    def scrolling_distance() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::scrolling distance", inputs={}, dropdowns={}
        )

    @staticmethod
    def set_scrolling_distance(amount: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::set scrolling distance to (AMOUNT)",
            inputs={
                "AMOUNT": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def change_scrolling_distance_by(amount: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::change scrolling distance by (AMOUNT)",
            inputs={
                "AMOUNT": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def current_key_pressed() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::current key pressed", inputs={}, dropdowns={}
        )

    @staticmethod
    def get_last_key_pressed() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::last key pressed", inputs={}, dropdowns={}
        )

    @staticmethod
    def get_button_is_down(mouse_button: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::([MOUSE_BUTTON]) mouse button down?",
            inputs={
                "MOUSE_BUTTON": InputValue.try_as_input(
                    mouse_button, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def changed(one: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::(ONE) changed?",
            inputs={"ONE": InputValue.try_as_input(one, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def amount_of_time_key_has_been_held(key: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::seconds since holding ([KEY])",
            inputs={
                "KEY": InputValue.try_as_input(key, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def menu_key() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::#menu:key", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_mouse_button() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::#menu:mouseButton", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_url_sections() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmSensingExpansion::#menu:urlSections", inputs={}, dropdowns={}
        )
