from . lamp import Lamp
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataLamps(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name, type):
        '''Add a new lamp to the main database
        
        Parameter:
          name: (String) New name for the datablock
          type: (Enum) The type of texture to add
        
        Returns:
          lamp: (Lamp) New lamp datablock'''
        return Lamp()
    def remove(self, lamp):
        '''Remove a lamp from the current blendfile
        
        Parameter:
          lamp: (Lamp) Lamp to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Lamp()
    def __getitem__(key): return Lamp()
    def __iter__(key): yield Lamp()