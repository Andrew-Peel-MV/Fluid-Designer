from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesLampSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def cast_shadow(self):
        '''(Boolean) Lamp casts shadows'''
        return bool()
    @property
    def samples(self):
        '''(Integer) Number of light samples to render for each AA sample'''
        return int()
    @property
    def max_bounces(self):
        '''(Integer) Maximum number of bounces the light will contribute to the
        render'''
        return int()
    @property
    def use_multiple_importance_sampling(self):
        '''(Boolean) Use multiple importance sampling for the lamp, reduces noise
        for area lamps and sharp glossy materials'''
        return bool()
    @property
    def is_portal(self):
        '''(Boolean) Use this area lamp to guide sampling of the background, note
        that this will make the lamp invisible'''
        return bool()