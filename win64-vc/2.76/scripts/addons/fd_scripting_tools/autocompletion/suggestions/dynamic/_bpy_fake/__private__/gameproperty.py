from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GameProperty(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Available as GameObject attributes in the game engine's
        python API'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [BOOL, INT, FLOAT, STRING, TIMER]'''
        return str()
    @property
    def show_debug(self):
        '''(Boolean) Print debug information for this property'''
        return bool()