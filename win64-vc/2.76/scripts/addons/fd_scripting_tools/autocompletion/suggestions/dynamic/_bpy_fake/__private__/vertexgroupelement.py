from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class VertexGroupElement(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def group(self):
        '''(Integer)'''
        return int()
    @property
    def weight(self):
        '''(Float) Vertex Weight'''
        return float()