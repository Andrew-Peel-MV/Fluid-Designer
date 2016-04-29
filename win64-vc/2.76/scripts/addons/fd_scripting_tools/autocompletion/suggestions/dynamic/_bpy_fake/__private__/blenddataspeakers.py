from . speaker import Speaker
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataSpeakers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new speaker to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          speaker: (Speaker) New speaker datablock'''
        return Speaker()
    def remove(self, speaker):
        '''Remove a speaker from the current blendfile
        
        Parameter:
          speaker: (Speaker) Speaker to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Speaker()
    def __getitem__(key): return Speaker()
    def __iter__(key): yield Speaker()