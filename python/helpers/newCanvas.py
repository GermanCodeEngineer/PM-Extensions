from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class newCanvas:

    @grepr_dataclass()
    class canvas_getter(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::[canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class set_size(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set width: (width) height: (height) of [canvas]"
        INPUT_SPECS: ClassVar = (
            ("width", "width", p.SRBlockAndTextInputValue, None),
            ("height", "height", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class set_property(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set [prop] of [canvas] to"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"), ("prop", "prop"))
        canvas: str
        prop: str

    @grepr_dataclass()
    class get_property(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::get [prop] of [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"), ("prop", "prop"))
        canvas: str
        prop: str

    @grepr_dataclass()
    class dash(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set line dash to (dashing) in [canvas]"
        INPUT_SPECS: ClassVar = (
            ("dashing", "dashing", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        dashing: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class clear_canvas(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::clear canvas [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class clear_aria(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::clear area at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            ("width", "width", p.SRBlockAndTextInputValue, None),
            ("height", "height", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class draw_text(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::draw text (text) at (x) (y) onto [canvas]"
        INPUT_SPECS: ClassVar = (
            ("text", "text", p.SRBlockAndTextInputValue, None),
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class draw_text_with_cap(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::draw text (text) at (x) (y) with size cap (cap) onto [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("text", "text", p.SRBlockAndTextInputValue, None),
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            ("cap", "cap", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        cap: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class outline_text(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::draw text outline for (text) at (x) (y) onto [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("text", "text", p.SRBlockAndTextInputValue, None),
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class outline_text_with_cap(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::draw text outline for (text) at (x) (y) with size cap (cap) onto [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("text", "text", p.SRBlockAndTextInputValue, None),
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            ("cap", "cap", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        text: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        cap: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class draw_rect(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::draw rectangle at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            ("width", "width", p.SRBlockAndTextInputValue, None),
            ("height", "height", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class outline_rect(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::draw rectangle outline at x: (x) y: (y) with width: (width) height: (height) on [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            ("width", "width", p.SRBlockAndTextInputValue, None),
            ("height", "height", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class preload_uri_image(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::preload image (URI) as (NAME)"
        INPUT_SPECS: ClassVar = (
            ("URI", "uri", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        uri: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class unload_uri_image(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::unload image (NAME)"
        INPUT_SPECS: ClassVar = (("NAME", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_width_of_preloaded(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::get width of (name)"
        INPUT_SPECS: ClassVar = (("name", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_height_of_preloaded(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::get height of (name)"
        INPUT_SPECS: ClassVar = (("name", "name", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class draw_uri_image(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::draw image (URI) at x:[X] y:[Y] onto canvas [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("URI", "uri", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        uri: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class draw_uri_image_whr(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] pointed at: (ROTATE) onto canvas [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("URI", "uri", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
            ("WIDTH", "width", p.SRBlockAndTextInputValue, None),
            ("HEIGHT", "height", p.SRBlockAndTextInputValue, None),
            ("ROTATE", "rotate", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        uri: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        rotate: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class draw_uri_image_whcx1_y1_x2_y2_r(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::draw image (URI) at x:[X] y:[Y] width:[WIDTH] height:[HEIGHT] cropping from x:[CROPX] y:[CROPY] width:[CROPW] height:[CROPH] pointed at: (ROTATE) onto canvas [canvas]"
        )
        INPUT_SPECS: ClassVar = (
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
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
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

    @grepr_dataclass()
    class begin_path(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::begin path drawing on [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class move_to(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::move pen to x:[x] y:[y] on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class line_to(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::add line going to x:[x] y:[y] on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class arc_to(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::add arc going to x:[x] y:[y] on [canvas] with control points {:controlPoints:} and radius (radius)"
        )
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            (
                "controlPoints",
                "control_points",
                p.SREmbeddedBlockInputValue,
                lambda: newCanvas.param(),
            ),
            ("radius", "radius", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        radius: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class add_rect(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::add a rectangle at x:[x] y:[y] with width:[width] height:[height] to [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            ("width", "width", p.SRBlockAndTextInputValue, None),
            ("height", "height", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class add_ellipse(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::add a ellipse at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            ("width", "width", p.SRBlockAndTextInputValue, None),
            ("height", "height", p.SRBlockAndTextInputValue, None),
            ("dir", "dir", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        dir: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class add_ellipse_start_stop(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::add a ellipse with starting rotation (start) and ending rotation (end) at x:[x] y:[y] with width:[width] height:[height] pointed towards (dir) to [canvas]"
        )
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
            ("width", "width", p.SRBlockAndTextInputValue, None),
            ("height", "height", p.SRBlockAndTextInputValue, None),
            ("start", "start", p.SRBlockAndTextInputValue, None),
            ("end", "end", p.SRBlockAndTextInputValue, None),
            ("dir", "dir", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        width: INPUT_COMPATIBLE_T
        height: INPUT_COMPATIBLE_T
        start: INPUT_COMPATIBLE_T
        end: INPUT_COMPATIBLE_T
        dir: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class close_path(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::attempt to close any open path in [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class stroke(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::draw outline for current path in [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class fill(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::draw fill for current path in [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class save_transform(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::save [canvas]'s transform"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class restore_transform(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::reset to [canvas]'s saved transform"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class turn_rotation_left(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::turn left (degrees) in [canvas]"
        INPUT_SPECS: ClassVar = (
            ("degrees", "degrees", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        degrees: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class turn_rotation_right(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::turn right (degrees) in [canvas]"
        INPUT_SPECS: ClassVar = (
            ("degrees", "degrees", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        degrees: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class set_rotation(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set rotation to (degrees) in [canvas]"
        INPUT_SPECS: ClassVar = (
            ("degrees", "degrees", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        degrees: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class set_translate_xy(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set translation X: (x) Y: (y) on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class change_translate_xy(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::change translation X: (x) Y: (y) on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("x", "x", p.SRBlockAndTextInputValue, None),
            ("y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class change_translate_x(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::change X translation by (amount) on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("amount", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        amount: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class set_translate_x(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set X scaler to (amount) on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("amount", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        amount: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class change_translate_y(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::change Y translation by (amount) on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("amount", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        amount: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class set_translate_y(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set Y translation by (amount) on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("amount", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        amount: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class change_scale_xy(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::change XY scaler by [percent]% on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("percent", "percent", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        percent: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class set_scale_xy(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set XY scaler to [percent]% on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("percent", "percent", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        percent: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class change_scale_x(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::change X scaler by [percent]% on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("percent", "percent", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        percent: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class set_scale_x(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set X scaler to [percent]% on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("percent", "percent", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        percent: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class change_scale_y(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::change Y scaler by [percent]% on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("percent", "percent", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        percent: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class set_scale_y(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set Y scaler to [percent]% on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("percent", "percent", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        percent: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class reset_transform(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::clear transform in [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class load_transform(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set new transform (transform) on [canvas]"
        INPUT_SPECS: ClassVar = (
            ("transform", "transform", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        transform: INPUT_COMPATIBLE_T
        canvas: str

    @grepr_dataclass()
    class get_transform(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::get current transform in [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class put_onto_sprite(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::set this sprites costume to [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class get_data_uri(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::get data URL of [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class get_width_of_canvas(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::get width of [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class get_height_of_canvas(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::get height of [canvas]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("canvas", "canvas"),)
        canvas: str

    @grepr_dataclass()
    class get_drawn_width_of_text(ThirdBlock):
        OPCODE: ClassVar = (
            "&newCanvas::get [dimension] of text (text) when drawn to [canvas]"
        )
        INPUT_SPECS: ClassVar = (("text", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("dimension", "dimension"), ("canvas", "canvas"))
        text: INPUT_COMPATIBLE_T
        dimension: str
        canvas: str

    @grepr_dataclass()
    class menu_text_dimension(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::#menu:textDimension"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_canvas(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::#menu:canvas"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_canvas_props(ThirdBlock):
        OPCODE: ClassVar = "&newCanvas::#menu:canvasProps"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
