from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ColorManagedDisplaySettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def display_device(self):
        '''(Enum) Display device name
        
        [DEFAULT]'''
        return str()