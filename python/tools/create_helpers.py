from __future__ import annotations
import sys; from pathlib import Path
sys.path.append(
    str(Path(__file__).parent.parent)
)

import argparse
import black
import dcst as d
import keyword
import re
import pmp_manip as p
from pmp_manip.opcode_info import api as info
from pmp_manip.utility.errors import MANIP_ExtensionFetchError


GCEUTILS_NAME = d.Name(id="gceutils", ctx=d.Load())
PMP_MANIP_NAME = d.Name(id="p", ctx=d.Load())
GREPR_DATACLASS_NAME = d.Name(id="grepr_dataclass", ctx=d.Load())
THIRD_BLOCK_NAME = d.Name(id="ThirdBlock", ctx=d.Load())
INPUT_COMPATIBLE_T_NAME = d.Name(id="INPUT_COMPATIBLE_T", ctx=d.Load())
STR_NAME = d.Name(id="str", ctx=d.Load())
CLASSVAR_NAME = d.Name(id="ClassVar", ctx=d.Load())

def to_snake_case(target_name: str) -> str:
    target_name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", target_name)
    target_name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", target_name)
    target_name = target_name.replace("-", "_").replace(" ", "_")
    return target_name.lower()


def pick_legal_name(target_name: str) -> str:
    cleaned = "".join(
        char if (char.isalnum() or char == "_") else "_"
        for char in target_name
    )
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    if not cleaned:
        cleaned = "param"
    if not cleaned[0].isalpha():
        cleaned = "param_" + cleaned
    if keyword.iskeyword(cleaned):
        cleaned += "_"
    return cleaned


def get_method_name(old_opcode: str) -> str:
    return pick_legal_name(to_snake_case("_".join(old_opcode.split("_")[1:])))

def create_imports() -> list[d.Import | d.ImportFrom]:
    return [
        d.ImportFrom(
            module="__future__",
            names=[
                d.alias(name="annotations", asname=None),
            ],
            level=0,
        ),
        d.ImportFrom(
            module=GCEUTILS_NAME.id,
            names=[
                d.alias(name=GREPR_DATACLASS_NAME.id, asname=None),
            ],
        ),
        d.Import(
            names=[
                d.alias(name="pmp_manip", asname=PMP_MANIP_NAME.id),
            ],
        ),
        d.ImportFrom(
            module="third",
            names=[
                d.alias(name=THIRD_BLOCK_NAME.id, asname=None),
                d.alias(name=INPUT_COMPATIBLE_T_NAME.id, asname=None),
            ],
            level=0,
        ),
        d.ImportFrom(
            module="typing",
            names=[
                d.alias(name=CLASSVAR_NAME.id, asname=None),
            ],
            level=0,
        ),
    ]

def get_new_input_ids_infos(opcode_info: info.OpcodeInfo) -> dict[str, info.InputInfo] | None:
    instead_case = opcode_info.get_special_case(info.SpecialCaseType.GET_ALL_INPUT_IDS_INFO)
    if instead_case is None:
        return opcode_info.get_new_input_ids_infos(
            block=None, fti_if=None # block is not needed when there is no special case
        )
    else:
        return None


def create_specs_value(specs: list[d.Tuple] | None) -> d.Tuple | d.Constant:
    if specs is None:
        return d.Constant(value=None, kind=None)
    return d.Tuple(elts=specs, ctx=d.Load())


def create_classvar_annotation() -> d.Name:
    return CLASSVAR_NAME


def create_input_specs(
    input_infos: dict[str, info.InputInfo],
    class_name: str,
) -> tuple[list[d.AnnAssign], list[d.Tuple]]:
    field_ann_assignments: list[d.AnnAssign] = []
    input_specs: list[d.Tuple] = []

    for input_id, input_info in input_infos.items():
        legal_name = pick_legal_name(to_snake_case(input_id))
        if input_info.type.mode is not info.InputMode.FORCED_EMBEDDED_BLOCK:
            field_ann_assignments.append(
                d.AnnAssign(
                    target=d.Name(id=legal_name, ctx=d.Store()),
                    annotation=INPUT_COMPATIBLE_T_NAME,
                    value=None,
                    simple=1,
                )
            )

        example_input_value = p.SRInputValue.from_mode(input_info.type.mode)
        input_type_name = pick_legal_name(type(example_input_value).__name__)
        shadow_method_name = (
            get_method_name(input_info.type.embedded_block_opcode)
            if input_info.type.mode is info.InputMode.FORCED_EMBEDDED_BLOCK
            else None
        )

        input_specs.append(
            d.Tuple(
                elts=[
                    d.Constant(value=input_id, kind=None),
                    d.Constant(value=legal_name, kind=None),
                    d.Attribute(value=PMP_MANIP_NAME, attr=input_type_name, ctx=d.Load()),
                    d.Lambda(
                        args=d.arguments(
                            posonlyargs=[],
                            args=[],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=d.Call(
                            func=d.Attribute(
                                value=d.Attribute(
                                    value=d.Name(id="h", ctx=d.Load()),
                                    attr=class_name,
                                    ctx=d.Load(),
                                ),
                                attr=shadow_method_name,
                                ctx=d.Load(),
                            ),
                            args=[],
                            keywords=[],
                        ),
                    )
                    if shadow_method_name is not None
                    else d.Constant(value=None, kind=None),
                ],
                ctx=d.Load(),
            )
        )

    return field_ann_assignments, input_specs


def create_dropdown_specs(
    dropdown_infos: dict[str, info.DropdownInfo],
) -> tuple[list[d.AnnAssign], list[d.Tuple]]:
    field_ann_assignments: list[d.AnnAssign] = []
    dropdown_specs: list[d.Tuple] = []

    for dropdown_id, _dropdown_info in dropdown_infos.items():
        legal_name = pick_legal_name(to_snake_case(dropdown_id))
        field_ann_assignments.append(
            d.AnnAssign(
                target=d.Name(id=legal_name, ctx=d.Store()),
                annotation=STR_NAME,
                value=None,
                simple=1,
            )
        )

        dropdown_specs.append(
            d.Tuple(
                elts=[
                    d.Constant(value=dropdown_id, kind=None),
                    d.Constant(value=legal_name, kind=None),
                ],
                ctx=d.Load(),
            )
        )

    return field_ann_assignments, dropdown_specs


def create_specs_assignments(
    input_specs: list[d.Tuple],
    dropdown_specs: list[d.Tuple],
) -> list[d.AnnAssign]:
    assigns = []
    if input_specs:
        assigns.append(
            d.AnnAssign(
                target=d.Name(id="INPUT_SPECS", ctx=d.Store()),
                annotation=create_classvar_annotation(),
                value=create_specs_value(input_specs),
                simple=1,
            )
        )
    if dropdown_specs:
        assigns.append(
            d.AnnAssign(
                target=d.Name(id="DROPDOWN_SPECS", ctx=d.Store()),
                annotation=create_classvar_annotation(),
                value=create_specs_value(dropdown_specs),
                simple=1,
            )
        )
    return assigns

def create_block_class_def(
    block_id: str,
    new_opcode: str,
    field_ann_assignments: list[d.AnnAssign],
    specs_assignments: list[d.AnnAssign],
) -> d.ClassDef:
    return d.ClassDef(
        name=block_id,
        bases=[THIRD_BLOCK_NAME],
        keywords=[],
        body=[
            d.AnnAssign(
                target=d.Name(id="OPCODE", ctx=d.Store()),
                annotation=create_classvar_annotation(),
                value=d.Constant(value=new_opcode, kind=None),
                simple=1,
            ),
            *specs_assignments,
            *field_ann_assignments,
        ],
        decorator_list=[
            d.Call(
                func=GREPR_DATACLASS_NAME,
                args=[],
                keywords=[],
            ),
        ],
        type_params=[],
    )


def create_block_helper(info_api: info.OpcodeInfoAPI, old_opcode: str, opcode_info: info.OpcodeInfo, class_name: str) -> d.FunctionDef:
    block_id = get_method_name(old_opcode)
    input_infos = get_new_input_ids_infos(opcode_info)
    dropdown_infos = opcode_info.get_new_dropdown_ids_infos()
    new_opcode = info_api.get_new_by_old(old_opcode)

    field_ann_assignments: list[d.AnnAssign] = []
    if input_infos is not None:
        input_fields, input_specs = create_input_specs(input_infos, class_name)
        dropdown_fields, dropdown_specs = create_dropdown_specs(dropdown_infos)
        field_ann_assignments.extend(input_fields)
        field_ann_assignments.extend(dropdown_fields)
        specs_assignments = create_specs_assignments(input_specs, dropdown_specs)
    else:
        specs_assignments = create_specs_assignments([], [])

    return create_block_class_def(
        block_id=block_id,
        new_opcode=new_opcode,
        field_ann_assignments=field_ann_assignments,
        specs_assignments=specs_assignments,
    )

def try_format_code(dcst: d.Module | d.DCST) -> str:
    if not isinstance(dcst, d.Module):
        dcst = d.Module(body=[dcst], type_ignores=[])
    code = d.unparse(dcst)
    try:
        return black.format_str(code, mode=black.Mode(line_length=88))
    except Exception as error:
        raise ValueError(f"Failed to format code: {error}") from error

def create_category_class(
        info_api: info.OpcodeInfoAPI, category_id: str,
        category_source: str | None = None, fallback_source: str | None = None,
        skip_generation: bool = False
    ) -> d.ClassDef:
    if not skip_generation:
        try:
            info_api.generate_and_add_extension(
                extension_id=category_id,
                extension_source=category_source,
            )
        except MANIP_ExtensionFetchError:
            if fallback_source is not None:
                info_api.generate_and_add_extension(
                    extension_id=category_id,
                    extension_source=fallback_source,
                )
            else:
                raise

    
    opcode_prefix = category_id + "_"
    class_name = pick_legal_name(category_id)
    body = []
    for old_opcode in info_api.all_old:
        if not old_opcode.startswith(opcode_prefix):
            continue

        body.append(create_block_helper(
            info_api=info_api,
            old_opcode=old_opcode,
            opcode_info=info_api.get_info_by_old(old_opcode),
            class_name=class_name,
        ))
    
    if not body:
        body.append(d.Pass())

    cls = d.ClassDef(
        name=class_name,
        bases=[],
        keywords=[],
        body=[
            *body,
        ],
        decorator_list=[],
        type_params=[],
    )
    
    # Test classes individually
    try_format_code(cls)
    return cls

##########################################################################################

LOCALHOST_BASE = "http://localhost:5173/extensions"
RELEASE_BASE = (
    "https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/refs/heads/main/extensions"
)

def own_extension_url_or_fallback(filename: str) -> tuple[str, str]:
    return (
        f"{LOCALHOST_BASE}/{filename}",
        f"{RELEASE_BASE}/{filename}"
    )

GCE_EXTENSIONS = {
    "gceOOP": own_extension_url_or_fallback("gceOOP.js"),
    "gceFuncsScopes": own_extension_url_or_fallback("gceFuncsScopes.js"),
    "gceTestRunner": own_extension_url_or_fallback("gceTestRunner.js"),
}
EXTENSIONS = GCE_EXTENSIONS | {
    "agBuffer": "https://extensions.penguinmod.com/extensions/AndrewGaming587/agBuffer.js",
    # agBuffer: vm.agBuffer.Type
    # agBufferPointer: vm.agBuffer.PointerType
    "ddeDateFormat": "https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormat.js",
    "ddeDateFormatV2": "https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormatV2.js",
    "divAlgEffects": "https://extensions.penguinmod.com/extensions/Div/divAlgEffects.js",
    # divEffect: vm.divAlgEffects.Effect
    "divIterator": "https://extensions.penguinmod.com/extensions/Div/divIterators.js",
    # divIterator: vm.divIterator.Type
    "dogeiscutObject": "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js",
    "dogeiscutRegularExpressions": "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutRegularExpressions.js",
    # dogeiscutRegularExpression: vm.dogeiscutRegularExpression.Type
    "dogeiscutSet": "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutSet.js",
    "fruitsPaintUtils": "https://extensions.penguinmod.com/extensions/Fruits555000/PaintUtils.js",
    # paintUtilsColour: Object.getPrototypeOf(vm.runtime.ext_fruitsPaintUtils.getColour({COLOUR_NAME: "orange"}))
    "jwArray": None,
    "jwColor": None,
    "jwDate": None,
    "jwLambda": None,
    "jwNum": None,
    "jwTargets": None,
    "jwVector": None,
    "jwXML": None,
    "newCanvas": None,
    # canvasData: runtime._extensionVariables.canvas
    "steve0greatnesstimers": "https://extensions.penguinmod.com/extensions/steve0greatness/timers.js",
    # externaltimer: runtime._extensionVariables.externaltimer


    "jwProto": None,
    "SPjavascriptV2": None,
}



def create_helpers(info_api: info.OpcodeInfoAPI) -> None:
    cfg = p.get_default_config()
    handler = lambda url: url.startswith("https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/")
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    cfg.ext_info_gen.node_js_exec_timeout = 10.0
    p.init_config(cfg)

    added_categories = set()
    extension_classes: list[d.ClassDef] = []
    
    for old_opcode in info_api.all_old:
        opcode_category = old_opcode.split("_")[0]
        if opcode_category not in added_categories:
            added_categories.add(opcode_category)
            
            extension_classes.append(create_category_class(
                info_api=info_api,
                category_id=opcode_category,
                skip_generation=True,
            ))
    
    for extension_id, extension_source in EXTENSIONS.items():
        if isinstance(extension_source, tuple):
            extension_source, fallback_source = extension_source
        else:
            fallback_source = None
        extension_classes.append(create_category_class(
            info_api=info_api,
            category_id=extension_id,
            category_source=extension_source,
            fallback_source=fallback_source,
        ))
    
    final_class = d.ClassDef(
        name="BlockHelpers",
        bases=[],
        keywords=[],
        body=[
            *extension_classes,
        ],
        decorator_list=[],
        type_params=[],
    )
    final_module = d.Module(
        body=[
            *create_imports(),
            final_class,
            d.Assign(
                targets=[d.Name(id="h", ctx=d.Store())],
                value=d.Name(id="BlockHelpers", ctx=d.Load()),
            ),
        ],
        type_ignores=[],
    )
    code = try_format_code(final_module)

    Path(f"python/helpers.py").write_text(code, encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    opcode_info_copy = p.info_api.opcode_info.copy()
    info_api_copy = info.OpcodeInfoAPI(opcode_info_copy)
    create_helpers(info_api_copy)

if __name__ == "__main__":
    main()
