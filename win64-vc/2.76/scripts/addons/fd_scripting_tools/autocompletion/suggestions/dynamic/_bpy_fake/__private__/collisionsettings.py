from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CollisionSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use(self):
        '''(Boolean) Enable this objects as a collider for physics systems'''
        return bool()
    @property
    def damping_factor(self):
        '''(Float) Amount of damping during particle collision'''
        return float()
    @property
    def damping_random(self):
        '''(Float) Random variation of damping'''
        return float()
    @property
    def friction_factor(self):
        '''(Float) Amount of friction during particle collision'''
        return float()
    @property
    def friction_random(self):
        '''(Float) Random variation of friction'''
        return float()
    @property
    def permeability(self):
        '''(Float) Chance that the particle will pass through the mesh'''
        return float()
    @property
    def use_particle_kill(self):
        '''(Boolean) Kill collided particles'''
        return bool()
    @property
    def stickiness(self):
        '''(Float) Amount of stickiness to surface collision'''
        return float()
    @property
    def thickness_inner(self):
        '''(Float) Inner face thickness (only used by softbodies)'''
        return float()
    @property
    def thickness_outer(self):
        '''(Float) Outer face thickness'''
        return float()
    @property
    def damping(self):
        '''(Float) Amount of damping during collision'''
        return float()
    @property
    def absorption(self):
        '''(Float) How much of effector force gets lost during collision with
        this object (in percent)'''
        return float()