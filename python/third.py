from __future__ import annotations
from abc import ABC, abstractmethod
import copy
from gceutils import field, grepr_dataclass, enforce_argument_types
import pmp_manip as p
from uuid import UUID, uuid4
from typing import Any, Callable

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
    def create_empty(cls) -> ThirdProject:
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
        return p.SRProject(
            stage=self.stage.to_second(),
            sprites=[sprite.to_second() for sprite in self.sprites],
            sprite_layer_stack=copy.copy(self.sprite_layer_stack),
            global_variables=copy.deepcopy(self.global_variables),
            global_lists=copy.deepcopy(self.global_lists),
            global_monitors=copy.deepcopy(self.global_monitors),
            extensions=copy.deepcopy(self.extensions),
            tempo=60,
            video_transparency=50,
            video_state=p.SRVideoState.ON,
            text_to_speech_language=None,
        )

p.SRTarget
@grepr_dataclass()
class ThirdTarget:
    scripts: list[ThirdScript]
    comments: list[p.SRComment]
    costumes: list[p.SRVectorCostume | p.SRBitmapCostume]
    sounds: list[p.SRSound]
    costume_index: int
    volume: int | float

    @staticmethod
    def _default_map_position(row: int | None, col: int | None) -> tuple[int | float, int | float]:
        return (
            float(0 if col is None else col),
            float(0 if row is None else row),
        )

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

        mapper = map_position or self._default_map_position
        return [script.to_second(mapper) for script in self.scripts]

p.SRSprite
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
    def create_empty(cls, name: str) -> ThirdSprite:
        return cls(
            scripts=[],
            comments=[],
            costumes=[p.SRVectorCostume.create_empty()],
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

    def to_second(self) -> p.SRSprite:
        return p.SRSprite(
            scripts=self._to_second_scripts(),
            comments=copy.deepcopy(self.comments),
            costumes=copy.deepcopy(self.costumes),
            sounds=copy.deepcopy(self.sounds),
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
    
p.SRStage
@grepr_dataclass()
class ThirdStage(ThirdTarget):
    LAYOUT_LEFT_PADDING = 48
    LAYOUT_TOP_PADDING = 64
    LAYOUT_COLUMN_GAP = 96
    LAYOUT_BLOCK_HEIGHT = 48
    LAYOUT_STACK_PADDING = 72
    LAYOUT_SCRIPT_WIDTH = 260
    LAYOUT_NESTED_BLOCK_HEIGHT_FACTOR = 0.9

    @classmethod
    def create_empty(cls) -> ThirdStage:
        return cls(
            scripts=[],
            comments=[],
            costumes=[p.SRVectorCostume.create_empty()],
            sounds=[],
            costume_index=0,
            volume=100,
        )

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

    def to_second(self) -> p.SRStage:
        spaced_positions = self._compute_spaced_positions()

        return p.SRStage(
            scripts=self._to_second_scripts(
                map_script_position=lambda script: (
                    float(spaced_positions[id(script)][0]),
                    float(spaced_positions[id(script)][1]),
                )
            ),
            comments=copy.deepcopy(self.comments),
            costumes=copy.deepcopy(self.costumes),
            sounds=copy.deepcopy(self.sounds),
            costume_index=self.costume_index,
            volume=self.volume,
        )
    
p.SRScript
@grepr_dataclass()
class ThirdScript:
    blocks: list[ThirdBlock]
    row: int | None
    col: int | None

    def to_second(self, map_position: Callable[[int | None, int | None], tuple[int | float, int | float]]) -> p.SRScript:
        return p.SRScript(
            position=map_position(self.row, self.col),
            blocks=[block.to_second() for block in self.blocks],
        )

p.SRBlock
@grepr_dataclass()
class ThirdBlock(ABC):
    @abstractmethod
    def to_second(self) -> p.SRBlock:
        ...

# TODO: properly convert the following to actual classes not just conversion helpr
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
                else: raise ValueError(self.value, type(self.value))

            case p.SRBlockAndDropdownInputValue:
                if isinstance(self.value, ThirdBlock):
                    return input_type(block=self.value, dropdown=None)
                elif isinstance(self.value, ThirdDropdownValue):
                    return input_type(block=None, dropdown=self.value.to_second())
                elif isinstance(self.value, str):
                    return input_type(block=None, dropdown=p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.value,
                    ))
                else: raise ValueError(self.value)

            case p.SRBlockAndBoolInputValue:
                if isinstance(self.value, ThirdBlock):
                    return input_type(block=self.value, immediate=False)
                elif isinstance(self.value, bool):
                    return input_type(block=None, immediate=self.value)
                else: raise ValueError(self.value)

            case p.SRBlockOnlyInputValue | p.SREmbeddedBlockInputValue:
                if isinstance(self.value, ThirdBlock) or self.value is None:
                    return input_type(block=self.value)
                else: raise ValueError(self.value)

            case p.SRScriptInputValue:
                if isinstance(self.value, list):
                    # and all(isinstance(item, ThirdBlock) for item in self.value)
                    return input_type(blocks=self.value)
                else: raise ValueError(self.value)

            case _:
                raise ValueError("Value is not compatible with input type", self.value, input_type)

    @enforce_argument_types
    @staticmethod
    def as_input[_T: p.SRInputValue](value: list[ThirdBlock] | ThirdBlock | str | bool | ThirdDropdownValue | None | ThirdInputValue | Any, input_type: type[_T]) -> _T:
        if isinstance(value, (list, ThirdBlock, str, bool, ThirdDropdownValue, type(None))):
            return ThirdInputValue(value).to_second(input_type)
        elif isinstance(value, ThirdInputValue):
            return value.to_second(input_type)
        else:
            raise ValueError("Value is not compatible with any input type", value)

p.SRDropdownValue
@grepr_dataclass()
class ThirdDropdownValue:
    value: str
    kind: p.DropdownValueKind = p.DropdownValueKind.STANDARD

    def to_second(self) -> p.SRDropdownValue:
        return p.SRDropdownValue(self.kind, self.value)
