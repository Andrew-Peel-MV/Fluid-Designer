from . struct import Struct
from . keyingset import KeyingSet
from . bpy_struct import bpy_struct
import mathutils

class KeyingSetsAll(bpy_struct):
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
    def get(key): return KeyingSet()
    def __getitem__(key): return KeyingSet()
    def __iter__(key): yield KeyingSet()