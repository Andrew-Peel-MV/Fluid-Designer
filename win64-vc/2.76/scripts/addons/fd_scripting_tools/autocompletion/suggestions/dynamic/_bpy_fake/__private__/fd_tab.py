from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class fd_tab(bpy_struct):
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
        
        [VISIBLE, HIDDEN, CALCULATOR]'''
        return str()
    @property
    def index(self):
        '''(Integer)'''
        return int()
    @property
    def calculator_deduction(self):
        '''(Float)'''
        return float()
    @property
    def calculator_type(self):
        '''(Enum)
        
        [XDIM, YDIM, ZDIM]'''
        return str()