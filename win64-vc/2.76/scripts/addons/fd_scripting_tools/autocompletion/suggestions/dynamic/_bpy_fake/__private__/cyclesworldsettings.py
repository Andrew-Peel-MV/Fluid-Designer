from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesWorldSettings(bpy_struct):
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
        '''(Boolean) Use multiple importance sampling for the environment,
        enabling for non-solid colors is recommended'''
        return bool()
    @property
    def sample_map_resolution(self):
        '''(Integer) Importance map size is resolution x resolution; higher
        values potentially produce less noise, at the cost of memory and speed'''
        return int()
    @property
    def samples(self):
        '''(Integer) Number of light samples to render for each AA sample'''
        return int()
    @property
    def max_bounces(self):
        '''(Integer) Maximum number of bounces the background light will
        contribute to the render'''
        return int()
    @property
    def homogeneous_volume(self):
        '''(Boolean) When using volume rendering, assume volume has the same
        density everywhere(not using any textures), for faster rendering'''
        return bool()
    @property
    def volume_sampling(self):
        '''(Enum) Sampling method to use for volumes
        
        [DISTANCE, EQUIANGULAR, MULTIPLE_IMPORTANCE]'''
        return str()
    @property
    def volume_interpolation(self):
        '''(Enum) Interpolation method to use for volumes
        
        [LINEAR, CUBIC]'''
        return str()