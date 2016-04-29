from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ThemeWidgetStateColors(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def inner_anim(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def inner_anim_sel(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def inner_key(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def inner_key_sel(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def inner_driven(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def inner_driven_sel(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def blend(self):
        '''(Float)'''
        return float()