from . struct import Struct
from . object import Object
from . texture import Texture
from . bpy_struct import bpy_struct
import mathutils

class WorldTextureSlot(bpy_struct):
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
    def use_map_blend(self):
        '''(Boolean) Affect the color progression of the background'''
        return bool()
    @property
    def use_map_horizon(self):
        '''(Boolean) Affect the color of the horizon'''
        return bool()
    @property
    def use_map_zenith_up(self):
        '''(Boolean) Affect the color of the zenith above'''
        return bool()
    @property
    def use_map_zenith_down(self):
        '''(Boolean) Affect the color of the zenith below'''
        return bool()
    @property
    def texture_coords(self):
        '''(Enum) Texture coordinates used to map the texture onto the background
        
        [VIEW, GLOBAL, ANGMAP, SPHERE, EQUIRECT, TUBE, OBJECT]'''
        return str()
    @property
    def object(self):
        '''(Object) Object to use for mapping with Object texture coordinates'''
        return Object()
    @property
    def blend_factor(self):
        '''(Float) Amount texture affects color progression of the background'''
        return float()
    @property
    def horizon_factor(self):
        '''(Float) Amount texture affects color of the horizon'''
        return float()
    @property
    def zenith_up_factor(self):
        '''(Float) Amount texture affects color of the zenith above'''
        return float()
    @property
    def zenith_down_factor(self):
        '''(Float) Amount texture affects color of the zenith below'''
        return float()