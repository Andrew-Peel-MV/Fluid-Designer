from . id import ID
from . object import Object
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataObjects(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name, object_data):
        '''Add a new object to the main database
        
        Parameter:
          name: (String) New name for the datablock
          object_data: (ID) Object data or None for an empty object
        
        Returns:
          object: (Object) New object datablock'''
        return Object()
    def remove(self, object):
        '''Remove a object from the current blendfile
        
        Parameter:
          object: (Object) Object to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Object()
    def __getitem__(key): return Object()
    def __iter__(key): yield Object()