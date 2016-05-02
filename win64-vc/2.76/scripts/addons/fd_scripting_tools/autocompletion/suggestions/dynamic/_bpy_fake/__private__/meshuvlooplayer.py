from . struct import Struct
from . meshuvloop import MeshUVLoop
from . bpy_struct import bpy_struct
import mathutils

class MeshUVLoopLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def data(self):
        '''(Sequence of MeshUVLoop)'''
        return (MeshUVLoop(),)
    @property
    def name(self):
        '''(String) Name of UV map'''
        return str()