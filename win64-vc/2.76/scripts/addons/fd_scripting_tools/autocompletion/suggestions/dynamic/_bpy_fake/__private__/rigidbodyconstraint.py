from . struct import Struct
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class RigidBodyConstraint(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Type of Rigid Body Constraint
        
        [FIXED, POINT, HINGE, SLIDER, PISTON, GENERIC, GENERIC_SPRING, MOTOR]'''
        return str()
    @property
    def enabled(self):
        '''(Boolean) Enable this constraint'''
        return bool()
    @property
    def disable_collisions(self):
        '''(Boolean) Disable collisions between constrained rigid bodies'''
        return bool()
    @property
    def object1(self):
        '''(Object) First Rigid Body Object to be constrained'''
        return Object()
    @property
    def object2(self):
        '''(Object) Second Rigid Body Object to be constrained'''
        return Object()
    @property
    def use_breaking(self):
        '''(Boolean) Constraint can be broken if it receives an impulse above the
        threshold'''
        return bool()
    @property
    def breaking_threshold(self):
        '''(Float) Impulse threshold that must be reached for the constraint to
        break'''
        return float()
    @property
    def use_override_solver_iterations(self):
        '''(Boolean) Override the number of solver iterations for this constraint'''
        return bool()
    @property
    def solver_iterations(self):
        '''(Integer) Number of constraint solver iterations made per simulation
        step (higher values are more accurate but slower)'''
        return int()
    @property
    def use_limit_lin_x(self):
        '''(Boolean) Limit translation on X axis'''
        return bool()
    @property
    def use_limit_lin_y(self):
        '''(Boolean) Limit translation on Y axis'''
        return bool()
    @property
    def use_limit_lin_z(self):
        '''(Boolean) Limit translation on Z axis'''
        return bool()
    @property
    def use_limit_ang_x(self):
        '''(Boolean) Limit rotation around X axis'''
        return bool()
    @property
    def use_limit_ang_y(self):
        '''(Boolean) Limit rotation around Y axis'''
        return bool()
    @property
    def use_limit_ang_z(self):
        '''(Boolean) Limit rotation around Z axis'''
        return bool()
    @property
    def use_spring_x(self):
        '''(Boolean) Enable spring on X axis'''
        return bool()
    @property
    def use_spring_y(self):
        '''(Boolean) Enable spring on Y axis'''
        return bool()
    @property
    def use_spring_z(self):
        '''(Boolean) Enable spring on Z axis'''
        return bool()
    @property
    def use_motor_lin(self):
        '''(Boolean) Enable linear motor'''
        return bool()
    @property
    def use_motor_ang(self):
        '''(Boolean) Enable angular motor'''
        return bool()
    @property
    def limit_lin_x_lower(self):
        '''(Float) Lower limit of X axis translation'''
        return float()
    @property
    def limit_lin_x_upper(self):
        '''(Float) Upper limit of X axis translation'''
        return float()
    @property
    def limit_lin_y_lower(self):
        '''(Float) Lower limit of Y axis translation'''
        return float()
    @property
    def limit_lin_y_upper(self):
        '''(Float) Upper limit of Y axis translation'''
        return float()
    @property
    def limit_lin_z_lower(self):
        '''(Float) Lower limit of Z axis translation'''
        return float()
    @property
    def limit_lin_z_upper(self):
        '''(Float) Upper limit of Z axis translation'''
        return float()
    @property
    def limit_ang_x_lower(self):
        '''(Float) Lower limit of X axis rotation'''
        return float()
    @property
    def limit_ang_x_upper(self):
        '''(Float) Upper limit of X axis rotation'''
        return float()
    @property
    def limit_ang_y_lower(self):
        '''(Float) Lower limit of Y axis rotation'''
        return float()
    @property
    def limit_ang_y_upper(self):
        '''(Float) Upper limit of Y axis rotation'''
        return float()
    @property
    def limit_ang_z_lower(self):
        '''(Float) Lower limit of Z axis rotation'''
        return float()
    @property
    def limit_ang_z_upper(self):
        '''(Float) Upper limit of Z axis rotation'''
        return float()
    @property
    def spring_stiffness_x(self):
        '''(Float) Stiffness on the X axis'''
        return float()
    @property
    def spring_stiffness_y(self):
        '''(Float) Stiffness on the Y axis'''
        return float()
    @property
    def spring_stiffness_z(self):
        '''(Float) Stiffness on the Z axis'''
        return float()
    @property
    def spring_damping_x(self):
        '''(Float) Damping on the X axis'''
        return float()
    @property
    def spring_damping_y(self):
        '''(Float) Damping on the Y axis'''
        return float()
    @property
    def spring_damping_z(self):
        '''(Float) Damping on the Z axis'''
        return float()
    @property
    def motor_lin_target_velocity(self):
        '''(Float) Target linear motor velocity'''
        return float()
    @property
    def motor_lin_max_impulse(self):
        '''(Float) Maximum linear motor impulse'''
        return float()
    @property
    def motor_ang_target_velocity(self):
        '''(Float) Target angular motor velocity'''
        return float()
    @property
    def motor_ang_max_impulse(self):
        '''(Float) Maximum angular motor impulse'''
        return float()