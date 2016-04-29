from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshPolygon(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def vertices(self):
        '''(Integer[3]) Vertex indices'''
        return int()
    @property
    def loop_start(self):
        '''(Integer) Index of the first loop of this polygon'''
        return int()
    @property
    def loop_total(self):
        '''(Integer) Number of loops used by this polygon'''
        return int()
    @property
    def material_index(self):
        '''(Integer)'''
        return int()
    @property
    def select(self):
        '''(Boolean)'''
        return bool()
    @property
    def hide(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_smooth(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_freestyle_mark(self):
        '''(Boolean) Face mark for Freestyle line rendering'''
        return bool()
    @property
    def normal(self):
        '''(Vector 3D) Local space unit length normal vector for this polygon'''
        return mathutils.Vector()
    @property
    def center(self):
        '''(Vector 3D) Center of this polygon'''
        return mathutils.Vector()
    @property
    def area(self):
        '''(Float) Read only area of this polygon'''
        return float()
    @property
    def index(self):
        '''(Integer) Index of this polygon'''
        return int()