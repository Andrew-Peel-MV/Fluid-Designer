from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ParticleKey(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def location(self):
        '''(Vector 3D) Key location'''
        return mathutils.Vector()
    @property
    def velocity(self):
        '''(Vector 3D) Key velocity'''
        return mathutils.Vector()
    @property
    def rotation(self):
        '''(Float[4]) Key rotation quaternion'''
        return ''
    @property
    def angular_velocity(self):
        '''(Vector 3D) Key angular velocity'''
        return mathutils.Vector()
    @property
    def time(self):
        '''(Float) Time of key over the simulation'''
        return float()