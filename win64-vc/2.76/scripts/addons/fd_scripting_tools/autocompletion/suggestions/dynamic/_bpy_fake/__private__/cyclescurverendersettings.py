from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesCurveRenderSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def primitive(self):
        '''(Enum) Type of primitive used for hair rendering
        
        [TRIANGLES, LINE_SEGMENTS, CURVE_SEGMENTS]'''
        return str()
    @property
    def shape(self):
        '''(Enum) Form of hair
        
        [RIBBONS, THICK]'''
        return str()
    @property
    def cull_backfacing(self):
        '''(Boolean) Do not test the back-face of each strand'''
        return bool()
    @property
    def use_curves(self):
        '''(Boolean) Activate Cycles hair rendering for particle system'''
        return bool()
    @property
    def resolution(self):
        '''(Integer) Resolution of generated mesh'''
        return int()
    @property
    def minimum_width(self):
        '''(Float) Minimal pixel width for strands (0 - deactivated)'''
        return float()
    @property
    def maximum_width(self):
        '''(Float) Maximum extension that strand radius can be increased by'''
        return float()
    @property
    def subdivisions(self):
        '''(Integer) Number of subdivisions used in Cardinal curve intersection
        (power of 2)'''
        return int()