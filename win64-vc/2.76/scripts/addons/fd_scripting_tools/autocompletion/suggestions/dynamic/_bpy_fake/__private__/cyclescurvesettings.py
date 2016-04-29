from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesCurveSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def radius_scale(self):
        '''(Float) Multiplier of width properties'''
        return float()
    @property
    def root_width(self):
        '''(Float) Strand's width at root'''
        return float()
    @property
    def tip_width(self):
        '''(Float) Strand's width at tip'''
        return float()
    @property
    def shape(self):
        '''(Float) Strand shape parameter'''
        return float()
    @property
    def use_closetip(self):
        '''(Boolean) Set tip radius to zero'''
        return bool()