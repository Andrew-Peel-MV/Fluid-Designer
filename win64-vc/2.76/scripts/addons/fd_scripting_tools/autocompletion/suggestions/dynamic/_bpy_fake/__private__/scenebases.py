from . objectbase import ObjectBase
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SceneBases(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(ObjectBase) Active object base in the scene'''
        return ObjectBase()
    def get(key): return ObjectBase()
    def __getitem__(key): return ObjectBase()
    def __iter__(key): yield ObjectBase()