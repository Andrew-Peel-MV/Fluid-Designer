from . meshskinvertex import MeshSkinVertex
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshSkinVertexLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Name of skin layer'''
        return str()
    @property
    def data(self):
        '''(Sequence of MeshSkinVertex)'''
        return (MeshSkinVertex(),)