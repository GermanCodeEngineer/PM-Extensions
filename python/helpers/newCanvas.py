from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class newCanvas:

    @staticmethod
    def canvas_getter(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::[canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_size(
        width: INPUT_COMPATIBLE_T, height: INPUT_COMPATIBLE_T, canvas: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set width: (width) height: (height) of [canvas]",
            inputs={
                "width": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "height": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_property(canvas: str, prop: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set [prop] of [canvas] to",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas),
                "prop": p.SRDropdownValue(p.DropdownValueKind.STANDARD, prop),
            },
        )

    @staticmethod
    def get_property(canvas: str, prop: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::get [prop] of [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas),
                "prop": p.SRDropdownValue(p.DropdownValueKind.STANDARD, prop),
            },
        )

    @staticmethod
    def dash(dashing: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set line dash to (dashing) in [canvas]",
            inputs={
                "dashing": InputValue.try_as_input(dashing, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def clear_canvas(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::clear canvas [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def clear_aria(
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        width: INPUT_COMPATIBLE_T,
        height: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::clear area at x: (x) y: (y) with width: (width) height: (height) on [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "width": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "height": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def draw_text(
        text: INPUT_COMPATIBLE_T,
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw text (text) at (x) (y) onto [canvas]",
            inputs={
                "text": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def draw_text_with_cap(
        text: INPUT_COMPATIBLE_T,
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        cap: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw text (text) at (x) (y) with size cap (cap) onto [canvas]",
            inputs={
                "text": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "cap": InputValue.try_as_input(cap, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def outline_text(
        text: INPUT_COMPATIBLE_T,
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw text outline for (text) at (x) (y) onto [canvas]",
            inputs={
                "text": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def outline_text_with_cap(
        text: INPUT_COMPATIBLE_T,
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        cap: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw text outline for (text) at (x) (y) with size cap (cap) onto [canvas]",
            inputs={
                "text": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "cap": InputValue.try_as_input(cap, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def draw_rect(
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        width: INPUT_COMPATIBLE_T,
        height: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw rectangle at x: (x) y: (y) with width: (width) height: (height) on [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "width": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "height": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def outline_rect(
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        width: INPUT_COMPATIBLE_T,
        height: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw rectangle outline at x: (x) y: (y) with width: (width) height: (height) on [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "width": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "height": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def preload_uri_image(
        uri: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::preload image (URI) as (NAME)",
            inputs={
                "URI": InputValue.try_as_input(uri, p.SRBlockAndTextInputValue),
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def unload_uri_image(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::unload image (NAME)",
            inputs={"NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_width_of_preloaded(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::get width of (name)",
            inputs={"name": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_height_of_preloaded(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::get height of (name)",
            inputs={"name": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def draw_uri_image(
        uri: INPUT_COMPATIBLE_T,
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw image (URI) at x:[X] y:[Y] onto canvas [canvas]",
            inputs={
                "URI": InputValue.try_as_input(uri, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def draw_uri_image_whr(
        uri: INPUT_COMPATIBLE_T,
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        width: INPUT_COMPATIBLE_T,
        height: INPUT_COMPATIBLE_T,
        rotate: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] pointed at: (ROTATE) onto canvas [canvas]",
            inputs={
                "URI": InputValue.try_as_input(uri, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "WIDTH": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "HEIGHT": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
                "ROTATE": InputValue.try_as_input(rotate, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def draw_uri_image_whcx1_y1_x2_y2_r(
        uri: INPUT_COMPATIBLE_T,
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        width: INPUT_COMPATIBLE_T,
        height: INPUT_COMPATIBLE_T,
        cropx: INPUT_COMPATIBLE_T,
        cropy: INPUT_COMPATIBLE_T,
        cropw: INPUT_COMPATIBLE_T,
        croph: INPUT_COMPATIBLE_T,
        rotate: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] cropping from x:[CROPX] y:[CROPY] width:[CROPW] height:[CROPH] pointed at: (ROTATE) onto canvas [canvas]",
            inputs={
                "URI": InputValue.try_as_input(uri, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "WIDTH": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "HEIGHT": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
                "CROPX": InputValue.try_as_input(cropx, p.SRBlockAndTextInputValue),
                "CROPY": InputValue.try_as_input(cropy, p.SRBlockAndTextInputValue),
                "CROPW": InputValue.try_as_input(cropw, p.SRBlockAndTextInputValue),
                "CROPH": InputValue.try_as_input(croph, p.SRBlockAndTextInputValue),
                "ROTATE": InputValue.try_as_input(rotate, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def begin_path(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::begin path drawing on [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def move_to(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::move pen to x:[x] y:[y] on [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def line_to(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::add line going to x:[x] y:[y] on [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def arc_to(
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        radius: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::add arc going to x:[x] y:[y] on [canvas] with control points {:controlPoints:} and radius (radius)",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "controlPoints": InputValue.try_as_input(
                    InputValue(newCanvas.param()), p.SREmbeddedBlockInputValue
                ),
                "radius": InputValue.try_as_input(radius, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def add_rect(
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        width: INPUT_COMPATIBLE_T,
        height: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::add a rectangle at x:[x] y:[y] with width:[width] height:[height] to [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "width": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "height": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def add_ellipse(
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        width: INPUT_COMPATIBLE_T,
        height: INPUT_COMPATIBLE_T,
        dir: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::add a ellipse at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "width": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "height": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
                "dir": InputValue.try_as_input(dir, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def add_ellipse_start_stop(
        x: INPUT_COMPATIBLE_T,
        y: INPUT_COMPATIBLE_T,
        width: INPUT_COMPATIBLE_T,
        height: INPUT_COMPATIBLE_T,
        start: INPUT_COMPATIBLE_T,
        end: INPUT_COMPATIBLE_T,
        dir: INPUT_COMPATIBLE_T,
        canvas: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::add a ellipse with starting rotation (start) and ending rotation (end) at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
                "width": InputValue.try_as_input(width, p.SRBlockAndTextInputValue),
                "height": InputValue.try_as_input(height, p.SRBlockAndTextInputValue),
                "start": InputValue.try_as_input(start, p.SRBlockAndTextInputValue),
                "end": InputValue.try_as_input(end, p.SRBlockAndTextInputValue),
                "dir": InputValue.try_as_input(dir, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def close_path(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::attempt to close any open path in [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def stroke(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw outline for current path in [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def fill(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::draw fill for current path in [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def save_transform(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::save [canvas]'s transform",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def restore_transform(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::reset to [canvas]'s saved transform",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def turn_rotation_left(degrees: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::turn left (degrees) in [canvas]",
            inputs={
                "degrees": InputValue.try_as_input(degrees, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def turn_rotation_right(degrees: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::turn right (degrees) in [canvas]",
            inputs={
                "degrees": InputValue.try_as_input(degrees, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_rotation(degrees: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set rotation to (degrees) in [canvas]",
            inputs={
                "degrees": InputValue.try_as_input(degrees, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_translate_xy(
        x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T, canvas: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set translation X: (x) Y: (y) on [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def change_translate_xy(
        x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T, canvas: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::change translation X: (x) Y: (y) on [canvas]",
            inputs={
                "x": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def change_translate_x(amount: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::change X translation by (amount) on [canvas]",
            inputs={
                "amount": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_translate_x(amount: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set X scaler to (amount) on [canvas]",
            inputs={
                "amount": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def change_translate_y(amount: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::change Y translation by (amount) on [canvas]",
            inputs={
                "amount": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_translate_y(amount: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set Y translation by (amount) on [canvas]",
            inputs={
                "amount": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def change_scale_xy(percent: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::change XY scaler by [percent]% on [canvas]",
            inputs={
                "percent": InputValue.try_as_input(percent, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_scale_xy(percent: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set XY scaler to [percent]% on [canvas]",
            inputs={
                "percent": InputValue.try_as_input(percent, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def change_scale_x(percent: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::change X scaler by [percent]% on [canvas]",
            inputs={
                "percent": InputValue.try_as_input(percent, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_scale_x(percent: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set X scaler to [percent]% on [canvas]",
            inputs={
                "percent": InputValue.try_as_input(percent, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def change_scale_y(percent: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::change Y scaler by [percent]% on [canvas]",
            inputs={
                "percent": InputValue.try_as_input(percent, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def set_scale_y(percent: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set Y scaler to [percent]% on [canvas]",
            inputs={
                "percent": InputValue.try_as_input(percent, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def reset_transform(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::clear transform in [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def load_transform(transform: INPUT_COMPATIBLE_T, canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set new transform (transform) on [canvas]",
            inputs={
                "transform": InputValue.try_as_input(
                    transform, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def get_transform(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::get current transform in [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def put_onto_sprite(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::set this sprites costume to [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def get_data_uri(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::get data URL of [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def get_width_of_canvas(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::get width of [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def get_height_of_canvas(canvas: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::get height of [canvas]",
            inputs={},
            dropdowns={
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas)
            },
        )

    @staticmethod
    def get_drawn_width_of_text(
        text: INPUT_COMPATIBLE_T, dimension: str, canvas: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::get [dimension] of text (text) when drawn to [canvas]",
            inputs={"text": InputValue.try_as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={
                "dimension": p.SRDropdownValue(p.DropdownValueKind.STANDARD, dimension),
                "canvas": p.SRDropdownValue(p.DropdownValueKind.STANDARD, canvas),
            },
        )

    @staticmethod
    def menu_text_dimension() -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::#menu:textDimension", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_canvas() -> p.SRBlock:
        return p.SRBlock(opcode="&newCanvas::#menu:canvas", inputs={}, dropdowns={})

    @staticmethod
    def menu_canvas_props() -> p.SRBlock:
        return p.SRBlock(
            opcode="&newCanvas::#menu:canvasProps", inputs={}, dropdowns={}
        )
