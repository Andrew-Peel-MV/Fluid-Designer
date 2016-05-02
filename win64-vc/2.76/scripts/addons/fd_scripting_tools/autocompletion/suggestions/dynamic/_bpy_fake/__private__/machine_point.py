from . machine_token import Machine_Token
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Machine_Point(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def machine_tokens(self):
        '''(Sequence of Machine_Token) Collection of machine tokens'''
        return (Machine_Token(),)
    @property
    def machine_token_index(self):
        '''(Integer)'''
        return int()