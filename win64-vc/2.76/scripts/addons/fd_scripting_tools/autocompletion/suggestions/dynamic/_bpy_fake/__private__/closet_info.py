from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Closet_Info(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def Wall_Type(self):
        '''(Enum)
        
        [DRYWALL, CONCRETE, PLASTER, OTHER]'''
        return str()
    @property
    def Notch_2_Width(self):
        '''(Float)'''
        return float()
    @property
    def Notch_1_Width(self):
        '''(Float)'''
        return float()
    @property
    def Floor_Type(self):
        '''(Enum)
        
        [CARPET, CONCRETE, HARDWOOD, OTHER]'''
        return str()
    @property
    def Notch_2_Height(self):
        '''(Float)'''
        return float()
    @property
    def Notch_Type(self):
        '''(Enum)
        
        [SINGLE, DOUBLE]'''
        return str()
    @property
    def Closet_Tear_Out(self):
        '''(Enum)
        
        [NONE, STANDARD, OTHER]'''
        return str()
    @property
    def Door_Opening_Type(self):
        '''(Enum)
        
        [SWING_IN, SWING_OUT, POCKET, BI_FOLD, OTHER]'''
        return str()
    @property
    def Base_Board(self):
        '''(Enum)
        
        [NONE, REMOVE, NOTCH]'''
        return str()
    @property
    def Notch_1_Height(self):
        '''(Float)'''
        return float()