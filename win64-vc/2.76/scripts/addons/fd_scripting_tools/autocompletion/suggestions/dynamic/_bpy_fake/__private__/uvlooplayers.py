from . struct import Struct
from . meshuvlooplayer import MeshUVLoopLayer
from . bpy_struct import bpy_struct
import mathutils

class UVLoopLayers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MeshUVLoopLayer) Active UV loop layer'''
        return MeshUVLoopLayer()
    @property
    def active_index(self):
        '''(Integer) Active UV loop layer index'''
        return int()
    def get(key): return MeshUVLoopLayer()
    def __getitem__(key): return MeshUVLoopLayer()
    def __iter__(key): yield MeshUVLoopLayer()