from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SequenceElement(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def filename(self):
        '''(String)'''
        return str()
    @property
    def orig_width(self):
        '''(Integer) Original image width'''
        return int()
    @property
    def orig_height(self):
        '''(Integer) Original image height'''
        return int()