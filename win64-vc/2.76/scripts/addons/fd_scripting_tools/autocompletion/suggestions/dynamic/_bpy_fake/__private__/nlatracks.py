from . nlatrack import NlaTrack
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class NlaTracks(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(NlaTrack) Active Object constraint'''
        return NlaTrack()
    def new(self, prev):
        '''Add a new NLA Track
        
        Parameter:
          prev: (NlaTrack) NLA Track to add the new one after
        
        Returns:
          track: (NlaTrack) New NLA Track'''
        return NlaTrack()
    def remove(self, track):
        '''Remove a NLA Track
        
        Parameter:
          track: (NlaTrack) NLA Track to remove'''
        return 
    def get(key): return NlaTrack()
    def __getitem__(key): return NlaTrack()
    def __iter__(key): yield NlaTrack()