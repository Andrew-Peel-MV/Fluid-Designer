from . masksplinepoints import MaskSplinePoints
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaskSpline(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def offset_mode(self):
        '''(Enum) The method used for calculating the feather offset
        
        [EVEN, SMOOTH]'''
        return str()
    @property
    def weight_interpolation(self):
        '''(Enum) The type of weight interpolation for spline
        
        [LINEAR, EASE]'''
        return str()
    @property
    def use_cyclic(self):
        '''(Boolean) Make this spline a closed loop'''
        return bool()
    @property
    def use_fill(self):
        '''(Boolean) Make this spline filled'''
        return bool()
    @property
    def use_self_intersection_check(self):
        '''(Boolean) Prevent feather from self-intersections'''
        return bool()
    @property
    def points(self):
        '''(Sequence of MaskSplinePoint) Collection of points'''
        return MaskSplinePoints()