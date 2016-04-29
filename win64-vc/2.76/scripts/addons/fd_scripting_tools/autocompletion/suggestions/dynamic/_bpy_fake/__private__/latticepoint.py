from . vertexgroupelement import VertexGroupElement
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class LatticePoint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def select(self):
        '''(Boolean) Selection status'''
        return bool()
    @property
    def co(self):
        '''(Vector 3D) Original undeformed location used to calculate the
        strength of the deform effect (edit/animate the Deformed Location
        instead)'''
        return mathutils.Vector()
    @property
    def co_deform(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def weight_softbody(self):
        '''(Float) Softbody goal weight'''
        return float()
    @property
    def groups(self):
        '''(Sequence of VertexGroupElement) Weights for the vertex groups this
        point is member of'''
        return (VertexGroupElement(),)