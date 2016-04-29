from . masksplinepoint import MaskSplinePoint
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaskSplinePoints(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self, count):
        '''Add a number of point to this spline
        
        Parameter:
          count: (Integer) Number of points to add to the spline'''
        return 
    def remove(self, point):
        '''Remove a point from a spline
        
        Parameter:
          point: (MaskSplinePoint) The point to remove'''
        return 
    def get(key): return MaskSplinePoint()
    def __getitem__(key): return MaskSplinePoint()
    def __iter__(key): yield MaskSplinePoint()