from . struct import Struct
from . texture import Texture
from . bpy_struct import bpy_struct
import mathutils

class BrushTextureSlot(bpy_struct):
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
    def angle(self):
        '''(Float) Brush texture rotation'''
        return float()
    @property
    def map_mode(self):
        '''(Enum)
        
        [VIEW_PLANE, AREA_PLANE, TILED, 3D, RANDOM, STENCIL]'''
        return str()
    @property
    def tex_paint_map_mode(self):
        '''(Enum)
        
        [VIEW_PLANE, TILED, 3D, RANDOM, STENCIL]'''
        return str()
    @property
    def mask_map_mode(self):
        '''(Enum)
        
        [VIEW_PLANE, TILED, RANDOM, STENCIL]'''
        return str()
    @property
    def use_rake(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_random(self):
        '''(Boolean)'''
        return bool()
    @property
    def random_angle(self):
        '''(Float) Brush texture random angle'''
        return float()
    @property
    def has_texture_angle_source(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_random_texture_angle(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_texture_angle(self):
        '''(Boolean)'''
        return bool()