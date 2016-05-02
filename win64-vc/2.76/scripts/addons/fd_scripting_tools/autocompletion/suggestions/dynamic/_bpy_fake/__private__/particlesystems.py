from . struct import Struct
from . particlesystem import ParticleSystem
from . bpy_struct import bpy_struct
import mathutils

class ParticleSystems(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(ParticleSystem) Active particle system being displayed'''
        return ParticleSystem()
    @property
    def active_index(self):
        '''(Integer) Index of active particle system slot'''
        return int()
    def get(key): return ParticleSystem()
    def __getitem__(key): return ParticleSystem()
    def __iter__(key): yield ParticleSystem()