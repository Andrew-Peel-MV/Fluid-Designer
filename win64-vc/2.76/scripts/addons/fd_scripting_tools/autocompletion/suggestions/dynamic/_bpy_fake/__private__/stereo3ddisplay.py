from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Stereo3dDisplay(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def display_mode(self):
        '''(Enum)
        
        [ANAGLYPH, INTERLACE, TIMESEQUENTIAL, SIDEBYSIDE, TOPBOTTOM]'''
        return str()
    @property
    def anaglyph_type(self):
        '''(Enum)
        
        [RED_CYAN, GREEN_MAGENTA, YELLOW_BLUE]'''
        return str()
    @property
    def interlace_type(self):
        '''(Enum)
        
        [ROW_INTERLEAVED, COLUMN_INTERLEAVED, CHECKERBOARD_INTERLEAVED]'''
        return str()
    @property
    def use_interlace_swap(self):
        '''(Boolean) Swap left and right stereo channels'''
        return bool()
    @property
    def use_sidebyside_crosseyed(self):
        '''(Boolean) Right eye should see left image and vice-versa'''
        return bool()