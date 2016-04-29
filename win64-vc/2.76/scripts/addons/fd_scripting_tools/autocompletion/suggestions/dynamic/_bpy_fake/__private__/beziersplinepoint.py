from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BezierSplinePoint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def select_left_handle(self):
        '''(Boolean) Handle 1 selection status'''
        return bool()
    @property
    def select_right_handle(self):
        '''(Boolean) Handle 2 selection status'''
        return bool()
    @property
    def select_control_point(self):
        '''(Boolean) Control point selection status'''
        return bool()
    @property
    def hide(self):
        '''(Boolean) Visibility status'''
        return bool()
    @property
    def handle_left_type(self):
        '''(Enum) Handle types
        
        [FREE, VECTOR, ALIGNED, AUTO]'''
        return str()
    @property
    def handle_right_type(self):
        '''(Enum) Handle types
        
        [FREE, VECTOR, ALIGNED, AUTO]'''
        return str()
    @property
    def handle_left(self):
        '''(Vector 3D) Coordinates of the first handle'''
        return mathutils.Vector()
    @property
    def co(self):
        '''(Vector 3D) Coordinates of the control point'''
        return mathutils.Vector()
    @property
    def handle_right(self):
        '''(Vector 3D) Coordinates of the second handle'''
        return mathutils.Vector()
    @property
    def tilt(self):
        '''(Float) Tilt in 3D View'''
        return float()
    @property
    def weight_softbody(self):
        '''(Float) Softbody goal weight'''
        return float()
    @property
    def radius(self):
        '''(Float) Radius for beveling'''
        return float()