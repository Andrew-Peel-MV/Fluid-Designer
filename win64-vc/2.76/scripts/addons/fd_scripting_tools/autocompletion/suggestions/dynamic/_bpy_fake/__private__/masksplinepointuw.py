from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaskSplinePointUW(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def u(self):
        '''(Float) U coordinate of point along spline segment'''
        return float()
    @property
    def weight(self):
        '''(Float) Weight of feather point'''
        return float()
    @property
    def select(self):
        '''(Boolean) Selection status'''
        return bool()