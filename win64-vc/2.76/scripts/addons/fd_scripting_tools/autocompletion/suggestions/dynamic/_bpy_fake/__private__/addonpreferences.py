from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class AddonPreferences(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def bl_idname(self):
        '''(String)'''
        return str()