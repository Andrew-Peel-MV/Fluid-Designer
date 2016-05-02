from . struct import Struct
from . splinepoint import SplinePoint
from . bpy_struct import bpy_struct
import mathutils

class SplinePoints(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self, count):
        '''Add a number of points to this spline
        
        Parameter:
          count: (Integer) Number of points to add to the spline'''
        return 
    def get(key): return SplinePoint()
    def __getitem__(key): return SplinePoint()
    def __iter__(key): yield SplinePoint()