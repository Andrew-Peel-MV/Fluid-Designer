from . renderslot import RenderSlot
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class RenderSlots(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(RenderSlot) Active render slot of the image'''
        return RenderSlot()
    @property
    def active_index(self):
        '''(Integer) Index of an active render slot of the image'''
        return int()
    def get(key): return RenderSlot()
    def __getitem__(key): return RenderSlot()
    def __iter__(key): yield RenderSlot()