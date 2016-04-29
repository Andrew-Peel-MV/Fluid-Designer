from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ColorRampElement(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def color(self):
        '''(Float[4]) Set color of selected color stop'''
        return ''
    @property
    def alpha(self):
        '''(Float) Set alpha of selected color stop'''
        return float()
    @property
    def position(self):
        '''(Float) Set position of selected color stop'''
        return float()