from . struct import Struct
from . particlesystem import ParticleSystem
from . texture import Texture
from . bpy_struct import bpy_struct
import mathutils

class SmokeFlowSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def density(self):
        '''(Float)'''
        return float()
    @property
    def smoke_color(self):
        '''(Vector 3D) Color of smoke'''
        return mathutils.Vector()
    @property
    def fuel_amount(self):
        '''(Float)'''
        return float()
    @property
    def temperature(self):
        '''(Float) Temperature difference to ambient temperature'''
        return float()
    @property
    def particle_system(self):
        '''(ParticleSystem) Particle systems emitted from the object'''
        return ParticleSystem()
    @property
    def smoke_flow_type(self):
        '''(Enum) Change how flow affects the simulation
        
        [OUTFLOW, SMOKE, BOTH, FIRE]'''
        return str()
    @property
    def smoke_flow_source(self):
        '''(Enum) Change how smoke is emitted
        
        [PARTICLES, MESH]'''
        return str()
    @property
    def use_absolute(self):
        '''(Boolean) Only allow given density value in emitter area'''
        return bool()
    @property
    def use_initial_velocity(self):
        '''(Boolean) Smoke has some initial velocity when it is emitted'''
        return bool()
    @property
    def velocity_factor(self):
        '''(Float) Multiplier of source velocity passed to smoke'''
        return float()
    @property
    def velocity_normal(self):
        '''(Float) Amount of normal directional velocity'''
        return float()
    @property
    def velocity_random(self):
        '''(Float) Amount of random velocity'''
        return float()
    @property
    def volume_density(self):
        '''(Float) Factor for smoke emitted from inside the mesh volume'''
        return float()
    @property
    def surface_distance(self):
        '''(Float) Maximum distance from mesh surface to emit smoke'''
        return float()
    @property
    def particle_size(self):
        '''(Float) Particle size in simulation cells'''
        return float()
    @property
    def use_particle_size(self):
        '''(Boolean) Set particle size in simulation cells or use nearest cell'''
        return bool()
    @property
    def subframes(self):
        '''(Integer) Number of additional samples to take between frames to
        improve quality of fast moving flows'''
        return int()
    @property
    def density_vertex_group(self):
        '''(String) Name of vertex group which determines surface emission rate'''
        return str()
    @property
    def use_texture(self):
        '''(Boolean) Use a texture to control emission strength'''
        return bool()
    @property
    def texture_map_type(self):
        '''(Enum) Texture mapping type
        
        [AUTO, UV]'''
        return str()
    @property
    def uv_layer(self):
        '''(String) UV map name'''
        return str()
    @property
    def noise_texture(self):
        '''(Texture) Texture that controls emission strength'''
        return Texture()
    @property
    def texture_size(self):
        '''(Float) Size of texture mapping'''
        return float()
    @property
    def texture_offset(self):
        '''(Float) Z-offset of texture mapping'''
        return float()