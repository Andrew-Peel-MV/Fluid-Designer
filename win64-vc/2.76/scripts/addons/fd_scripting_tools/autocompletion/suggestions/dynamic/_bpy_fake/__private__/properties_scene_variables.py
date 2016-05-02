from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PROPERTIES_Scene_Variables(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def Upper_Width_Blind(self):
        '''(Float) Default width for upper blind corner cabinets'''
        return float()
    @property
    def Tall_Cabinet_Height(self):
        '''(Float) Default height for tall cabinets'''
        return float()
    @property
    def Suspended_Cabinet_Height(self):
        '''(Float) Default height for suspended cabinets'''
        return float()
    @property
    def Base_Inside_Corner_Size(self):
        '''(Float) Default width and depth for the inside base corner cabinets'''
        return float()
    @property
    def Upper_Inside_Corner_Size(self):
        '''(Float) Default width and depth for the inside upper corner cabinets'''
        return float()
    @property
    def Width_1_Door(self):
        '''(Float) Default width for one door wide cabinets'''
        return float()
    @property
    def Blind_Panel_Reveal(self):
        '''(Float) Default reveal for blind panels'''
        return float()
    @property
    def Base_Cabinet_Depth(self):
        '''(Float) Default depth for base cabinets'''
        return float()
    @property
    def Tall_Cabinet_Depth(self):
        '''(Float) Default depth for tall cabinets'''
        return float()
    @property
    def Base_Cabinet_Height(self):
        '''(Float) Default height for base cabinets'''
        return float()
    @property
    def Inset_Blind_Panel(self):
        '''(Boolean) Check this to inset the blind panel into the cabinet carcass'''
        return bool()
    @property
    def Sink_Cabinet_Height(self):
        '''(Float) Default height for sink cabinets'''
        return float()
    @property
    def Upper_Cabinet_Depth(self):
        '''(Float) Default depth for upper cabinets'''
        return float()
    @property
    def Suspended_Cabinet_Depth(self):
        '''(Float) Default depth for suspended cabinets'''
        return float()
    @property
    def Width_2_Door(self):
        '''(Float) Default width for two door wide and open cabinets'''
        return float()
    @property
    def Top_Drawer_Front_Height(self):
        '''(Float) Default top drawer front height.'''
        return float()
    @property
    def Width_Drawer(self):
        '''(Float) Default width for drawer cabinets'''
        return float()
    @property
    def Equal_Drawer_Stack_Heights(self):
        '''(Boolean) Check this make all drawer stack heights equal. Otherwise
        the Top Drawer Height will be set.'''
        return bool()
    @property
    def Sink_Cabinet_Depth(self):
        '''(Float) Default depth for sink cabinets'''
        return float()
    @property
    def Height_Above_Floor(self):
        '''(Float) Default height above floor for upper cabinets'''
        return float()
    @property
    def Base_Width_Blind(self):
        '''(Float) Default width for base blind corner cabinets'''
        return float()
    @property
    def Upper_Cabinet_Height(self):
        '''(Float) Default height for upper cabinets'''
        return float()
    @property
    def Tall_Width_Blind(self):
        '''(Float) Default width for tall blind corner cabinets'''
        return float()