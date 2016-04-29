from . bone import Bone
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ArmatureBones(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Bone) Armature's active bone'''
        return Bone()
    def get(key): return Bone()
    def __getitem__(key): return Bone()
    def __iter__(key): yield Bone()