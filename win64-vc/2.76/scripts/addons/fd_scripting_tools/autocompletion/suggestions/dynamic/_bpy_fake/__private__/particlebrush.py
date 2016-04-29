from . curvemapping import CurveMapping
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ParticleBrush(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def size(self):
        '''(Integer) Radius of the brush in pixels'''
        return int()
    @property
    def strength(self):
        '''(Float) Brush strength'''
        return float()
    @property
    def count(self):
        '''(Integer) Particle count'''
        return int()
    @property
    def steps(self):
        '''(Integer) Brush steps'''
        return int()
    @property
    def puff_mode(self):
        '''(Enum)
        
        [ADD, SUB]'''
        return str()
    @property
    def use_puff_volume(self):
        '''(Boolean) Apply puff to unselected end-points (helps maintain hair
        volume when puffing root)'''
        return bool()
    @property
    def length_mode(self):
        '''(Enum)
        
        [GROW, SHRINK]'''
        return str()
    @property
    def curve(self):
        '''(CurveMapping)'''
        return CurveMapping()