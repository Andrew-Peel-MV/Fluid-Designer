from . palette import Palette
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataPalettes(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new palette to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          palette: (Palette) New palette datablock'''
        return Palette()
    def remove(self, palette):
        '''Remove a palette from the current blendfile
        
        Parameter:
          palette: (Palette) Palette to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Palette()
    def __getitem__(key): return Palette()
    def __iter__(key): yield Palette()