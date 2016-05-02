from . sheet_size import Sheet_Size
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Sheet_Stock(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def bottom_material(self):
        '''(String)'''
        return str()
    @property
    def sizes(self):
        '''(Sequence of Sheet_Size)'''
        return (Sheet_Size(),)
    @property
    def core_material(self):
        '''(String)'''
        return str()
    @property
    def size_index(self):
        '''(Integer)'''
        return int()
    @property
    def top_material(self):
        '''(String)'''
        return str()
    @property
    def thickness(self):
        '''(Float)'''
        return float()
    @property
    def grain(self):
        '''(Enum)
        
        [NONE, WIDTH, LENGTH]'''
        return str()