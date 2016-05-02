from . struct import Struct
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class LodLevel(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def distance(self):
        '''(Float) Distance to begin using this level of detail'''
        return float()
    @property
    def object_hysteresis_percentage(self):
        '''(Integer) Minimum distance change required to transition to the
        previous level of detail'''
        return int()
    @property
    def object(self):
        '''(Object) Object to use for this level of detail'''
        return Object()
    @property
    def use_mesh(self):
        '''(Boolean) Use the mesh from this object at this level of detail'''
        return bool()
    @property
    def use_material(self):
        '''(Boolean) Use the material from this object at this level of detail'''
        return bool()
    @property
    def use_object_hysteresis(self):
        '''(Boolean) Override LoD Hysteresis scene setting for this LoD level'''
        return bool()