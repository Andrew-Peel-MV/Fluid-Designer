from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialVolume(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def step_method(self):
        '''(Enum) Method of calculating the steps through the volume
        
        [RANDOMIZED, CONSTANT]'''
        return str()
    @property
    def step_size(self):
        '''(Float) Distance between subsequent volume depth samples'''
        return float()
    @property
    def light_method(self):
        '''(Enum) Method of shading, attenuating, and scattering light through
        the volume
        
        [SHADELESS, SHADOWED, SHADED, MULTIPLE_SCATTERING,
        SHADED_PLUS_MULTIPLE_SCATTERING]'''
        return str()
    @property
    def use_external_shadows(self):
        '''(Boolean) Receive shadows from sources outside the volume (temporary)'''
        return bool()
    @property
    def use_light_cache(self):
        '''(Boolean) Pre-calculate the shading information into a voxel grid,
        speeds up shading at slightly less accuracy'''
        return bool()
    @property
    def cache_resolution(self):
        '''(Integer) Resolution of the voxel grid, low resolutions are faster,
        high resolutions use more memory'''
        return int()
    @property
    def ms_diffusion(self):
        '''(Float) Diffusion factor, the strength of the blurring effect'''
        return float()
    @property
    def ms_spread(self):
        '''(Float) Proportional distance over which the light is diffused'''
        return float()
    @property
    def ms_intensity(self):
        '''(Float) Multiplier for multiple scattered light energy'''
        return float()
    @property
    def depth_threshold(self):
        '''(Float) Stop ray marching early if transmission drops below this
        luminance - higher values give speedups in dense volumes at the
        expense of accuracy'''
        return float()
    @property
    def density(self):
        '''(Float) The base density of the volume'''
        return float()
    @property
    def density_scale(self):
        '''(Float) Multiplier for the material's density'''
        return float()
    @property
    def scattering(self):
        '''(Float) Amount of light that gets scattered out by the volume - the
        more out-scattering, the shallower the light will penetrate'''
        return float()
    @property
    def transmission_color(self):
        '''(Vector 3D) Result color of the volume, after other light has been
        scattered/absorbed'''
        return mathutils.Vector()
    @property
    def reflection_color(self):
        '''(Vector 3D) Color of light scattered out of the volume (does not
        affect transmission)'''
        return mathutils.Vector()
    @property
    def reflection(self):
        '''(Float) Multiplier to make out-scattered light brighter or darker
        (non-physically correct)'''
        return float()
    @property
    def emission_color(self):
        '''(Vector 3D) Color of emitted light'''
        return mathutils.Vector()
    @property
    def emission(self):
        '''(Float) Amount of light that gets emitted by the volume'''
        return float()
    @property
    def asymmetry(self):
        '''(Float) Back scattering (-1.0) to Forward scattering (1.0) and the
        range in between'''
        return float()