from . lamptextureslot import LampTextureSlot
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class LampTextureSlots(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self):
        '''add
        
        Returns:
          mtex: (LampTextureSlot) The newly initialized mtex'''
        return LampTextureSlot()
    def create(self, index):
        '''create
        
        Parameter:
          index: (Integer) Slot index to initialize
        
        Returns:
          mtex: (LampTextureSlot) The newly initialized mtex'''
        return LampTextureSlot()
    def clear(self, index):
        '''clear
        
        Parameter:
          index: (Integer) Slot index to clear'''
        return 
    def get(key): return LampTextureSlot()
    def __getitem__(key): return LampTextureSlot()
    def __iter__(key): yield LampTextureSlot()