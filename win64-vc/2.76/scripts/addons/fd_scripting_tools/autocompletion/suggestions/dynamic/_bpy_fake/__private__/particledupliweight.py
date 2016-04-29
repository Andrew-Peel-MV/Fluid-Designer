from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ParticleDupliWeight(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Particle dupliobject name'''
        return str()
    @property
    def count(self):
        '''(Integer) The number of times this object is repeated with respect to
        other objects'''
        return int()