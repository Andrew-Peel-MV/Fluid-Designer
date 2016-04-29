from . channeldrivervariables import ChannelDriverVariables
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Driver(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Driver type
        
        [AVERAGE, SUM, SCRIPTED, MIN, MAX]'''
        return str()
    @property
    def expression(self):
        '''(String) Expression to use for Scripted Expression'''
        return str()
    @property
    def variables(self):
        '''(Sequence of DriverVariable) Properties acting as inputs for this
        driver'''
        return ChannelDriverVariables()
    @property
    def show_debug_info(self):
        '''(Boolean) Show intermediate values for the driver calculations to
        allow debugging of drivers'''
        return bool()
    @property
    def is_valid(self):
        '''(Boolean) Driver could not be evaluated in past, so should be skipped'''
        return bool()