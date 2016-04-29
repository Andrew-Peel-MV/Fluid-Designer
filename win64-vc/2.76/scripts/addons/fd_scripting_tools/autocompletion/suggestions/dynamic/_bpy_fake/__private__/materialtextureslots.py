from . materialtextureslot import MaterialTextureSlot
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialTextureSlots(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self):
        '''add
        
        Returns:
          mtex: (MaterialTextureSlot) The newly initialized mtex'''
        return MaterialTextureSlot()
    def create(self, index):
        '''create
        
        Parameter:
          index: (Integer) Slot index to initialize
        
        Returns:
          mtex: (MaterialTextureSlot) The newly initialized mtex'''
        return MaterialTextureSlot()
    def clear(self, index):
        '''clear
        
        Parameter:
          index: (Integer) Slot index to clear'''
        return 
    def get(key): return MaterialTextureSlot()
    def __getitem__(key): return MaterialTextureSlot()
    def __iter__(key): yield MaterialTextureSlot()