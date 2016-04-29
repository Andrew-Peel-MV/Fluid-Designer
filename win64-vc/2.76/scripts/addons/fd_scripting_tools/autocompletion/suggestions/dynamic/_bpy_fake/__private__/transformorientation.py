from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class TransformOrientation(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def matrix(self):
        '''(Float[9])'''
        return ''
    @property
    def name(self):
        '''(String) Name of the custom transform orientation'''
        return str()