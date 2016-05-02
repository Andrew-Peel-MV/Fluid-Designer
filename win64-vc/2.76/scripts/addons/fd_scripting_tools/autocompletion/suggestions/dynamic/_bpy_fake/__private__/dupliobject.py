from . struct import Struct
from . object import Object
from . particlesystem import ParticleSystem
from . bpy_struct import bpy_struct
import mathutils

class DupliObject(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def object(self):
        '''(Object) Object being duplicated'''
        return Object()
    @property
    def matrix(self):
        '''(Matrix) Object duplicate transformation matrix'''
        return mathutils.Matrix()
    @property
    def hide(self):
        '''(Boolean) Don't show dupli object in viewport or render'''
        return bool()
    @property
    def index(self):
        '''(Integer) Index in the lowest-level dupli list'''
        return int()
    @property
    def persistent_id(self):
        '''(Integer[8]) Persistent identifier for inter-frame matching of objects
        with motion blur'''
        return int()
    @property
    def particle_system(self):
        '''(ParticleSystem) Particle system that this dupli object was instanced
        from'''
        return ParticleSystem()
    @property
    def orco(self):
        '''(Vector 3D) Generated coordinates in parent object space'''
        return mathutils.Vector()
    @property
    def uv(self):
        '''(Vector 2D) UV coordinates in parent object space'''
        return mathutils.Vector()
    @property
    def type(self):
        '''(Enum) Duplicator type that generated this dupli object
        
        [NONE, FRAMES, VERTS, FACES, GROUP]'''
        return str()