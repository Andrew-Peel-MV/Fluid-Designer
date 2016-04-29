from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshStatVis(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Type of data to visualize/check
        
        [OVERHANG, THICKNESS, INTERSECT, DISTORT, SHARP]'''
        return str()
    @property
    def overhang_min(self):
        '''(Float) Minimum angle to display'''
        return float()
    @property
    def overhang_max(self):
        '''(Float) Maximum angle to display'''
        return float()
    @property
    def overhang_axis(self):
        '''(Enum)
        
        [POS_X, POS_Y, POS_Z, NEG_X, NEG_Y, NEG_Z]'''
        return str()
    @property
    def thickness_min(self):
        '''(Float) Minimum for measuring thickness'''
        return float()
    @property
    def thickness_max(self):
        '''(Float) Maximum for measuring thickness'''
        return float()
    @property
    def thickness_samples(self):
        '''(Integer) Number of samples to test per face'''
        return int()
    @property
    def distort_min(self):
        '''(Float) Minimum angle to display'''
        return float()
    @property
    def distort_max(self):
        '''(Float) Maximum angle to display'''
        return float()
    @property
    def sharp_min(self):
        '''(Float) Minimum angle to display'''
        return float()
    @property
    def sharp_max(self):
        '''(Float) Maximum angle to display'''
        return float()