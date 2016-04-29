from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialRaytraceTransparency(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def ior(self):
        '''(Float) Angular index of refraction for raytraced refraction'''
        return float()
    @property
    def fresnel(self):
        '''(Float) Power of Fresnel for transparency (Ray or ZTransp)'''
        return float()
    @property
    def fresnel_factor(self):
        '''(Float) Blending factor for Fresnel'''
        return float()
    @property
    def gloss_factor(self):
        '''(Float) The clarity of the refraction. Values < 1.0 give diffuse,
        blurry refractions'''
        return float()
    @property
    def gloss_samples(self):
        '''(Integer) Number of cone samples averaged for blurry refractions'''
        return int()
    @property
    def gloss_threshold(self):
        '''(Float) Threshold for adaptive sampling. If a sample contributes less
        than this amount (as a percentage), sampling is stopped'''
        return float()
    @property
    def depth(self):
        '''(Integer) Maximum allowed number of light inter-refractions'''
        return int()
    @property
    def filter(self):
        '''(Float) Amount to blend in the material's diffuse color in raytraced
        transparency (simulating absorption)'''
        return float()
    @property
    def depth_max(self):
        '''(Float) Maximum depth for light to travel through the transparent
        material before becoming fully filtered (0.0 is disabled)'''
        return float()
    @property
    def falloff(self):
        '''(Float) Falloff power for transmissivity filter effect (1.0 is linear)'''
        return float()