from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshUVLoop(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def uv(self):
        '''(Vector 2D)'''
        return mathutils.Vector()
    @property
    def pin_uv(self):
        '''(Boolean)'''
        return bool()
    @property
    def select(self):
        '''(Boolean)'''
        return bool()
    @property
    def select_edge(self):
        '''(Boolean)'''
        return bool()