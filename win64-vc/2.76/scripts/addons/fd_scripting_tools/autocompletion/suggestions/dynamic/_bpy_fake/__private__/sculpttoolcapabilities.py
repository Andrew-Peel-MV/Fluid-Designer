from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SculptToolCapabilities(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def has_accumulate(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_auto_smooth(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_height(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_jitter(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_normal_weight(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_persistence(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_pinch_factor(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_plane_offset(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_random_texture_angle(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_sculpt_plane(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_secondary_color(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_smooth_stroke(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_space_attenuation(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_strength_pressure(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_gravity(self):
        '''(Boolean)'''
        return bool()