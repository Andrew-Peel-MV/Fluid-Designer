from . curvemap import CurveMap
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CurveMapping(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_clip(self):
        '''(Boolean) Force the curve view to fit a defined boundary'''
        return bool()
    @property
    def clip_min_x(self):
        '''(Float)'''
        return float()
    @property
    def clip_min_y(self):
        '''(Float)'''
        return float()
    @property
    def clip_max_x(self):
        '''(Float)'''
        return float()
    @property
    def clip_max_y(self):
        '''(Float)'''
        return float()
    @property
    def curves(self):
        '''(Sequence of CurveMap)'''
        return (CurveMap(),)
    @property
    def black_level(self):
        '''(Vector 3D) For RGB curves, the color that black is mapped to'''
        return mathutils.Vector()
    @property
    def white_level(self):
        '''(Vector 3D) For RGB curves, the color that white is mapped to'''
        return mathutils.Vector()
    def update(self):
        '''Update curve mapping after making changes'''
        return 
    def initialize(self):
        '''Initialize curve'''
        return 