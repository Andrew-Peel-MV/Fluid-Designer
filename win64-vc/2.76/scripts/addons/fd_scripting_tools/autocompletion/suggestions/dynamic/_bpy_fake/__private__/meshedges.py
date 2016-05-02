from . struct import Struct
from . meshedge import MeshEdge
from . bpy_struct import bpy_struct
import mathutils

class MeshEdges(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self, count):
        '''add
        
        Parameter:
          count: (Integer) Number of edges to add'''
        return 
    def get(key): return MeshEdge()
    def __getitem__(key): return MeshEdge()
    def __iter__(key): yield MeshEdge()