from . texture import Texture
from . struct import Struct
from . group import Group
from . effectorweights import EffectorWeights
from . object import Object
from . pointcache import PointCache
from . bpy_struct import bpy_struct
import mathutils

class DynamicPaintSurface(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def surface_format(self):
        '''(Enum) Surface Format
        
        [VERTEX, IMAGE]'''
        return str()
    @property
    def surface_type(self):
        '''(Enum) Surface Type
        
        [PAINT]'''
        return str()
    @property
    def is_active(self):
        '''(Boolean) Toggle whether surface is processed or ignored'''
        return bool()
    @property
    def show_preview(self):
        '''(Boolean) Display surface preview in 3D-views'''
        return bool()
    @property
    def name(self):
        '''(String) Surface name'''
        return str()
    @property
    def brush_group(self):
        '''(Group) Only use brush objects from this group'''
        return Group()
    @property
    def use_dissolve(self):
        '''(Boolean) Enable to make surface changes disappear over time'''
        return bool()
    @property
    def dissolve_speed(self):
        '''(Integer) Approximately in how many frames should dissolve happen'''
        return int()
    @property
    def use_drying(self):
        '''(Boolean) Enable to make surface wetness dry over time'''
        return bool()
    @property
    def dry_speed(self):
        '''(Integer) Approximately in how many frames should drying happen'''
        return int()
    @property
    def image_resolution(self):
        '''(Integer) Output image resolution'''
        return int()
    @property
    def uv_layer(self):
        '''(String) UV map name'''
        return str()
    @property
    def frame_start(self):
        '''(Integer) Simulation start frame'''
        return int()
    @property
    def frame_end(self):
        '''(Integer) Simulation end frame'''
        return int()
    @property
    def frame_substeps(self):
        '''(Integer) Do extra frames between scene frames to ensure smooth motion'''
        return int()
    @property
    def use_antialiasing(self):
        '''(Boolean) Use 5x multisampling to smooth paint edges'''
        return bool()
    @property
    def brush_influence_scale(self):
        '''(Float) Adjust influence brush objects have on this surface'''
        return float()
    @property
    def brush_radius_scale(self):
        '''(Float) Adjust radius of proximity brushes or particles for this
        surface'''
        return float()
    @property
    def init_color_type(self):
        '''(Enum)
        
        [NONE, COLOR, TEXTURE, VERTEX_COLOR]'''
        return str()
    @property
    def init_color(self):
        '''(Float[4]) Initial color of the surface'''
        return ''
    @property
    def init_texture(self):
        '''(Texture)'''
        return Texture()
    @property
    def init_layername(self):
        '''(String)'''
        return str()
    @property
    def effect_ui(self):
        '''(Enum)
        
        [SPREAD, DRIP, SHRINK]'''
        return str()
    @property
    def use_dry_log(self):
        '''(Boolean) Use logarithmic drying (makes high values to dry faster than
        low values)'''
        return bool()
    @property
    def use_dissolve_log(self):
        '''(Boolean) Use logarithmic dissolve (makes high values to fade faster
        than low values)'''
        return bool()
    @property
    def use_spread(self):
        '''(Boolean) Process spread effect (spread wet paint around surface)'''
        return bool()
    @property
    def spread_speed(self):
        '''(Float) How fast spread effect moves on the canvas surface'''
        return float()
    @property
    def color_dry_threshold(self):
        '''(Float) The wetness level when colors start to shift to the background'''
        return float()
    @property
    def color_spread_speed(self):
        '''(Float) How fast colors get mixed within wet paint'''
        return float()
    @property
    def use_drip(self):
        '''(Boolean) Process drip effect (drip wet paint to gravity direction)'''
        return bool()
    @property
    def use_shrink(self):
        '''(Boolean) Process shrink effect (shrink paint areas)'''
        return bool()
    @property
    def shrink_speed(self):
        '''(Float) How fast shrink effect moves on the canvas surface'''
        return float()
    @property
    def effector_weights(self):
        '''(EffectorWeights)'''
        return EffectorWeights()
    @property
    def drip_velocity(self):
        '''(Float) How much surface velocity affects dripping'''
        return float()
    @property
    def drip_acceleration(self):
        '''(Float) How much surface acceleration affects dripping'''
        return float()
    @property
    def use_premultiply(self):
        '''(Boolean) Multiply color by alpha (recommended for Blender input)'''
        return bool()
    @property
    def image_output_path(self):
        '''(String) Directory to save the textures'''
        return str()
    @property
    def output_name_a(self):
        '''(String) Name used to save output from this surface'''
        return str()
    @property
    def use_output_a(self):
        '''(Boolean) Save this output layer'''
        return bool()
    @property
    def output_name_b(self):
        '''(String) Name used to save output from this surface'''
        return str()
    @property
    def use_output_b(self):
        '''(Boolean) Save this output layer'''
        return bool()
    @property
    def preview_id(self):
        '''(Enum)
        
        [PAINT, WETMAP]'''
        return str()
    @property
    def depth_clamp(self):
        '''(Float) Maximum level of depth intersection in object space (use 0.0
        to disable)'''
        return float()
    @property
    def displace_factor(self):
        '''(Float) Strength of displace when applied to the mesh'''
        return float()
    @property
    def image_fileformat(self):
        '''(Enum)
        
        [PNG, OPENEXR]'''
        return str()
    @property
    def displace_type(self):
        '''(Enum)
        
        [DISPLACE, DEPTH]'''
        return str()
    @property
    def use_incremental_displace(self):
        '''(Boolean) New displace is added cumulatively on top of existing'''
        return bool()
    @property
    def wave_damping(self):
        '''(Float) Wave damping factor'''
        return float()
    @property
    def wave_speed(self):
        '''(Float) Wave propagation speed'''
        return float()
    @property
    def wave_timescale(self):
        '''(Float) Wave time scaling factor'''
        return float()
    @property
    def wave_spring(self):
        '''(Float) Spring force that pulls water level back to zero'''
        return float()
    @property
    def wave_smoothness(self):
        '''(Float) Limit maximum steepness of wave slope between simulation
        points (use higher values for smoother waves at expense of reduced
        detail)'''
        return float()
    @property
    def use_wave_open_border(self):
        '''(Boolean) Pass waves through mesh edges'''
        return bool()
    @property
    def point_cache(self):
        '''(PointCache)'''
        return PointCache()
    @property
    def is_cache_user(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_color_preview(self):
        '''(Boolean) Whether this surface has some color preview for 3D view'''
        return bool()
    def output_exists(self, object, index):
        '''Checks if surface output layer of given name exists
        
        Parameter:
          object: (Object)
          index: (Integer)
        
        Returns:
          exists: (Boolean)'''
        return bool()