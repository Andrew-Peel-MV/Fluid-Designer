from . struct import Struct
from . linestylecolormodifier import LineStyleColorModifier
from . bpy_struct import bpy_struct
import mathutils

class LineStyleColorModifiers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name, type):
        '''Add a color modifier to line style
        
        Parameter:
          name: (String) New name for the color modifier (not unique)
          type: (Enum) Color modifier type to add
        
        Returns:
          modifier: (LineStyleColorModifier) Newly added color modifier'''
        return LineStyleColorModifier()
    def remove(self, modifier):
        '''Remove a color modifier from line style
        
        Parameter:
          modifier: (LineStyleColorModifier) Color modifier to remove'''
        return 
    def get(key): return LineStyleColorModifier()
    def __getitem__(key): return LineStyleColorModifier()
    def __iter__(key): yield LineStyleColorModifier()