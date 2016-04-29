from . particlesettingstextureslot import ParticleSettingsTextureSlot
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ParticleSettingsTextureSlots(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def add(self):
        '''add
        
        Returns:
          mtex: (ParticleSettingsTextureSlot) The newly initialized mtex'''
        return ParticleSettingsTextureSlot()
    def create(self, index):
        '''create
        
        Parameter:
          index: (Integer) Slot index to initialize
        
        Returns:
          mtex: (ParticleSettingsTextureSlot) The newly initialized mtex'''
        return ParticleSettingsTextureSlot()
    def clear(self, index):
        '''clear
        
        Parameter:
          index: (Integer) Slot index to clear'''
        return 
    def get(key): return ParticleSettingsTextureSlot()
    def __getitem__(key): return ParticleSettingsTextureSlot()
    def __iter__(key): yield ParticleSettingsTextureSlot()