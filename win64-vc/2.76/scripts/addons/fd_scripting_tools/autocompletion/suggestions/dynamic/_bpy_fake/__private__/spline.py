from . splinepoints import SplinePoints
from . splinebezierpoints import SplineBezierPoints
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Spline(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def points(self):
        '''(Sequence of SplinePoint) Collection of points that make up this poly
        or nurbs spline'''
        return SplinePoints()
    @property
    def bezier_points(self):
        '''(Sequence of BezierSplinePoint) Collection of points for Bezier curves
        only'''
        return SplineBezierPoints()
    @property
    def tilt_interpolation(self):
        '''(Enum) The type of tilt interpolation for 3D, Bezier curves
        
        [LINEAR, CARDINAL, BSPLINE, EASE]'''
        return str()
    @property
    def radius_interpolation(self):
        '''(Enum) The type of radius interpolation for Bezier curves
        
        [LINEAR, CARDINAL, BSPLINE, EASE]'''
        return str()
    @property
    def type(self):
        '''(Enum) The interpolation type for this curve element
        
        [POLY, BEZIER, BSPLINE, CARDINAL, NURBS]'''
        return str()
    @property
    def point_count_u(self):
        '''(Integer) Total number points for the curve or surface in the U
        direction'''
        return int()
    @property
    def point_count_v(self):
        '''(Integer) Total number points for the surface on the V direction'''
        return int()
    @property
    def order_u(self):
        '''(Integer) NURBS order in the U direction (for splines and surfaces,
        higher values let points influence a greater area)'''
        return int()
    @property
    def order_v(self):
        '''(Integer) NURBS order in the V direction (for surfaces only, higher
        values let points influence a greater area)'''
        return int()
    @property
    def resolution_u(self):
        '''(Integer) Curve or Surface subdivisions per segment'''
        return int()
    @property
    def resolution_v(self):
        '''(Integer) Surface subdivisions per segment'''
        return int()
    @property
    def use_cyclic_u(self):
        '''(Boolean) Make this curve or surface a closed loop in the U direction'''
        return bool()
    @property
    def use_cyclic_v(self):
        '''(Boolean) Make this surface a closed loop in the V direction'''
        return bool()
    @property
    def use_endpoint_u(self):
        '''(Boolean) Make this nurbs curve or surface meet the endpoints in the U
        direction (Cyclic U must be disabled)'''
        return bool()
    @property
    def use_endpoint_v(self):
        '''(Boolean) Make this nurbs surface meet the endpoints in the V
        direction (Cyclic V must be disabled)'''
        return bool()
    @property
    def use_bezier_u(self):
        '''(Boolean) Make this nurbs curve or surface act like a Bezier spline in
        the U direction (Order U must be 3 or 4, Cyclic U must be disabled)'''
        return bool()
    @property
    def use_bezier_v(self):
        '''(Boolean) Make this nurbs surface act like a Bezier spline in the V
        direction (Order V must be 3 or 4, Cyclic V must be disabled)'''
        return bool()
    @property
    def use_smooth(self):
        '''(Boolean) Smooth the normals of the surface or beveled curve'''
        return bool()
    @property
    def hide(self):
        '''(Boolean) Hide this curve in Edit mode'''
        return bool()
    @property
    def material_index(self):
        '''(Integer)'''
        return int()
    @property
    def character_index(self):
        '''(Integer) Location of this character in the text data (only for text
        curves)'''
        return int()