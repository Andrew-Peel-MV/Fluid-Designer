from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SplinePoint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def select(self):
        '''(Boolean) Selection status'''
        return bool()
    @property
    def hide(self):
        '''(Boolean) Visibility status'''
        return bool()
    @property
    def co(self):
        '''(Float[4]) Point coordinates'''
        return ''
    @property
    def weight(self):
        '''(Float) NURBS weight'''
        return float()
    @property
    def tilt(self):
        '''(Float) Tilt in 3D View'''
        return float()
    @property
    def weight_softbody(self):
        '''(Float) Softbody goal weight'''
        return float()
    @property
    def radius(self):
        '''(Float) Radius for beveling'''
        return float()