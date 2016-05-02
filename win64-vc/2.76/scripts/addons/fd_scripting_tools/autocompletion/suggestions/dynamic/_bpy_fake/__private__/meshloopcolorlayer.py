from . struct import Struct
from . meshloopcolor import MeshLoopColor
from . bpy_struct import bpy_struct
import mathutils

class MeshLoopColorLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Name of Vertex color layer'''
        return str()
    @property
    def active(self):
        '''(Boolean) Sets the layer as active for display and editing'''
        return bool()
    @property
    def active_render(self):
        '''(Boolean) Sets the layer as active for rendering'''
        return bool()
    @property
    def data(self):
        '''(Sequence of MeshLoopColor)'''
        return (MeshLoopColor(),)