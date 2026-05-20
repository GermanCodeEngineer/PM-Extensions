from __future__ import annotations
from gceutils import field, grepr_dataclass, enforce_argument_types
import pmp_manip as p
from uuid import UUID, uuid4
from typing import Any

# TODO: add relevant methods?
# TODO: (atleast for scripts/blocks): implement cached conversion to SR on init + call validate immediately for good feedback if possible

# Derived from SR of py-pmp-manip
p.SRProject
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
        """
        Create an empty SRProject with no sprites, variables etc. and the default settings

        Returns:
            the empty SRProject
        """
        return cls(
            stage=ThirdStage.create_empty(),
            sprites=[],
            sprite_layer_stack=[],
            global_variables=[],
            global_lists=[],
            global_monitors=[],
            extensions=[],
        )

p.SRTarget
class ThirdTarget:
    scripts: list[ThirdScript]
    comments: list[p.SRComment]
    costumes: list[p.SRVectorCostume | p.SRBitmapCostume]
    sounds: list[p.SRSound]
    costume_index: int
    volume: int | float

p.SRSprite
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
    
p.SRStage
class ThirdStage(ThirdTarget):
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

p.SRScript
class ThirdScript:
    position: tuple[int | float, int | float]
    blocks: list[ThirdBlock]

p.SRBlock
class ThirdBlock:
    opcode: str
    inputs: dict[str, ThirdInputValue] = field(default_factory=dict)
    dropdowns: dict[str, ThirdDropdownValue] = field(default_factory=dict)
    comment: p.SRComment | None = field(default=None)
    mutation: p.SRMutation | None = field(default=None)



INPUT_COMPATIBLE_T = list[p.SRBlock] | p.SRBlock | str | bool | p.SRDropdownValue | None

# TODO: properly convert the following to actual classes not just conversion helpr
p.SRInputValue
@grepr_dataclass()
class ThirdInputValue:
    value: INPUT_COMPATIBLE_T

    def to_second[_T: p.SRInputValue](self, input_type: type[_T]) -> _T:
        match input_type:
            case p.SRBlockAndTextInputValue:
                if isinstance(self.value, p.SRBlock):
                    return input_type(block=self.value, immediate="")
                elif isinstance(self.value, str):
                    return input_type(block=None, immediate=self.value)
                elif isinstance(self.value, bool):
                    return input_type(
                        block=p.SRBlock(opcode="&operators::true" if self.value else "&operators::false"),
                        immediate="",
                    )
                else: raise ValueError(self.value, type(self.value))

            case p.SRBlockAndDropdownInputValue:
                if isinstance(self.value, p.SRBlock):
                    return input_type(block=self.value, dropdown=None)
                elif isinstance(self.value, p.SRDropdownValue):
                    return input_type(block=None, dropdown=self.value)
                elif isinstance(self.value, str):
                    return input_type(block=None, dropdown=p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.value,
                    ))
                else: raise ValueError(self.value)

            case p.SRBlockAndBoolInputValue:
                if isinstance(self.value, p.SRBlock):
                    return input_type(block=self.value, immediate=False)
                elif isinstance(self.value, bool):
                    return input_type(block=None, immediate=self.value)
                else: raise ValueError(self.value)

            case p.SRBlockOnlyInputValue | p.SREmbeddedBlockInputValue:
                if isinstance(self.value, p.SRBlock) or self.value is None:
                    return input_type(block=self.value)
                else: raise ValueError(self.value)

            case p.SRScriptInputValue:
                if isinstance(self.value, list):
                    # and all(isinstance(item, p.SRBlock) for item in self.value)
                    return input_type(blocks=self.value)
                else: raise ValueError(self.value)

            case _:
                raise ValueError("Value is not compatible with input type", self.value, input_type)

    @enforce_argument_types
    @staticmethod
    def as_input[_T: p.SRInputValue](value: INPUT_COMPATIBLE_T | ThirdInputValue | Any, input_type: type[_T]) -> _T:
        if isinstance(value, (list, p.SRBlock, str, bool, p.SRDropdownValue, type(None))):
            return ThirdInputValue(value).to_second(input_type)
        elif isinstance(value, ThirdInputValue):
            return value.to_second(input_type)
        else:
            raise ValueError("Value is not compatible with any input type", value)

p.SRDropdownValue
class ThirdDropdownValue:
    ...
