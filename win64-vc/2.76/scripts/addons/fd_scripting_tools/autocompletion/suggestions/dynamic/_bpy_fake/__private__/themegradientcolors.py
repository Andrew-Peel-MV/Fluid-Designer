from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ThemeGradientColors(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def show_grad(self):
        '''(Boolean) Do a gradient for the background of the viewport working
        area'''
        return bool()
    @property
    def gradient(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def high_gradient(self):
        '''(Vector 3D)'''
        return mathutils.Vector()