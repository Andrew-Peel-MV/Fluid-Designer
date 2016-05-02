from . struct import Struct
from . metaelement import MetaElement
from . bpy_struct import bpy_struct
import mathutils

class MetaBallElements(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MetaElement) Last selected element'''
        return MetaElement()
    def new(self, type):
        '''Add a new element to the metaball
        
        Parameter:
          type: (Enum) type for the new meta-element
        
        Returns:
          element: (MetaElement) The newly created meta-element'''
        return MetaElement()
    def remove(self, element):
        '''Remove an element from the metaball
        
        Parameter:
          element: (MetaElement) The element to remove'''
        return 
    def clear(self):
        '''Remove all elements from the metaball'''
        return 
    def get(key): return MetaElement()
    def __getitem__(key): return MetaElement()
    def __iter__(key): yield MetaElement()