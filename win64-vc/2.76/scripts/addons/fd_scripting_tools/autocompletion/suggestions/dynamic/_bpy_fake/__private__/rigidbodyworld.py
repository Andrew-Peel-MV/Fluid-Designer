from . struct import Struct
from . pointcache import PointCache
from . object import Object
from . group import Group
from . effectorweights import EffectorWeights
from . bpy_struct import bpy_struct
import mathutils

class RigidBodyWorld(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def group(self):
        '''(Group) Group containing objects participating in this simulation'''
        return Group()
    @property
    def constraints(self):
        '''(Group) Group containing rigid body constraint objects'''
        return Group()
    @property
    def enabled(self):
        '''(Boolean) Simulation will be evaluated'''
        return bool()
    @property
    def time_scale(self):
        '''(Float) Change the speed of the simulation'''
        return float()
    @property
    def steps_per_second(self):
        '''(Integer) Number of simulation steps taken per second (higher values
        are more accurate but slower)'''
        return int()
    @property
    def solver_iterations(self):
        '''(Integer) Number of constraint solver iterations made per simulation
        step (higher values are more accurate but slower)'''
        return int()
    @property
    def use_split_impulse(self):
        '''(Boolean) Reduce extra velocity that can build up when objects collide
        (lowers simulation stability a little so use only when necessary)'''
        return bool()
    @property
    def point_cache(self):
        '''(PointCache)'''
        return PointCache()
    @property
    def effector_weights(self):
        '''(EffectorWeights)'''
        return EffectorWeights()
    def convex_sweep_test(self, object, start, end):
        '''Sweep test convex rigidbody against the current rigidbody world
        
        Parameter:
          object: (Object) Rigidbody object with a convex collision shape
          start: (Vector 3D)
          end: (Vector 3D)
        
        Returns:
          object_location: (Vector 3D) The hit location of this sweep test
          hitpoint: (Vector 3D) The hit location of this sweep test
          normal: (Vector 3D) The face normal at the sweep test hit location
          has_hit:
            (Integer) If the function has found collision point, value is 1,
            otherwise 0'''
        return mathutils.Vector(), mathutils.Vector(), mathutils.Vector(), int()