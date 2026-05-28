from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class sensing:

    @grepr_dataclass()
    class touchingobject(ThirdBlock):
        OPCODE: ClassVar = "&sensing::touching ([OBJECT]) ?"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class objecttouchingobject(ThirdBlock):
        OPCODE: ClassVar = "&sensing::([OBJECT]) touching ([SPRITE]) ?"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
            ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        sprite: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class objecttouchingclonesprite(ThirdBlock):
        OPCODE: ClassVar = "&sensing::([OBJECT]) touching clone of ([SPRITE]) ?"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
            ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T
        sprite: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class touchingcolor(ThirdBlock):
        OPCODE: ClassVar = "&sensing::touching color (COLOR) ?"
        INPUT_SPECS: ClassVar = (("COLOR", "color", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        color: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class coloristouchingcolor(ThirdBlock):
        OPCODE: ClassVar = "&sensing::color (COLOR1) is touching color (COLOR2) ?"
        INPUT_SPECS: ClassVar = (
            ("COLOR1", "color1", p.SRBlockAndTextInputValue, None),
            ("COLOR2", "color2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        color1: INPUT_COMPATIBLE_T
        color2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class getxyoftouchingsprite(ThirdBlock):
        OPCODE: ClassVar = "&sensing::[COORDINATE] of touching ([OBJECT]) point"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("COORDINATE", "coordinate"),)
        object: INPUT_COMPATIBLE_T
        coordinate: str

    @grepr_dataclass()
    class distanceto(ThirdBlock):
        OPCODE: ClassVar = "&sensing::distance to ([OBJECT])"
        INPUT_SPECS: ClassVar = (
            ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        object: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class distance_to(ThirdBlock):
        OPCODE: ClassVar = "&sensing::distance from (X1) (Y1) to (X2) (Y2)"
        INPUT_SPECS: ClassVar = (
            ("X1", "x1", p.SRBlockAndTextInputValue, None),
            ("Y1", "y1", p.SRBlockAndTextInputValue, None),
            ("X2", "x2", p.SRBlockAndTextInputValue, None),
            ("Y2", "y2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class direction_to(ThirdBlock):
        OPCODE: ClassVar = "&sensing::direction to (X1) (Y1) from (X2) (Y2)"
        INPUT_SPECS: ClassVar = (
            ("X1", "x1", p.SRBlockAndTextInputValue, None),
            ("Y1", "y1", p.SRBlockAndTextInputValue, None),
            ("X2", "x2", p.SRBlockAndTextInputValue, None),
            ("Y2", "y2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class askandwait(ThirdBlock):
        OPCODE: ClassVar = "&sensing::ask (QUESTION) and wait"
        INPUT_SPECS: ClassVar = (
            ("QUESTION", "question", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        question: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class answer(ThirdBlock):
        OPCODE: ClassVar = "&sensing::answer"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class thing_is_text(ThirdBlock):
        OPCODE: ClassVar = "&sensing::(STRING) is text?"
        INPUT_SPECS: ClassVar = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class thing_is_number(ThirdBlock):
        OPCODE: ClassVar = "&sensing::(STRING) is number?"
        INPUT_SPECS: ClassVar = (
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class keypressed(ThirdBlock):
        OPCODE: ClassVar = "&sensing::key ([KEY]) pressed?"
        INPUT_SPECS: ClassVar = (("KEY", "key", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class keyhit(ThirdBlock):
        OPCODE: ClassVar = "&sensing::key ([KEY]) hit?"
        INPUT_SPECS: ClassVar = (("KEY", "key", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        key: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mousescrolling(ThirdBlock):
        OPCODE: ClassVar = "&sensing::is mouse scrolling ([DIRECTION]) ?"
        INPUT_SPECS: ClassVar = (
            ("DIRECTION", "direction", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        direction: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mousedown(ThirdBlock):
        OPCODE: ClassVar = "&sensing::mouse down?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class mouseclicked(ThirdBlock):
        OPCODE: ClassVar = "&sensing::mouse clicked?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class mousex(ThirdBlock):
        OPCODE: ClassVar = "&sensing::mouse x"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class mousey(ThirdBlock):
        OPCODE: ClassVar = "&sensing::mouse y"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class setclipboard(ThirdBlock):
        OPCODE: ClassVar = "&sensing::add (TEXT) to clipboard"
        INPUT_SPECS: ClassVar = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class getclipboard(ThirdBlock):
        OPCODE: ClassVar = "&sensing::clipboard item"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class setdragmode(ThirdBlock):
        OPCODE: ClassVar = "&sensing::set drag mode [MODE]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("MODE", "mode"),)
        mode: str

    @grepr_dataclass()
    class getdragmode(ThirdBlock):
        OPCODE: ClassVar = "&sensing::draggable?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class loudness(ThirdBlock):
        OPCODE: ClassVar = "&sensing::loudness"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class loud(ThirdBlock):
        OPCODE: ClassVar = "&sensing::loud?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class resettimer(ThirdBlock):
        OPCODE: ClassVar = "&sensing::reset timer"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class timer(ThirdBlock):
        OPCODE: ClassVar = "&sensing::timer"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class set_of(ThirdBlock):
        OPCODE: ClassVar = "&sensing::set [PROPERTY] of ([TARGET]) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
        value: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T
        property: str

    @grepr_dataclass()
    class of(ThirdBlock):
        OPCODE: ClassVar = "&sensing::[PROPERTY] of ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
        target: INPUT_COMPATIBLE_T
        property: str

    @grepr_dataclass()
    class current(ThirdBlock):
        OPCODE: ClassVar = "&sensing::current [PROPERTY]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("PROPERTY", "property"),)
        property: str

    @grepr_dataclass()
    class dayssince2000(ThirdBlock):
        OPCODE: ClassVar = "&sensing::days since 2000"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class mobile(ThirdBlock):
        OPCODE: ClassVar = "&sensing::mobile?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class fingerdown(ThirdBlock):
        OPCODE: ClassVar = "&sensing::finger ([INDEX]) down?"
        INPUT_SPECS: ClassVar = (
            ("INDEX", "index", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fingertapped(ThirdBlock):
        OPCODE: ClassVar = "&sensing::finger ([INDEX]) tapped?"
        INPUT_SPECS: ClassVar = (
            ("INDEX", "index", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fingerx(ThirdBlock):
        OPCODE: ClassVar = "&sensing::finger ([INDEX]) x"
        INPUT_SPECS: ClassVar = (
            ("INDEX", "index", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class fingery(ThirdBlock):
        OPCODE: ClassVar = "&sensing::finger ([INDEX]) y"
        INPUT_SPECS: ClassVar = (
            ("INDEX", "index", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        index: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class username(ThirdBlock):
        OPCODE: ClassVar = "&sensing::username"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class loggedin(ThirdBlock):
        OPCODE: ClassVar = "&sensing::logged in?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class touchingobjectmenu(ThirdBlock):
        OPCODE: ClassVar = "&sensing::#TOUCHING OBJECT MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class fulltouchingobjectmenu(ThirdBlock):
        OPCODE: ClassVar = "&sensing::#FULL TOUCHING OBJECT MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class touchingobjectmenusprites(ThirdBlock):
        OPCODE: ClassVar = "&sensing::#TOUCHING OBJECT MENU SPRITES"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class distancetomenu(ThirdBlock):
        OPCODE: ClassVar = "&sensing::#DISTANCE TO MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class keyoptions(ThirdBlock):
        OPCODE: ClassVar = "&sensing::#KEY MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class scrolldirections(ThirdBlock):
        OPCODE: ClassVar = "&sensing::#SCROLL DIRECTION MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class of_object_menu(ThirdBlock):
        OPCODE: ClassVar = "&sensing::#OJBECT PROPERTY MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class fingeroptions(ThirdBlock):
        OPCODE: ClassVar = "&sensing::#FINGER INDEX MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class thing_has_number(ThirdBlock):
        OPCODE: ClassVar = "&sensing::(TEXT1) has number?"
        INPUT_SPECS: ClassVar = (("TEXT1", "text1", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        text1: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_upper_case(ThirdBlock):
        OPCODE: ClassVar = "&sensing::is character (text) uppercase?"
        INPUT_SPECS: ClassVar = (("text", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class regextest(ThirdBlock):
        OPCODE: ClassVar = "&sensing::test regex (reg) (regrule) with text (text)"
        INPUT_SPECS: ClassVar = (
            ("text", "text", p.SRBlockAndTextInputValue, None),
            ("reg", "reg", p.SRBlockAndTextInputValue, None),
            ("regrule", "regrule", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T
        reg: INPUT_COMPATIBLE_T
        regrule: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class getspritewithattrib(ThirdBlock):
        OPCODE: ClassVar = "&sensing::get sprite with (var) set to (val)"
        INPUT_SPECS: ClassVar = (
            ("var", "var", p.SRBlockAndTextInputValue, None),
            ("val", "val", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        var: INPUT_COMPATIBLE_T
        val: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class getoperatingsystem(ThirdBlock):
        OPCODE: ClassVar = "&sensing::operating system"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class getbrowser(ThirdBlock):
        OPCODE: ClassVar = "&sensing::browser"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class geturl(ThirdBlock):
        OPCODE: ClassVar = "&sensing::url"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
