from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ThemePanelColors(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def header(self):
        '''(Float[4])'''
        return ''
    @property
    def back(self):
        '''(Float[4])'''
        return ''
    @property
    def show_header(self):
        '''(Boolean)'''
        return bool()
    @property
    def show_back(self):
        '''(Boolean)'''
        return bool()