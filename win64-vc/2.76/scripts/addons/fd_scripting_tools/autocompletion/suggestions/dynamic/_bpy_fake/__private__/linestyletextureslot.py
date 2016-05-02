from . struct import Struct
from . texture import Texture
from . bpy_struct import bpy_struct
import mathutils

class LineStyleTextureSlot(bpy_struct):
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
    def use_map_color_diffuse(self):
        '''(Boolean) The texture affects basic color of the stroke'''
        return bool()
    @property
    def use_map_alpha(self):
        '''(Boolean) The texture affects the alpha value'''
        return bool()
    @property
    def use_tips(self):
        '''(Boolean) Lower half of the texture is for tips of the stroke'''
        return bool()
    @property
    def texture_coords(self):
        '''(Enum) Texture coordinates used to map the texture onto the background
        
        [WINDOW, GLOBAL, ALONG_STROKE, ORCO]'''
        return str()
    @property
    def alpha_factor(self):
        '''(Float) Amount texture affects alpha'''
        return float()
    @property
    def diffuse_color_factor(self):
        '''(Float) Amount texture affects diffuse color'''
        return float()