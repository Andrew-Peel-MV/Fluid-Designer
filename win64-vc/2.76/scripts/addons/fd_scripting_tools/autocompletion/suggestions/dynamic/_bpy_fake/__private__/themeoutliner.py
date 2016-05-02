from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeOutliner(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()
    @property
    def match(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def selected_highlight(self):
        '''(Vector 3D)'''
        return mathutils.Vector()