from . struct import Struct
from . colorrampelements import ColorRampElements
from . bpy_struct import bpy_struct
import mathutils

class ColorRamp(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def elements(self):
        '''(Sequence of ColorRampElement)'''
        return ColorRampElements()
    @property
    def interpolation(self):
        '''(Enum) Set interpolation between color stops
        
        [EASE, CARDINAL, LINEAR, B_SPLINE, CONSTANT]'''
        return str()
    @property
    def hue_interpolation(self):
        '''(Enum) Set color interpolation
        
        [NEAR, FAR, CW, CCW]'''
        return str()
    @property
    def color_mode(self):
        '''(Enum) Set color mode to use for interpolation
        
        [RGB, HSV, HSL]'''
        return str()
    def evaluate(self, position):
        '''Evaluate ColorRamp
        
        Parameter:
          position: (Float) Evaluate ColorRamp at position
        
        Returns:
          color: (Float[4]) Color at given position'''
        return ''