from . struct import Struct
from . library_items import library_items
from . bpy_struct import bpy_struct
import mathutils

class blend_file(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def items(self):
        '''(Sequence of library_items)'''
        return (library_items(),)
    @property
    def show_expanded(self):
        '''(Boolean)'''
        return bool()
    @property
    def is_selected(self):
        '''(Boolean)'''
        return bool()