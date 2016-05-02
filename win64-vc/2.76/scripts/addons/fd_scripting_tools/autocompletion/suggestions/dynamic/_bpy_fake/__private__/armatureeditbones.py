from . struct import Struct
from . editbone import EditBone
from . bpy_struct import bpy_struct
import mathutils

class ArmatureEditBones(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(EditBone) Armatures active edit bone'''
        return EditBone()
    def new(self, name):
        '''Add a new bone
        
        Parameter:
          name: (String) New name for the bone
        
        Returns:
          bone: (EditBone) Newly created edit bone'''
        return EditBone()
    def remove(self, bone):
        '''Remove an existing bone from the armature
        
        Parameter:
          bone: (EditBone) EditBone to remove'''
        return 
    def get(key): return EditBone()
    def __getitem__(key): return EditBone()
    def __iter__(key): yield EditBone()