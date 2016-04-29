from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialRaytraceMirror(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use(self):
        '''(Boolean) Enable raytraced reflections'''
        return bool()
    @property
    def reflect_factor(self):
        '''(Float) Amount of mirror reflection for raytrace'''
        return float()
    @property
    def fresnel(self):
        '''(Float) Power of Fresnel for mirror reflection'''
        return float()
    @property
    def fresnel_factor(self):
        '''(Float) Blending factor for Fresnel'''
        return float()
    @property
    def gloss_factor(self):
        '''(Float) The shininess of the reflection (values < 1.0 give diffuse,
        blurry reflections)'''
        return float()
    @property
    def gloss_anisotropic(self):
        '''(Float) The shape of the reflection, from 0.0 (circular) to 1.0 (fully
        stretched along the tangent'''
        return float()
    @property
    def gloss_samples(self):
        '''(Integer) Number of cone samples averaged for blurry reflections'''
        return int()
    @property
    def gloss_threshold(self):
        '''(Float) Threshold for adaptive sampling (if a sample contributes less
        than this amount [as a percentage], sampling is stopped)'''
        return float()
    @property
    def depth(self):
        '''(Integer) Maximum allowed number of light inter-reflections'''
        return int()
    @property
    def distance(self):
        '''(Float) Maximum distance of reflected rays (reflections further than
        this range fade to sky color or material color)'''
        return float()
    @property
    def fade_to(self):
        '''(Enum) The color that rays with no intersection within the Max
        Distance take (material color can be best for indoor scenes, sky color
        for outdoor)
        
        [FADE_TO_SKY, FADE_TO_MATERIAL]'''
        return str()