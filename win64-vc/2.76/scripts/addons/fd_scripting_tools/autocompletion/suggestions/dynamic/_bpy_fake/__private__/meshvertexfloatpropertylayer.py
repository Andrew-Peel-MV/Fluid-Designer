from . struct import Struct
from . meshvertexfloatproperty import MeshVertexFloatProperty
from . bpy_struct import bpy_struct
import mathutils

class MeshVertexFloatPropertyLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def data(self):
        '''(Sequence of MeshVertexFloatProperty)'''
        return (MeshVertexFloatProperty(),)