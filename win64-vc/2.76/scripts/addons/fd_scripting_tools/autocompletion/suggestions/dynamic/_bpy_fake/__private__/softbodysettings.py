from . struct import Struct
from . effectorweights import EffectorWeights
from . bpy_struct import bpy_struct
import mathutils

class SoftBodySettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def friction(self):
        '''(Float) General media friction for point movements'''
        return float()
    @property
    def mass(self):
        '''(Float) General Mass value'''
        return float()
    @property
    def vertex_group_mass(self):
        '''(String) Control point mass values'''
        return str()
    @property
    def gravity(self):
        '''(Float) Apply gravitation to point movement'''
        return float()
    @property
    def speed(self):
        '''(Float) Tweak timing for physics to control frequency and speed'''
        return float()
    @property
    def vertex_group_goal(self):
        '''(String) Control point weight values'''
        return str()
    @property
    def goal_min(self):
        '''(Float) Goal minimum, vertex weights are scaled to match this range'''
        return float()
    @property
    def goal_max(self):
        '''(Float) Goal maximum, vertex weights are scaled to match this range'''
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
    def pull(self):
        '''(Float) Edge spring stiffness when longer than rest length'''
        return float()
    @property
    def push(self):
        '''(Float) Edge spring stiffness when shorter than rest length'''
        return float()
    @property
    def damping(self):
        '''(Float) Edge spring friction'''
        return float()
    @property
    def spring_length(self):
        '''(Integer) Alter spring length to shrink/blow up (unit %) 0 to disable'''
        return int()
    @property
    def aero(self):
        '''(Integer) Make edges 'sail''''
        return int()
    @property
    def plastic(self):
        '''(Integer) Permanent deform'''
        return int()
    @property
    def bend(self):
        '''(Float) Bending Stiffness'''
        return float()
    @property
    def shear(self):
        '''(Float) Shear Stiffness'''
        return float()
    @property
    def vertex_group_spring(self):
        '''(String) Control point spring strength values'''
        return str()
    @property
    def collision_type(self):
        '''(Enum) Choose Collision Type
        
        [MANUAL, AVERAGE, MINIMAL, MAXIMAL, MINMAX]'''
        return str()
    @property
    def ball_size(self):
        '''(Float) Absolute ball size or factor if not manually adjusted'''
        return float()
    @property
    def ball_stiff(self):
        '''(Float) Ball inflating pressure'''
        return float()
    @property
    def ball_damp(self):
        '''(Float) Blending to inelastic collision'''
        return float()
    @property
    def error_threshold(self):
        '''(Float) The Runge-Kutta ODE solver error limit, low value gives more
        precision, high values speed'''
        return float()
    @property
    def step_min(self):
        '''(Integer) Minimal # solver steps/frame'''
        return int()
    @property
    def step_max(self):
        '''(Integer) Maximal # solver steps/frame'''
        return int()
    @property
    def choke(self):
        '''(Integer) 'Viscosity' inside collision target'''
        return int()
    @property
    def fuzzy(self):
        '''(Integer) Fuzziness while on collision, high values make collision
        handling faster but less stable'''
        return int()
    @property
    def use_auto_step(self):
        '''(Boolean) Use velocities for automagic step sizes'''
        return bool()
    @property
    def use_diagnose(self):
        '''(Boolean) Turn on SB diagnose console prints'''
        return bool()
    @property
    def use_estimate_matrix(self):
        '''(Boolean) Estimate matrix... split to COM, ROT, SCALE'''
        return bool()
    @property
    def location_mass_center(self):
        '''(Vector 3D) Location of Center of mass'''
        return mathutils.Vector()
    @property
    def rotation_estimate(self):
        '''(Float[9]) Estimated rotation matrix'''
        return ''
    @property
    def scale_estimate(self):
        '''(Float[9]) Estimated scale matrix'''
        return ''
    @property
    def use_goal(self):
        '''(Boolean) Define forces for vertices to stick to animated position'''
        return bool()
    @property
    def use_edges(self):
        '''(Boolean) Use Edges as springs'''
        return bool()
    @property
    def use_stiff_quads(self):
        '''(Boolean) Add diagonal springs on 4-gons'''
        return bool()
    @property
    def use_edge_collision(self):
        '''(Boolean) Edges collide too'''
        return bool()
    @property
    def use_face_collision(self):
        '''(Boolean) Faces collide too, can be very slow'''
        return bool()
    @property
    def aerodynamics_type(self):
        '''(Enum) Method of calculating aerodynamic interaction
        
        [SIMPLE, LIFT_FORCE]'''
        return str()
    @property
    def use_self_collision(self):
        '''(Boolean) Enable naive vertex ball self collision'''
        return bool()
    @property
    def effector_weights(self):
        '''(EffectorWeights)'''
        return EffectorWeights()