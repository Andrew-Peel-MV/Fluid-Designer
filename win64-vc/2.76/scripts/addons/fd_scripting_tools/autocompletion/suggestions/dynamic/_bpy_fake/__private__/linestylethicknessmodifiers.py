from . struct import Struct
from . linestylethicknessmodifier import LineStyleThicknessModifier
from . bpy_struct import bpy_struct
import mathutils

class LineStyleThicknessModifiers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name, type):
        '''Add a thickness modifier to line style
        
        Parameter:
          name: (String) New name for the thickness modifier (not unique)
          type: (Enum) Thickness modifier type to add
        
        Returns:
          modifier: (LineStyleThicknessModifier) Newly added thickness modifier'''
        return LineStyleThicknessModifier()
    def remove(self, modifier):
        '''Remove a thickness modifier from line style
        
        Parameter:
          modifier: (LineStyleThicknessModifier) Thickness modifier to remove'''
        return 
    def get(key): return LineStyleThicknessModifier()
    def __getitem__(key): return LineStyleThicknessModifier()
    def __iter__(key): yield LineStyleThicknessModifier()