from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class RigidBodyObject(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Role of object in Rigid Body Simulations
        
        [ACTIVE, PASSIVE]'''
        return str()
    @property
    def mesh_source(self):
        '''(Enum) Source of the mesh used to create collision shape
        
        [BASE, DEFORM, FINAL]'''
        return str()
    @property
    def enabled(self):
        '''(Boolean) Rigid Body actively participates to the simulation'''
        return bool()
    @property
    def collision_shape(self):
        '''(Enum) Collision Shape of object in Rigid Body Simulations
        
        [BOX, SPHERE, CAPSULE, CYLINDER, CONE, CONVEX_HULL, MESH]'''
        return str()
    @property
    def kinematic(self):
        '''(Boolean) Allow rigid body to be controlled by the animation system'''
        return bool()
    @property
    def use_deform(self):
        '''(Boolean) Rigid body deforms during simulation'''
        return bool()
    @property
    def mass(self):
        '''(Float) How much the object 'weighs' irrespective of gravity'''
        return float()
    @property
    def use_deactivation(self):
        '''(Boolean) Enable deactivation of resting rigid bodies (increases
        performance and stability but can cause glitches)'''
        return bool()
    @property
    def use_start_deactivated(self):
        '''(Boolean) Deactivate rigid body at the start of the simulation'''
        return bool()
    @property
    def deactivate_linear_velocity(self):
        '''(Float) Linear Velocity below which simulation stops simulating object'''
        return float()
    @property
    def deactivate_angular_velocity(self):
        '''(Float) Angular Velocity below which simulation stops simulating
        object'''
        return float()
    @property
    def linear_damping(self):
        '''(Float) Amount of linear velocity that is lost over time'''
        return float()
    @property
    def angular_damping(self):
        '''(Float) Amount of angular velocity that is lost over time'''
        return float()
    @property
    def friction(self):
        '''(Float) Resistance of object to movement'''
        return float()
    @property
    def restitution(self):
        '''(Float) Tendency of object to bounce after colliding with another (0 =
        stays still, 1 = perfectly elastic)'''
        return float()
    @property
    def use_margin(self):
        '''(Boolean) Use custom collision margin (some shapes will have a visible
        gap around them)'''
        return bool()
    @property
    def collision_margin(self):
        '''(Float) Threshold of distance near surface where collisions are still
        considered (best results when non-zero)'''
        return float()
    @property
    def collision_groups(self):
        '''(Boolean[20]) Collision Groups Rigid Body belongs to'''
        return bool()