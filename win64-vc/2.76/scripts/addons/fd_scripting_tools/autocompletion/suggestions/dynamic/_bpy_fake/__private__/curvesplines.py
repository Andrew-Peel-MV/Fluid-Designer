from . spline import Spline
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CurveSplines(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Spline) Active curve spline'''
        return Spline()
    def new(self, type):
        '''Add a new spline to the curve
        
        Parameter:
          type: (Enum) type for the new spline
        
        Returns:
          spline: (Spline) The newly created spline'''
        return Spline()
    def remove(self, spline):
        '''Remove a spline from a curve
        
        Parameter:
          spline: (Spline) The spline to remove'''
        return 
    def clear(self):
        '''Remove all splines from a curve'''
        return 
    def get(key): return Spline()
    def __getitem__(key): return Spline()
    def __iter__(key): yield Spline()