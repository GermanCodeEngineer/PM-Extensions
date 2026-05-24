from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class newCanvas:

    @grepr_dataclass()
    class canvas_getter(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::[canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_size(ThirdBlock):
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set width: (width) height: (height) of [canvas]",
                inputs={
                    "width": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "height": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_property(ThirdBlock):
        canvas: str
        prop: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set [prop] of [canvas] to",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    ),
                    "prop": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.prop),
                },
            )

    @grepr_dataclass()
    class get_property(ThirdBlock):
        canvas: str
        prop: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::get [prop] of [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    ),
                    "prop": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.prop),
                },
            )

    @grepr_dataclass()
    class dash(ThirdBlock):
        dashing: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set line dash to (dashing) in [canvas]",
                inputs={
                    "dashing": ThirdInputValue.as_input(
                        self.dashing, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class clear_canvas(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::clear canvas [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class clear_aria(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::clear area at x: (x) y: (y) with width: (width) height: (height) on [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "width": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "height": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class draw_text(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw text (text) at (x) (y) onto [canvas]",
                inputs={
                    "text": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class draw_text_with_cap(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        cap: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw text (text) at (x) (y) with size cap (cap) onto [canvas]",
                inputs={
                    "text": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "cap": ThirdInputValue.as_input(
                        self.cap, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class outline_text(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw text outline for (text) at (x) (y) onto [canvas]",
                inputs={
                    "text": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class outline_text_with_cap(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        cap: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw text outline for (text) at (x) (y) with size cap (cap) onto [canvas]",
                inputs={
                    "text": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "cap": ThirdInputValue.as_input(
                        self.cap, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class draw_rect(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw rectangle at x: (x) y: (y) with width: (width) height: (height) on [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "width": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "height": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class outline_rect(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw rectangle outline at x: (x) y: (y) with width: (width) height: (height) on [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "width": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "height": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class preload_uri_image(ThirdBlock):
        uri: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::preload image (URI) as (NAME)",
                inputs={
                    "URI": ThirdInputValue.as_input(
                        self.uri, p.SRBlockAndTextInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class unload_uri_image(ThirdBlock):
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::unload image (NAME)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_width_of_preloaded(ThirdBlock):
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::get width of (name)",
                inputs={
                    "name": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_height_of_preloaded(ThirdBlock):
        name: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::get height of (name)",
                inputs={
                    "name": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class draw_uri_image(ThirdBlock):
        uri: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw image (URI) at x:[X] y:[Y] onto canvas [canvas]",
                inputs={
                    "URI": ThirdInputValue.as_input(
                        self.uri, p.SRBlockAndTextInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class draw_uri_image_whr(ThirdBlock):
        uri: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        rotate: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] pointed at: (ROTATE) onto canvas [canvas]",
                inputs={
                    "URI": ThirdInputValue.as_input(
                        self.uri, p.SRBlockAndTextInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "WIDTH": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "HEIGHT": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                    "ROTATE": ThirdInputValue.as_input(
                        self.rotate, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class draw_uri_image_whcx1_y1_x2_y2_r(ThirdBlock):
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

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] cropping from x:[CROPX] y:[CROPY] width:[CROPW] height:[CROPH] pointed at: (ROTATE) onto canvas [canvas]",
                inputs={
                    "URI": ThirdInputValue.as_input(
                        self.uri, p.SRBlockAndTextInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "WIDTH": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "HEIGHT": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                    "CROPX": ThirdInputValue.as_input(
                        self.cropx, p.SRBlockAndTextInputValue
                    ),
                    "CROPY": ThirdInputValue.as_input(
                        self.cropy, p.SRBlockAndTextInputValue
                    ),
                    "CROPW": ThirdInputValue.as_input(
                        self.cropw, p.SRBlockAndTextInputValue
                    ),
                    "CROPH": ThirdInputValue.as_input(
                        self.croph, p.SRBlockAndTextInputValue
                    ),
                    "ROTATE": ThirdInputValue.as_input(
                        self.rotate, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class begin_path(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::begin path drawing on [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class move_to(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::move pen to x:[x] y:[y] on [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class line_to(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::add line going to x:[x] y:[y] on [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class arc_to(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        radius: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::add arc going to x:[x] y:[y] on [canvas] with control points {:controlPoints:} and radius (radius)",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "controlPoints": ThirdInputValue.as_input(
                        ThirdInputValue(newCanvas.param()), p.SREmbeddedBlockInputValue
                    ),
                    "radius": ThirdInputValue.as_input(
                        self.radius, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class add_rect(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::add a rectangle at x:[x] y:[y] with width:[width] height:[height] to [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "width": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "height": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class add_ellipse(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        dir: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::add a ellipse at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "width": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "height": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                    "dir": ThirdInputValue.as_input(
                        self.dir, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class add_ellipse_start_stop(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        start: INPUT_COMPATIBLE_T
        end: INPUT_COMPATIBLE_T
        dir: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::add a ellipse with starting rotation (start) and ending rotation (end) at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                    "width": ThirdInputValue.as_input(
                        self.width, p.SRBlockAndTextInputValue
                    ),
                    "height": ThirdInputValue.as_input(
                        self.height, p.SRBlockAndTextInputValue
                    ),
                    "start": ThirdInputValue.as_input(
                        self.start, p.SRBlockAndTextInputValue
                    ),
                    "end": ThirdInputValue.as_input(
                        self.end, p.SRBlockAndTextInputValue
                    ),
                    "dir": ThirdInputValue.as_input(
                        self.dir, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class close_path(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::attempt to close any open path in [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class stroke(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw outline for current path in [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class fill(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::draw fill for current path in [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class save_transform(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::save [canvas]'s transform",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class restore_transform(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::reset to [canvas]'s saved transform",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class turn_rotation_left(ThirdBlock):
        degrees: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::turn left (degrees) in [canvas]",
                inputs={
                    "degrees": ThirdInputValue.as_input(
                        self.degrees, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class turn_rotation_right(ThirdBlock):
        degrees: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::turn right (degrees) in [canvas]",
                inputs={
                    "degrees": ThirdInputValue.as_input(
                        self.degrees, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_rotation(ThirdBlock):
        degrees: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set rotation to (degrees) in [canvas]",
                inputs={
                    "degrees": ThirdInputValue.as_input(
                        self.degrees, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_translate_xy(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set translation X: (x) Y: (y) on [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class change_translate_xy(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::change translation X: (x) Y: (y) on [canvas]",
                inputs={
                    "x": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class change_translate_x(ThirdBlock):
        amount: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::change X translation by (amount) on [canvas]",
                inputs={
                    "amount": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_translate_x(ThirdBlock):
        amount: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set X scaler to (amount) on [canvas]",
                inputs={
                    "amount": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class change_translate_y(ThirdBlock):
        amount: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::change Y translation by (amount) on [canvas]",
                inputs={
                    "amount": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_translate_y(ThirdBlock):
        amount: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set Y translation by (amount) on [canvas]",
                inputs={
                    "amount": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class change_scale_xy(ThirdBlock):
        percent: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::change XY scaler by [percent]% on [canvas]",
                inputs={
                    "percent": ThirdInputValue.as_input(
                        self.percent, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_scale_xy(ThirdBlock):
        percent: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set XY scaler to [percent]% on [canvas]",
                inputs={
                    "percent": ThirdInputValue.as_input(
                        self.percent, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class change_scale_x(ThirdBlock):
        percent: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::change X scaler by [percent]% on [canvas]",
                inputs={
                    "percent": ThirdInputValue.as_input(
                        self.percent, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_scale_x(ThirdBlock):
        percent: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set X scaler to [percent]% on [canvas]",
                inputs={
                    "percent": ThirdInputValue.as_input(
                        self.percent, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class change_scale_y(ThirdBlock):
        percent: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::change Y scaler by [percent]% on [canvas]",
                inputs={
                    "percent": ThirdInputValue.as_input(
                        self.percent, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class set_scale_y(ThirdBlock):
        percent: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set Y scaler to [percent]% on [canvas]",
                inputs={
                    "percent": ThirdInputValue.as_input(
                        self.percent, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class reset_transform(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::clear transform in [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class load_transform(ThirdBlock):
        transform: INPUT_COMPATIBLE_T
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set new transform (transform) on [canvas]",
                inputs={
                    "transform": ThirdInputValue.as_input(
                        self.transform, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class get_transform(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::get current transform in [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class put_onto_sprite(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::set this sprites costume to [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class get_data_uri(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::get data URL of [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class get_width_of_canvas(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::get width of [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class get_height_of_canvas(ThirdBlock):
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::get height of [canvas]",
                inputs={},
                dropdowns={
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    )
                },
            )

    @grepr_dataclass()
    class get_drawn_width_of_text(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        dimension: str
        canvas: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::get [dimension] of text (text) when drawn to [canvas]",
                inputs={
                    "text": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "dimension": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.dimension
                    ),
                    "canvas": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.canvas
                    ),
                },
            )

    @grepr_dataclass()
    class menu_text_dimension(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::#menu:textDimension", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_canvas(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&newCanvas::#menu:canvas", inputs={}, dropdowns={})

    @grepr_dataclass()
    class menu_canvas_props(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&newCanvas::#menu:canvasProps", inputs={}, dropdowns={}
            )
