from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Library_Pointer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [NONE, WIDTH, LENGTH]'''
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
    def pointer_value(self):
        '''(Float)'''
        return float()
    @property
    def assign_material(self):
        '''(Boolean)'''
        return bool()
    @property
    def item_name(self):
        '''(String)'''
        return str()