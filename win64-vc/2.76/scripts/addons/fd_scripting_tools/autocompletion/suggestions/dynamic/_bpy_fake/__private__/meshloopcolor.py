from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshLoopColor(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def color(self):
        '''(Vector 3D)'''
        return mathutils.Vector()