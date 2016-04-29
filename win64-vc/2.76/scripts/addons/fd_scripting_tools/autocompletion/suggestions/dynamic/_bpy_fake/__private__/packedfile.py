from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PackedFile(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def size(self):
        '''(Integer) Size of packed file in bytes'''
        return int()
    @property
    def data(self):
        '''(String) Raw data (bytes, exact content of the embedded file)'''
        return str()