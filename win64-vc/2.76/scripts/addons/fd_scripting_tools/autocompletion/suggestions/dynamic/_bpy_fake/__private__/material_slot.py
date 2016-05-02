from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Material_Slot(bpy_struct):
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
    def library_name(self):
        '''(String)'''
        return str()
    @property
    def category_name(self):
        '''(String)'''
        return str()
    @property
    def pointer_name(self):
        '''(String)'''
        return str()
    @property
    def item_name(self):
        '''(String)'''
        return str()