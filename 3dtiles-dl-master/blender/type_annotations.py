from typing import DefaultDict
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

import bpy
from mathutils import Vector

import blender.globs

BlClasses = Union[
    bpy.types.Panel, bpy.types.Operator, bpy.types.PropertyGroup, bpy.types.AddonPreferences, bpy.types.UIList
]

# SMCIcons = Union[bpy.utils.previews.ImagePreviewCollection, Dict[str, bpy.types.ImagePreview], None]

Scene = bpy.types.ViewLayer if blender.globs.is_blender_2_80_or_newer else bpy.types.Scene

SMCObDataItem = Dict[bpy.types.Material, int]
SMCObData = Dict[str, SMCObDataItem]

MatsUV = Dict[str, DefaultDict[bpy.types.Material, List[Vector]]]

StructureItem = Dict[str, Union[List, Dict[str, Union[Dict[str, int], Tuple, bpy.types.PackedFile, None]]]]
Structure = Dict[bpy.types.Material, StructureItem]

ObMats = Union[bpy.types.bpy_prop_collection, List[bpy.types.Material]]

CombMats = Dict[int, bpy.types.Material]

MatDictItem = List[bpy.types.Material]
MatDict = DefaultDict[Tuple, MatDictItem]

CombineListDataMat = Dict[str, Union[int, bool]]
CombineListDataItem = Dict[str, Union[Dict[bpy.types.Material, CombineListDataMat], bool]]
CombineListData = Dict[bpy.types.Object, CombineListDataItem]

Diffuse = Union[bpy.types.bpy_prop_collection, Tuple[float, float, float], Tuple[int, int, int]]
