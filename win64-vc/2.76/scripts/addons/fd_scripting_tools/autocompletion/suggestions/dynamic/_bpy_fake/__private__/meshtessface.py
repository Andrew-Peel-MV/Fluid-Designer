from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshTessFace(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def vertices(self):
        '''(Integer[4]) Vertex indices'''
        return int()
    @property
    def vertices_raw(self):
        '''(Integer[4]) Fixed size vertex indices array'''
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
    def normal(self):
        '''(Vector 3D) Local space unit length normal vector for this face'''
        return mathutils.Vector()
    @property
    def split_normals(self):
        '''(Float[12]) Local space unit length split normals vectors of the
        vertices of this face (must be computed beforehand using
        calc_normals_split or calc_tangents, and then calc_tessface)'''
        return ''
    @property
    def area(self):
        '''(Float) Read only area of this face'''
        return float()
    @property
    def index(self):
        '''(Integer) Index of this face'''
        return int()