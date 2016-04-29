from . pricing_options import Pricing_Options
from . closet_info import Closet_Info
from . wall import Wall
from . closet_options import Closet_Options
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Global_Variables(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def Adj_Shelf_Setback(self):
        '''(Float) This sets the default adjustable shelf setback'''
        return float()
    @property
    def Panel_Height(self):
        '''(Float)'''
        return float()
    @property
    def Tall_Top_Reveal(self):
        '''(Float) This sets the top reveal for tall overlay doors.'''
        return float()
    @property
    def WallIndex(self):
        '''(Integer)'''
        return int()
    @property
    def Pull_Name(self):
        '''(String)'''
        return str()
    @property
    def Vertical_Gap(self):
        '''(Float) This sets the distance between double doors.'''
        return float()
    @property
    def Backing_Type(self):
        '''(Enum)
        
        [NONE, STANDARD_BACKS, THICK_BACKS]'''
        return str()
    @property
    def Right_Reveal(self):
        '''(Float) This sets the right reveal for overlay doors.'''
        return float()
    @property
    def Center_Pulls_on_Drawers(self):
        '''(Boolean) Center pulls on the drawer heights. Otherwise the pull z
        location is controlled with Drawer Pull From Top'''
        return bool()
    @property
    def Inset_Reveal(self):
        '''(Float) This sets the reveal for inset doors.'''
        return float()
    @property
    def Pricing_Info(self):
        '''(Pricing_Options)'''
        return Pricing_Options()
    @property
    def Pull_Rotation(self):
        '''(Float) Rotation of pulls on doors'''
        return float()
    @property
    def Inset_Door(self):
        '''(Boolean) Check this to use inset doors'''
        return bool()
    @property
    def Drawer_Pull_From_Top(self):
        '''(Float) When Center Pulls on Drawers is off this is the amount from
        the top of the drawer front to the enter pull'''
        return float()
    @property
    def Pull_From_Edge(self):
        '''(Float) X Distance from the door edge to the pull'''
        return float()
    @property
    def Room_Type(self):
        '''(Enum)
        
        [SINGLE, LSHAPE, USHAPE, SQUARE]'''
        return str()
    @property
    def Upper_Pull_Location(self):
        '''(Float) Z Distance from the bottom of the door edge to the bottom of
        the pull'''
        return float()
    @property
    def Base_Door_Style(self):
        '''(Enum)'''
        return str()
    @property
    def Drawer_Front_Style(self):
        '''(Enum)'''
        return str()
    @property
    def Closet_Options(self):
        '''(Closet_Options)'''
        return Closet_Options()
    @property
    def ECR(self):
        '''(Enum)
        
        [EVERYDAY, CLASSIC, REGENCY]'''
        return str()
    @property
    def Door_To_Cabinet_Gap(self):
        '''(Float) This sets the distance between the back of the door and the
        front cabinet edge.'''
        return float()
    @property
    def Upper_Bottom_Reveal(self):
        '''(Float) This sets the bottom reveal for upper overlay doors.'''
        return float()
    @property
    def Main_Tabs(self):
        '''(Enum)
        
        [INFO, OPTIONS, TOTAL]'''
        return str()
    @property
    def Tall_Bottom_Reveal(self):
        '''(Float) This sets the bottom reveal for tall overlay doors.'''
        return float()
    @property
    def Upper_Door_Style(self):
        '''(Enum)'''
        return str()
    @property
    def Center_Pulls_on_Doors(self):
        '''(Boolean) Center pulls on the width of the doors. This is typically
        used with horizontal pulls'''
        return bool()
    @property
    def Base_Pull_Location(self):
        '''(Float) Z Distance from the top of the door edge to the top of the
        pull'''
        return float()
    @property
    def Base_Top_Reveal(self):
        '''(Float) This sets the top reveal for base overlay doors.'''
        return float()
    @property
    def Discount(self):
        '''(Float)'''
        return float()
    @property
    def Tall_Pull_Location(self):
        '''(Float) Z Distance from the bottom of the door edge to the center of
        the pull'''
        return float()
    @property
    def Panel_Depth(self):
        '''(Float)'''
        return float()
    @property
    def Left_Reveal(self):
        '''(Float) This sets the left reveal for overlay doors.'''
        return float()
    @property
    def Tall_Door_Style(self):
        '''(Enum)'''
        return str()
    @property
    def Walls(self):
        '''(Sequence of Wall)'''
        return (Wall(),)
    @property
    def Upper_Top_Reveal(self):
        '''(Float) This sets the top reveal for upper overlay doors.'''
        return float()
    @property
    def Fixed_Shelf_Setback(self):
        '''(Float) This sets the default fixed shelf setback'''
        return float()
    @property
    def Base_Bottom_Reveal(self):
        '''(Float) This sets the bottom reveal for base overlay doors.'''
        return float()
    @property
    def Closet_Info(self):
        '''(Closet_Info)'''
        return Closet_Info()