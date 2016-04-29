from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CurveMapPoint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def location(self):
        '''(Vector 2D) X/Y coordinates of the curve point'''
        return mathutils.Vector()
    @property
    def handle_type(self):
        '''(Enum) Curve interpolation at this point: Bezier or vector
        
        [AUTO, VECTOR]'''
        return str()
    @property
    def select(self):
        '''(Boolean) Selection state of the curve point'''
        return bool()