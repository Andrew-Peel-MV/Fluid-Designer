from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PathCompare(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def path(self):
        '''(String)'''
        return str()
    @property
    def use_glob(self):
        '''(Boolean) Enable wildcard globbing'''
        return bool()