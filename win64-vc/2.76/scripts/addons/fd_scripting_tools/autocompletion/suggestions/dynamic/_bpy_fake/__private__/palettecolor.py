from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PaletteColor(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def color(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def strength(self):
        '''(Float)'''
        return float()
    @property
    def weight(self):
        '''(Float)'''
        return float()