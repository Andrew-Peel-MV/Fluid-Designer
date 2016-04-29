from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BrushCapabilities(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def has_overlay(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_random_texture_angle(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_spacing(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_smooth_stroke(self):
        '''(Boolean)'''
        return bool()