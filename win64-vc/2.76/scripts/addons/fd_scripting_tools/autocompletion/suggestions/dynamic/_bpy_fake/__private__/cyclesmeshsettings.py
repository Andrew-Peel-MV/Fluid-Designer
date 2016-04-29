from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesMeshSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def displacement_method(self):
        '''(Enum) Method to use for the displacement
        
        [BUMP, TRUE, BOTH]'''
        return str()
    @property
    def use_subdivision(self):
        '''(Boolean) Subdivide mesh for rendering'''
        return bool()
    @property
    def dicing_rate(self):
        '''(Float)'''
        return float()