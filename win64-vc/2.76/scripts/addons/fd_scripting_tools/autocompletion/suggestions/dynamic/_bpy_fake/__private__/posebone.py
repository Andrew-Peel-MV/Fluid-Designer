from . bone import Bone
from . bonegroup import BoneGroup
from . struct import Struct
from . posebone import PoseBone
from . poseboneconstraints import PoseBoneConstraints
from . motionpath import MotionPath
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class PoseBone(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def constraints(self):
        '''(Sequence of Constraint) Constraints that act on this PoseChannel'''
        return PoseBoneConstraints()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def motion_path(self):
        '''(MotionPath) Motion Path for this element'''
        return MotionPath()
    @property
    def bone(self):
        '''(Bone) Bone associated with this PoseBone'''
        return Bone()
    @property
    def parent(self):
        '''(PoseBone) Parent of this pose bone'''
        return PoseBone()
    @property
    def child(self):
        '''(PoseBone) Child of this pose bone'''
        return PoseBone()
    @property
    def location(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def scale(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def rotation_quaternion(self):
        '''(Float[4]) Rotation in Quaternions'''
        return ''
    @property
    def rotation_axis_angle(self):
        '''(Float[4]) Angle of Rotation for Axis-Angle rotation representation'''
        return ''
    @property
    def rotation_euler(self):
        '''(Vector 3D) Rotation in Eulers'''
        return mathutils.Vector()
    @property
    def rotation_mode(self):
        '''(Enum)
        
        [QUATERNION, XYZ, XZY, YXZ, YZX, ZXY, ZYX, AXIS_ANGLE]'''
        return str()
    @property
    def matrix_channel(self):
        '''(Matrix) 4x4 matrix, before constraints'''
        return mathutils.Matrix()
    @property
    def matrix_basis(self):
        '''(Matrix) Alternative access to location/scale/rotation relative to the
        parent and own rest bone'''
        return mathutils.Matrix()
    @property
    def matrix(self):
        '''(Matrix) Final 4x4 matrix after constraints and drivers are applied
        (object space)'''
        return mathutils.Matrix()
    @property
    def head(self):
        '''(Vector 3D) Location of head of the channel's bone'''
        return mathutils.Vector()
    @property
    def tail(self):
        '''(Vector 3D) Location of tail of the channel's bone'''
        return mathutils.Vector()
    @property
    def is_in_ik_chain(self):
        '''(Boolean) Is part of an IK chain'''
        return bool()
    @property
    def lock_ik_x(self):
        '''(Boolean) Disallow movement around the X axis'''
        return bool()
    @property
    def lock_ik_y(self):
        '''(Boolean) Disallow movement around the Y axis'''
        return bool()
    @property
    def lock_ik_z(self):
        '''(Boolean) Disallow movement around the Z axis'''
        return bool()
    @property
    def use_ik_limit_x(self):
        '''(Boolean) Limit movement around the X axis'''
        return bool()
    @property
    def use_ik_limit_y(self):
        '''(Boolean) Limit movement around the Y axis'''
        return bool()
    @property
    def use_ik_limit_z(self):
        '''(Boolean) Limit movement around the Z axis'''
        return bool()
    @property
    def use_ik_rotation_control(self):
        '''(Boolean) Apply channel rotation as IK constraint'''
        return bool()
    @property
    def use_ik_linear_control(self):
        '''(Boolean) Apply channel size as IK constraint if stretching is enabled'''
        return bool()
    @property
    def ik_min_x(self):
        '''(Float) Minimum angles for IK Limit'''
        return float()
    @property
    def ik_max_x(self):
        '''(Float) Maximum angles for IK Limit'''
        return float()
    @property
    def ik_min_y(self):
        '''(Float) Minimum angles for IK Limit'''
        return float()
    @property
    def ik_max_y(self):
        '''(Float) Maximum angles for IK Limit'''
        return float()
    @property
    def ik_min_z(self):
        '''(Float) Minimum angles for IK Limit'''
        return float()
    @property
    def ik_max_z(self):
        '''(Float) Maximum angles for IK Limit'''
        return float()
    @property
    def ik_stiffness_x(self):
        '''(Float) IK stiffness around the X axis'''
        return float()
    @property
    def ik_stiffness_y(self):
        '''(Float) IK stiffness around the Y axis'''
        return float()
    @property
    def ik_stiffness_z(self):
        '''(Float) IK stiffness around the Z axis'''
        return float()
    @property
    def ik_stretch(self):
        '''(Float) Allow scaling of the bone for IK'''
        return float()
    @property
    def ik_rotation_weight(self):
        '''(Float) Weight of rotation constraint for IK'''
        return float()
    @property
    def ik_linear_weight(self):
        '''(Float) Weight of scale constraint for IK'''
        return float()
    @property
    def custom_shape(self):
        '''(Object) Object that defines custom draw type for this bone'''
        return Object()
    @property
    def custom_shape_transform(self):
        '''(PoseBone) Bone that defines the display transform of this custom
        shape'''
        return PoseBone()
    @property
    def bone_group_index(self):
        '''(Integer) Bone Group this pose channel belongs to (0=no group)'''
        return int()
    @property
    def bone_group(self):
        '''(BoneGroup) Bone Group this pose channel belongs to'''
        return BoneGroup()
    @property
    def lock_location(self):
        '''(Boolean[3]) Lock editing of location in the interface'''
        return bool()
    @property
    def lock_rotation(self):
        '''(Boolean[3]) Lock editing of rotation in the interface'''
        return bool()
    @property
    def lock_rotation_w(self):
        '''(Boolean) Lock editing of 'angle' component of four-component
        rotations in the interface'''
        return bool()
    @property
    def lock_rotations_4d(self):
        '''(Boolean) Lock editing of four component rotations by components
        (instead of as Eulers)'''
        return bool()
    @property
    def lock_scale(self):
        '''(Boolean[3]) Lock editing of scale in the interface'''
        return bool()
    def evaluate_envelope(self, point):
        '''Calculate bone envelope at given point
        
        Parameter:
          point: (Vector 3D) Position in 3d space to evaluate
        
        Returns:
          factor: (Float) Envelope factor'''
        return float()