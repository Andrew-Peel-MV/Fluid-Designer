from . brush import Brush
from . curvemapping import CurveMapping
from . struct import Struct
from . palette import Palette
from . bpy_struct import bpy_struct
import mathutils

class UvSculpt(bpy_struct):
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