from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GameSoftBodySettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def linear_stiffness(self):
        '''(Float) Linear stiffness of the soft body links'''
        return float()
    @property
    def dynamic_friction(self):
        '''(Float) Dynamic Friction'''
        return float()
    @property
    def shape_threshold(self):
        '''(Float) Shape matching threshold'''
        return float()
    @property
    def collision_margin(self):
        '''(Float) Collision margin for soft body. Small value makes the
        algorithm unstable'''
        return float()
    @property
    def weld_threshold(self):
        '''(Float) Welding threshold: distance between nearby vertices to be
        considered equal => set to 0.0 to disable welding test and speed up
        scene loading (ok if the mesh has no duplicates)'''
        return float()
    @property
    def location_iterations(self):
        '''(Integer) Position solver iterations'''
        return int()
    @property
    def cluster_iterations(self):
        '''(Integer) Number of cluster iterations'''
        return int()
    @property
    def use_shape_match(self):
        '''(Boolean) Enable soft body shape matching goal'''
        return bool()
    @property
    def use_bending_constraints(self):
        '''(Boolean) Enable bending constraints'''
        return bool()
    @property
    def use_cluster_rigid_to_softbody(self):
        '''(Boolean) Enable cluster collision between soft and rigid body'''
        return bool()
    @property
    def use_cluster_soft_to_softbody(self):
        '''(Boolean) Enable cluster collision between soft and soft body'''
        return bool()