from . boidstate import BoidState
from . struct import Struct
from . boidrule import BoidRule
from . bpy_struct import bpy_struct
import mathutils

class BoidSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def land_smooth(self):
        '''(Float) How smoothly the boids land'''
        return float()
    @property
    def bank(self):
        '''(Float) Amount of rotation around velocity vector on turns'''
        return float()
    @property
    def pitch(self):
        '''(Float) Amount of rotation around side vector'''
        return float()
    @property
    def height(self):
        '''(Float) Boid height relative to particle size'''
        return float()
    @property
    def states(self):
        '''(Sequence of BoidState)'''
        return (BoidState(),)
    @property
    def active_boid_state(self):
        '''(BoidRule)'''
        return BoidRule()
    @property
    def active_boid_state_index(self):
        '''(Integer)'''
        return int()
    @property
    def health(self):
        '''(Float) Initial boid health when born'''
        return float()
    @property
    def strength(self):
        '''(Float) Maximum caused damage on attack per second'''
        return float()
    @property
    def aggression(self):
        '''(Float) Boid will fight this times stronger enemy'''
        return float()
    @property
    def accuracy(self):
        '''(Float) Accuracy of attack'''
        return float()
    @property
    def range(self):
        '''(Float) Maximum distance from which a boid can attack'''
        return float()
    @property
    def air_speed_min(self):
        '''(Float) Minimum speed in air (relative to maximum speed)'''
        return float()
    @property
    def air_speed_max(self):
        '''(Float) Maximum speed in air'''
        return float()
    @property
    def air_acc_max(self):
        '''(Float) Maximum acceleration in air (relative to maximum speed)'''
        return float()
    @property
    def air_ave_max(self):
        '''(Float) Maximum angular velocity in air (relative to 180 degrees)'''
        return float()
    @property
    def air_personal_space(self):
        '''(Float) Radius of boids personal space in air (% of particle size)'''
        return float()
    @property
    def land_jump_speed(self):
        '''(Float) Maximum speed for jumping'''
        return float()
    @property
    def land_speed_max(self):
        '''(Float) Maximum speed on land'''
        return float()
    @property
    def land_acc_max(self):
        '''(Float) Maximum acceleration on land (relative to maximum speed)'''
        return float()
    @property
    def land_ave_max(self):
        '''(Float) Maximum angular velocity on land (relative to 180 degrees)'''
        return float()
    @property
    def land_personal_space(self):
        '''(Float) Radius of boids personal space on land (% of particle size)'''
        return float()
    @property
    def land_stick_force(self):
        '''(Float) How strong a force must be to start effecting a boid on land'''
        return float()
    @property
    def use_flight(self):
        '''(Boolean) Allow boids to move in air'''
        return bool()
    @property
    def use_land(self):
        '''(Boolean) Allow boids to move on land'''
        return bool()
    @property
    def use_climb(self):
        '''(Boolean) Allow boids to climb goal objects'''
        return bool()