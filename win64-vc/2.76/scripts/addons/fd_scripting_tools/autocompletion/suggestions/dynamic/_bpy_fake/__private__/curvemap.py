from . struct import Struct
from . curvemappoints import CurveMapPoints
from . bpy_struct import bpy_struct
import mathutils

class CurveMap(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def extend(self):
        '''(Enum) Extrapolate the curve or extend it horizontally
        
        [HORIZONTAL, EXTRAPOLATED]'''
        return str()
    @property
    def points(self):
        '''(Sequence of CurveMapPoint)'''
        return CurveMapPoints()
    def evaluate(self, position):
        '''Evaluate curve at given location
        
        Parameter:
          position: (Float) Position to evaluate curve at
        
        Returns:
          value: (Float) Value of curve at given location'''
        return float()