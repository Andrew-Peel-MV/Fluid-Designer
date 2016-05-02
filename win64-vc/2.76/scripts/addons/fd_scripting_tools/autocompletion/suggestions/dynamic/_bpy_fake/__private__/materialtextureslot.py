from . struct import Struct
from . object import Object
from . texture import Texture
from . bpy_struct import bpy_struct
import mathutils

class MaterialTextureSlot(bpy_struct):
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
        '''(Enum)
        
        [GLOBAL, OBJECT, UV, ORCO, STRAND, WINDOW, NORMAL, REFLECTION, STRESS,
        TANGENT]'''
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
    def use_from_dupli(self):
        '''(Boolean) Dupli's instanced from verts, faces or particles, inherit
        texture coordinate from their parent'''
        return bool()
    @property
    def use_map_to_bounds(self):
        '''(Boolean) Map coordinates in object bounds'''
        return bool()
    @property
    def use_from_original(self):
        '''(Boolean) Dupli's derive their object coordinates from the original
        object's transformation'''
        return bool()
    @property
    def use_map_color_diffuse(self):
        '''(Boolean) The texture affects basic color of the material'''
        return bool()
    @property
    def use_map_normal(self):
        '''(Boolean) The texture affects the rendered normal'''
        return bool()
    @property
    def use_map_color_spec(self):
        '''(Boolean) The texture affects the specularity color'''
        return bool()
    @property
    def use_map_mirror(self):
        '''(Boolean) The texture affects the mirror color'''
        return bool()
    @property
    def use_map_diffuse(self):
        '''(Boolean) The texture affects the value of diffuse reflectivity'''
        return bool()
    @property
    def use_map_specular(self):
        '''(Boolean) The texture affects the value of specular reflectivity'''
        return bool()
    @property
    def use_map_ambient(self):
        '''(Boolean) The texture affects the value of ambient'''
        return bool()
    @property
    def use_map_hardness(self):
        '''(Boolean) The texture affects the hardness value'''
        return bool()
    @property
    def use_map_raymir(self):
        '''(Boolean) The texture affects the ray-mirror value'''
        return bool()
    @property
    def use_map_alpha(self):
        '''(Boolean) The texture affects the alpha value'''
        return bool()
    @property
    def use_map_emit(self):
        '''(Boolean) The texture affects the emit value'''
        return bool()
    @property
    def use_map_translucency(self):
        '''(Boolean) The texture affects the translucency value'''
        return bool()
    @property
    def use_map_displacement(self):
        '''(Boolean) Let the texture displace the surface'''
        return bool()
    @property
    def use_map_warp(self):
        '''(Boolean) Let the texture warp texture coordinates of next channels'''
        return bool()
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
    def normal_map_space(self):
        '''(Enum) Set space of normal map image
        
        [CAMERA, WORLD, OBJECT, TANGENT]'''
        return str()
    @property
    def normal_factor(self):
        '''(Float) Amount texture affects normal values'''
        return float()
    @property
    def displacement_factor(self):
        '''(Float) Amount texture displaces the surface'''
        return float()
    @property
    def warp_factor(self):
        '''(Float) Amount texture affects texture coordinates of next channels'''
        return float()
    @property
    def specular_color_factor(self):
        '''(Float) Amount texture affects specular color'''
        return float()
    @property
    def diffuse_color_factor(self):
        '''(Float) Amount texture affects diffuse color'''
        return float()
    @property
    def mirror_factor(self):
        '''(Float) Amount texture affects mirror color'''
        return float()
    @property
    def alpha_factor(self):
        '''(Float) Amount texture affects alpha'''
        return float()
    @property
    def diffuse_factor(self):
        '''(Float) Amount texture affects diffuse reflectivity'''
        return float()
    @property
    def specular_factor(self):
        '''(Float) Amount texture affects specular reflectivity'''
        return float()
    @property
    def emit_factor(self):
        '''(Float) Amount texture affects emission'''
        return float()
    @property
    def hardness_factor(self):
        '''(Float) Amount texture affects hardness'''
        return float()
    @property
    def raymir_factor(self):
        '''(Float) Amount texture affects ray mirror'''
        return float()
    @property
    def translucency_factor(self):
        '''(Float) Amount texture affects translucency'''
        return float()
    @property
    def ambient_factor(self):
        '''(Float) Amount texture affects ambient'''
        return float()
    @property
    def use_map_color_emission(self):
        '''(Boolean) The texture affects the color of emission'''
        return bool()
    @property
    def use_map_color_reflection(self):
        '''(Boolean) The texture affects the color of scattered light'''
        return bool()
    @property
    def use_map_color_transmission(self):
        '''(Boolean) The texture affects the result color after other light has
        been scattered/absorbed'''
        return bool()
    @property
    def use_map_density(self):
        '''(Boolean) The texture affects the volume's density'''
        return bool()
    @property
    def use_map_emission(self):
        '''(Boolean) The texture affects the volume's emission'''
        return bool()
    @property
    def use_map_scatter(self):
        '''(Boolean) The texture affects the volume's scattering'''
        return bool()
    @property
    def use_map_reflect(self):
        '''(Boolean) The texture affects the reflected light's brightness'''
        return bool()
    @property
    def emission_color_factor(self):
        '''(Float) Amount texture affects emission color'''
        return float()
    @property
    def reflection_color_factor(self):
        '''(Float) Amount texture affects color of out-scattered light'''
        return float()
    @property
    def transmission_color_factor(self):
        '''(Float) Amount texture affects result color after light has been
        scattered/absorbed'''
        return float()
    @property
    def density_factor(self):
        '''(Float) Amount texture affects density'''
        return float()
    @property
    def emission_factor(self):
        '''(Float) Amount texture affects emission'''
        return float()
    @property
    def scattering_factor(self):
        '''(Float) Amount texture affects scattering'''
        return float()
    @property
    def reflection_factor(self):
        '''(Float) Amount texture affects brightness of out-scattered light'''
        return float()
    @property
    def use(self):
        '''(Boolean) Enable this material texture slot'''
        return bool()
    @property
    def bump_method(self):
        '''(Enum) Method to use for bump mapping
        
        [BUMP_ORIGINAL, BUMP_COMPATIBLE, BUMP_LOW_QUALITY,
        BUMP_MEDIUM_QUALITY, BUMP_BEST_QUALITY]'''
        return str()
    @property
    def bump_objectspace(self):
        '''(Enum) Space to apply bump mapping in
        
        [BUMP_VIEWSPACE, BUMP_OBJECTSPACE, BUMP_TEXTURESPACE]'''
        return str()