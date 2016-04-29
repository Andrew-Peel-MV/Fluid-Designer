from . fmodifier import FModifier
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class FCurveModifiers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(FModifier) Active F-Curve Modifier'''
        return FModifier()
    def new(self, type):
        '''Add a constraint to this object
        
        Parameter:
          type: (Enum) Constraint type to add
        
        Returns:
          fmodifier: (FModifier) New fmodifier'''
        return FModifier()
    def remove(self, modifier):
        '''Remove a modifier from this F-Curve
        
        Parameter:
          modifier: (FModifier) Removed modifier'''
        return 
    def get(key): return FModifier()
    def __getitem__(key): return FModifier()
    def __iter__(key): yield FModifier()