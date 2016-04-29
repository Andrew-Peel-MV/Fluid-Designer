from . sound import Sound
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataSounds(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def load(self, filepath):
        '''Add a new sound to the main database from a file
        
        Parameter:
          filepath: (String) path for the datablock
        
        Returns:
          sound: (Sound) New text datablock'''
        return Sound()
    def remove(self, sound):
        '''Remove a sound from the current blendfile
        
        Parameter:
          sound: (Sound) Sound to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Sound()
    def __getitem__(key): return Sound()
    def __iter__(key): yield Sound()