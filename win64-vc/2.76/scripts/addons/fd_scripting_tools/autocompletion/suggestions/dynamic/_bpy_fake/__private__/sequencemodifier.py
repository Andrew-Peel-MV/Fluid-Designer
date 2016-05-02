from . struct import Struct
from . sequence import Sequence
from . mask import Mask
from . bpy_struct import bpy_struct
import mathutils

class SequenceModifier(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [COLOR_BALANCE, CURVES, HUE_CORRECT, BRIGHT_CONTRAST, MASK]'''
        return str()
    @property
    def mute(self):
        '''(Boolean) Mute this modifier'''
        return bool()
    @property
    def show_expanded(self):
        '''(Boolean) Mute expanded settings for the modifier'''
        return bool()
    @property
    def input_mask_type(self):
        '''(Enum) Type of input data used for mask
        
        [STRIP, ID]'''
        return str()
    @property
    def input_mask_strip(self):
        '''(Sequence) Strip used as mask input for the modifier'''
        return Sequence()
    @property
    def input_mask_id(self):
        '''(Mask) Mask ID used as mask input for the modifier'''
        return Mask()