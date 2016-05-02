from . themespacelistgeneric import ThemeSpaceListGeneric
from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeFileBrowser(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()
    @property
    def space_list(self):
        '''(ThemeSpaceListGeneric) Settings for space list'''
        return ThemeSpaceListGeneric()
    @property
    def selected_file(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def scrollbar(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def scroll_handle(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def active_file(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def active_file_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()