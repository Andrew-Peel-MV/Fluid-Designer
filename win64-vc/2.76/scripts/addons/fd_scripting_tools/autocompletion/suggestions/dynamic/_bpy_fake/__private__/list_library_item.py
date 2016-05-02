from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class List_Library_Item(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def has_thumbnail(self):
        '''(Boolean)'''
        return bool()
    @property
    def library_name(self):
        '''(String)'''
        return str()
    @property
    def is_custom(self):
        '''(Boolean)'''
        return bool()
    @property
    def has_file(self):
        '''(Boolean)'''
        return bool()
    @property
    def category_name(self):
        '''(String)'''
        return str()
    @property
    def bp_name(self):
        '''(String)'''
        return str()
    @property
    def class_name(self):
        '''(String)'''
        return str()
    @property
    def selected(self):
        '''(Boolean)'''
        return bool()