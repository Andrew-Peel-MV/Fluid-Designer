from . masksplinepoint import MaskSplinePoint
from . struct import Struct
from . maskspline import MaskSpline
from . bpy_struct import bpy_struct
import mathutils

class MaskSplines(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MaskSpline) Active spline of masking layer'''
        return MaskSpline()
    @property
    def active_point(self):
        '''(MaskSplinePoint) Active spline of masking layer'''
        return MaskSplinePoint()
    def new(self):
        '''Add a new spline to the layer
        
        Returns:
          spline: (MaskSpline) The newly created spline'''
        return MaskSpline()
    def remove(self, spline):
        '''Remove a spline from a layer
        
        Parameter:
          spline: (MaskSpline) The spline to remove'''
        return 
    def get(key): return MaskSpline()
    def __getitem__(key): return MaskSpline()
    def __iter__(key): yield MaskSpline()