from . struct import Struct
from . object import Object
from . texture import Texture
from . bpy_struct import bpy_struct
import mathutils

class ParticleSettingsTextureSlot(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def texture(self):
        '''(Texture) Texture datablock used by this texture slot'''
        return Texture()
    @property
    def name(self):
        '''(String) Texture slot name'''
        return str()
    @property
    def offset(self):
        '''(Vector 3D) Fine tune of the texture mapping X, Y and Z locations'''
        return mathutils.Vector()
    @property
    def scale(self):
        '''(Vector 3D) Set scaling for the texture's X, Y and Z sizes'''
        return mathutils.Vector()
    @property
    def color(self):
        '''(Vector 3D) Default color for textures that don't return RGB or when
        RGB to intensity is enabled'''
        return mathutils.Vector()
    @property
    def blend_type(self):
        '''(Enum) Mode used to apply the texture
        
        [MIX, ADD, SUBTRACT, MULTIPLY, SCREEN, OVERLAY, DIFFERENCE, DIVIDE,
        DARKEN, LIGHTEN, HUE, SATURATION, VALUE, COLOR, SOFT_LIGHT,
        LINEAR_LIGHT]'''
        return str()
    @property
    def use_stencil(self):
        '''(Boolean) Use this texture as a blending value on the next texture'''
        return bool()
    @property
    def invert(self):
        '''(Boolean) Invert the values of the texture to reverse its effect'''
        return bool()
    @property
    def use_rgb_to_intensity(self):
        '''(Boolean) Convert texture RGB values to intensity (gray) values'''
        return bool()
    @property
    def default_value(self):
        '''(Float) Value to use for Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu
        and Hard'''
        return float()
    @property
    def output_node(self):
        '''(Enum) Which output node to use, for node-based textures
        
        [DUMMY]'''
        return str()
    @property
    def texture_coords(self):
        '''(Enum) Texture coordinates used to map the texture onto the background
        
        [GLOBAL, OBJECT, UV, ORCO, STRAND]'''
        return str()
    @property
    def object(self):
        '''(Object) Object to use for mapping with Object texture coordinates'''
        return Object()
    @property
    def uv_layer(self):
        '''(String) UV map to use for mapping with UV texture coordinates'''
        return str()
    @property
    def mapping_x(self):
        '''(Enum)
        
        [NONE, X, Y, Z]'''
        return str()
    @property
    def mapping_y(self):
        '''(Enum)
        
        [NONE, X, Y, Z]'''
        return str()
    @property
    def mapping_z(self):
        '''(Enum)
        
        [NONE, X, Y, Z]'''
        return str()
    @property
    def mapping(self):
        '''(Enum)
        
        [FLAT, CUBE, TUBE, SPHERE]'''
        return str()
    @property
    def use_map_time(self):
        '''(Boolean) Affect the emission time of the particles'''
        return bool()
    @property
    def use_map_life(self):
        '''(Boolean) Affect the life time of the particles'''
        return bool()
    @property
    def use_map_density(self):
        '''(Boolean) Affect the density of the particles'''
        return bool()
    @property
    def use_map_size(self):
        '''(Boolean) Affect the particle size'''
        return bool()
    @property
    def use_map_velocity(self):
        '''(Boolean) Affect the particle initial velocity'''
        return bool()
    @property
    def use_map_field(self):
        '''(Boolean) Affect the particle force fields'''
        return bool()
    @property
    def use_map_gravity(self):
        '''(Boolean) Affect the particle gravity'''
        return bool()
    @property
    def use_map_damp(self):
        '''(Boolean) Affect the particle velocity damping'''
        return bool()
    @property
    def use_map_clump(self):
        '''(Boolean) Affect the child clumping'''
        return bool()
    @property
    def use_map_kink_amp(self):
        '''(Boolean) Affect the child kink amplitude'''
        return bool()
    @property
    def use_map_kink_freq(self):
        '''(Boolean) Affect the child kink frequency'''
        return bool()
    @property
    def use_map_rough(self):
        '''(Boolean) Affect the child rough'''
        return bool()
    @property
    def use_map_length(self):
        '''(Boolean) Affect the child hair length'''
        return bool()
    @property
    def time_factor(self):
        '''(Float) Amount texture affects particle emission time'''
        return float()
    @property
    def life_factor(self):
        '''(Float) Amount texture affects particle life time'''
        return float()
    @property
    def density_factor(self):
        '''(Float) Amount texture affects particle density'''
        return float()
    @property
    def size_factor(self):
        '''(Float) Amount texture affects physical particle size'''
        return float()
    @property
    def velocity_factor(self):
        '''(Float) Amount texture affects particle initial velocity'''
        return float()
    @property
    def field_factor(self):
        '''(Float) Amount texture affects particle force fields'''
        return float()
    @property
    def gravity_factor(self):
        '''(Float) Amount texture affects particle gravity'''
        return float()
    @property
    def damp_factor(self):
        '''(Float) Amount texture affects particle damping'''
        return float()
    @property
    def length_factor(self):
        '''(Float) Amount texture affects child hair length'''
        return float()
    @property
    def clump_factor(self):
        '''(Float) Amount texture affects child clump'''
        return float()
    @property
    def kink_amp_factor(self):
        '''(Float) Amount texture affects child kink amplitude'''
        return float()
    @property
    def kink_freq_factor(self):
        '''(Float) Amount texture affects child kink frequency'''
        return float()
    @property
    def rough_factor(self):
        '''(Float) Amount texture affects child roughness'''
        return float()