from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class sensing:

    @staticmethod
    def touchingobject(object: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::touching ([OBJECT]) ?",
            inputs={
                "OBJECT": InputValue.try_as_input(
                    object, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def objecttouchingobject(
        object: INPUT_COMPATIBLE_T, sprite: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::([OBJECT]) touching ([SPRITE]) ?",
            inputs={
                "OBJECT": InputValue.try_as_input(
                    object, p.SRBlockAndDropdownInputValue
                ),
                "SPRITE": InputValue.try_as_input(
                    sprite, p.SRBlockAndDropdownInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def objecttouchingclonesprite(
        object: INPUT_COMPATIBLE_T, sprite: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::([OBJECT]) touching clone of ([SPRITE]) ?",
            inputs={
                "OBJECT": InputValue.try_as_input(
                    object, p.SRBlockAndDropdownInputValue
                ),
                "SPRITE": InputValue.try_as_input(
                    sprite, p.SRBlockAndDropdownInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def touchingcolor(color: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::touching color (COLOR) ?",
            inputs={
                "COLOR": InputValue.try_as_input(color, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def coloristouchingcolor(
        color1: INPUT_COMPATIBLE_T, color2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::color (COLOR1) is touching color (COLOR2) ?",
            inputs={
                "COLOR1": InputValue.try_as_input(color1, p.SRBlockAndTextInputValue),
                "COLOR2": InputValue.try_as_input(color2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def getxyoftouchingsprite(object: INPUT_COMPATIBLE_T, coordinate: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::[COORDINATE] of touching ([OBJECT]) point",
            inputs={
                "OBJECT": InputValue.try_as_input(
                    object, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={
                "COORDINATE": p.SRDropdownValue(
                    p.DropdownValueKind.STANDARD, coordinate
                )
            },
        )

    @staticmethod
    def distanceto(object: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::distance to ([OBJECT])",
            inputs={
                "OBJECT": InputValue.try_as_input(
                    object, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def distance_to(
        x1: INPUT_COMPATIBLE_T,
        y1: INPUT_COMPATIBLE_T,
        x2: INPUT_COMPATIBLE_T,
        y2: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::distance from (X1) (Y1) to (X2) (Y2)",
            inputs={
                "X1": InputValue.try_as_input(x1, p.SRBlockAndTextInputValue),
                "Y1": InputValue.try_as_input(y1, p.SRBlockAndTextInputValue),
                "X2": InputValue.try_as_input(x2, p.SRBlockAndTextInputValue),
                "Y2": InputValue.try_as_input(y2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def direction_to(
        x1: INPUT_COMPATIBLE_T,
        y1: INPUT_COMPATIBLE_T,
        x2: INPUT_COMPATIBLE_T,
        y2: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::direction to (X1) (Y1) from (X2) (Y2)",
            inputs={
                "X1": InputValue.try_as_input(x1, p.SRBlockAndTextInputValue),
                "Y1": InputValue.try_as_input(y1, p.SRBlockAndTextInputValue),
                "X2": InputValue.try_as_input(x2, p.SRBlockAndTextInputValue),
                "Y2": InputValue.try_as_input(y2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def askandwait(question: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::ask (QUESTION) and wait",
            inputs={
                "QUESTION": InputValue.try_as_input(
                    question, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def answer() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::answer", inputs={}, dropdowns={})

    @staticmethod
    def thing_is_text(string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::(STRING) is text?",
            inputs={
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def thing_is_number(string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::(STRING) is number?",
            inputs={
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def keypressed(key: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::key ([KEY]) pressed?",
            inputs={
                "KEY": InputValue.try_as_input(key, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def keyhit(key: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::key ([KEY]) hit?",
            inputs={
                "KEY": InputValue.try_as_input(key, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def mousescrolling(direction: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::is mouse scrolling ([DIRECTION]) ?",
            inputs={
                "DIRECTION": InputValue.try_as_input(
                    direction, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def mousedown() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::mouse down?", inputs={}, dropdowns={})

    @staticmethod
    def mouseclicked() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::mouse clicked?", inputs={}, dropdowns={})

    @staticmethod
    def mousex() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::mouse x", inputs={}, dropdowns={})

    @staticmethod
    def mousey() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::mouse y", inputs={}, dropdowns={})

    @staticmethod
    def setclipboard(text: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::add (TEXT) to clipboard",
            inputs={"TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def getclipboard() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::clipboard item", inputs={}, dropdowns={})

    @staticmethod
    def setdragmode(mode: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::set drag mode [MODE]",
            inputs={},
            dropdowns={"MODE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, mode)},
        )

    @staticmethod
    def getdragmode() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::draggable?", inputs={}, dropdowns={})

    @staticmethod
    def loudness() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::loudness", inputs={}, dropdowns={})

    @staticmethod
    def loud() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::loud?", inputs={}, dropdowns={})

    @staticmethod
    def resettimer() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::reset timer", inputs={}, dropdowns={})

    @staticmethod
    def timer() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::timer", inputs={}, dropdowns={})

    @staticmethod
    def set_of(
        value: INPUT_COMPATIBLE_T, target: INPUT_COMPATIBLE_T, property: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::set [PROPERTY] of ([TARGET]) to (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                ),
            },
            dropdowns={
                "PROPERTY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, property)
            },
        )

    @staticmethod
    def of(target: INPUT_COMPATIBLE_T, property: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::[PROPERTY] of ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={
                "PROPERTY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, property)
            },
        )

    @staticmethod
    def current(property: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::current [PROPERTY]",
            inputs={},
            dropdowns={
                "PROPERTY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, property)
            },
        )

    @staticmethod
    def dayssince2000() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::days since 2000", inputs={}, dropdowns={})

    @staticmethod
    def mobile() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::mobile?", inputs={}, dropdowns={})

    @staticmethod
    def fingerdown(index: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::finger ([INDEX]) down?",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def fingertapped(index: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::finger ([INDEX]) tapped?",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def fingerx(index: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::finger ([INDEX]) x",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def fingery(index: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::finger ([INDEX]) y",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def username() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::username", inputs={}, dropdowns={})

    @staticmethod
    def loggedin() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::logged in?", inputs={}, dropdowns={})

    @staticmethod
    def touchingobjectmenu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::#TOUCHING OBJECT MENU", inputs={}, dropdowns={}
        )

    @staticmethod
    def fulltouchingobjectmenu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::#FULL TOUCHING OBJECT MENU", inputs={}, dropdowns={}
        )

    @staticmethod
    def touchingobjectmenusprites() -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::#TOUCHING OBJECT MENU SPRITES", inputs={}, dropdowns={}
        )

    @staticmethod
    def distancetomenu() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::#DISTANCE TO MENU", inputs={}, dropdowns={})

    @staticmethod
    def keyoptions() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::#KEY MENU", inputs={}, dropdowns={})

    @staticmethod
    def scrolldirections() -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::#SCROLL DIRECTION MENU", inputs={}, dropdowns={}
        )

    @staticmethod
    def of_object_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::#OJBECT PROPERTY MENU", inputs={}, dropdowns={}
        )

    @staticmethod
    def fingeroptions() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::#FINGER INDEX MENU", inputs={}, dropdowns={})

    @staticmethod
    def thing_has_number(text1: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::(TEXT1) has number?",
            inputs={
                "TEXT1": InputValue.try_as_input(text1, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def is_upper_case(text: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::is character (text) uppercase?",
            inputs={"text": InputValue.try_as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def regextest(
        text: INPUT_COMPATIBLE_T, reg: INPUT_COMPATIBLE_T, regrule: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::test regex (reg) (regrule) with text (text)",
            inputs={
                "text": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "reg": InputValue.try_as_input(reg, p.SRBlockAndTextInputValue),
                "regrule": InputValue.try_as_input(regrule, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def getspritewithattrib(
        var: INPUT_COMPATIBLE_T, val: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sensing::get sprite with (var) set to (val)",
            inputs={
                "var": InputValue.try_as_input(var, p.SRBlockAndTextInputValue),
                "val": InputValue.try_as_input(val, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def getoperatingsystem() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::operating system", inputs={}, dropdowns={})

    @staticmethod
    def getbrowser() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::browser", inputs={}, dropdowns={})

    @staticmethod
    def geturl() -> p.SRBlock:
        return p.SRBlock(opcode="&sensing::url", inputs={}, dropdowns={})
