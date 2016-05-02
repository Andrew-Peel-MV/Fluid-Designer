from . maskparent import MaskParent
from . struct import Struct
from . masksplinepointuw import MaskSplinePointUW
from . bpy_struct import bpy_struct
import mathutils

class MaskSplinePoint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def handle_left(self):
        '''(Vector 2D) Coordinates of the first handle'''
        return mathutils.Vector()
    @property
    def co(self):
        '''(Vector 2D) Coordinates of the control point'''
        return mathutils.Vector()
    @property
    def handle_right(self):
        '''(Vector 2D) Coordinates of the second handle'''
        return mathutils.Vector()
    @property
    def handle_type(self):
        '''(Enum) Handle type
        
        [AUTO, VECTOR, ALIGNED, ALIGNED_DOUBLESIDE, FREE]'''
        return str()
    @property
    def handle_left_type(self):
        '''(Enum) Handle type
        
        [AUTO, VECTOR, ALIGNED, ALIGNED_DOUBLESIDE, FREE]'''
        return str()
    @property
    def handle_right_type(self):
        '''(Enum) Handle type
        
        [AUTO, VECTOR, ALIGNED, ALIGNED_DOUBLESIDE, FREE]'''
        return str()
    @property
    def weight(self):
        '''(Float) Weight of the point'''
        return float()
    @property
    def select(self):
        '''(Boolean) Selection status'''
        return bool()
    @property
    def parent(self):
        '''(MaskParent)'''
        return MaskParent()
    @property
    def feather_points(self):
        '''(Sequence of MaskSplinePointUW) Points defining feather'''
        return (MaskSplinePointUW(),)