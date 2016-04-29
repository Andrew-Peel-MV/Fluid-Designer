from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Constraint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Constraint name'''
        return str()
    @property
    def type(self):
        '''(Enum)
        
        [CAMERA_SOLVER, FOLLOW_TRACK, OBJECT_SOLVER, COPY_LOCATION,
        COPY_ROTATION, COPY_SCALE, COPY_TRANSFORMS, LIMIT_DISTANCE,
        LIMIT_LOCATION, LIMIT_ROTATION, LIMIT_SCALE, MAINTAIN_VOLUME,
        TRANSFORM, CLAMP_TO, DAMPED_TRACK, IK, LOCKED_TRACK, SPLINE_IK,
        STRETCH_TO, TRACK_TO, ACTION, CHILD_OF, FLOOR, FOLLOW_PATH, PIVOT,
        RIGID_BODY_JOINT, SHRINKWRAP]'''
        return str()
    @property
    def owner_space(self):
        '''(Enum) Space that owner is evaluated in
        
        [WORLD, POSE, LOCAL_WITH_PARENT, LOCAL]'''
        return str()
    @property
    def target_space(self):
        '''(Enum) Space that target is evaluated in
        
        [WORLD, POSE, LOCAL_WITH_PARENT, LOCAL]'''
        return str()
    @property
    def mute(self):
        '''(Boolean) Enable/Disable Constraint'''
        return bool()
    @property
    def show_expanded(self):
        '''(Boolean) Constraint's panel is expanded in UI'''
        return bool()
    @property
    def is_valid(self):
        '''(Boolean) Constraint has valid settings and can be evaluated'''
        return bool()
    @property
    def active(self):
        '''(Boolean) Constraint is the one being edited'''
        return bool()
    @property
    def is_proxy_local(self):
        '''(Boolean) Constraint was added in this proxy instance (i.e. did not
        belong to source Armature)'''
        return bool()
    @property
    def influence(self):
        '''(Float) Amount of influence constraint will have on the final solution'''
        return float()
    @property
    def error_location(self):
        '''(Float) Amount of residual error in Blender space unit for constraints
        that work on position'''
        return float()
    @property
    def error_rotation(self):
        '''(Float) Amount of residual error in radians for constraints that work
        on orientation'''
        return float()