from . struct import Struct
from . shapekey import ShapeKey
from . unknowntype import UnknownType
from . bpy_struct import bpy_struct
import mathutils

class ShapeKey(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Name of Shape Key'''
        return str()
    @property
    def frame(self):
        '''(Float) Frame for absolute keys'''
        return float()
    @property
    def value(self):
        '''(Float) Value of shape key at the current frame'''
        return float()
    @property
    def interpolation(self):
        '''(Enum) Interpolation type for absolute shape keys
        
        [KEY_LINEAR, KEY_CARDINAL, KEY_CATMULL_ROM, KEY_BSPLINE]'''
        return str()
    @property
    def vertex_group(self):
        '''(String) Vertex weight group, to blend with basis shape'''
        return str()
    @property
    def relative_key(self):
        '''(ShapeKey) Shape used as a relative key'''
        return ShapeKey()
    @property
    def mute(self):
        '''(Boolean) Mute this shape key'''
        return bool()
    @property
    def slider_min(self):
        '''(Float) Minimum for slider'''
        return float()
    @property
    def slider_max(self):
        '''(Float) Maximum for slider'''
        return float()
    @property
    def data(self):
        '''(Sequence of UnknownType)'''
        return (UnknownType(),)