from . struct import Struct
from . armature import Armature
from . bpy_struct import bpy_struct
import mathutils

class BlendDataArmatures(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new armature to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          armature: (Armature) New armature datablock'''
        return Armature()
    def remove(self, armature):
        '''Remove a armature from the current blendfile
        
        Parameter:
          armature: (Armature) Armature to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Armature()
    def __getitem__(key): return Armature()
    def __iter__(key): yield Armature()