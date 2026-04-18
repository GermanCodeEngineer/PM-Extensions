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


PMP_MANIP_NAME = d.Name(id="p", ctx=d.Load())
INPUT_VALUE_NAME = d.Name(id="InputValue", ctx=d.Load())
INPUT_COMPATIBLE_T_NAME = d.Name(id="INPUT_COMPATIBLE_T", ctx=d.Load())
DROPDOWN_VALUE_NAME = d.Name(id="SRDropdownValue", ctx=d.Load())
DROPDOWN_VALUE_KIND_NAME = d.Name(id="DropdownValueKind", ctx=d.Load())
STR_NAME = d.Name(id="str", ctx=d.Load())
NOT_IMPLEMENTED_ERROR_NAME = d.Name(id="NotImplementedError", ctx=d.Load())
STATICMETHOD_NAME = d.Name(id="staticmethod", ctx=d.Load())

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
        d.Import(
            names=[
                d.alias(name="pmp_manip", asname=PMP_MANIP_NAME.id),
            ],
        ),
        d.ImportFrom(
            module="utils",
            names=[
                d.alias(name=INPUT_VALUE_NAME.id, asname=None),
                d.alias(name=INPUT_COMPATIBLE_T_NAME.id, asname=None),
            ],
            level=0,
        ),
    ]

def create_input_value_call(input_id: str, input_info: info.InputInfo, class_name: str) -> d.Call:
    if input_info.type.mode is info.InputMode.FORCED_EMBEDDED_BLOCK:
        # Use constant blocks for shadow inputs
        shadow_method_name = get_method_name(input_info.type.embedded_block_opcode)
        try_as_input_arg = d.Call(
            func=INPUT_VALUE_NAME,
            args=[
                d.Call(
                    func=d.Attribute(
                        value=d.Name(id=class_name, ctx=d.Load()),
                        attr=shadow_method_name,
                        ctx=d.Load(),
                    ),
                    args=[],
                    keywords=[],
                ),
            ],
            keywords=[],
        )
    else:
        try_as_input_arg = d.Name(id=pick_legal_name(to_snake_case(input_id)), ctx=d.Load())

    example_input_value = p.SRInputValue.from_mode(input_info.type.mode)

    return d.Call(
        func=d.Attribute(
            value=INPUT_VALUE_NAME,
            attr="try_as_input",
            ctx=d.Load(),
        ),
        args=[
            try_as_input_arg,
            d.Attribute(
                value=PMP_MANIP_NAME,
                attr=pick_legal_name(type(example_input_value).__name__),
                ctx=d.Load(),
            ),
        ],
        keywords=[],
    )

def create_dropdown_value_call(dropdown_id: str) -> d.Call:
    return d.Call(
        func=d.Attribute(
            value=PMP_MANIP_NAME,
            attr=DROPDOWN_VALUE_NAME.id,
            ctx=d.Load(),
        ),
        args=[
            d.Attribute(
                value=d.Attribute(
                    value=PMP_MANIP_NAME,
                    attr=DROPDOWN_VALUE_KIND_NAME.id,
                    ctx=d.Load(),
                ),
                attr="STANDARD",
                ctx=d.Load(),
            ),
            d.Name(id=pick_legal_name(to_snake_case(dropdown_id)), ctx=d.Load()),
        ],
        keywords=[],
    )

def create_block_call(
        old_opcode: str, class_name: str,
        input_infos: dict[str, info.InputInfo],
        dropdown_infos: dict[str, info.DropdownInfo],
    ) -> d.Call:
    new_opcode = p.info_api.get_new_by_old(old_opcode)

    input_keys = []
    input_values = []
    for input_id, input_info in input_infos.items():
        input_keys.append(d.Constant(value=input_id, kind=None))
        input_values.append(create_input_value_call(input_id, input_info, class_name))

    dropdown_keys = []
    dropdown_values = []
    for dropdown_id, dropdown_info in dropdown_infos.items():
        dropdown_keys.append(d.Constant(value=dropdown_id, kind=None))
        dropdown_values.append(create_dropdown_value_call(dropdown_id))

    return d.Call(
        func=d.Attribute(
            value=PMP_MANIP_NAME,
            attr="SRBlock",
            ctx=d.Load(),
        ),
        args=[],
        keywords=[
            d.keyword(
                arg="opcode",
                value=d.Constant(value=new_opcode, kind=None),
            ),
            d.keyword(
                arg="inputs",
                value=d.Dict(
                    keys=input_keys,
                    values=input_values,
                ),
            ),
            d.keyword(
                arg="dropdowns",
                value=d.Dict(
                    keys=dropdown_keys,
                    values=dropdown_values,
                ),
            ),
        ],
    )

def get_new_input_ids_infos(opcode_info: info.OpcodeInfo) -> dict[str, info.InputInfo] | None:
    instead_case = opcode_info.get_special_case(info.SpecialCaseType.GET_ALL_INPUT_IDS_INFO)
    if instead_case is None:
        return opcode_info.get_new_input_ids_infos(
            block=None, fti_if=None # block is not needed when there is no special case
        )
    else:
        return None
    

def create_staticmethod(old_opcode: str, opcode_info: info.OpcodeInfo, class_name: str) -> d.FunctionDef:
    block_id = get_method_name(old_opcode)
    input_infos = get_new_input_ids_infos(opcode_info)
    dropdown_infos = opcode_info.get_new_dropdown_ids_infos()

    args = []
    if input_infos is not None:
        for input_id, input_info in input_infos.items():
            # Skip shadow blocks (not needed as inputs)
            if input_info.type.mode is info.InputMode.FORCED_EMBEDDED_BLOCK:
                continue
            arg = d.arg(
                arg=pick_legal_name(to_snake_case(input_id)),
                annotation=INPUT_COMPATIBLE_T_NAME,
                type_comment=None,
            )
            args.append(arg)

        for dropdown_id, dropdown_info in dropdown_infos.items():
            arg = d.arg(
                arg=pick_legal_name(to_snake_case(dropdown_id)),
                annotation=STR_NAME,
                type_comment=None,
            )
            args.append(arg)
        
        body = [d.Return(
            value=create_block_call(old_opcode, class_name, input_infos, dropdown_infos)
        )]
    else:
        body = [d.Raise(
            exc=d.Call(
                func=NOT_IMPLEMENTED_ERROR_NAME,
                args=[
                    d.Constant(
                        value="This opcode is not supported yet, because it requires flexible input counts."
                    )
                ]
            )
        )]
    
    return d.FunctionDef(
        name=block_id,
        args=d.arguments(
            posonlyargs=[],
            args=args,
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[],
        ),
        body=body,
        decorator_list=[
            STATICMETHOD_NAME,
        ],
        returns=d.Attribute(
            value=PMP_MANIP_NAME,
            attr="SRBlock",
            ctx=d.Load(),
        ),
        type_comment=None,
        type_params=[],
    )

def create_module(extension_id: str) -> d.Module | None:
    opcode_prefix = extension_id + "_"
    class_name = pick_legal_name(extension_id)
    body = []
    for old_opcode in p.info_api.all_old:
        if not old_opcode.startswith(opcode_prefix):
            continue

        body.append(create_staticmethod(
            old_opcode=old_opcode,
            opcode_info=p.info_api.get_info_by_old(old_opcode),
            class_name=class_name,
        ))

    if not body:
        return None

    return d.Module(
        body=[
            *create_imports(),
            d.ClassDef(
                name=class_name,
                bases=[],
                keywords=[],
                body=body,
                decorator_list=[],
                type_params=[],
            ),
        ],
        type_ignores=[],
    )

def create_category_file(output_path: Path, category_id: str, category_source: str | None = None, skip_generation: bool = False) -> None:
    if not skip_generation:
        p.info_api.generate_and_add_extension(
            extension_id=category_id,
            extension_source=category_source,
        )
    

    module = create_module(category_id)
    if module is None:
        return
    code = d.unparse(module)
    try:
        code = black.format_str(code, mode=black.Mode(line_length=88))
    except Exception as error:
        print(ValueError(f"Failed to format code: {error}"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(code, "utf8")

def create_helpers() -> None:
    cfg = p.get_default_config()
    handler = lambda url: url.startswith("https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/")
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    p.init_config(cfg)

    added_categories = set()
    for old_opcode in p.info_api.all_old:
        opcode_category = old_opcode.split("_")[0]
        if opcode_category not in added_categories:
            added_categories.add(opcode_category)
            create_category_file(
                output_path=Path(f"python/helpers/{opcode_category}.py"),
                category_id=opcode_category,
                skip_generation=True,
            )
    
    create_category_file(
        output_path=Path("python/helpers/gceOOP.py"),
        category_id="gceOOP",
        category_source=("http://localhost:5173/extensions/gceOOP.js"),
    )
    create_category_file(
        output_path=Path("python/helpers/gceFuncsScopes.py"),
        category_id="gceFuncsScopes",
        category_source=("http://localhost:5173/extensions/gceFuncsScopes.js"),
    )
    create_category_file(
        output_path=Path("python/helpers/gceTestRunner.py"),
        category_id="gceTestRunner",
        category_source=("http://localhost:5173/extensions/gceTestRunner.js"),
    )

    create_category_file(
        output_path=Path("python/helpers/jwArray.py"),
        category_id="jwArray",
    )
    create_category_file(
        output_path=Path("python/helpers/dogeiscutObject.py"),
        category_id="dogeiscutObject",
        category_source="https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js",
    )
    create_category_file(
        output_path=Path("python/helpers/jwProto.py"),
        category_id="jwProto",
    )

def main() -> None:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    create_helpers()

if __name__ == "__main__":
    main()
