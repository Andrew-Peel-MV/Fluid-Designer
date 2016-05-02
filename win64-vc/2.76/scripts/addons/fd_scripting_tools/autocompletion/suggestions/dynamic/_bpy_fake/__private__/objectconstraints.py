from . struct import Struct
from . constraint import Constraint
from . bpy_struct import bpy_struct
import mathutils

class ObjectConstraints(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Constraint) Active Object constraint'''
        return Constraint()
    def new(self, type):
        '''Add a new constraint to this object
        
        Parameter:
          type: (Enum) Constraint type to add
        
        Returns:
          constraint: (Constraint) New constraint'''
        return Constraint()
    def remove(self, constraint):
        '''Remove a constraint from this object
        
        Parameter:
          constraint: (Constraint) Removed constraint'''
        return 
    def clear(self):
        '''Remove all constraint from this object'''
        return 
    def get(key): return Constraint()
    def __getitem__(key): return Constraint()
    def __iter__(key): yield Constraint()