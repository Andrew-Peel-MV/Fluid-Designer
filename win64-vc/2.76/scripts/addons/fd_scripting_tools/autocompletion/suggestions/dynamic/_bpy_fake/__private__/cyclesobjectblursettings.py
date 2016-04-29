from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesObjectBlurSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def use_motion_blur(self):
        '''(Boolean) Use motion blur for this object'''
        return bool()
    @property
    def use_deform_motion(self):
        '''(Boolean) Use deformation motion blur for this object'''
        return bool()
    @property
    def motion_steps(self):
        '''(Integer) Control accuracy of deformation motion blur, more steps
        gives more memory usage (actual number of steps is 2^(steps - 1))'''
        return int()
    @property
    def use_camera_cull(self):
        '''(Boolean) Allow this object and its duplicators to be culled by camera
        space culling'''
        return bool()