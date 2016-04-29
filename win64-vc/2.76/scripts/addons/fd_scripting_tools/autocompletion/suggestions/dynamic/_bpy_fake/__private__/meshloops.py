from . meshloop import MeshLoop
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshLoops(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self, count):
        '''add
        
        Parameter:
          count: (Integer) Number of loops to add'''
        return 
    def get(key): return MeshLoop()
    def __getitem__(key): return MeshLoop()
    def __iter__(key): yield MeshLoop()