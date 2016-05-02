from . struct import Struct
from . fd_tab import fd_tab
from . bpy_struct import bpy_struct
import mathutils

class mvPrompt(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def AngleValue(self):
        '''(Float)'''
        return float()
    @property
    def EnumIndex(self):
        '''(Integer)'''
        return int()
    @property
    def export(self):
        '''(Boolean) This determines if the prompt should be exported'''
        return bool()
    @property
    def COL_EnumItem(self):
        '''(Sequence of fd_tab)'''
        return (fd_tab(),)
    @property
    def columns(self):
        '''(Integer) Used for Combo Boxes to determine how many columns should be
        displayed'''
        return int()
    @property
    def DistanceValue(self):
        '''(Float)'''
        return float()
    @property
    def lock_value(self):
        '''(Boolean)'''
        return bool()
    @property
    def equal(self):
        '''(Boolean) Used in calculators to calculate remaining size'''
        return bool()
    @property
    def TabIndex(self):
        '''(Integer)'''
        return int()
    @property
    def NumberValue(self):
        '''(Float)'''
        return float()
    @property
    def TextValue(self):
        '''(String)'''
        return str()
    @property
    def QuantityValue(self):
        '''(Integer)'''
        return int()
    @property
    def PercentageValue(self):
        '''(Float)'''
        return float()
    @property
    def PriceValue(self):
        '''(Float)'''
        return float()
    @property
    def Type(self):
        '''(Enum)
        
        [NUMBER, QUANTITY, COMBOBOX, CHECKBOX, TEXT, DISTANCE, ANGLE,
        PERCENTAGE, PRICE]'''
        return str()
    @property
    def CheckBoxValue(self):
        '''(Boolean)'''
        return bool()