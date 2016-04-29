from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GPUSSAOSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def factor(self):
        '''(Float) Strength of the SSAO effect'''
        return float()
    @property
    def distance_max(self):
        '''(Float) Distance of object that contribute to the SSAO effect'''
        return float()
    @property
    def attenuation(self):
        '''(Float) Attenuation constant'''
        return float()
    @property
    def samples(self):
        '''(Integer) Number of samples'''
        return int()
    @property
    def color(self):
        '''(Vector 3D) Color for screen space ambient occlusion effect'''
        return mathutils.Vector()