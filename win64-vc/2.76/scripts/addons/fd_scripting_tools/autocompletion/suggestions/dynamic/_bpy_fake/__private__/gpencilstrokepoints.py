from . gpencilstrokepoint import GPencilStrokePoint
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GPencilStrokePoints(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self, count):
        '''Add a new grease pencil stroke point
        
        Parameter:
          count: (Integer) Number of points to add to the stroke'''
        return 
    def pop(self, index):
        '''Remove a grease pencil stroke point
        
        Parameter:
          index: (Integer) point index'''
        return 
    def get(key): return GPencilStrokePoint()
    def __getitem__(key): return GPencilStrokePoint()
    def __iter__(key): yield GPencilStrokePoint()