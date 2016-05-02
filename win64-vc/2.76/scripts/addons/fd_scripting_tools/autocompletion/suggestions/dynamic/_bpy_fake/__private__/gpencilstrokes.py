from . struct import Struct
from . gpencilstroke import GPencilStroke
from . bpy_struct import bpy_struct
import mathutils

class GPencilStrokes(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self):
        '''Add a new grease pencil stroke
        
        Returns:
          stroke: (GPencilStroke) The newly created stroke'''
        return GPencilStroke()
    def remove(self, stroke):
        '''Remove a grease pencil stroke
        
        Parameter:
          stroke: (GPencilStroke) The stroke to remove'''
        return 
    def get(key): return GPencilStroke()
    def __getitem__(key): return GPencilStroke()
    def __iter__(key): yield GPencilStroke()