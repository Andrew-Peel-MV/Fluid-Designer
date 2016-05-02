from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class library_items(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def is_selected(self):
        '''(Boolean)'''
        return bool()