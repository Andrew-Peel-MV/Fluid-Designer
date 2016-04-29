from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ColorManagedInputColorspaceSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(Enum) Color space of the image or movie on disk
        
        [Linear, Linear ACES, Non-Color, Raw, sRGB, VD16, XYZ]'''
        return str()