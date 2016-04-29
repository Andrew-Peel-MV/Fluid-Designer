from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Object_Props(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def is_ceiling(self):
        '''(Boolean)'''
        return bool()
    @property
    def is_floor(self):
        '''(Boolean)'''
        return bool()