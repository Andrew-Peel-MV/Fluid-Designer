from . struct import Struct
from . freestylelinestyle import FreestyleLineStyle
from . bpy_struct import bpy_struct
import mathutils

class BlendDataLineStyles(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def new(self, name):
        '''Add a new line style instance to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          linestyle: (FreestyleLineStyle) New line style datablock'''
        return FreestyleLineStyle()
    def remove(self, linestyle):
        '''Remove a line style instance from the current blendfile
        
        Parameter:
          linestyle: (FreestyleLineStyle) Line style to remove'''
        return 
    def get(key): return FreestyleLineStyle()
    def __getitem__(key): return FreestyleLineStyle()
    def __iter__(key): yield FreestyleLineStyle()