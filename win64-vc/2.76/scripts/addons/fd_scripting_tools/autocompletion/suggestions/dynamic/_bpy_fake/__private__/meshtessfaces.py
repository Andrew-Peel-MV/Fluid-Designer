from . struct import Struct
from . meshtessface import MeshTessFace
from . bpy_struct import bpy_struct
import mathutils

class MeshTessFaces(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Integer) The active face for this mesh'''
        return int()
    def add(self, count):
        '''add
        
        Parameter:
          count: (Integer) Number of faces to add'''
        return 
    def get(key): return MeshTessFace()
    def __getitem__(key): return MeshTessFace()
    def __iter__(key): yield MeshTessFace()