from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class newCanvas:

    @grepr_dataclass()
    class canvas_getter(ThirdBlock):
        OPCODE = "&newCanvas::[canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class set_size(ThirdBlock):
        OPCODE = "&newCanvas::set width: (width) height: (height) of [canvas]"
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class set_property(ThirdBlock):
        OPCODE = "&newCanvas::set [prop] of [canvas] to"
        canvas: str
        prop: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"), ("prop", "prop"))
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (), (("canvas", "canvas"), ("prop", "prop"))
            )

    @grepr_dataclass()
    class get_property(ThirdBlock):
        OPCODE = "&newCanvas::get [prop] of [canvas]"
        canvas: str
        prop: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"), ("prop", "prop"))
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (), (("canvas", "canvas"), ("prop", "prop"))
            )

    @grepr_dataclass()
    class dash(ThirdBlock):
        OPCODE = "&newCanvas::set line dash to (dashing) in [canvas]"
        dashing: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("dashing", "dashing", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("dashing", "dashing", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class clear_canvas(ThirdBlock):
        OPCODE = "&newCanvas::clear canvas [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class clear_aria(ThirdBlock):
        OPCODE = "&newCanvas::clear area at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class draw_text(ThirdBlock):
        OPCODE = "&newCanvas::draw text (text) at (x) (y) onto [canvas]"
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class draw_text_with_cap(ThirdBlock):
        OPCODE = (
            "&newCanvas::draw text (text) at (x) (y) with size cap (cap) onto [canvas]"
        )
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        cap: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("cap", "cap", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("cap", "cap", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class outline_text(ThirdBlock):
        OPCODE = "&newCanvas::draw text outline for (text) at (x) (y) onto [canvas]"
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class outline_text_with_cap(ThirdBlock):
        OPCODE = "&newCanvas::draw text outline for (text) at (x) (y) with size cap (cap) onto [canvas]"
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        cap: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("cap", "cap", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("text", "text", p.SRBlockAndTextInputValue, None),
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("cap", "cap", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class draw_rect(ThirdBlock):
        OPCODE = "&newCanvas::draw rectangle at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class outline_rect(ThirdBlock):
        OPCODE = "&newCanvas::draw rectangle outline at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class preload_uri_image(ThirdBlock):
        OPCODE = "&newCanvas::preload image (URI) as (NAME)"
        uri: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("URI", "uri", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("URI", "uri", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class unload_uri_image(ThirdBlock):
        OPCODE = "&newCanvas::unload image (NAME)"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NAME", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NAME", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_width_of_preloaded(ThirdBlock):
        OPCODE = "&newCanvas::get width of (name)"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("name", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("name", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_height_of_preloaded(ThirdBlock):
        OPCODE = "&newCanvas::get height of (name)"
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("name", "name", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("name", "name", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class draw_uri_image(ThirdBlock):
        OPCODE = "&newCanvas::draw image (URI) at x:[X] y:[Y] onto canvas [canvas]"
        uri: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("URI", "uri", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("URI", "uri", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class draw_uri_image_whr(ThirdBlock):
        OPCODE = "&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] pointed at: (ROTATE) onto canvas [canvas]"
        uri: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        rotate: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("URI", "uri", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                    ("WIDTH", "width", p.SRBlockAndTextInputValue, None),
                    ("HEIGHT", "height", p.SRBlockAndTextInputValue, None),
                    ("ROTATE", "rotate", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("URI", "uri", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                    ("WIDTH", "width", p.SRBlockAndTextInputValue, None),
                    ("HEIGHT", "height", p.SRBlockAndTextInputValue, None),
                    ("ROTATE", "rotate", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class draw_uri_image_whcx1_y1_x2_y2_r(ThirdBlock):
        OPCODE = "&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] cropping from x:[CROPX] y:[CROPY] width:[CROPW] height:[CROPH] pointed at: (ROTATE) onto canvas [canvas]"
        uri: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        cropx: INPUT_COMPATIBLE_T
        cropy: INPUT_COMPATIBLE_T
        cropw: INPUT_COMPATIBLE_T
        croph: INPUT_COMPATIBLE_T
        rotate: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("URI", "uri", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                    ("WIDTH", "width", p.SRBlockAndTextInputValue, None),
                    ("HEIGHT", "height", p.SRBlockAndTextInputValue, None),
                    ("CROPX", "cropx", p.SRBlockAndTextInputValue, None),
                    ("CROPY", "cropy", p.SRBlockAndTextInputValue, None),
                    ("CROPW", "cropw", p.SRBlockAndTextInputValue, None),
                    ("CROPH", "croph", p.SRBlockAndTextInputValue, None),
                    ("ROTATE", "rotate", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("URI", "uri", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                    ("WIDTH", "width", p.SRBlockAndTextInputValue, None),
                    ("HEIGHT", "height", p.SRBlockAndTextInputValue, None),
                    ("CROPX", "cropx", p.SRBlockAndTextInputValue, None),
                    ("CROPY", "cropy", p.SRBlockAndTextInputValue, None),
                    ("CROPW", "cropw", p.SRBlockAndTextInputValue, None),
                    ("CROPH", "croph", p.SRBlockAndTextInputValue, None),
                    ("ROTATE", "rotate", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class begin_path(ThirdBlock):
        OPCODE = "&newCanvas::begin path drawing on [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class move_to(ThirdBlock):
        OPCODE = "&newCanvas::move pen to x:[x] y:[y] on [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class line_to(ThirdBlock):
        OPCODE = "&newCanvas::add line going to x:[x] y:[y] on [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class arc_to(ThirdBlock):
        OPCODE = "&newCanvas::add arc going to x:[x] y:[y] on [canvas] with control points {:controlPoints:} and radius (radius)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        radius: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    (
                        "controlPoints",
                        "control_points",
                        p.SREmbeddedBlockInputValue,
                        newCanvas.param,
                    ),
                    ("radius", "radius", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    (
                        "controlPoints",
                        "control_points",
                        p.SREmbeddedBlockInputValue,
                        newCanvas.param,
                    ),
                    ("radius", "radius", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class add_rect(ThirdBlock):
        OPCODE = "&newCanvas::add a rectangle at x:[x] y:[y] with width:[width] height:[height] to [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class add_ellipse(ThirdBlock):
        OPCODE = "&newCanvas::add a ellipse at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        dir: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                    ("dir", "dir", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                    ("dir", "dir", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class add_ellipse_start_stop(ThirdBlock):
        OPCODE = "&newCanvas::add a ellipse with starting rotation (start) and ending rotation (end) at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        start: INPUT_COMPATIBLE_T
        end: INPUT_COMPATIBLE_T
        dir: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                    ("start", "start", p.SRBlockAndTextInputValue, None),
                    ("end", "end", p.SRBlockAndTextInputValue, None),
                    ("dir", "dir", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                    ("width", "width", p.SRBlockAndTextInputValue, None),
                    ("height", "height", p.SRBlockAndTextInputValue, None),
                    ("start", "start", p.SRBlockAndTextInputValue, None),
                    ("end", "end", p.SRBlockAndTextInputValue, None),
                    ("dir", "dir", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class close_path(ThirdBlock):
        OPCODE = "&newCanvas::attempt to close any open path in [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class stroke(ThirdBlock):
        OPCODE = "&newCanvas::draw outline for current path in [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class fill(ThirdBlock):
        OPCODE = "&newCanvas::draw fill for current path in [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class save_transform(ThirdBlock):
        OPCODE = "&newCanvas::save [canvas]'s transform"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class restore_transform(ThirdBlock):
        OPCODE = "&newCanvas::reset to [canvas]'s saved transform"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class turn_rotation_left(ThirdBlock):
        OPCODE = "&newCanvas::turn left (degrees) in [canvas]"
        degrees: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("degrees", "degrees", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("degrees", "degrees", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class turn_rotation_right(ThirdBlock):
        OPCODE = "&newCanvas::turn right (degrees) in [canvas]"
        degrees: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("degrees", "degrees", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("degrees", "degrees", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class set_rotation(ThirdBlock):
        OPCODE = "&newCanvas::set rotation to (degrees) in [canvas]"
        degrees: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("degrees", "degrees", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("degrees", "degrees", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class set_translate_xy(ThirdBlock):
        OPCODE = "&newCanvas::set translation X: (x) Y: (y) on [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class change_translate_xy(ThirdBlock):
        OPCODE = "&newCanvas::change translation X: (x) Y: (y) on [canvas]"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("x", "x", p.SRBlockAndTextInputValue, None),
                    ("y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class change_translate_x(ThirdBlock):
        OPCODE = "&newCanvas::change X translation by (amount) on [canvas]"
        amount: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("amount", "amount", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("amount", "amount", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class set_translate_x(ThirdBlock):
        OPCODE = "&newCanvas::set X scaler to (amount) on [canvas]"
        amount: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("amount", "amount", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("amount", "amount", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class change_translate_y(ThirdBlock):
        OPCODE = "&newCanvas::change Y translation by (amount) on [canvas]"
        amount: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("amount", "amount", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("amount", "amount", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class set_translate_y(ThirdBlock):
        OPCODE = "&newCanvas::set Y translation by (amount) on [canvas]"
        amount: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("amount", "amount", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("amount", "amount", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class change_scale_xy(ThirdBlock):
        OPCODE = "&newCanvas::change XY scaler by [percent]% on [canvas]"
        percent: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class set_scale_xy(ThirdBlock):
        OPCODE = "&newCanvas::set XY scaler to [percent]% on [canvas]"
        percent: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class change_scale_x(ThirdBlock):
        OPCODE = "&newCanvas::change X scaler by [percent]% on [canvas]"
        percent: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class set_scale_x(ThirdBlock):
        OPCODE = "&newCanvas::set X scaler to [percent]% on [canvas]"
        percent: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class change_scale_y(ThirdBlock):
        OPCODE = "&newCanvas::change Y scaler by [percent]% on [canvas]"
        percent: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class set_scale_y(ThirdBlock):
        OPCODE = "&newCanvas::set Y scaler to [percent]% on [canvas]"
        percent: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("percent", "percent", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class reset_transform(ThirdBlock):
        OPCODE = "&newCanvas::clear transform in [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class load_transform(ThirdBlock):
        OPCODE = "&newCanvas::set new transform (transform) on [canvas]"
        transform: INPUT_COMPATIBLE_T
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("transform", "transform", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("transform", "transform", p.SRBlockAndTextInputValue, None),),
                (("canvas", "canvas"),),
            )

    @grepr_dataclass()
    class get_transform(ThirdBlock):
        OPCODE = "&newCanvas::get current transform in [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class put_onto_sprite(ThirdBlock):
        OPCODE = "&newCanvas::set this sprites costume to [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class get_data_uri(ThirdBlock):
        OPCODE = "&newCanvas::get data URL of [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class get_width_of_canvas(ThirdBlock):
        OPCODE = "&newCanvas::get width of [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class get_height_of_canvas(ThirdBlock):
        OPCODE = "&newCanvas::get height of [canvas]"
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("canvas", "canvas"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("canvas", "canvas"),))

    @grepr_dataclass()
    class get_drawn_width_of_text(ThirdBlock):
        OPCODE = "&newCanvas::get [dimension] of text (text) when drawn to [canvas]"
        text: INPUT_COMPATIBLE_T
        dimension: str
        canvas: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("text", "text", p.SRBlockAndTextInputValue, None),),
                (("dimension", "dimension"), ("canvas", "canvas")),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("text", "text", p.SRBlockAndTextInputValue, None),),
                (("dimension", "dimension"), ("canvas", "canvas")),
            )

    @grepr_dataclass()
    class menu_text_dimension(ThirdBlock):
        OPCODE = "&newCanvas::#menu:textDimension"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_canvas(ThirdBlock):
        OPCODE = "&newCanvas::#menu:canvas"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_canvas_props(ThirdBlock):
        OPCODE = "&newCanvas::#menu:canvasProps"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
