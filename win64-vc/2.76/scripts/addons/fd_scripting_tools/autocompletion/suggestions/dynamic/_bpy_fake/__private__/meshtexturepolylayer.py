from . struct import Struct
from . meshtexturepoly import MeshTexturePoly
from . bpy_struct import bpy_struct
import mathutils

class MeshTexturePolyLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Name of UV map'''
        return str()
    @property
    def active(self):
        '''(Boolean) Set the map as active for display and editing'''
        return bool()
    @property
    def active_render(self):
        '''(Boolean) Set the map as active for rendering'''
        return bool()
    @property
    def active_clone(self):
        '''(Boolean) Set the map as active for cloning'''
        return bool()
    @property
    def data(self):
        '''(Sequence of MeshTexturePoly)'''
        return (MeshTexturePoly(),)