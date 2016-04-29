from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GPUDOFSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def focus_distance(self):
        '''(Float) Viewport depth of field focus distance'''
        return float()
    @property
    def focal_length(self):
        '''(Float) Focal length for dof effect'''
        return float()
    @property
    def sensor(self):
        '''(Float) Size of sensor'''
        return float()
    @property
    def fstop(self):
        '''(Float) F-stop for dof effect'''
        return float()
    @property
    def blades(self):
        '''(Integer) Blades for dof effect'''
        return int()
    @property
    def use_high_quality(self):
        '''(Boolean) Use high quality depth of field'''
        return bool()
    @property
    def is_hq_supported(self):
        '''(Boolean) Use high quality depth of field'''
        return bool()