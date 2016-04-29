from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshLoop(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def vertex_index(self):
        '''(Integer) Vertex index'''
        return int()
    @property
    def edge_index(self):
        '''(Integer) Edge index'''
        return int()
    @property
    def index(self):
        '''(Integer) Index of this loop'''
        return int()
    @property
    def normal(self):
        '''(Vector 3D) Local space unit length split normal vector of this vertex
        for this polygon (must be computed beforehand using calc_normals_split
        or calc_tangents)'''
        return mathutils.Vector()
    @property
    def tangent(self):
        '''(Vector 3D) Local space unit length tangent vector of this vertex for
        this polygon (must be computed beforehand using calc_tangents)'''
        return mathutils.Vector()
    @property
    def bitangent_sign(self):
        '''(Float) Sign of the bitangent vector of this vertex for this polygon
        (must be computed beforehand using calc_tangents, bitangent =
        bitangent_sign * cross(normal, tangent))'''
        return float()
    @property
    def bitangent(self):
        '''(Vector 3D) Bitangent vector of this vertex for this polygon (must be
        computed beforehand using calc_tangents, *use it only if really
        needed*, slower access than bitangent_sign)'''
        return mathutils.Vector()