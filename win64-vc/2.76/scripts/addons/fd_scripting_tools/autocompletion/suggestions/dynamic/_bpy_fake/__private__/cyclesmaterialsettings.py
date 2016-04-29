from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesMaterialSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def sample_as_light(self):
        '''(Boolean) Use multiple importance sampling for this material,
        disabling may reduce overall noise for large objects that emit little
        light compared to other light sources'''
        return bool()
    @property
    def use_transparent_shadow(self):
        '''(Boolean) Use transparent shadows for this material if it contains a
        Transparent BSDF, disabling will render faster but not give accurate
        shadows'''
        return bool()
    @property
    def homogeneous_volume(self):
        '''(Boolean) When using volume rendering, assume volume has the same
        density everywhere (not using any textures), for faster rendering'''
        return bool()
    @property
    def volume_sampling(self):
        '''(Enum) Sampling method to use for volumes
        
        [DISTANCE, EQUIANGULAR, MULTIPLE_IMPORTANCE]'''
        return str()
    @property
    def volume_interpolation(self):
        '''(Enum) Interpolation method to use for smoke/fire volumes
        
        [LINEAR, CUBIC]'''
        return str()