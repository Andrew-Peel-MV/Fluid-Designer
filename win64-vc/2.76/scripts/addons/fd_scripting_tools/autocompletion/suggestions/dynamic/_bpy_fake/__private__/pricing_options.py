from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Pricing_Options(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def Pull_Qty(self):
        '''(Integer)'''
        return int()
    @property
    def Top_Shelf_Price(self):
        '''(Float)'''
        return float()
    @property
    def Total_Price(self):
        '''(Float)'''
        return float()
    @property
    def Wire_Basket_Price(self):
        '''(Float)'''
        return float()
    @property
    def Backing_Price(self):
        '''(Float)'''
        return float()
    @property
    def Countertop_Price(self):
        '''(Float)'''
        return float()
    @property
    def Wire_Basket_Qty(self):
        '''(Integer)'''
        return int()