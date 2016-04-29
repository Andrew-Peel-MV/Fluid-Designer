from . linestyletextureslot import LineStyleTextureSlot
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class LineStyleTextureSlots(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self):
        '''add
        
        Returns:
          mtex: (LineStyleTextureSlot) The newly initialized mtex'''
        return LineStyleTextureSlot()
    def create(self, index):
        '''create
        
        Parameter:
          index: (Integer) Slot index to initialize
        
        Returns:
          mtex: (LineStyleTextureSlot) The newly initialized mtex'''
        return LineStyleTextureSlot()
    def clear(self, index):
        '''clear
        
        Parameter:
          index: (Integer) Slot index to clear'''
        return 
    def get(key): return LineStyleTextureSlot()
    def __getitem__(key): return LineStyleTextureSlot()
    def __iter__(key): yield LineStyleTextureSlot()