from . worldtextureslot import WorldTextureSlot
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class WorldTextureSlots(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self):
        '''add
        
        Returns:
          mtex: (WorldTextureSlot) The newly initialized mtex'''
        return WorldTextureSlot()
    def create(self, index):
        '''create
        
        Parameter:
          index: (Integer) Slot index to initialize
        
        Returns:
          mtex: (WorldTextureSlot) The newly initialized mtex'''
        return WorldTextureSlot()
    def clear(self, index):
        '''clear
        
        Parameter:
          index: (Integer) Slot index to clear'''
        return 
    def get(key): return WorldTextureSlot()
    def __getitem__(key): return WorldTextureSlot()
    def __iter__(key): yield WorldTextureSlot()