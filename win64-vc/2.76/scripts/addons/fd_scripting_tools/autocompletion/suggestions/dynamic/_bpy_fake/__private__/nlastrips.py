from . nlastrip import NlaStrip
from . action import Action
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class NlaStrips(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name, start, action):
        '''Add a new Action-Clip strip to the track
        
        Parameter:
          name: (String) Name for the NLA Strips
          start: (Integer) Start frame for this strip
          action: (Action) Action to assign to this strip
        
        Returns:
          strip: (NlaStrip) New NLA Strip'''
        return NlaStrip()
    def remove(self, strip):
        '''Remove a NLA Strip
        
        Parameter:
          strip: (NlaStrip) NLA Strip to remove'''
        return 
    def get(key): return NlaStrip()
    def __getitem__(key): return NlaStrip()
    def __iter__(key): yield NlaStrip()