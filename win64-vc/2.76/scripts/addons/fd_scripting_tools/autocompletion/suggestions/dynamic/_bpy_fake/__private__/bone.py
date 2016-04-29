from . bone import Bone
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Bone(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def parent(self):
        '''(Bone) Parent bone (in same Armature)'''
        return Bone()
    @property
    def children(self):
        '''(Sequence of Bone) Bones which are children of this bone'''
        return (Bone(),)
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def layers(self):
        '''(Boolean[32]) Layers bone exists in'''
        return bool()
    @property
    def use_connect(self):
        '''(Boolean) When bone has a parent, bone's head is stuck to the parent's
        tail'''
        return bool()
    @property
    def use_inherit_rotation(self):
        '''(Boolean) Bone inherits rotation or scale from parent bone'''
        return bool()
    @property
    def use_envelope_multiply(self):
        '''(Boolean) When deforming bone, multiply effects of Vertex Group
        weights with Envelope influence'''
        return bool()
    @property
    def use_deform(self):
        '''(Boolean) Enable Bone to deform geometry'''
        return bool()
    @property
    def use_inherit_scale(self):
        '''(Boolean) Bone inherits scaling from parent bone'''
        return bool()
    @property
    def use_local_location(self):
        '''(Boolean) Bone location is set in local space'''
        return bool()
    @property
    def use_relative_parent(self):
        '''(Boolean) Object children will use relative transform, like deform'''
        return bool()
    @property
    def show_wire(self):
        '''(Boolean) Bone is always drawn as Wireframe regardless of viewport
        draw mode (useful for non-obstructive custom bone shapes)'''
        return bool()
    @property
    def use_cyclic_offset(self):
        '''(Boolean) When bone doesn't have a parent, it receives cyclic offset
        effects (Deprecated)'''
        return bool()
    @property
    def hide_select(self):
        '''(Boolean) Bone is able to be selected'''
        return bool()
    @property
    def envelope_distance(self):
        '''(Float) Bone deformation distance (for Envelope deform only)'''
        return float()
    @property
    def envelope_weight(self):
        '''(Float) Bone deformation weight (for Envelope deform only)'''
        return float()
    @property
    def head_radius(self):
        '''(Float) Radius of head of bone (for Envelope deform only)'''
        return float()
    @property
    def tail_radius(self):
        '''(Float) Radius of tail of bone (for Envelope deform only)'''
        return float()
    @property
    def bbone_segments(self):
        '''(Integer) Number of subdivisions of bone (for B-Bones only)'''
        return int()
    @property
    def bbone_in(self):
        '''(Float) Length of first Bezier Handle (for B-Bones only)'''
        return float()
    @property
    def bbone_out(self):
        '''(Float) Length of second Bezier Handle (for B-Bones only)'''
        return float()
    @property
    def bbone_x(self):
        '''(Float) B-Bone X size'''
        return float()
    @property
    def bbone_z(self):
        '''(Float) B-Bone Z size'''
        return float()
    @property
    def hide(self):
        '''(Boolean) Bone is not visible when it is not in Edit Mode (i.e. in
        Object or Pose Modes)'''
        return bool()
    @property
    def select(self):
        '''(Boolean)'''
        return bool()
    @property
    def select_head(self):
        '''(Boolean)'''
        return bool()
    @property
    def select_tail(self):
        '''(Boolean)'''
        return bool()
    @property
    def matrix(self):
        '''(Float[9]) 3x3 bone matrix'''
        return ''
    @property
    def matrix_local(self):
        '''(Matrix) 4x4 bone matrix relative to armature'''
        return mathutils.Matrix()
    @property
    def tail(self):
        '''(Vector 3D) Location of tail end of the bone'''
        return mathutils.Vector()
    @property
    def tail_local(self):
        '''(Vector 3D) Location of tail end of the bone relative to armature'''
        return mathutils.Vector()
    @property
    def head(self):
        '''(Vector 3D) Location of head end of the bone relative to its parent'''
        return mathutils.Vector()
    @property
    def head_local(self):
        '''(Vector 3D) Location of head end of the bone relative to armature'''
        return mathutils.Vector()
    def evaluate_envelope(self, point):
        '''Calculate bone envelope at given point
        
        Parameter:
          point: (Vector 3D) Position in 3d space to evaluate
        
        Returns:
          factor: (Float) Envelope factor'''
        return float()