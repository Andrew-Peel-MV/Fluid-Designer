from . struct import Struct
from . group import Group
from . bpy_struct import bpy_struct
import mathutils

class ClothCollisionSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_collision(self):
        '''(Boolean) Enable collisions with other objects'''
        return bool()
    @property
    def repel_force(self):
        '''(Float) Repulsion force to apply on cloth when close to colliding'''
        return float()
    @property
    def distance_repel(self):
        '''(Float) Maximum distance to apply repulsion force, must be greater
        than minimum distance'''
        return float()
    @property
    def distance_min(self):
        '''(Float) Minimum distance between collision objects before collision
        response takes in'''
        return float()
    @property
    def friction(self):
        '''(Float) Friction force if a collision happened (higher = less
        movement)'''
        return float()
    @property
    def damping(self):
        '''(Float) Amount of velocity lost on collision'''
        return float()
    @property
    def collision_quality(self):
        '''(Integer) How many collision iterations should be done. (higher is
        better quality but slower)'''
        return int()
    @property
    def use_self_collision(self):
        '''(Boolean) Enable self collisions'''
        return bool()
    @property
    def self_distance_min(self):
        '''(Float) 0.5 means no distance at all, 1.0 is maximum distance'''
        return float()
    @property
    def self_friction(self):
        '''(Float) Friction/damping with self contact'''
        return float()
    @property
    def self_collision_quality(self):
        '''(Integer) How many self collision iterations should be done (higher is
        better quality but slower)'''
        return int()
    @property
    def group(self):
        '''(Group) Limit colliders to this Group'''
        return Group()
    @property
    def vertex_group_self_collisions(self):
        '''(String) Vertex group to define vertices which are not used during
        self collisions'''
        return str()