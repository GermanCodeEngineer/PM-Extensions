from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class pmSensingExpansion:

    @grepr_dataclass()
    class battery_percentage(ThirdBlock):
        OPCODE = "&pmSensingExpansion::battery percentage"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class battery_charging(ThirdBlock):
        OPCODE = "&pmSensingExpansion::is device charging?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class vibrate_device(ThirdBlock):
        OPCODE = "&pmSensingExpansion::vibrate"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class browser_language(ThirdBlock):
        OPCODE = "&pmSensingExpansion::preferred language"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class url_options(ThirdBlock):
        OPCODE = "&pmSensingExpansion::url ([OPTIONS])"
        INPUT_SPECS = (("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        options: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class url_options_of(ThirdBlock):
        OPCODE = "&pmSensingExpansion::([OPTIONS]) of url (URL)"
        INPUT_SPECS = (
            ("OPTIONS", "options", p.SRBlockAndDropdownInputValue, None),
            ("URL", "url", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        options: INPUT_COMPATIBLE_T
        url: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_username(ThirdBlock):
        OPCODE = "&pmSensingExpansion::set username to (NAME)"
        INPUT_SPECS = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_url_end(ThirdBlock):
        OPCODE = "&pmSensingExpansion::set url path to (PATH)"
        INPUT_SPECS = (("PATH", "path", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        path: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class query_param_of_url(ThirdBlock):
        OPCODE = "&pmSensingExpansion::query parameter (PARAM) of url (URL)"
        INPUT_SPECS = (
            ("PARAM", "param", p.SRBlockAndTextInputValue, None),
            ("URL", "url", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        param: INPUT_COMPATIBLE_T
        url: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class packaged(ThirdBlock):
        OPCODE = "&pmSensingExpansion::project packaged?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class sprite_name(ThirdBlock):
        OPCODE = "&pmSensingExpansion::sprite name"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class framed(ThirdBlock):
        OPCODE = "&pmSensingExpansion::project in iframe?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class current_millisecond(ThirdBlock):
        OPCODE = "&pmSensingExpansion::current millisecond"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class delta_time(ThirdBlock):
        OPCODE = "&pmSensingExpansion::delta time"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class pick_color(ThirdBlock):
        OPCODE = "&pmSensingExpansion::grab color at x: (X) y: (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class max_sprite_layers(ThirdBlock):
        OPCODE = "&pmSensingExpansion::max sprite layers"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class average_loudness(ThirdBlock):
        OPCODE = "&pmSensingExpansion::average loudness"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class scrolling_distance(ThirdBlock):
        OPCODE = "&pmSensingExpansion::scrolling distance"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class set_scrolling_distance(ThirdBlock):
        OPCODE = "&pmSensingExpansion::set scrolling distance to (AMOUNT)"
        INPUT_SPECS = (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        amount: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class change_scrolling_distance_by(ThirdBlock):
        OPCODE = "&pmSensingExpansion::change scrolling distance by (AMOUNT)"
        INPUT_SPECS = (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        amount: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class current_key_pressed(ThirdBlock):
        OPCODE = "&pmSensingExpansion::current key pressed"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class get_last_key_pressed(ThirdBlock):
        OPCODE = "&pmSensingExpansion::last key pressed"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class get_button_is_down(ThirdBlock):
        OPCODE = "&pmSensingExpansion::([MOUSE_BUTTON]) mouse button down?"
        INPUT_SPECS = (
            ("MOUSE_BUTTON", "mouse_button", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        mouse_button: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class changed(ThirdBlock):
        OPCODE = "&pmSensingExpansion::(ONE) changed?"
        INPUT_SPECS = (("ONE", "one", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class amount_of_time_key_has_been_held(ThirdBlock):
        OPCODE = "&pmSensingExpansion::seconds since holding ([KEY])"
        INPUT_SPECS = (("KEY", "key", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_key(ThirdBlock):
        OPCODE = "&pmSensingExpansion::#menu:key"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_mouse_button(ThirdBlock):
        OPCODE = "&pmSensingExpansion::#menu:mouseButton"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_url_sections(ThirdBlock):
        OPCODE = "&pmSensingExpansion::#menu:urlSections"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
