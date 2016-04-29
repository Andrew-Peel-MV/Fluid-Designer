from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class TextLine(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def body(self):
        '''(String) Text in the line'''
        return str()