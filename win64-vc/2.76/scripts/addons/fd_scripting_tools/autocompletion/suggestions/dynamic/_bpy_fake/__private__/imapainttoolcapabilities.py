from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ImapaintToolCapabilities(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def has_accumulate(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_space_attenuation(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_radius(self):
        '''(Boolean)'''
        return bool()