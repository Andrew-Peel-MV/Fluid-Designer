from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshColor(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def color1(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def color2(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def color3(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def color4(self):
        '''(Vector 3D)'''
        return mathutils.Vector()