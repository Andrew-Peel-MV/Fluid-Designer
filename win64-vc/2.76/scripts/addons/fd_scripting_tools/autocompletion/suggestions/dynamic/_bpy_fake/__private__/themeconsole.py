from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeConsole(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()
    @property
    def line_output(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def line_input(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def line_info(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def line_error(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def cursor(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def select(self):
        '''(Float[4])'''
        return ''