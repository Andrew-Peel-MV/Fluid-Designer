from . struct import Struct
from . effectorweights import EffectorWeights
from . shapekey import ShapeKey
from . bpy_struct import bpy_struct
import mathutils

class ClothSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def goal_min(self):
        '''(Float) Goal minimum, vertex group weights are scaled to match this
        range'''
        return float()
    @property
    def goal_max(self):
        '''(Float) Goal maximum, vertex group weights are scaled to match this
        range'''
        return float()
    @property
    def goal_default(self):
        '''(Float) Default Goal (vertex target position) value, when no Vertex
        Group used'''
        return float()
    @property
    def goal_spring(self):
        '''(Float) Goal (vertex target position) spring stiffness'''
        return float()
    @property
    def goal_friction(self):
        '''(Float) Goal (vertex target position) friction'''
        return float()
    @property
    def internal_friction(self):
        '''(Float)'''
        return float()
    @property
    def collider_friction(self):
        '''(Float)'''
        return float()
    @property
    def density_target(self):
        '''(Float) Maximum density of hair'''
        return float()
    @property
    def density_strength(self):
        '''(Float) Influence of target density on the simulation'''
        return float()
    @property
    def mass(self):
        '''(Float) Mass of cloth material'''
        return float()
    @property
    def vertex_group_mass(self):
        '''(String) Vertex Group for pinning of vertices'''
        return str()
    @property
    def gravity(self):
        '''(Vector 3D) Gravity or external force vector'''
        return mathutils.Vector()
    @property
    def air_damping(self):
        '''(Float) Air has normally some thickness which slows falling things
        down'''
        return float()
    @property
    def vel_damping(self):
        '''(Float) Damp velocity to help cloth reach the resting position faster
        (1.0 = no damping, 0.0 = fully dampened)'''
        return float()
    @property
    def use_pin_cloth(self):
        '''(Boolean) Enable pinning of cloth vertices to other objects/positions'''
        return bool()
    @property
    def pin_stiffness(self):
        '''(Float) Pin (vertex target position) spring stiffness'''
        return float()
    @property
    def quality(self):
        '''(Integer) Quality of the simulation in steps per frame (higher is
        better quality but slower)'''
        return int()
    @property
    def vertex_group_shrink(self):
        '''(String) Vertex Group for shrinking cloth'''
        return str()
    @property
    def shrink_min(self):
        '''(Float) Min amount to shrink cloth by'''
        return float()
    @property
    def shrink_max(self):
        '''(Float) Max amount to shrink cloth by'''
        return float()
    @property
    def voxel_cell_size(self):
        '''(Float) Size of the voxel grid cells for interaction effects'''
        return float()
    @property
    def use_stiffness_scale(self):
        '''(Boolean) If enabled, stiffness can be scaled along a weight painted
        vertex group'''
        return bool()
    @property
    def spring_damping(self):
        '''(Float) Damping of cloth velocity (higher = more smooth, less
        jiggling)'''
        return float()
    @property
    def structural_stiffness(self):
        '''(Float) Overall stiffness of structure'''
        return float()
    @property
    def structural_stiffness_max(self):
        '''(Float) Maximum structural stiffness value'''
        return float()
    @property
    def sewing_force_max(self):
        '''(Float) Maximum sewing force'''
        return float()
    @property
    def vertex_group_structural_stiffness(self):
        '''(String) Vertex group for fine control over structural stiffness'''
        return str()
    @property
    def bending_stiffness(self):
        '''(Float) Wrinkle coefficient (higher = less smaller but more big
        wrinkles)'''
        return float()
    @property
    def bending_stiffness_max(self):
        '''(Float) Maximum bending stiffness value'''
        return float()
    @property
    def bending_damping(self):
        '''(Float) Damping of bending motion'''
        return float()
    @property
    def use_sewing_springs(self):
        '''(Boolean) Pulls loose edges together'''
        return bool()
    @property
    def vertex_group_bending(self):
        '''(String) Vertex group for fine control over bending stiffness'''
        return str()
    @property
    def effector_weights(self):
        '''(EffectorWeights)'''
        return EffectorWeights()
    @property
    def rest_shape_key(self):
        '''(ShapeKey) Shape key to use the rest spring lengths from'''
        return ShapeKey()