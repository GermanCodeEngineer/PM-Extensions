from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class sensing:

    @grepr_dataclass()
    class touchingobject(ThirdBlock):
        object: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::touching ([OBJECT]) ?",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class objecttouchingobject(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        sprite: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::([OBJECT]) touching ([SPRITE]) ?",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockAndDropdownInputValue
                    ),
                    "SPRITE": ThirdInputValue.as_input(
                        self.sprite, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class objecttouchingclonesprite(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        sprite: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::([OBJECT]) touching clone of ([SPRITE]) ?",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockAndDropdownInputValue
                    ),
                    "SPRITE": ThirdInputValue.as_input(
                        self.sprite, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class touchingcolor(ThirdBlock):
        color: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::touching color (COLOR) ?",
                inputs={
                    "COLOR": ThirdInputValue.as_input(
                        self.color, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class coloristouchingcolor(ThirdBlock):
        color1: INPUT_COMPATIBLE_T
        color2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::color (COLOR1) is touching color (COLOR2) ?",
                inputs={
                    "COLOR1": ThirdInputValue.as_input(
                        self.color1, p.SRBlockAndTextInputValue
                    ),
                    "COLOR2": ThirdInputValue.as_input(
                        self.color2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class getxyoftouchingsprite(ThirdBlock):
        object: INPUT_COMPATIBLE_T
        coordinate: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::[COORDINATE] of touching ([OBJECT]) point",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={
                    "COORDINATE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.coordinate
                    )
                },
            )

    @grepr_dataclass()
    class distanceto(ThirdBlock):
        object: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::distance to ([OBJECT])",
                inputs={
                    "OBJECT": ThirdInputValue.as_input(
                        self.object, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class distance_to(ThirdBlock):
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::distance from (X1) (Y1) to (X2) (Y2)",
                inputs={
                    "X1": ThirdInputValue.as_input(self.x1, p.SRBlockAndTextInputValue),
                    "Y1": ThirdInputValue.as_input(self.y1, p.SRBlockAndTextInputValue),
                    "X2": ThirdInputValue.as_input(self.x2, p.SRBlockAndTextInputValue),
                    "Y2": ThirdInputValue.as_input(self.y2, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class direction_to(ThirdBlock):
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::direction to (X1) (Y1) from (X2) (Y2)",
                inputs={
                    "X1": ThirdInputValue.as_input(self.x1, p.SRBlockAndTextInputValue),
                    "Y1": ThirdInputValue.as_input(self.y1, p.SRBlockAndTextInputValue),
                    "X2": ThirdInputValue.as_input(self.x2, p.SRBlockAndTextInputValue),
                    "Y2": ThirdInputValue.as_input(self.y2, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class askandwait(ThirdBlock):
        question: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::ask (QUESTION) and wait",
                inputs={
                    "QUESTION": ThirdInputValue.as_input(
                        self.question, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class answer(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::answer", inputs={}, dropdowns={})

    @grepr_dataclass()
    class thing_is_text(ThirdBlock):
        string: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::(STRING) is text?",
                inputs={
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class thing_is_number(ThirdBlock):
        string: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::(STRING) is number?",
                inputs={
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class keypressed(ThirdBlock):
        key: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::key ([KEY]) pressed?",
                inputs={
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class keyhit(ThirdBlock):
        key: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::key ([KEY]) hit?",
                inputs={
                    "KEY": ThirdInputValue.as_input(
                        self.key, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class mousescrolling(ThirdBlock):
        direction: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::is mouse scrolling ([DIRECTION]) ?",
                inputs={
                    "DIRECTION": ThirdInputValue.as_input(
                        self.direction, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class mousedown(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mouse down?", inputs={}, dropdowns={})

    @grepr_dataclass()
    class mouseclicked(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mouse clicked?", inputs={}, dropdowns={})

    @grepr_dataclass()
    class mousex(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mouse x", inputs={}, dropdowns={})

    @grepr_dataclass()
    class mousey(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mouse y", inputs={}, dropdowns={})

    @grepr_dataclass()
    class setclipboard(ThirdBlock):
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::add (TEXT) to clipboard",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class getclipboard(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::clipboard item", inputs={}, dropdowns={})

    @grepr_dataclass()
    class setdragmode(ThirdBlock):
        mode: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::set drag mode [MODE]",
                inputs={},
                dropdowns={
                    "MODE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.mode)
                },
            )

    @grepr_dataclass()
    class getdragmode(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::draggable?", inputs={}, dropdowns={})

    @grepr_dataclass()
    class loudness(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::loudness", inputs={}, dropdowns={})

    @grepr_dataclass()
    class loud(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::loud?", inputs={}, dropdowns={})

    @grepr_dataclass()
    class resettimer(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::reset timer", inputs={}, dropdowns={})

    @grepr_dataclass()
    class timer(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::timer", inputs={}, dropdowns={})

    @grepr_dataclass()
    class set_of(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T
        property: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::set [PROPERTY] of ([TARGET]) to (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={
                    "PROPERTY": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.property
                    )
                },
            )

    @grepr_dataclass()
    class of(ThirdBlock):
        target: INPUT_COMPATIBLE_T
        property: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::[PROPERTY] of ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={
                    "PROPERTY": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.property
                    )
                },
            )

    @grepr_dataclass()
    class current(ThirdBlock):
        property: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::current [PROPERTY]",
                inputs={},
                dropdowns={
                    "PROPERTY": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.property
                    )
                },
            )

    @grepr_dataclass()
    class dayssince2000(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::days since 2000", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class mobile(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mobile?", inputs={}, dropdowns={})

    @grepr_dataclass()
    class fingerdown(ThirdBlock):
        index: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::finger ([INDEX]) down?",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class fingertapped(ThirdBlock):
        index: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::finger ([INDEX]) tapped?",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class fingerx(ThirdBlock):
        index: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::finger ([INDEX]) x",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class fingery(ThirdBlock):
        index: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::finger ([INDEX]) y",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class username(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::username", inputs={}, dropdowns={})

    @grepr_dataclass()
    class loggedin(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::logged in?", inputs={}, dropdowns={})

    @grepr_dataclass()
    class touchingobjectmenu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#TOUCHING OBJECT MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class fulltouchingobjectmenu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#FULL TOUCHING OBJECT MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class touchingobjectmenusprites(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#TOUCHING OBJECT MENU SPRITES",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class distancetomenu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#DISTANCE TO MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class keyoptions(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::#KEY MENU", inputs={}, dropdowns={})

    @grepr_dataclass()
    class scrolldirections(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#SCROLL DIRECTION MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class of_object_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#OJBECT PROPERTY MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class fingeroptions(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#FINGER INDEX MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class thing_has_number(ThirdBlock):
        text1: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::(TEXT1) has number?",
                inputs={
                    "TEXT1": ThirdInputValue.as_input(
                        self.text1, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_upper_case(ThirdBlock):
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::is character (text) uppercase?",
                inputs={
                    "text": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class regextest(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        reg: INPUT_COMPATIBLE_T
        regrule: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::test regex (reg) (regrule) with text (text)",
                inputs={
                    "text": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "reg": ThirdInputValue.as_input(
                        self.reg, p.SRBlockAndTextInputValue
                    ),
                    "regrule": ThirdInputValue.as_input(
                        self.regrule, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class getspritewithattrib(ThirdBlock):
        var: INPUT_COMPATIBLE_T
        val: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::get sprite with (var) set to (val)",
                inputs={
                    "var": ThirdInputValue.as_input(
                        self.var, p.SRBlockAndTextInputValue
                    ),
                    "val": ThirdInputValue.as_input(
                        self.val, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class getoperatingsystem(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::operating system", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class getbrowser(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::browser", inputs={}, dropdowns={})

    @grepr_dataclass()
    class geturl(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::url", inputs={}, dropdowns={})
