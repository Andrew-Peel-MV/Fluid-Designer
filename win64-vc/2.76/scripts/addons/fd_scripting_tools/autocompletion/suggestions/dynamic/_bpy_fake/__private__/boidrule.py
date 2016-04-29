from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BoidRule(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Boid rule name'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [GOAL, AVOID, AVOID_COLLISION, SEPARATE, FLOCK, FOLLOW_LEADER,
        AVERAGE_SPEED, FIGHT]'''
        return str()
    @property
    def use_in_air(self):
        '''(Boolean) Use rule when boid is flying'''
        return bool()
    @property
    def use_on_land(self):
        '''(Boolean) Use rule when boid is on land'''
        return bool()