from . colorrampelement import ColorRampElement
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ColorRampElements(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, position):
        '''Add element to ColorRamp
        
        Parameter:
          position: (Float) Position to add element
        
        Returns:
          element: (ColorRampElement) New element'''
        return ColorRampElement()
    def remove(self, element):
        '''Delete element from ColorRamp
        
        Parameter:
          element: (ColorRampElement) Element to remove'''
        return 
    def get(key): return ColorRampElement()
    def __getitem__(key): return ColorRampElement()
    def __iter__(key): yield ColorRampElement()