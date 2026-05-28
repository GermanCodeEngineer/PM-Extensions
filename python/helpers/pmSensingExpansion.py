from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class pmSensingExpansion:

    @grepr_dataclass()
    class battery_percentage(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::battery percentage"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class battery_charging(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::is device charging?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class vibrate_device(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::vibrate"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class browser_language(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::preferred language"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class url_options(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::url ([OPTIONS])"
        INPUT_SPECS: ClassVar = (
            ("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        options: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class url_options_of(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::([OPTIONS]) of url (URL)"
        INPUT_SPECS: ClassVar = (
            ("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),
            ("URL", "url", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        options: INPUT_COMPATIBLE_T
        url: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_username(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::set username to (NAME)"
        INPUT_SPECS: ClassVar = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_url_end(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::set url path to (PATH)"
        INPUT_SPECS: ClassVar = (("PATH", "path", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        path: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class query_param_of_url(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::query parameter (PARAM) of url (URL)"
        INPUT_SPECS: ClassVar = (
            ("PARAM", "param", p.SRBlockAndTextInputValue, None),
            ("URL", "url", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        param: INPUT_COMPATIBLE_T
        url: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class packaged(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::project packaged?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class sprite_name(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::sprite name"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class framed(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::project in iframe?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class current_millisecond(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::current millisecond"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class delta_time(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::delta time"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class pick_color(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::grab color at x: (X) y: (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class max_sprite_layers(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::max sprite layers"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class average_loudness(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::average loudness"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class scrolling_distance(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::scrolling distance"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class set_scrolling_distance(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::set scrolling distance to (AMOUNT)"
        INPUT_SPECS: ClassVar = (
            ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        amount: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class change_scrolling_distance_by(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::change scrolling distance by (AMOUNT)"
        INPUT_SPECS: ClassVar = (
            ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        amount: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class current_key_pressed(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::current key pressed"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class get_last_key_pressed(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::last key pressed"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class get_button_is_down(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::([MOUSE_BUTTON]) mouse button down?"
        INPUT_SPECS: ClassVar = (
            ("MOUSE_BUTTON", "mouse_button", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        mouse_button: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class changed(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::(ONE) changed?"
        INPUT_SPECS: ClassVar = (("ONE", "one", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class amount_of_time_key_has_been_held(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::seconds since holding ([KEY])"
        INPUT_SPECS: ClassVar = (("KEY", "key", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_key(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::#menu:key"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_mouse_button(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::#menu:mouseButton"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_url_sections(ThirdBlock):
        OPCODE: ClassVar = "&pmSensingExpansion::#menu:urlSections"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
