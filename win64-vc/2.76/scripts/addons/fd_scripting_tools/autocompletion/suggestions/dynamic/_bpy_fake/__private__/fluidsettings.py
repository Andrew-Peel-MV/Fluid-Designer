from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class FluidSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Type of participation in the fluid simulation
        
        [NONE, DOMAIN, FLUID, OBSTACLE, INFLOW, OUTFLOW, PARTICLE, CONTROL]'''
        return str()