from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeTextEditor(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()
    @property
    def line_numbers_background(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def selected_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def cursor(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def syntax_builtin(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def syntax_symbols(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def syntax_special(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def syntax_preprocessor(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def syntax_reserved(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def syntax_comment(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def syntax_string(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def syntax_numbers(self):
        '''(Vector 3D)'''
        return mathutils.Vector()