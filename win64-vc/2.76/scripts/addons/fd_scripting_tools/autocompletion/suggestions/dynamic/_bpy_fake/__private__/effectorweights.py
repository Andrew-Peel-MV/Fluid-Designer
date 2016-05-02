from . struct import Struct
from . group import Group
from . bpy_struct import bpy_struct
import mathutils

class EffectorWeights(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def apply_to_hair_growing(self):
        '''(Boolean) Use force fields when growing hair'''
        return bool()
    @property
    def group(self):
        '''(Group) Limit effectors to this Group'''
        return Group()
    @property
    def gravity(self):
        '''(Float) Global gravity weight'''
        return float()
    @property
    def all(self):
        '''(Float) All effector's weight'''
        return float()
    @property
    def force(self):
        '''(Float) Force effector weight'''
        return float()
    @property
    def vortex(self):
        '''(Float) Vortex effector weight'''
        return float()
    @property
    def magnetic(self):
        '''(Float) Magnetic effector weight'''
        return float()
    @property
    def wind(self):
        '''(Float) Wind effector weight'''
        return float()
    @property
    def curve_guide(self):
        '''(Float) Curve guide effector weight'''
        return float()
    @property
    def texture(self):
        '''(Float) Texture effector weight'''
        return float()
    @property
    def harmonic(self):
        '''(Float) Harmonic effector weight'''
        return float()
    @property
    def charge(self):
        '''(Float) Charge effector weight'''
        return float()
    @property
    def lennardjones(self):
        '''(Float) Lennard-Jones effector weight'''
        return float()
    @property
    def boid(self):
        '''(Float) Boid effector weight'''
        return float()
    @property
    def turbulence(self):
        '''(Float) Turbulence effector weight'''
        return float()
    @property
    def drag(self):
        '''(Float) Drag effector weight'''
        return float()
    @property
    def smokeflow(self):
        '''(Float) Smoke Flow effector weight'''
        return float()