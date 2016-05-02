from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeInfo(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()
    @property
    def info_selected(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_selected_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_error(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_error_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_warning(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_warning_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_info(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_info_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_debug(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def info_debug_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()