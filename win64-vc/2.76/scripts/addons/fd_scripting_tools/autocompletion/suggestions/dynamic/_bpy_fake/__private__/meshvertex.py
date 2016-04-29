from . vertexgroupelement import VertexGroupElement
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshVertex(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def co(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def normal(self):
        '''(Vector 3D) Vertex Normal'''
        return mathutils.Vector()
    @property
    def select(self):
        '''(Boolean)'''
        return bool()
    @property
    def hide(self):
        '''(Boolean)'''
        return bool()
    @property
    def bevel_weight(self):
        '''(Float) Weight used by the Bevel modifier 'Only Vertices' option'''
        return float()
    @property
    def groups(self):
        '''(Sequence of VertexGroupElement) Weights for the vertex groups this
        vertex is member of'''
        return (VertexGroupElement(),)
    @property
    def index(self):
        '''(Integer) Index of this vertex'''
        return int()
    @property
    def undeformed_co(self):
        '''(Vector 3D) For meshes with modifiers applied, the coordinate of the
        vertex with no deforming modifiers applied, as used for generated
        texture coordinates'''
        return mathutils.Vector()