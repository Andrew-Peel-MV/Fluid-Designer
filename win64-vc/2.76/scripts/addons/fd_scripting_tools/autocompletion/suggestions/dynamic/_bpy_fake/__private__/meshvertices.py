from . meshvertex import MeshVertex
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshVertices(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self, count):
        '''add
        
        Parameter:
          count: (Integer) Number of vertices to add'''
        return 
    def get(key): return MeshVertex()
    def __getitem__(key): return MeshVertex()
    def __iter__(key): yield MeshVertex()