from . struct import Struct
from . pointcache import PointCache
from . group import Group
from . effectorweights import EffectorWeights
from . bpy_struct import bpy_struct
import mathutils

class SmokeDomainSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def resolution_max(self):
        '''(Integer) Maximal resolution used in the fluid domain'''
        return int()
    @property
    def amplify(self):
        '''(Integer) Enhance the resolution of smoke by this factor using noise'''
        return int()
    @property
    def use_high_resolution(self):
        '''(Boolean) Enable high resolution (using amplification)'''
        return bool()
    @property
    def show_high_resolution(self):
        '''(Boolean) Show high resolution (using amplification)'''
        return bool()
    @property
    def noise_type(self):
        '''(Enum) Noise method which is used for creating the high resolution
        
        [NOISEWAVE, NOISEFFT]'''
        return str()
    @property
    def alpha(self):
        '''(Float) How much density affects smoke motion (higher value results in
        faster rising smoke)'''
        return float()
    @property
    def beta(self):
        '''(Float) How much heat affects smoke motion (higher value results in
        faster rising smoke)'''
        return float()
    @property
    def collision_group(self):
        '''(Group) Limit collisions to this group'''
        return Group()
    @property
    def fluid_group(self):
        '''(Group) Limit fluid objects to this group'''
        return Group()
    @property
    def effector_group(self):
        '''(Group) Limit effectors to this group'''
        return Group()
    @property
    def strength(self):
        '''(Float) Strength of noise'''
        return float()
    @property
    def dissolve_speed(self):
        '''(Integer) Dissolve Speed'''
        return int()
    @property
    def use_dissolve_smoke(self):
        '''(Boolean) Enable smoke to disappear over time'''
        return bool()
    @property
    def use_dissolve_smoke_log(self):
        '''(Boolean) Using 1/x'''
        return bool()
    @property
    def point_cache(self):
        '''(PointCache)'''
        return PointCache()
    @property
    def point_cache_compress_type(self):
        '''(Enum) Compression method to be used
        
        [CACHELIGHT, CACHEHEAVY]'''
        return str()
    @property
    def collision_extents(self):
        '''(Enum) Select which domain border will be treated as collision object
        
        [BORDEROPEN, BORDERVERTICAL, BORDERCLOSED]'''
        return str()
    @property
    def effector_weights(self):
        '''(EffectorWeights)'''
        return EffectorWeights()
    @property
    def highres_sampling(self):
        '''(Enum) Method for sampling the high resolution flow
        
        [FULLSAMPLE, LINEAR, NEAREST]'''
        return str()
    @property
    def time_scale(self):
        '''(Float) Adjust simulation speed'''
        return float()
    @property
    def vorticity(self):
        '''(Float) Amount of turbulence/rotation in fluid'''
        return float()
    @property
    def density_grid(self):
        '''(Float[32]) Smoke density grid'''
        return ''
    @property
    def velocity_grid(self):
        '''(Float[32]) Smoke velocity grid'''
        return ''
    @property
    def flame_grid(self):
        '''(Float[32]) Smoke flame grid'''
        return ''
    @property
    def color_grid(self):
        '''(Float[32]) Smoke color grid'''
        return ''
    @property
    def cell_size(self):
        '''(Vector 3D) Cell Size'''
        return mathutils.Vector()
    @property
    def start_point(self):
        '''(Vector 3D) Start point'''
        return mathutils.Vector()
    @property
    def domain_resolution(self):
        '''(Integer[3]) Smoke Grid Resolution'''
        return int()
    @property
    def burning_rate(self):
        '''(Float) Speed of the burning reaction (use larger values for smaller
        flame)'''
        return float()
    @property
    def flame_smoke(self):
        '''(Float) Amount of smoke created by burning fuel'''
        return float()
    @property
    def flame_vorticity(self):
        '''(Float) Additional vorticity for the flames'''
        return float()
    @property
    def flame_ignition(self):
        '''(Float) Minimum temperature of flames'''
        return float()
    @property
    def flame_max_temp(self):
        '''(Float) Maximum temperature of flames'''
        return float()
    @property
    def flame_smoke_color(self):
        '''(Vector 3D) Color of smoke emitted from burning fuel'''
        return mathutils.Vector()
    @property
    def use_adaptive_domain(self):
        '''(Boolean) Adapt simulation resolution and size to fluid'''
        return bool()
    @property
    def additional_res(self):
        '''(Integer) Maximum number of additional cells'''
        return int()
    @property
    def adapt_margin(self):
        '''(Integer) Margin added around fluid to minimize boundary interference'''
        return int()
    @property
    def adapt_threshold(self):
        '''(Float) Maximum amount of fluid cell can contain before it is
        considered empty'''
        return float()