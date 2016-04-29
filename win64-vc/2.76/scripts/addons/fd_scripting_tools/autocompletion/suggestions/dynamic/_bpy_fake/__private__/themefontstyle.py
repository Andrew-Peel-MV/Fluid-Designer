from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ThemeFontStyle(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def points(self):
        '''(Integer)'''
        return int()
    @property
    def font_kerning_style(self):
        '''(Enum) Which style to use for font kerning
        
        [UNFITTED, FITTED]'''
        return str()
    @property
    def shadow(self):
        '''(Integer) Shadow size (0, 3 and 5 supported)'''
        return int()
    @property
    def shadow_offset_x(self):
        '''(Integer) Shadow offset in pixels'''
        return int()
    @property
    def shadow_offset_y(self):
        '''(Integer) Shadow offset in pixels'''
        return int()
    @property
    def shadow_alpha(self):
        '''(Float)'''
        return float()
    @property
    def shadow_value(self):
        '''(Float) Shadow color in gray value'''
        return float()