from . struct import Struct
from . sequencemodifier import SequenceModifier
from . bpy_struct import bpy_struct
import mathutils

class SequenceModifiers(bpy_struct):
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
          modifier: (SequenceModifier) Newly created modifier'''
        return SequenceModifier()
    def remove(self, modifier):
        '''Remove an existing modifier from the sequence
        
        Parameter:
          modifier: (SequenceModifier) Modifier to remove'''
        return 
    def clear(self):
        '''Remove all modifiers from the sequence'''
        return 
    def get(key): return SequenceModifier()
    def __getitem__(key): return SequenceModifier()
    def __iter__(key): yield SequenceModifier()