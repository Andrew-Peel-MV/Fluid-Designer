from . keyingsetpath import KeyingSetPath
from . id import ID
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class KeyingSetPaths(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(KeyingSetPath) Active Keying Set used to insert/delete keyframes'''
        return KeyingSetPath()
    @property
    def active_index(self):
        '''(Integer) Current Keying Set index'''
        return int()
    def add(self, target_id, data_path, index, group_method, group_name):
        '''Add a new path for the Keying Set
        
        Parameter:
          target_id: (ID) ID-Datablock for the destination
          data_path: (String) RNA-Path to destination property
          index:
            (Integer) The index of the destination property (i.e. axis of
            Location/Rotation/etc.), or -1 for the entire array
          group_method: (Enum) Method used to define which Group-name to use
          group_name:
            (String) Name of Action Group to assign destination to (only if
            grouping mode is to use this name)
        
        Returns:
          ksp: (KeyingSetPath) Path created and added to the Keying Set'''
        return KeyingSetPath()
    def remove(self, path):
        '''Remove the given path from the Keying Set
        
        Parameter:
          path: (KeyingSetPath)'''
        return 
    def clear(self):
        '''Remove all the paths from the Keying Set'''
        return 
    def get(key): return KeyingSetPath()
    def __getitem__(key): return KeyingSetPath()
    def __iter__(key): yield KeyingSetPath()