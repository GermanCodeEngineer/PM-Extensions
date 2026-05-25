from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class sensing:

    @grepr_dataclass()
    class touchingobject(ThirdBlock):
        OPCODE = "&sensing::touching ([OBJECT]) ?"
        INPUT_SPECS = (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class objecttouchingobject(ThirdBlock):
        OPCODE = "&sensing::([OBJECT]) touching ([SPRITE]) ?"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
            ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        sprite: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class objecttouchingclonesprite(ThirdBlock):
        OPCODE = "&sensing::([OBJECT]) touching clone of ([SPRITE]) ?"
        INPUT_SPECS = (
            ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
            ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T
        sprite: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class touchingcolor(ThirdBlock):
        OPCODE = "&sensing::touching color (COLOR) ?"
        INPUT_SPECS = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class coloristouchingcolor(ThirdBlock):
        OPCODE = "&sensing::color (COLOR1) is touching color (COLOR2) ?"
        INPUT_SPECS = (
            ("COLOR1", "color1", p.SRBlockAndTextInputValue, None),
            ("COLOR2", "color2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        color1: INPUT_COMPATIBLE_T
        color2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class getxyoftouchingsprite(ThirdBlock):
        OPCODE = "&sensing::[COORDINATE] of touching ([OBJECT]) point"
        INPUT_SPECS = (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = (("COORDINATE", "coordinate"),)
        object: INPUT_COMPATIBLE_T
        coordinate: str

    @grepr_dataclass()
    class distanceto(ThirdBlock):
        OPCODE = "&sensing::distance to ([OBJECT])"
        INPUT_SPECS = (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class distance_to(ThirdBlock):
        OPCODE = "&sensing::distance from (X1) (Y1) to (X2) (Y2)"
        INPUT_SPECS = (
            ("X1", "x1", p.SRBlockAndTextInputValue, None),
            ("Y1", "y1", p.SRBlockAndTextInputValue, None),
            ("X2", "x2", p.SRBlockAndTextInputValue, None),
            ("Y2", "y2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class direction_to(ThirdBlock):
        OPCODE = "&sensing::direction to (X1) (Y1) from (X2) (Y2)"
        INPUT_SPECS = (
            ("X1", "x1", p.SRBlockAndTextInputValue, None),
            ("Y1", "y1", p.SRBlockAndTextInputValue, None),
            ("X2", "x2", p.SRBlockAndTextInputValue, None),
            ("Y2", "y2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class askandwait(ThirdBlock):
        OPCODE = "&sensing::ask (QUESTION) and wait"
        INPUT_SPECS = (("QUESTION", "question", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        question: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class answer(ThirdBlock):
        OPCODE = "&sensing::answer"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class thing_is_text(ThirdBlock):
        OPCODE = "&sensing::(STRING) is text?"
        INPUT_SPECS = (("STRING", "string", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class thing_is_number(ThirdBlock):
        OPCODE = "&sensing::(STRING) is number?"
        INPUT_SPECS = (("STRING", "string", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class keypressed(ThirdBlock):
        OPCODE = "&sensing::key ([KEY]) pressed?"
        INPUT_SPECS = (("KEY", "key", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class keyhit(ThirdBlock):
        OPCODE = "&sensing::key ([KEY]) hit?"
        INPUT_SPECS = (("KEY", "key", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mousescrolling(ThirdBlock):
        OPCODE = "&sensing::is mouse scrolling ([DIRECTION]) ?"
        INPUT_SPECS = (
            ("DIRECTION", "direction", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        direction: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mousedown(ThirdBlock):
        OPCODE = "&sensing::mouse down?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class mouseclicked(ThirdBlock):
        OPCODE = "&sensing::mouse clicked?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class mousex(ThirdBlock):
        OPCODE = "&sensing::mouse x"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class mousey(ThirdBlock):
        OPCODE = "&sensing::mouse y"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class setclipboard(ThirdBlock):
        OPCODE = "&sensing::add (TEXT) to clipboard"
        INPUT_SPECS = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class getclipboard(ThirdBlock):
        OPCODE = "&sensing::clipboard item"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class setdragmode(ThirdBlock):
        OPCODE = "&sensing::set drag mode [MODE]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("MODE", "mode"),)
        mode: str

    @grepr_dataclass()
    class getdragmode(ThirdBlock):
        OPCODE = "&sensing::draggable?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class loudness(ThirdBlock):
        OPCODE = "&sensing::loudness"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class loud(ThirdBlock):
        OPCODE = "&sensing::loud?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class resettimer(ThirdBlock):
        OPCODE = "&sensing::reset timer"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class timer(ThirdBlock):
        OPCODE = "&sensing::timer"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class set_of(ThirdBlock):
        OPCODE = "&sensing::set [PROPERTY] of ([TARGET]) to (VALUE)"
        INPUT_SPECS = (
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = (("PROPERTY", "property"),)
        value: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T
        property: str

    @grepr_dataclass()
    class of(ThirdBlock):
        OPCODE = "&sensing::[PROPERTY] of ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = (("PROPERTY", "property"),)
        target: INPUT_COMPATIBLE_T
        property: str

    @grepr_dataclass()
    class current(ThirdBlock):
        OPCODE = "&sensing::current [PROPERTY]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("PROPERTY", "property"),)
        property: str

    @grepr_dataclass()
    class dayssince2000(ThirdBlock):
        OPCODE = "&sensing::days since 2000"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class mobile(ThirdBlock):
        OPCODE = "&sensing::mobile?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class fingerdown(ThirdBlock):
        OPCODE = "&sensing::finger ([INDEX]) down?"
        INPUT_SPECS = (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fingertapped(ThirdBlock):
        OPCODE = "&sensing::finger ([INDEX]) tapped?"
        INPUT_SPECS = (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fingerx(ThirdBlock):
        OPCODE = "&sensing::finger ([INDEX]) x"
        INPUT_SPECS = (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fingery(ThirdBlock):
        OPCODE = "&sensing::finger ([INDEX]) y"
        INPUT_SPECS = (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class username(ThirdBlock):
        OPCODE = "&sensing::username"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class loggedin(ThirdBlock):
        OPCODE = "&sensing::logged in?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class touchingobjectmenu(ThirdBlock):
        OPCODE = "&sensing::#TOUCHING OBJECT MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class fulltouchingobjectmenu(ThirdBlock):
        OPCODE = "&sensing::#FULL TOUCHING OBJECT MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class touchingobjectmenusprites(ThirdBlock):
        OPCODE = "&sensing::#TOUCHING OBJECT MENU SPRITES"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class distancetomenu(ThirdBlock):
        OPCODE = "&sensing::#DISTANCE TO MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class keyoptions(ThirdBlock):
        OPCODE = "&sensing::#KEY MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class scrolldirections(ThirdBlock):
        OPCODE = "&sensing::#SCROLL DIRECTION MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class of_object_menu(ThirdBlock):
        OPCODE = "&sensing::#OJBECT PROPERTY MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class fingeroptions(ThirdBlock):
        OPCODE = "&sensing::#FINGER INDEX MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class thing_has_number(ThirdBlock):
        OPCODE = "&sensing::(TEXT1) has number?"
        INPUT_SPECS = (("TEXT1", "text1", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        text1: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_upper_case(ThirdBlock):
        OPCODE = "&sensing::is character (text) uppercase?"
        INPUT_SPECS = (("text", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class regextest(ThirdBlock):
        OPCODE = "&sensing::test regex (reg) (regrule) with text (text)"
        INPUT_SPECS = (
            ("text", "text", p.SRBlockAndTextInputValue, None),
            ("reg", "reg", p.SRBlockAndTextInputValue, None),
            ("regrule", "regrule", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T
        reg: INPUT_COMPATIBLE_T
        regrule: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class getspritewithattrib(ThirdBlock):
        OPCODE = "&sensing::get sprite with (var) set to (val)"
        INPUT_SPECS = (
            ("var", "var", p.SRBlockAndTextInputValue, None),
            ("val", "val", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        var: INPUT_COMPATIBLE_T
        val: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class getoperatingsystem(ThirdBlock):
        OPCODE = "&sensing::operating system"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class getbrowser(ThirdBlock):
        OPCODE = "&sensing::browser"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class geturl(ThirdBlock):
        OPCODE = "&sensing::url"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
