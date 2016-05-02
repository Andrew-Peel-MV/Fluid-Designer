from . struct import Struct
from . linestylealphamodifier import LineStyleAlphaModifier
from . bpy_struct import bpy_struct
import mathutils

class LineStyleAlphaModifiers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name, type):
        '''Add a alpha modifier to line style
        
        Parameter:
          name: (String) New name for the alpha modifier (not unique)
          type: (Enum) Alpha modifier type to add
        
        Returns:
          modifier: (LineStyleAlphaModifier) Newly added alpha modifier'''
        return LineStyleAlphaModifier()
    def remove(self, modifier):
        '''Remove a alpha modifier from line style
        
        Parameter:
          modifier: (LineStyleAlphaModifier) Alpha modifier to remove'''
        return 
    def get(key): return LineStyleAlphaModifier()
    def __getitem__(key): return LineStyleAlphaModifier()
    def __iter__(key): yield LineStyleAlphaModifier()