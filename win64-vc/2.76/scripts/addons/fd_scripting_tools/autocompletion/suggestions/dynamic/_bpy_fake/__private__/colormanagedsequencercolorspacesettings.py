from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ColorManagedSequencerColorspaceSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(Enum) Color space that the sequencer operates in
        
        [Linear, Linear ACES, Non-Color, Raw, sRGB, VD16, XYZ]'''
        return str()