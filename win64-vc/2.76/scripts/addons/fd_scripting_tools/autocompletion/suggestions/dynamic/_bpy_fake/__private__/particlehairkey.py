from . struct import Struct
from . object import Object
from . particle import Particle
from . particlesystemmodifier import ParticleSystemModifier
from . bpy_struct import bpy_struct
import mathutils

class ParticleHairKey(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def time(self):
        '''(Float) Relative time of key over hair length'''
        return float()
    @property
    def weight(self):
        '''(Float) Weight for cloth simulation'''
        return float()
    @property
    def co(self):
        '''(Vector 3D) Location of the hair key in object space'''
        return mathutils.Vector()
    @property
    def co_local(self):
        '''(Vector 3D) Location of the hair key in its local coordinate system,
        relative to the emitting face'''
        return mathutils.Vector()
    def co_object(self, object, modifier, particle):
        '''Obtain hairkey location with particle and modifier data
        
        Parameter:
          object: (Object) Object
          modifier: (ParticleSystemModifier) Particle modifier
          particle: (Particle) hair particle
        
        Returns:
          co: (Vector 3D) Exported hairkey location'''
        return mathutils.Vector()