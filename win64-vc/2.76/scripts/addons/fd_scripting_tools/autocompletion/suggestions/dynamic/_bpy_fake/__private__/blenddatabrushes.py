from . brush import Brush
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataBrushes(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name, mode):
        '''Add a new brush to the main database
        
        Parameter:
          name: (String) New name for the datablock
          mode: (Enum) Paint Mode for the new brush
        
        Returns:
          brush: (Brush) New brush datablock'''
        return Brush()
    def remove(self, brush):
        '''Remove a brush from the current blendfile
        
        Parameter:
          brush: (Brush) Brush to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Brush()
    def __getitem__(key): return Brush()
    def __iter__(key): yield Brush()