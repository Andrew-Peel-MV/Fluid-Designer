from . struct import Struct
from . modifier import Modifier
from . bpy_struct import bpy_struct
import mathutils

class ObjectModifiers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name, type):
        '''Add a new modifier
        
        Parameter:
          name: (String) New name for the modifier
          type: (Enum) Modifier type to add
        
        Returns:
          modifier: (Modifier) Newly created modifier'''
        return Modifier()
    def remove(self, modifier):
        '''Remove an existing modifier from the object
        
        Parameter:
          modifier: (Modifier) Modifier to remove'''
        return 
    def clear(self):
        '''Remove all modifiers from the object'''
        return 
    def get(key): return Modifier()
    def __getitem__(key): return Modifier()
    def __iter__(key): yield Modifier()