from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ThemeBoneColorSet(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def normal(self):
        '''(Vector 3D) Color used for the surface of bones'''
        return mathutils.Vector()
    @property
    def select(self):
        '''(Vector 3D) Color used for selected bones'''
        return mathutils.Vector()
    @property
    def active(self):
        '''(Vector 3D) Color used for active bones'''
        return mathutils.Vector()
    @property
    def show_colored_constraints(self):
        '''(Boolean) Allow the use of colors indicating constraints/keyed status'''
        return bool()