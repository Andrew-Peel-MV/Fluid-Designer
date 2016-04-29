from . addon import Addon
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Addons(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self):
        '''Add a new add-on
        
        Returns:
          addon: (Addon) Addon datablock'''
        return Addon()
    def remove(self, addon):
        '''Remove add-on
        
        Parameter:
          addon: (Addon) Addon to remove'''
        return 
    def get(key): return Addon()
    def __getitem__(key): return Addon()
    def __iter__(key): yield Addon()