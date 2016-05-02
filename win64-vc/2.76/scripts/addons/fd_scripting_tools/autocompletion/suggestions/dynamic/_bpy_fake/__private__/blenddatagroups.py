from . struct import Struct
from . group import Group
from . bpy_struct import bpy_struct
import mathutils

class BlendDataGroups(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new group to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          group: (Group) New group datablock'''
        return Group()
    def remove(self, group):
        '''Remove a group from the current blendfile
        
        Parameter:
          group: (Group) Group to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Group()
    def __getitem__(key): return Group()
    def __iter__(key): yield Group()