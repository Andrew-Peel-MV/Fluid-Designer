from . curvemapping import CurveMapping
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ColorManagedViewSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def look(self):
        '''(Enum) Additional transform applied before view transform for an
        artistic needs
        
        [NONE]'''
        return str()
    @property
    def view_transform(self):
        '''(Enum) View used when converting image to a display space
        
        [NONE]'''
        return str()
    @property
    def exposure(self):
        '''(Float) Exposure (stops) applied before display transform'''
        return float()
    @property
    def gamma(self):
        '''(Float) Amount of gamma modification applied after display transform'''
        return float()
    @property
    def curve_mapping(self):
        '''(CurveMapping) Color curve mapping applied before display transform'''
        return CurveMapping()
    @property
    def use_curve_mapping(self):
        '''(Boolean) Use RGB curved for pre-display transformation'''
        return bool()