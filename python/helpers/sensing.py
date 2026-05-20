from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class sensing:

    class touchingobject(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T):
            self.object = object

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

    class objecttouchingobject(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, sprite: INPUT_COMPATIBLE_T):
            self.object = object
            self.sprite = sprite

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

    class objecttouchingclonesprite(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, sprite: INPUT_COMPATIBLE_T):
            self.object = object
            self.sprite = sprite

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

    class touchingcolor(ThirdBlock):

        def __init__(self, color: INPUT_COMPATIBLE_T):
            self.color = color

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

    class coloristouchingcolor(ThirdBlock):

        def __init__(self, color1: INPUT_COMPATIBLE_T, color2: INPUT_COMPATIBLE_T):
            self.color1 = color1
            self.color2 = color2

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

    class getxyoftouchingsprite(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T, coordinate: str):
            self.object = object
            self.coordinate = coordinate

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

    class distanceto(ThirdBlock):

        def __init__(self, object: INPUT_COMPATIBLE_T):
            self.object = object

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

    class distance_to(ThirdBlock):

        def __init__(
            self,
            x1: INPUT_COMPATIBLE_T,
            y1: INPUT_COMPATIBLE_T,
            x2: INPUT_COMPATIBLE_T,
            y2: INPUT_COMPATIBLE_T,
        ):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

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

    class direction_to(ThirdBlock):

        def __init__(
            self,
            x1: INPUT_COMPATIBLE_T,
            y1: INPUT_COMPATIBLE_T,
            x2: INPUT_COMPATIBLE_T,
            y2: INPUT_COMPATIBLE_T,
        ):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

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

    class askandwait(ThirdBlock):

        def __init__(self, question: INPUT_COMPATIBLE_T):
            self.question = question

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

    class answer(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::answer", inputs={}, dropdowns={})

    class thing_is_text(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T):
            self.string = string

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

    class thing_is_number(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T):
            self.string = string

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

    class keypressed(ThirdBlock):

        def __init__(self, key: INPUT_COMPATIBLE_T):
            self.key = key

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

    class keyhit(ThirdBlock):

        def __init__(self, key: INPUT_COMPATIBLE_T):
            self.key = key

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

    class mousescrolling(ThirdBlock):

        def __init__(self, direction: INPUT_COMPATIBLE_T):
            self.direction = direction

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

    class mousedown(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mouse down?", inputs={}, dropdowns={})

    class mouseclicked(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mouse clicked?", inputs={}, dropdowns={})

    class mousex(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mouse x", inputs={}, dropdowns={})

    class mousey(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mouse y", inputs={}, dropdowns={})

    class setclipboard(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T):
            self.text = text

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

    class getclipboard(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::clipboard item", inputs={}, dropdowns={})

    class setdragmode(ThirdBlock):

        def __init__(self, mode: str):
            self.mode = mode

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::set drag mode [MODE]",
                inputs={},
                dropdowns={
                    "MODE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.mode)
                },
            )

    class getdragmode(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::draggable?", inputs={}, dropdowns={})

    class loudness(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::loudness", inputs={}, dropdowns={})

    class loud(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::loud?", inputs={}, dropdowns={})

    class resettimer(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::reset timer", inputs={}, dropdowns={})

    class timer(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::timer", inputs={}, dropdowns={})

    class set_of(ThirdBlock):

        def __init__(
            self, value: INPUT_COMPATIBLE_T, target: INPUT_COMPATIBLE_T, property: str
        ):
            self.value = value
            self.target = target
            self.property = property

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

    class of(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T, property: str):
            self.target = target
            self.property = property

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

    class current(ThirdBlock):

        def __init__(self, property: str):
            self.property = property

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

    class dayssince2000(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::days since 2000", inputs={}, dropdowns={}
            )

    class mobile(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::mobile?", inputs={}, dropdowns={})

    class fingerdown(ThirdBlock):

        def __init__(self, index: INPUT_COMPATIBLE_T):
            self.index = index

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

    class fingertapped(ThirdBlock):

        def __init__(self, index: INPUT_COMPATIBLE_T):
            self.index = index

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

    class fingerx(ThirdBlock):

        def __init__(self, index: INPUT_COMPATIBLE_T):
            self.index = index

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

    class fingery(ThirdBlock):

        def __init__(self, index: INPUT_COMPATIBLE_T):
            self.index = index

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

    class username(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::username", inputs={}, dropdowns={})

    class loggedin(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::logged in?", inputs={}, dropdowns={})

    class touchingobjectmenu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#TOUCHING OBJECT MENU", inputs={}, dropdowns={}
            )

    class fulltouchingobjectmenu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#FULL TOUCHING OBJECT MENU", inputs={}, dropdowns={}
            )

    class touchingobjectmenusprites(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#TOUCHING OBJECT MENU SPRITES",
                inputs={},
                dropdowns={},
            )

    class distancetomenu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#DISTANCE TO MENU", inputs={}, dropdowns={}
            )

    class keyoptions(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::#KEY MENU", inputs={}, dropdowns={})

    class scrolldirections(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#SCROLL DIRECTION MENU", inputs={}, dropdowns={}
            )

    class of_object_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#OJBECT PROPERTY MENU", inputs={}, dropdowns={}
            )

    class fingeroptions(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::#FINGER INDEX MENU", inputs={}, dropdowns={}
            )

    class thing_has_number(ThirdBlock):

        def __init__(self, text1: INPUT_COMPATIBLE_T):
            self.text1 = text1

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

    class is_upper_case(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T):
            self.text = text

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

    class regextest(ThirdBlock):

        def __init__(
            self,
            text: INPUT_COMPATIBLE_T,
            reg: INPUT_COMPATIBLE_T,
            regrule: INPUT_COMPATIBLE_T,
        ):
            self.text = text
            self.reg = reg
            self.regrule = regrule

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

    class getspritewithattrib(ThirdBlock):

        def __init__(self, var: INPUT_COMPATIBLE_T, val: INPUT_COMPATIBLE_T):
            self.var = var
            self.val = val

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

    class getoperatingsystem(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sensing::operating system", inputs={}, dropdowns={}
            )

    class getbrowser(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::browser", inputs={}, dropdowns={})

    class geturl(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sensing::url", inputs={}, dropdowns={})
