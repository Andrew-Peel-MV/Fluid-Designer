from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Scene_Variables(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def Door_Depth(self):
        '''(Float) Default depth for doors'''
        return float()
    @property
    def Door_Width(self):
        '''(Float) Default width for doors'''
        return float()
    @property
    def Door_Height(self):
        '''(Float) Default height for doors'''
        return float()