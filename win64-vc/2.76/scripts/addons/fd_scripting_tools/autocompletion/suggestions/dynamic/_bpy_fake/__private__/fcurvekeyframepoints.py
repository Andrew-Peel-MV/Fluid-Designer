from . struct import Struct
from . keyframe import Keyframe
from . bpy_struct import bpy_struct
import mathutils

class FCurveKeyframePoints(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def insert(self, frame, value, options):
        '''Add a keyframe point to a F-Curve
        
        Parameter:
          frame: (Float) X Value of this keyframe point
          value: (Float) Y Value of this keyframe point
          options: (Enum) Keyframe options
        
        Returns:
          keyframe: (Keyframe) Newly created keyframe'''
        return Keyframe()
    def add(self, count):
        '''Add a keyframe point to a F-Curve
        
        Parameter:
          count: (Integer) Number of points to add to the spline'''
        return 
    def remove(self, keyframe, fast):
        '''Remove keyframe from an F-Curve
        
        Parameter:
          keyframe: (Keyframe) Keyframe to remove
          fast:
            (Boolean) Fast keyframe removal to avoid recalculating the curve each
            time'''
        return 
    def get(key): return Keyframe()
    def __getitem__(key): return Keyframe()
    def __iter__(key): yield Keyframe()