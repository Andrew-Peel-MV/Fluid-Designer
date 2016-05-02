from . linestylegeometrymodifier import LineStyleGeometryModifier
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class LineStyleGeometryModifiers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name, type):
        '''Add a geometry modifier to line style
        
        Parameter:
          name: (String) New name for the geometry modifier (not unique)
          type: (Enum) Geometry modifier type to add
        
        Returns:
          modifier: (LineStyleGeometryModifier) Newly added geometry modifier'''
        return LineStyleGeometryModifier()
    def remove(self, modifier):
        '''Remove a geometry modifier from line style
        
        Parameter:
          modifier: (LineStyleGeometryModifier) Geometry modifier to remove'''
        return 
    def get(key): return LineStyleGeometryModifier()
    def __getitem__(key): return LineStyleGeometryModifier()
    def __iter__(key): yield LineStyleGeometryModifier()