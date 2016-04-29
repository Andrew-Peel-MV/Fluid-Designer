from . curvemappoint import CurveMapPoint
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CurveMapPoints(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, position, value):
        '''Add point to CurveMap
        
        Parameter:
          position: (Float) Position to add point
          value: (Float) Value of point
        
        Returns:
          point: (CurveMapPoint) New point'''
        return CurveMapPoint()
    def remove(self, point):
        '''Delete point from CurveMap
        
        Parameter:
          point: (CurveMapPoint) PointElement to remove'''
        return 
    def get(key): return CurveMapPoint()
    def __getitem__(key): return CurveMapPoint()
    def __iter__(key): yield CurveMapPoint()