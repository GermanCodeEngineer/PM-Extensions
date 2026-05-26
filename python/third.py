from __future__ import annotations
from abc import ABC
import base64
import copy
from gceutils import field, grepr_dataclass, enforce_argument_types
import io
from lxml import etree
from PIL import Image
import pmp_manip as p
from pydub import AudioSegment
from uuid import UUID, uuid4
from typing import Any, Callable, ClassVar, Self

# TODO: add relevant methods?
# TODO: (atleast for scripts/blocks): implement cached conversion to SR on init + call validate immediately for good feedback if possible

# Derived from SR of py-pmp-manip
p.SRProject
@grepr_dataclass()
class ThirdProject:
    stage: ThirdStage
    sprites: list[ThirdSprite]
    sprite_layer_stack: list[UUID]
    global_variables: list[p.SRVariable]
    global_lists: list[p.SRList]
    global_monitors: list[p.SRMonitor]
    extensions: list[p.SRBuiltinExtension | p.SRCustomExtension]

    @classmethod
    def from_second(cls, project: p.SRProject) -> Self:
        return cls(
            stage=ThirdStage.from_second(project.stage),
            sprites=[ThirdSprite.from_second(sprite) for sprite in project.sprites],
            sprite_layer_stack=copy.copy(project.sprite_layer_stack),
            global_variables=copy.deepcopy(project.global_variables),
            global_lists=copy.deepcopy(project.global_lists),
            global_monitors=copy.deepcopy(project.global_monitors),
            extensions=copy.deepcopy(project.extensions),
        )

    @classmethod
    def create_empty(cls) -> Self:
        return cls(
            stage=ThirdStage.create_empty(),
            sprites=[],
            sprite_layer_stack=[],
            global_variables=[],
            global_lists=[],
            global_monitors=[],
            extensions=[],
        )

    def to_second(self) -> p.SRProject:
        converted_sprites = [sprite.to_second() for sprite in self.sprites]
        
        uuid_stack = []
        for uuid_idx, uuid in enumerate(self.sprite_layer_stack):
            for sprite_idx, sprite in enumerate(self.sprites):
                if sprite.uuid == uuid:
                    uuid_stack.append(converted_sprites[sprite_idx].uuid)
                    break

        return p.SRProject(
            stage=self.stage.to_second(),
            sprites=converted_sprites,
            sprite_layer_stack=uuid_stack,
            global_variables=copy.deepcopy(self.global_variables),
            global_lists=copy.deepcopy(self.global_lists),
            global_monitors=copy.deepcopy(self.global_monitors),
            extensions=copy.deepcopy(self.extensions),
            tempo=60,
            video_transparency=50,
            video_state=p.SRVideoState.ON,
            text_to_speech_language=None,
        )


@grepr_dataclass()
class ThirdTarget:
    LAYOUT_LEFT_PADDING = 48
    LAYOUT_TOP_PADDING = 64
    LAYOUT_COLUMN_GAP = 96
    LAYOUT_BLOCK_HEIGHT = 48
    LAYOUT_STACK_PADDING = 72
    LAYOUT_SCRIPT_WIDTH = 260
    LAYOUT_NESTED_BLOCK_HEIGHT_FACTOR = 0.9

    scripts: list[ThirdScript]
    comments: list[p.SRComment]
    costumes: list[ThirdVectorCostume | ThirdBitmapCostume]
    sounds: list[ThirdSound]
    costume_index: int
    volume: int | float

    @classmethod
    def from_second(cls, target: p.SRTarget) -> Self:
        converted_costumes = []
        for costume in target.costumes:
            if isinstance(costume, p.SRVectorCostume):
                converted_costumes.append(ThirdVectorCostume.from_second(costume))
            elif isinstance(costume, p.SRBitmapCostume):
                converted_costumes.append(ThirdBitmapCostume.from_second(costume))
        
        return cls(
            scripts=[ThirdScript.from_second(script) for script in target.scripts],
            comments=copy.deepcopy(target.comments),
            costumes=converted_costumes,
            sounds=[ThirdSound.from_second(sound) for sound in target.sounds],
            costume_index=target.costume_index,
            volume=target.volume,
        )

    @classmethod
    def create_empty(cls) -> Self:
        return cls(
            scripts=[],
            comments=[],
            costumes=[ThirdVectorCostume.create_empty()],
            sounds=[],
            costume_index=0,
            volume=100,
        )

    def to_second[T: p.SRTarget](self, cls: type[T] = p.SRTarget) -> T:
        return cls(
            scripts=self._to_second_scripts(),
            comments=copy.deepcopy(self.comments),
            costumes=[costume.to_second() for costume in self.costumes],
            sounds=[sound.to_second() for sound in self.sounds],
            costume_index=self.costume_index,
            volume=self.volume,
        )

    @staticmethod
    def _default_map_position(row: int | None, col: int | None) -> tuple[int | float, int | float]:
        return (float(0 if col is None else col), float(0 if row is None else row))

    def _to_second_scripts(
        self,
        map_position: Callable[[int | None, int | None], tuple[int | float, int | float]] | None = None,
        map_script_position: Callable[[ThirdScript], tuple[int | float, int | float]] | None = None,
    ) -> list[p.SRScript]:
        if map_script_position is not None:
            return [
                p.SRScript(
                    position=map_script_position(script),
                    blocks=[block.to_second() for block in script.blocks],
                )
                for script in self.scripts
            ]

        if map_position is not None:
            return [script.to_second(map_position) for script in self.scripts]

        spaced_positions = self._compute_spaced_positions()
        return [
            p.SRScript(
                position=(float(spaced_positions[id(script)][0]), float(spaced_positions[id(script)][1])),
                blocks=[block.to_second() for block in script.blocks],
            )
            for script in self.scripts
        ]

    def _group_script_columns(self) -> list[list[ThirdScript]]:
        columns: dict[int, list[ThirdScript]] = {}
        for script in self.scripts:
            col_key = 0 if script.col is None else script.col
            columns.setdefault(col_key, []).append(script)

        ordered_columns: list[list[ThirdScript]] = []
        for col_key in sorted(columns):
            column = columns[col_key]
            column.sort(key=lambda script: (script.row is None, script.row or 0))
            ordered_columns.append(column)
        return ordered_columns

    @classmethod
    def _iter_nested_blocks_from_value(cls, value: Any, seen: set[int]) -> list[ThirdBlock]:
        nested: list[ThirdBlock] = []

        if isinstance(value, ThirdInputValue):
            nested.extend(cls._iter_nested_blocks_from_value(value.value, seen))
            return nested

        if isinstance(value, ThirdBlock):
            value_id = id(value)
            if value_id in seen:
                return nested
            seen.add(value_id)
            nested.append(value)
            return nested

        if isinstance(value, dict):
            for item in value.values():
                nested.extend(cls._iter_nested_blocks_from_value(item, seen))
            return nested

        if isinstance(value, (list, tuple, set)):
            for item in value:
                nested.extend(cls._iter_nested_blocks_from_value(item, seen))
            return nested

        if hasattr(value, "__dict__"):
            for item in vars(value).values():
                nested.extend(cls._iter_nested_blocks_from_value(item, seen))

        return nested

    @classmethod
    def _estimate_block_visual_units(cls, block: ThirdBlock, seen: set[int] | None = None) -> float:
        if seen is None:
            seen = set()

        block_id = id(block)
        if block_id in seen:
            return 0.0
        seen.add(block_id)

        units = 1.0
        for attr_value in vars(block).values():
            nested_blocks = cls._iter_nested_blocks_from_value(attr_value, seen)
            for nested in nested_blocks:
                units += cls.LAYOUT_NESTED_BLOCK_HEIGHT_FACTOR * cls._estimate_block_visual_units(nested, seen)

        return units

    @classmethod
    def _estimate_script_height(cls, script: ThirdScript) -> int:
        if not script.blocks:
            return cls.LAYOUT_STACK_PADDING + cls.LAYOUT_BLOCK_HEIGHT

        block_units = 0.0
        seen: set[int] = set()
        for block in script.blocks:
            block_units += cls._estimate_block_visual_units(block, seen)

        return int(cls.LAYOUT_STACK_PADDING + cls.LAYOUT_BLOCK_HEIGHT * block_units)

    @classmethod
    def _estimate_script_width(cls, script: ThirdScript) -> int:
        return cls.LAYOUT_SCRIPT_WIDTH

    def _compute_spaced_positions(self) -> dict[int, tuple[int, int]]:
        ordered_columns = self._group_script_columns()
        script_positions: dict[int, tuple[int, int]] = {}

        cursor_x = self.LAYOUT_LEFT_PADDING
        for column in ordered_columns:
            cursor_y = self.LAYOUT_TOP_PADDING
            column_max_width = 0

            for script in column:
                script_positions[id(script)] = (cursor_x, cursor_y)
                cursor_y += self._estimate_script_height(script)
                column_max_width = max(column_max_width, self._estimate_script_width(script))

            cursor_x += column_max_width + self.LAYOUT_COLUMN_GAP

        return script_positions


@grepr_dataclass()
class ThirdSprite(ThirdTarget):
    name: str
    local_variables: list[p.SRVariable]
    local_lists: list[p.SRList]
    local_monitors: list[p.SRMonitor]
    is_visible: bool
    position: tuple[int | float, int | float]
    size: int | float
    direction: int | float
    is_draggable: bool
    rotation_style: p.SRSpriteRotationStyle
    uuid: UUID = field(default_factory=uuid4, init=False, compare=False)

    @classmethod
    def from_second(cls, sprite: p.SRSprite) -> Self:
        converted_costumes = []
        for costume in sprite.costumes:
            if isinstance(costume, p.SRVectorCostume):
                converted_costumes.append(ThirdVectorCostume.from_second(costume))
            elif isinstance(costume, p.SRBitmapCostume):
                converted_costumes.append(ThirdBitmapCostume.from_second(costume))
        
        return cls(
            scripts=[ThirdScript.from_second(script) for script in sprite.scripts],
            comments=copy.deepcopy(sprite.comments),
            costumes=converted_costumes,
            sounds=[ThirdSound.from_second(sound) for sound in sprite.sounds],
            costume_index=sprite.costume_index,
            volume=sprite.volume,
            name=sprite.name,
            local_variables=copy.deepcopy(sprite.local_variables),
            local_lists=copy.deepcopy(sprite.local_lists),
            local_monitors=copy.deepcopy(sprite.local_monitors),
            is_visible=sprite.is_visible,
            position=copy.copy(sprite.position),
            size=sprite.size,
            direction=sprite.direction,
            is_draggable=sprite.is_draggable,
            rotation_style=sprite.rotation_style,
        )

    @classmethod
    def create_empty(cls, name: str) -> Self:
        return cls(
            scripts=[],
            comments=[],
            costumes=[ThirdVectorCostume.create_empty()],
            sounds=[],
            costume_index=0,
            volume=100,
            name=name,
            local_variables=[],
            local_lists=[],
            local_monitors=[],
            is_visible=True,
            position=(0, 0),
            size=100,
            direction=90,
            is_draggable=False,
            rotation_style=p.SRSpriteRotationStyle.ALL_AROUND,
        )

    def to_second[T: p.SRSprite](self, cls: type[T] = p.SRSprite) -> T:
        return cls(
            scripts=self._to_second_scripts(),
            comments=copy.deepcopy(self.comments),
            costumes=[costume.to_second() for costume in self.costumes],
            sounds=[sound.to_second() for sound in self.sounds],
            costume_index=self.costume_index,
            volume=self.volume,
            name=self.name,
            local_variables=copy.deepcopy(self.local_variables),
            local_lists=copy.deepcopy(self.local_lists),
            local_monitors=copy.deepcopy(self.local_monitors),
            is_visible=self.is_visible,
            position=copy.copy(self.position),
            size=self.size,
            direction=self.direction,
            is_draggable=self.is_draggable,
            rotation_style=self.rotation_style,
        )


@grepr_dataclass()
class ThirdStage(ThirdTarget):
    def to_second[T: p.SRStage](self, cls: type[T] = p.SRStage) -> T:
        return super().to_second(cls)


@grepr_dataclass()
class ThirdScript:
    blocks: list[ThirdBlock]
    row: int | None
    col: int | None

    @classmethod
    def from_second(cls, script: p.SRScript) -> Self:
        return cls(
            blocks=[ThirdBlock.from_second(block) for block in script.blocks],
            row=None,
            col=None,
        )

    def to_second(self, map_position: Callable[[int | None, int | None], tuple[int | float, int | float]]) -> p.SRScript:
        return p.SRScript(
            position=map_position(self.row, self.col),
            blocks=[block.to_second() for block in self.blocks],
        )


@grepr_dataclass()
class ThirdBlock(ABC):
    OPCODE: str | None = field(default=None, init=False, compare=False)
    INPUT_SPECS: ClassVar[tuple[tuple[str, str, type[p.SRInputValue], Callable[[], ThirdBlock] | None], ...] | None] = ()
    DROPDOWN_SPECS: ClassVar[tuple[tuple[str, str], ...] | None] = ()
    _opcode_registry: ClassVar[dict[str, type[ThirdBlock]]] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        opcode = getattr(cls, "OPCODE", None)
        if opcode is not None:
            ThirdBlock._opcode_registry[opcode] = cls

    @classmethod
    def _from_second_block(
        cls,
        block: p.SRBlock,
        expected_opcode: str,
        input_specs: tuple[tuple[str, str, type[p.SRInputValue], Callable[[], ThirdBlock] | None], ...],
        dropdown_specs: tuple[tuple[str, str], ...],
    ):
        if block.opcode != expected_opcode:
            raise ValueError(f"Expected opcode '{expected_opcode}' while converting block.")

        kwargs = {}
        for input_id, attr_name, input_type, shadow_factory in input_specs:
            if shadow_factory is not None:
                continue

            input_value = block.inputs[input_id]
            if input_type in (
                p.SRBlockAndTextInputValue,
                p.SRBlockAndBoolInputValue,
            ):
                value = ThirdBlock.from_second(input_value.block) if input_value.block is not None else input_value.immediate
            elif input_type in (
                p.SRBlockAndDropdownInputValue,
            ):
                value = (
                    ThirdBlock.from_second(input_value.block)
                    if input_value.block is not None
                    else (input_value.dropdown.value if input_value.dropdown is not None else None)
                )
            elif input_type in (p.SRBlockOnlyInputValue, p.SREmbeddedBlockInputValue):
                value = ThirdBlock.from_second(input_value.block) if input_value.block is not None else None
            elif input_type is p.SRScriptInputValue:
                value = [ThirdBlock.from_second(item) for item in input_value.blocks]
            else:
                raise NotImplementedError(f"Unsupported conversion type: {input_type}")

            kwargs[attr_name] = value

        for dropdown_id, attr_name in dropdown_specs:
            kwargs[attr_name] = block.dropdowns[dropdown_id].value

        return cls(**kwargs)

    def _to_second_block(
        self,
        opcode: str,
        input_specs: tuple[tuple[str, str, type[p.SRInputValue], Callable[[], ThirdBlock] | None], ...],
        dropdown_specs: tuple[tuple[str, str], ...],
    ) -> p.SRBlock:
        inputs: dict[str, p.SRInputValue] = {}
        for input_id, attr_name, input_type, shadow_factory in input_specs:
            if shadow_factory is not None:
                value = ThirdInputValue(shadow_factory())
            else:
                value = getattr(self, attr_name)
            inputs[input_id] = ThirdInputValue.as_input(value, input_type)

        dropdowns: dict[str, p.SRDropdownValue] = {}
        for dropdown_id, attr_name in dropdown_specs:
            dropdowns[dropdown_id] = p.SRDropdownValue(
                p.DropdownValueKind.STANDARD,
                getattr(self, attr_name),
            )

        return p.SRBlock(opcode=opcode, inputs=inputs, dropdowns=dropdowns)

    @classmethod
    def _get_conversion_specs(
        cls,
    ) -> tuple[
        tuple[tuple[str, str, type[p.SRInputValue], Callable[[], ThirdBlock] | None], ...],
        tuple[tuple[str, str], ...],
    ]:
        if cls.INPUT_SPECS is None or cls.DROPDOWN_SPECS is None:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )
        return cls.INPUT_SPECS, cls.DROPDOWN_SPECS

    @classmethod
    def from_second(cls, block: p.SRBlock) -> Self:
        if cls is ThirdBlock:
            target_cls = ThirdBlock._opcode_registry.get(block.opcode)
            if target_cls is None:
                raise ValueError(f"No ThirdBlock subclass is registered for opcode '{block.opcode}'.")
            return target_cls.from_second(block)

        if cls.OPCODE is None:
            raise ValueError("Block class is missing OPCODE metadata.")

        input_specs, dropdown_specs = cls._get_conversion_specs()
        return cls._from_second_block(block, cls.OPCODE, input_specs, dropdown_specs)

    def to_second(self) -> p.SRBlock:
        cls = type(self)
        if cls.OPCODE is None:
            raise ValueError("Block class is missing OPCODE metadata.")

        input_specs, dropdown_specs = cls._get_conversion_specs()
        return self._to_second_block(cls.OPCODE, input_specs, dropdown_specs)


# TODO: properly convert the following to actual classes not just conversion helper
p.SRInputValue
@grepr_dataclass()
class ThirdInputValue:
    value: list[ThirdBlock] | ThirdBlock | str | bool | ThirdDropdownValue | None

    @enforce_argument_types
    def __init__(self, value: list[ThirdBlock] | ThirdBlock | str | bool | ThirdDropdownValue | None) -> None:
        self.value = value
    
    def to_second[_T: p.SRInputValue](self, input_type: type[_T]) -> _T:
        match input_type:
            case p.SRBlockAndTextInputValue:
                if isinstance(self.value, ThirdBlock):
                    return input_type(block=self.value.to_second(), immediate="")
                elif isinstance(self.value, str):
                    return input_type(block=None, immediate=self.value)
                elif isinstance(self.value, bool):
                    return input_type(
                        block=p.SRBlock(opcode="&operators::true" if self.value else "&operators::false"),
                        immediate="",
                    )
                else:
                    raise ValueError(self.value, type(self.value))

            case p.SRBlockAndDropdownInputValue:
                if isinstance(self.value, ThirdBlock):
                    return input_type(block=self.value.to_second(), dropdown=None)
                elif isinstance(self.value, ThirdDropdownValue):
                    return input_type(block=None, dropdown=self.value.to_second())
                elif isinstance(self.value, str):
                    return input_type(
                        block=None,
                        dropdown=p.SRDropdownValue(
                            p.DropdownValueKind.STANDARD, self.value,
                        ),
                    )
                else:
                    raise ValueError(self.value)

            case p.SRBlockAndBoolInputValue:
                if isinstance(self.value, ThirdBlock):
                    return input_type(block=self.value.to_second(), immediate=False)
                elif isinstance(self.value, bool):
                    return input_type(block=None, immediate=self.value)
                else:
                    raise ValueError(self.value)

            case p.SRBlockOnlyInputValue | p.SREmbeddedBlockInputValue:
                if isinstance(self.value, ThirdBlock) or self.value is None:
                    return input_type(block=self.value.to_second() if isinstance(self.value, ThirdBlock) else None)
                else:
                    raise ValueError(self.value)

            case p.SRScriptInputValue:
                if isinstance(self.value, list):
                    return input_type(blocks=[block.to_second() for block in self.value])
                else:
                    raise ValueError(self.value)

            case _:
                raise ValueError("Value is not compatible with input type", self.value, input_type)

    @staticmethod
    @enforce_argument_types
    def as_input[_T: p.SRInputValue](value: list[ThirdBlock] | ThirdBlock | str | bool | ThirdDropdownValue | None | ThirdInputValue, input_type: type[_T]) -> _T:
        if isinstance(value, (list, ThirdBlock, str, bool, ThirdDropdownValue, type(None))):
            return ThirdInputValue(value).to_second(input_type)
        elif isinstance(value, ThirdInputValue):
            return value.to_second(input_type)
        else:
            raise ValueError(value)

p.SRDropdownValue
@grepr_dataclass()
class ThirdDropdownValue:
    value: str
    kind: p.DropdownValueKind = p.DropdownValueKind.STANDARD

    def to_second(self) -> p.SRDropdownValue:
        return p.SRDropdownValue(self.kind, self.value)

INPUT_COMPATIBLE_T = list[ThirdBlock] | ThirdBlock | str | bool | ThirdDropdownValue | None | ThirdInputValue

p.SRVectorCostume
@grepr_dataclass()
class ThirdVectorCostume(p.SRVectorCostume):

    content: str

    @classmethod
    def from_second(cls, costume: p.SRVectorCostume) -> Self:
        xml_bytes: bytes = etree.tostring(costume.content, method="c14n")
        return cls(
            name=costume.name,
            file_extension=costume.file_extension,
            rotation_center=copy.copy(costume.rotation_center),
            content=xml_bytes.decode("utf-8"),
        )

    @classmethod
    def create_empty(cls, name: str = "empty") -> Self:
        return cls.from_second(super().create_empty(name))
    
    def to_second(self) -> p.SRVectorCostume:
        element = etree.fromstring(self.content)
        return p.SRVectorCostume(
            name=self.name,
            file_extension=self.file_extension,
            rotation_center=copy.copy(self.rotation_center),
            content=element,
        )

p.SRBitmapCostume
@grepr_dataclass()
class ThirdBitmapCostume(p.SRBitmapCostume):

    content: str

    @classmethod
    def from_second(cls, costume: p.SRBitmapCostume) -> Self:
        image_bytes_io = io.BytesIO()
        costume.content.save(image_bytes_io, format=costume.file_extension)
        return cls(
            name=costume.name,
            file_extension=costume.file_extension,
            rotation_center=copy.copy(costume.rotation_center),
            content=base64.b64encode(image_bytes_io.getvalue()).decode("ascii"),
            has_double_resolution=costume.has_double_resolution,
        )

    @classmethod
    def create_empty(cls, name: str = "empty") -> Self:
        return cls.from_second(super().create_empty(name))

    def to_second(self) -> p.SRBitmapCostume:
        image_bytes_io = io.BytesIO(base64.b64decode(self.content.encode("ascii")))
        image = Image.open(image_bytes_io)
        image.load()
        return p.SRBitmapCostume(
            name=self.name,
            file_extension=self.file_extension,
            rotation_center=copy.copy(self.rotation_center),
            content=image,
            has_double_resolution=self.has_double_resolution,
        )

p.SRSound
@grepr_dataclass()
class ThirdSound(p.SRSound):

    content: str

    @classmethod
    def from_second(cls, sound: p.SRSound) -> Self:
        sound_bytes_io = io.BytesIO()
        sound.content.export(sound_bytes_io, format=sound.file_extension)
        return cls(
            name=sound.name,
            file_extension=sound.file_extension,
            content=base64.b64encode(sound_bytes_io.getvalue()).decode("ascii"),
        )
    
    def to_second(self) -> p.SRSound:
        sound_bytes_io = io.BytesIO(base64.b64decode(self.content.encode("ascii")))
        audio_segment = AudioSegment.from_file(sound_bytes_io, format=self.file_extension)
        return p.SRSound(
            name=self.name,
            file_extension=self.file_extension,
            content=audio_segment,
        )
