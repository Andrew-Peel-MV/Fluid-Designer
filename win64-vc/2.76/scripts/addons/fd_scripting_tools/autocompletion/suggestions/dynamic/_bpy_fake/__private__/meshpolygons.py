from . struct import Struct
from . meshpolygon import MeshPolygon
from . bpy_struct import bpy_struct
import mathutils

class MeshPolygons(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Integer) The active polygon for this mesh'''
        return int()
    def add(self, count):
        '''add
        
        Parameter:
          count: (Integer) Number of polygons to add'''
        return 
    def get(key): return MeshPolygon()
    def __getitem__(key): return MeshPolygon()
    def __iter__(key): yield MeshPolygon()