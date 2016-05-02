from . particlekey import ParticleKey
from . struct import Struct
from . particlehairkey import ParticleHairKey
from . particlesystemmodifier import ParticleSystemModifier
from . bpy_struct import bpy_struct
import mathutils

class Particle(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def location(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def velocity(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def angular_velocity(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def rotation(self):
        '''(Float[4])'''
        return ''
    @property
    def prev_location(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def prev_velocity(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def prev_angular_velocity(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def prev_rotation(self):
        '''(Float[4])'''
        return ''
    @property
    def hair_keys(self):
        '''(Sequence of ParticleHairKey)'''
        return (ParticleHairKey(),)
    @property
    def particle_keys(self):
        '''(Sequence of ParticleKey)'''
        return (ParticleKey(),)
    @property
    def birth_time(self):
        '''(Float)'''
        return float()
    @property
    def lifetime(self):
        '''(Float)'''
        return float()
    @property
    def die_time(self):
        '''(Float)'''
        return float()
    @property
    def size(self):
        '''(Float)'''
        return float()
    @property
    def is_exist(self):
        '''(Boolean)'''
        return bool()
    @property
    def is_visible(self):
        '''(Boolean)'''
        return bool()
    @property
    def alive_state(self):
        '''(Enum)
        
        [DEAD, UNBORN, ALIVE, DYING]'''
        return str()
    def uv_on_emitter(self, modifier):
        '''Obtain uv for particle on derived mesh
        
        Parameter:
          modifier: (ParticleSystemModifier) Particle modifier
        
        Returns:
          uv: (Vector 2D)'''
        return mathutils.Vector()