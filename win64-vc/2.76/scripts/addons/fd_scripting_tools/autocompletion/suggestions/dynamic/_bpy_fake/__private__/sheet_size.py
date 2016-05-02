from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Sheet_Size(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def leading_length_trim(self):
        '''(Float)'''
        return float()
    @property
    def width(self):
        '''(Float)'''
        return float()
    @property
    def length(self):
        '''(Float)'''
        return float()
    @property
    def leading_width_trim(self):
        '''(Float)'''
        return float()
    @property
    def comment(self):
        '''(String)'''
        return str()
    @property
    def trailing_length_trim(self):
        '''(Float)'''
        return float()
    @property
    def trailing_width_trim(self):
        '''(Float)'''
        return float()