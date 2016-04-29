from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialPhysics(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def friction(self):
        '''(Float) Coulomb friction coefficient, when inside the physics distance
        area'''
        return float()
    @property
    def elasticity(self):
        '''(Float) Elasticity of collisions'''
        return float()
    @property
    def use_fh_normal(self):
        '''(Boolean) Align dynamic game objects along the surface normal, when
        inside the physics distance area'''
        return bool()
    @property
    def fh_force(self):
        '''(Float) Upward spring force, when inside the physics distance area'''
        return float()
    @property
    def fh_distance(self):
        '''(Float) Distance of the physics area'''
        return float()
    @property
    def fh_damping(self):
        '''(Float) Damping of the spring force, when inside the physics distance
        area'''
        return float()