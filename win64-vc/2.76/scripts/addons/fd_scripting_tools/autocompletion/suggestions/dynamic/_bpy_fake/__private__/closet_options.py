from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Closet_Options(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def Premium_Package(self):
        '''(Boolean)'''
        return bool()
    @property
    def Crown_Molding_Type(self):
        '''(Enum)
        
        [3, CONTEMPORARY]'''
        return str()
    @property
    def Base_Molding(self):
        '''(Boolean)'''
        return bool()
    @property
    def Material_Type(self):
        '''(Enum)
        
        [WHITE, MELAMINE, WOOD_MELAMINE]'''
        return str()
    @property
    def Backing_Type(self):
        '''(Enum)
        
        [NO_BACKING, BACKING, BRIO_BACKING]'''
        return str()
    @property
    def Door_Drawer_Style(self):
        '''(Enum)
        
        [STANDARD_FLAT, DECO, 5_PIECE]'''
        return str()
    @property
    def Base_Molding_Type(self):
        '''(Enum)
        
        [3, 400]'''
        return str()
    @property
    def Accent_Shelf_Type(self):
        '''(Enum)
        
        [NO_TOP_SHELF, ACCENT_TOP_SHELF]'''
        return str()
    @property
    def Five_Piece_Door_Style(self):
        '''(Enum)
        
        [TRADITIONAL, SMALL_SHARKER, LARGE_SHARKER, TRANSITIONAL]'''
        return str()
    @property
    def Deco_Style(self):
        '''(Enum)
        
        [100, 101, 102, 103, 200, 201, 202, 203, 300, 400, 500, 501, 700, 701,
        702, 703, 800, 801, 802, 803]'''
        return str()
    @property
    def Crown_Molding_To_Ceiling(self):
        '''(Boolean)'''
        return bool()
    @property
    def Accent_Top_Shelf(self):
        '''(Boolean)'''
        return bool()
    @property
    def Backing(self):
        '''(Boolean)'''
        return bool()
    @property
    def Crown_Molding(self):
        '''(Boolean)'''
        return bool()
    @property
    def Ball_Bearing_Slides(self):
        '''(Boolean)'''
        return bool()
    @property
    def Wood_Grain_Melamine(self):
        '''(Enum)
        
        [CAYENNE_MAPLE, SUNSET, CHOC_PEARWOOD, CANDELLIGHT, BRUSHED_ALUM]'''
        return str()
    @property
    def Closet_Style(self):
        '''(Enum)
        
        [EVERYDAY, CLASSIC, REGENCY, BRIO]'''
        return str()
    @property
    def Molding_Type(self):
        '''(Enum)
        
        [NO_MOLDING, MOLDING_PACKAGE, BASE_ONLY, CROWN_ONLY]'''
        return str()
    @property
    def Melamine_Material(self):
        '''(Enum)
        
        [ALMOND, GREY, BLACK_MELAMINE]'''
        return str()
    @property
    def Valet_Rod_Quantity(self):
        '''(Integer)'''
        return int()