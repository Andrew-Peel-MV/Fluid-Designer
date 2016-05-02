from . struct import Struct
from . mask import Mask
from . bpy_struct import bpy_struct
import mathutils

class BlendDataMasks(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def new(self, name):
        '''Add a new mask with a given name to the main database
        
        Parameter:
          name: (String) Name of new mask datablock
        
        Returns:
          mask: (Mask) New mask datablock'''
        return Mask()
    def remove(self, mask):
        '''Remove a masks from the current blendfile.
        
        Parameter:
          mask: (Mask) Mask to remove'''
        return 
    def get(key): return Mask()
    def __getitem__(key): return Mask()
    def __iter__(key): yield Mask()