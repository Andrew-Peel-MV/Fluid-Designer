from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GPencilStrokePoint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def co(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def pressure(self):
        '''(Float) Pressure of tablet at point when drawing it'''
        return float()
    @property
    def select(self):
        '''(Boolean) Point is selected for viewport editing'''
        return bool()