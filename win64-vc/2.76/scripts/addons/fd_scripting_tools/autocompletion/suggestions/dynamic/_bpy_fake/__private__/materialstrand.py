from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialStrand(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_tangent_shading(self):
        '''(Boolean) Use direction of strands as normal for tangent-shading'''
        return bool()
    @property
    def use_surface_diffuse(self):
        '''(Boolean) Make diffuse shading more similar to shading the surface'''
        return bool()
    @property
    def blend_distance(self):
        '''(Float) Worldspace distance over which to blend in the surface normal'''
        return float()
    @property
    def use_blender_units(self):
        '''(Boolean) Use Blender units for widths instead of pixels'''
        return bool()
    @property
    def root_size(self):
        '''(Float) Start size of strands in pixels or Blender units'''
        return float()
    @property
    def tip_size(self):
        '''(Float) End size of strands in pixels or Blender units'''
        return float()
    @property
    def size_min(self):
        '''(Float) Minimum size of strands in pixels'''
        return float()
    @property
    def shape(self):
        '''(Float) Positive values make strands rounder, negative ones make
        strands spiky'''
        return float()
    @property
    def width_fade(self):
        '''(Float) Transparency along the width of the strand'''
        return float()
    @property
    def uv_layer(self):
        '''(String) Name of UV map to override'''
        return str()