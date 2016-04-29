from . pathcompare import PathCompare
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PathCompareCollection(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self):
        '''Add a new path
        
        Returns:
          pathcmp: (PathCompare)'''
        return PathCompare()
    def remove(self, pathcmp):
        '''Remove path
        
        Parameter:
          pathcmp: (PathCompare)'''
        return 
    def get(key): return PathCompare()
    def __getitem__(key): return PathCompare()
    def __iter__(key): yield PathCompare()