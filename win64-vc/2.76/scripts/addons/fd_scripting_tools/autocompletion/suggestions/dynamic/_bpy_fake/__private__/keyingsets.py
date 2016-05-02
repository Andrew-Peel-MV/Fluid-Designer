from . struct import Struct
from . keyingset import KeyingSet
from . bpy_struct import bpy_struct
import mathutils

class KeyingSets(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(KeyingSet) Active Keying Set used to insert/delete keyframes'''
        return KeyingSet()
    @property
    def active_index(self):
        '''(Integer) Current Keying Set index (negative for 'builtin' and
        positive for 'absolute')'''
        return int()
    def new(self, idname, name):
        '''Add a new Keying Set to Scene
        
        Parameter:
          idname: (String) Internal identifier of Keying Set
          name: (String) User visible name of Keying Set
        
        Returns:
          keyingset: (KeyingSet) Newly created Keying Set'''
        return KeyingSet()
    def get(key): return KeyingSet()
    def __getitem__(key): return KeyingSet()
    def __iter__(key): yield KeyingSet()