from . brush import Brush
from . curvemapping import CurveMapping
from . struct import Struct
from . palette import Palette
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class Sculpt(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def brush(self):
        '''(Brush) Active Brush'''
        return Brush()
    @property
    def palette(self):
        '''(Palette) Active Palette'''
        return Palette()
    @property
    def show_brush(self):
        '''(Boolean)'''
        return bool()
    @property
    def show_brush_on_surface(self):
        '''(Boolean)'''
        return bool()
    @property
    def show_low_resolution(self):
        '''(Boolean) For multires, show low resolution while navigating the view'''
        return bool()
    @property
    def input_samples(self):
        '''(Integer) Average multiple input samples together to smooth the brush
        stroke'''
        return int()
    @property
    def use_symmetry_x(self):
        '''(Boolean) Mirror brush across the X axis'''
        return bool()
    @property
    def use_symmetry_y(self):
        '''(Boolean) Mirror brush across the Y axis'''
        return bool()
    @property
    def use_symmetry_z(self):
        '''(Boolean) Mirror brush across the Z axis'''
        return bool()
    @property
    def use_symmetry_feather(self):
        '''(Boolean) Reduce the strength of the brush where it overlaps
        symmetrical daubs'''
        return bool()
    @property
    def cavity_curve(self):
        '''(CurveMapping) Editable cavity curve'''
        return CurveMapping()
    @property
    def use_cavity(self):
        '''(Boolean) Mask painting according to mesh geometry cavity'''
        return bool()
    @property
    def tile_offset(self):
        '''(Vector 3D) Stride at which tiled strokes are copied'''
        return mathutils.Vector()
    @property
    def tile_x(self):
        '''(Boolean) Tile along X axis'''
        return bool()
    @property
    def tile_y(self):
        '''(Boolean) Tile along Y axis'''
        return bool()
    @property
    def tile_z(self):
        '''(Boolean) Tile along Z axis'''
        return bool()
    @property
    def radial_symmetry(self):
        '''(Integer[3]) Number of times to copy strokes across the surface'''
        return int()
    @property
    def lock_x(self):
        '''(Boolean) Disallow changes to the X axis of vertices'''
        return bool()
    @property
    def lock_y(self):
        '''(Boolean) Disallow changes to the Y axis of vertices'''
        return bool()
    @property
    def lock_z(self):
        '''(Boolean) Disallow changes to the Z axis of vertices'''
        return bool()
    @property
    def use_threaded(self):
        '''(Boolean) Take advantage of multiple CPU cores to improve sculpting
        performance'''
        return bool()
    @property
    def use_deform_only(self):
        '''(Boolean) Use only deformation modifiers (temporary disable all
        constructive modifiers except multi-resolution)'''
        return bool()
    @property
    def show_diffuse_color(self):
        '''(Boolean) Show diffuse color of object and overlay sculpt mask on top
        of it'''
        return bool()
    @property
    def detail_size(self):
        '''(Float) Maximum edge length for dynamic topology sculpting (in pixels)'''
        return float()
    @property
    def detail_percent(self):
        '''(Float) Maximum edge length for dynamic topology sculpting (in brush
        percenage)'''
        return float()
    @property
    def constant_detail(self):
        '''(Float) Maximum edge length for dynamic topology sculpting (as
        percentage of blender unit)'''
        return float()
    @property
    def use_smooth_shading(self):
        '''(Boolean) Show faces in dynamic-topology mode with smooth shading
        rather than flat shaded'''
        return bool()
    @property
    def symmetrize_direction(self):
        '''(Enum) Source and destination for symmetrize operator
        
        [NEGATIVE_X, POSITIVE_X, NEGATIVE_Y, POSITIVE_Y, NEGATIVE_Z,
        POSITIVE_Z]'''
        return str()
    @property
    def detail_refine_method(self):
        '''(Enum) In dynamic-topology mode, how to add or remove mesh detail
        
        [SUBDIVIDE, COLLAPSE, SUBDIVIDE_COLLAPSE]'''
        return str()
    @property
    def detail_type_method(self):
        '''(Enum) In dynamic-topology mode, how mesh detail size is calculated
        
        [RELATIVE, CONSTANT, BRUSH]'''
        return str()
    @property
    def gravity(self):
        '''(Float) Amount of gravity after each dab'''
        return float()
    @property
    def gravity_object(self):
        '''(Object) Object whose Z axis defines orientation of gravity'''
        return Object()