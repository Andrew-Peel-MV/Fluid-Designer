from . struct import Struct
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class ParticleTarget(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Particle target name'''
        return str()
    @property
    def object(self):
        '''(Object) The object that has the target particle system (empty if same
        object)'''
        return Object()
    @property
    def system(self):
        '''(Integer) The index of particle system on the target object'''
        return int()
    @property
    def time(self):
        '''(Float)'''
        return float()
    @property
    def duration(self):
        '''(Float)'''
        return float()
    @property
    def is_valid(self):
        '''(Boolean) Keyed particles target is valid'''
        return bool()
    @property
    def alliance(self):
        '''(Enum)
        
        [FRIEND, NEUTRAL, ENEMY]'''
        return str()