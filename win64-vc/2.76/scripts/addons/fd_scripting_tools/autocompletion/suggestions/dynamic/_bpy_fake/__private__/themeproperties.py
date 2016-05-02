from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeProperties(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()