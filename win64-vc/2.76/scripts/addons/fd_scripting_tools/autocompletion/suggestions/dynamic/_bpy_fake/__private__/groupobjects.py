from . object import Object
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GroupObjects(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def link(self, object):
        '''Add this object to a group
        
        Parameter:
          object: (Object) Object to add'''
        return 
    def unlink(self, object):
        '''Remove this object to a group
        
        Parameter:
          object: (Object) Object to remove'''
        return 
    def get(key): return Object()
    def __getitem__(key): return Object()
    def __iter__(key): yield Object()