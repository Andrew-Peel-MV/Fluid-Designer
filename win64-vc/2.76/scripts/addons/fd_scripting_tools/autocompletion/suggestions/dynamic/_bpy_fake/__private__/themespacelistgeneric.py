from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ThemeSpaceListGeneric(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def list(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def list_title(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def list_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def list_text_hi(self):
        '''(Vector 3D)'''
        return mathutils.Vector()