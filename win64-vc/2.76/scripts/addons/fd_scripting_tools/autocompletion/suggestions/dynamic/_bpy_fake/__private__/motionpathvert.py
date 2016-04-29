from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MotionPathVert(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def co(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def select(self):
        '''(Boolean) Path point is selected for editing'''
        return bool()