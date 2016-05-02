from . struct import Struct
from . list_library_item import List_Library_Item
from . bpy_struct import bpy_struct
import mathutils

class List_Library(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def index(self):
        '''(Integer)'''
        return int()
    @property
    def items(self):
        '''(Sequence of List_Library_Item)'''
        return (List_Library_Item(),)
    @property
    def module_name(self):
        '''(String)'''
        return str()