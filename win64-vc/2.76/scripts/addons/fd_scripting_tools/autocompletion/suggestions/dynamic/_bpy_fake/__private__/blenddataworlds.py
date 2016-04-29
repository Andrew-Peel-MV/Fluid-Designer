from . world import World
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataWorlds(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new world to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          world: (World) New world datablock'''
        return World()
    def remove(self, world):
        '''Remove a world from the current blendfile
        
        Parameter:
          world: (World) World to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return World()
    def __getitem__(key): return World()
    def __iter__(key): yield World()