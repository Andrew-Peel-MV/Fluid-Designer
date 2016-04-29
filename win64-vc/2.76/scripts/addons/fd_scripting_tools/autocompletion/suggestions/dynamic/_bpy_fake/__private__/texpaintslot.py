from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class TexPaintSlot(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def uv_layer(self):
        '''(String) Name of UV map'''
        return str()
    @property
    def index(self):
        '''(Integer) Index of MTex slot in the material'''
        return int()