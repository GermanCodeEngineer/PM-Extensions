from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class sensing:

    @grepr_dataclass()
    class touchingobject(ThirdBlock):
        OPCODE = "&sensing::touching ([OBJECT]) ?"
        object: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class objecttouchingobject(ThirdBlock):
        OPCODE = "&sensing::([OBJECT]) touching ([SPRITE]) ?"
        object: INPUT_COMPATIBLE_T
        sprite: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
                    ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
                    ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class objecttouchingclonesprite(ThirdBlock):
        OPCODE = "&sensing::([OBJECT]) touching clone of ([SPRITE]) ?"
        object: INPUT_COMPATIBLE_T
        sprite: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
                    ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),
                    ("SPRITE", "sprite", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class touchingcolor(ThirdBlock):
        OPCODE = "&sensing::touching color (COLOR) ?"
        color: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("COLOR", "color", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("COLOR", "color", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class coloristouchingcolor(ThirdBlock):
        OPCODE = "&sensing::color (COLOR1) is touching color (COLOR2) ?"
        color1: INPUT_COMPATIBLE_T
        color2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("COLOR1", "color1", p.SRBlockAndTextInputValue, None),
                    ("COLOR2", "color2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("COLOR1", "color1", p.SRBlockAndTextInputValue, None),
                    ("COLOR2", "color2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class getxyoftouchingsprite(ThirdBlock):
        OPCODE = "&sensing::[COORDINATE] of touching ([OBJECT]) point"
        object: INPUT_COMPATIBLE_T
        coordinate: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),),
                (("COORDINATE", "coordinate"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),),
                (("COORDINATE", "coordinate"),),
            )

    @grepr_dataclass()
    class distanceto(ThirdBlock):
        OPCODE = "&sensing::distance to ([OBJECT])"
        object: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("OBJECT", "object", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class distance_to(ThirdBlock):
        OPCODE = "&sensing::distance from (X1) (Y1) to (X2) (Y2)"
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X1", "x1", p.SRBlockAndTextInputValue, None),
                    ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                    ("X2", "x2", p.SRBlockAndTextInputValue, None),
                    ("Y2", "y2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X1", "x1", p.SRBlockAndTextInputValue, None),
                    ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                    ("X2", "x2", p.SRBlockAndTextInputValue, None),
                    ("Y2", "y2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class direction_to(ThirdBlock):
        OPCODE = "&sensing::direction to (X1) (Y1) from (X2) (Y2)"
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X1", "x1", p.SRBlockAndTextInputValue, None),
                    ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                    ("X2", "x2", p.SRBlockAndTextInputValue, None),
                    ("Y2", "y2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X1", "x1", p.SRBlockAndTextInputValue, None),
                    ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                    ("X2", "x2", p.SRBlockAndTextInputValue, None),
                    ("Y2", "y2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class askandwait(ThirdBlock):
        OPCODE = "&sensing::ask (QUESTION) and wait"
        question: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("QUESTION", "question", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("QUESTION", "question", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class answer(ThirdBlock):
        OPCODE = "&sensing::answer"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class thing_is_text(ThirdBlock):
        OPCODE = "&sensing::(STRING) is text?"
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("STRING", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("STRING", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class thing_is_number(ThirdBlock):
        OPCODE = "&sensing::(STRING) is number?"
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("STRING", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("STRING", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class keypressed(ThirdBlock):
        OPCODE = "&sensing::key ([KEY]) pressed?"
        key: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("KEY", "key", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("KEY", "key", p.SRBlockAndDropdownInputValue, None),), ()
            )

    @grepr_dataclass()
    class keyhit(ThirdBlock):
        OPCODE = "&sensing::key ([KEY]) hit?"
        key: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("KEY", "key", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("KEY", "key", p.SRBlockAndDropdownInputValue, None),), ()
            )

    @grepr_dataclass()
    class mousescrolling(ThirdBlock):
        OPCODE = "&sensing::is mouse scrolling ([DIRECTION]) ?"
        direction: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("DIRECTION", "direction", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("DIRECTION", "direction", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class mousedown(ThirdBlock):
        OPCODE = "&sensing::mouse down?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class mouseclicked(ThirdBlock):
        OPCODE = "&sensing::mouse clicked?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class mousex(ThirdBlock):
        OPCODE = "&sensing::mouse x"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class mousey(ThirdBlock):
        OPCODE = "&sensing::mouse y"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class setclipboard(ThirdBlock):
        OPCODE = "&sensing::add (TEXT) to clipboard"
        text: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TEXT", "text", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TEXT", "text", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class getclipboard(ThirdBlock):
        OPCODE = "&sensing::clipboard item"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class setdragmode(ThirdBlock):
        OPCODE = "&sensing::set drag mode [MODE]"
        mode: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("MODE", "mode"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("MODE", "mode"),))

    @grepr_dataclass()
    class getdragmode(ThirdBlock):
        OPCODE = "&sensing::draggable?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class loudness(ThirdBlock):
        OPCODE = "&sensing::loudness"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class loud(ThirdBlock):
        OPCODE = "&sensing::loud?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class resettimer(ThirdBlock):
        OPCODE = "&sensing::reset timer"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class timer(ThirdBlock):
        OPCODE = "&sensing::timer"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class set_of(ThirdBlock):
        OPCODE = "&sensing::set [PROPERTY] of ([TARGET]) to (VALUE)"
        value: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T
        property: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
                ),
                (("PROPERTY", "property"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                    ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
                ),
                (("PROPERTY", "property"),),
            )

    @grepr_dataclass()
    class of(ThirdBlock):
        OPCODE = "&sensing::[PROPERTY] of ([TARGET])"
        target: INPUT_COMPATIBLE_T
        property: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (("PROPERTY", "property"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (("PROPERTY", "property"),),
            )

    @grepr_dataclass()
    class current(ThirdBlock):
        OPCODE = "&sensing::current [PROPERTY]"
        property: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("PROPERTY", "property"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("PROPERTY", "property"),))

    @grepr_dataclass()
    class dayssince2000(ThirdBlock):
        OPCODE = "&sensing::days since 2000"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class mobile(ThirdBlock):
        OPCODE = "&sensing::mobile?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class fingerdown(ThirdBlock):
        OPCODE = "&sensing::finger ([INDEX]) down?"
        index: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class fingertapped(ThirdBlock):
        OPCODE = "&sensing::finger ([INDEX]) tapped?"
        index: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class fingerx(ThirdBlock):
        OPCODE = "&sensing::finger ([INDEX]) x"
        index: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class fingery(ThirdBlock):
        OPCODE = "&sensing::finger ([INDEX]) y"
        index: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INDEX", "index", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class username(ThirdBlock):
        OPCODE = "&sensing::username"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class loggedin(ThirdBlock):
        OPCODE = "&sensing::logged in?"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class touchingobjectmenu(ThirdBlock):
        OPCODE = "&sensing::#TOUCHING OBJECT MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class fulltouchingobjectmenu(ThirdBlock):
        OPCODE = "&sensing::#FULL TOUCHING OBJECT MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class touchingobjectmenusprites(ThirdBlock):
        OPCODE = "&sensing::#TOUCHING OBJECT MENU SPRITES"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class distancetomenu(ThirdBlock):
        OPCODE = "&sensing::#DISTANCE TO MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class keyoptions(ThirdBlock):
        OPCODE = "&sensing::#KEY MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class scrolldirections(ThirdBlock):
        OPCODE = "&sensing::#SCROLL DIRECTION MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class of_object_menu(ThirdBlock):
        OPCODE = "&sensing::#OJBECT PROPERTY MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class fingeroptions(ThirdBlock):
        OPCODE = "&sensing::#FINGER INDEX MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class thing_has_number(ThirdBlock):
        OPCODE = "&sensing::(TEXT1) has number?"
        text1: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TEXT1", "text1", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TEXT1", "text1", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class is_upper_case(ThirdBlock):
        OPCODE = "&sensing::is character (text) uppercase?"
        text: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("text", "text", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("text", "text", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class regextest(ThirdBlock):
        OPCODE = "&sensing::test regex (reg) (regrule) with text (text)"
        text: INPUT_COMPATIBLE_T
        reg: INPUT_COMPATIBLE_T
        regrule: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("reg", "reg", p.SRBlockAndTextInputValue, None),
                    ("regrule", "regrule", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("reg", "reg", p.SRBlockAndTextInputValue, None),
                    ("regrule", "regrule", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class getspritewithattrib(ThirdBlock):
        OPCODE = "&sensing::get sprite with (var) set to (val)"
        var: INPUT_COMPATIBLE_T
        val: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("var", "var", p.SRBlockAndTextInputValue, None),
                    ("val", "val", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("var", "var", p.SRBlockAndTextInputValue, None),
                    ("val", "val", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class getoperatingsystem(ThirdBlock):
        OPCODE = "&sensing::operating system"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class getbrowser(ThirdBlock):
        OPCODE = "&sensing::browser"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class geturl(ThirdBlock):
        OPCODE = "&sensing::url"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
