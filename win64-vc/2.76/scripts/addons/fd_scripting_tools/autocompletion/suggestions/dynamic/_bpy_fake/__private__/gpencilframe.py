from . struct import Struct
from . gpencilstrokes import GPencilStrokes
from . bpy_struct import bpy_struct
import mathutils

class GPencilFrame(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def strokes(self):
        '''(Sequence of GPencilStroke) Freehand curves defining the sketch on
        this frame'''
        return GPencilStrokes()
    @property
    def frame_number(self):
        '''(Integer) The frame on which this sketch appears'''
        return int()
    @property
    def is_edited(self):
        '''(Boolean) Frame is being edited (painted on)'''
        return bool()
    @property
    def select(self):
        '''(Boolean) Frame is selected for editing in the Dope Sheet'''
        return bool()
    def clear(self):
        '''Remove all the grease pencil frame data'''
        return 