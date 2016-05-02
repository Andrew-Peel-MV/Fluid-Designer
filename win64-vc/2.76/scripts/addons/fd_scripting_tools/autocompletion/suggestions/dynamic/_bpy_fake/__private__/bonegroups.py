from . bonegroup import BoneGroup
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BoneGroups(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(BoneGroup) Active bone group for this pose'''
        return BoneGroup()
    @property
    def active_index(self):
        '''(Integer) Active index in bone groups array'''
        return int()
    def new(self, name):
        '''Add a new bone group to the object
        
        Parameter:
          name: (String) Name of the new group
        
        Returns:
          group: (BoneGroup) New bone group'''
        return BoneGroup()
    def remove(self, group):
        '''Remove a bone group from this object
        
        Parameter:
          group: (BoneGroup) Removed bone group'''
        return 
    def get(key): return BoneGroup()
    def __getitem__(key): return BoneGroup()
    def __iter__(key): yield BoneGroup()