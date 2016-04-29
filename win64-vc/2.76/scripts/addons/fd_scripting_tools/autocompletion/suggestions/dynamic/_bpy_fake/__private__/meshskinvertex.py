from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshSkinVertex(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def radius(self):
        '''(Vector 2D) Radius of the skin'''
        return mathutils.Vector()
    @property
    def use_root(self):
        '''(Boolean) Vertex is a root for rotation calculations and armature
        generation'''
        return bool()
    @property
    def use_loose(self):
        '''(Boolean) If vertex has multiple adjacent edges, it is hulled to them
        directly'''
        return bool()