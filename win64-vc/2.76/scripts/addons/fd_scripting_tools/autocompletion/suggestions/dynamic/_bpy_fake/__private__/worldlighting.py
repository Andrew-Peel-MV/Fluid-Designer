from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class WorldLighting(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_ambient_occlusion(self):
        '''(Boolean) Use Ambient Occlusion to add shadowing based on distance
        between objects'''
        return bool()
    @property
    def ao_factor(self):
        '''(Float) Factor for ambient occlusion blending'''
        return float()
    @property
    def ao_blend_type(self):
        '''(Enum) Defines how AO mixes with material shading
        
        [MULTIPLY, ADD]'''
        return str()
    @property
    def use_environment_light(self):
        '''(Boolean) Add light coming from the environment'''
        return bool()
    @property
    def environment_energy(self):
        '''(Float) Defines the strength of environment light'''
        return float()
    @property
    def environment_color(self):
        '''(Enum) Defines where the color of the environment light comes from
        
        [PLAIN, SKY_COLOR, SKY_TEXTURE]'''
        return str()
    @property
    def use_indirect_light(self):
        '''(Boolean) Add indirect light bouncing of surrounding objects'''
        return bool()
    @property
    def indirect_factor(self):
        '''(Float) Factor for how much surrounding objects contribute to light'''
        return float()
    @property
    def indirect_bounces(self):
        '''(Integer) Number of indirect diffuse light bounces'''
        return int()
    @property
    def gather_method(self):
        '''(Enum)
        
        [RAYTRACE, APPROXIMATE]'''
        return str()
    @property
    def passes(self):
        '''(Integer) Number of preprocessing passes to reduce over-occlusion'''
        return int()
    @property
    def distance(self):
        '''(Float) Length of rays, defines how far away other faces give
        occlusion effect'''
        return float()
    @property
    def falloff_strength(self):
        '''(Float) Attenuation falloff strength, the higher, the less influence
        distant objects have'''
        return float()
    @property
    def bias(self):
        '''(Float) Bias (in radians) to prevent smoothed faces from showing
        banding (for Raytrace Constant Jittered)'''
        return float()
    @property
    def threshold(self):
        '''(Float) Samples below this threshold will be considered fully
        shadowed/unshadowed and skipped (for Raytrace Adaptive QMC)'''
        return float()
    @property
    def adapt_to_speed(self):
        '''(Float) Use the speed vector pass to reduce AO samples in fast moving
        pixels - higher values result in more aggressive sample reduction
        (requires Vec pass enabled, for Raytrace Adaptive QMC)'''
        return float()
    @property
    def error_threshold(self):
        '''(Float) Low values are slower and higher quality'''
        return float()
    @property
    def correction(self):
        '''(Float) Ad-hoc correction for over-occlusion due to the approximation'''
        return float()
    @property
    def use_falloff(self):
        '''(Boolean) Distance will be used to attenuate shadows'''
        return bool()
    @property
    def use_cache(self):
        '''(Boolean) Cache AO results in pixels and interpolate over neighboring
        pixels for speedup'''
        return bool()
    @property
    def samples(self):
        '''(Integer) Amount of ray samples. Higher values give smoother results
        and longer rendering times'''
        return int()
    @property
    def sample_method(self):
        '''(Enum) Method for generating shadow samples (for Raytrace)
        
        [CONSTANT_JITTERED, ADAPTIVE_QMC, CONSTANT_QMC]'''
        return str()