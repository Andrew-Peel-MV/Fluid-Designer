from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class UnifiedPaintSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_unified_size(self):
        '''(Boolean) Instead of per-brush radius, the radius is shared across
        brushes'''
        return bool()
    @property
    def use_unified_strength(self):
        '''(Boolean) Instead of per-brush strength, the strength is shared across
        brushes'''
        return bool()
    @property
    def use_unified_weight(self):
        '''(Boolean) Instead of per-brush weight, the weight is shared across
        brushes'''
        return bool()
    @property
    def use_unified_color(self):
        '''(Boolean) Instead of per-brush color, the color is shared across
        brushes'''
        return bool()
    @property
    def size(self):
        '''(Integer) Radius of the brush'''
        return int()
    @property
    def unprojected_radius(self):
        '''(Float) Radius of brush in Blender units'''
        return float()
    @property
    def strength(self):
        '''(Float) How powerful the effect of the brush is when applied'''
        return float()
    @property
    def weight(self):
        '''(Float) Weight to assign in vertex groups'''
        return float()
    @property
    def color(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def secondary_color(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def use_pressure_size(self):
        '''(Boolean) Enable tablet pressure sensitivity for size'''
        return bool()
    @property
    def use_pressure_strength(self):
        '''(Boolean) Enable tablet pressure sensitivity for strength'''
        return bool()
    @property
    def use_locked_size(self):
        '''(Boolean) When locked brush stays same size relative to object; when
        unlocked brush size is given in pixels'''
        return bool()