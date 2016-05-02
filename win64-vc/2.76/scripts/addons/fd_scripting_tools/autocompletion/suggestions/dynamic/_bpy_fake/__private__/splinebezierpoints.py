from . struct import Struct
from . beziersplinepoint import BezierSplinePoint
from . bpy_struct import bpy_struct
import mathutils

class SplineBezierPoints(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self, count):
        '''Add a number of points to this spline
        
        Parameter:
          count: (Integer) Number of points to add to the spline'''
        return 
    def get(key): return BezierSplinePoint()
    def __getitem__(key): return BezierSplinePoint()
    def __iter__(key): yield BezierSplinePoint()