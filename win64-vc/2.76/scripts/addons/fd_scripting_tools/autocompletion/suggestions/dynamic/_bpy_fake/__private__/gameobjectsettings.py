from . sensor import Sensor
from . gameproperty import GameProperty
from . struct import Struct
from . controller import Controller
from . gamesoftbodysettings import GameSoftBodySettings
from . actuator import Actuator
from . bpy_struct import bpy_struct
import mathutils

class GameObjectSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def sensors(self):
        '''(Sequence of Sensor) Game engine sensor to detect events'''
        return (Sensor(),)
    @property
    def controllers(self):
        '''(Sequence of Controller) Game engine controllers to process events,
        connecting sensors to actuators'''
        return (Controller(),)
    @property
    def actuators(self):
        '''(Sequence of Actuator) Game engine actuators to act on events'''
        return (Actuator(),)
    @property
    def properties(self):
        '''(Sequence of GameProperty) Game engine properties'''
        return (GameProperty(),)
    @property
    def show_sensors(self):
        '''(Boolean) Shows sensors for this object in the user interface'''
        return bool()
    @property
    def show_controllers(self):
        '''(Boolean) Shows controllers for this object in the user interface'''
        return bool()
    @property
    def show_actuators(self):
        '''(Boolean) Shows actuators for this object in the user interface'''
        return bool()
    @property
    def physics_type(self):
        '''(Enum) Select the type of physical representation
        
        [NO_COLLISION, STATIC, DYNAMIC, RIGID_BODY, SOFT_BODY, OCCLUDER,
        SENSOR, NAVMESH, CHARACTER]'''
        return str()
    @property
    def use_record_animation(self):
        '''(Boolean) Record animation objects without physics'''
        return bool()
    @property
    def use_actor(self):
        '''(Boolean) Object is detected by the Near and Radar sensor'''
        return bool()
    @property
    def use_ghost(self):
        '''(Boolean) Object does not react to collisions, like a ghost'''
        return bool()
    @property
    def mass(self):
        '''(Float) Mass of the object'''
        return float()
    @property
    def radius(self):
        '''(Float) Radius of bounding sphere and material physics'''
        return float()
    @property
    def use_sleep(self):
        '''(Boolean) Disable auto (de)activation in physics simulation'''
        return bool()
    @property
    def damping(self):
        '''(Float) General movement damping'''
        return float()
    @property
    def rotation_damping(self):
        '''(Float) General rotation damping'''
        return float()
    @property
    def velocity_min(self):
        '''(Float) Clamp velocity to this minimum speed (except when totally
        still), in distance per second'''
        return float()
    @property
    def velocity_max(self):
        '''(Float) Clamp velocity to this maximum speed, in distance per second'''
        return float()
    @property
    def angular_velocity_min(self):
        '''(Float) Clamp angular velocity to this minimum speed (except when
        totally still), in angle per second'''
        return float()
    @property
    def angular_velocity_max(self):
        '''(Float) Clamp angular velocity to this maximum speed, in angle per
        second'''
        return float()
    @property
    def step_height(self):
        '''(Float) Maximum height of steps the character can run over'''
        return float()
    @property
    def jump_speed(self):
        '''(Float) Upward velocity applied to the character when jumping'''
        return float()
    @property
    def fall_speed(self):
        '''(Float) Maximum speed at which the character will fall'''
        return float()
    @property
    def collision_group(self):
        '''(Boolean[16]) The collision group of the object'''
        return bool()
    @property
    def collision_mask(self):
        '''(Boolean[16]) The groups this object can collide with'''
        return bool()
    @property
    def lock_location_x(self):
        '''(Boolean) Disable simulation of linear motion along the X axis'''
        return bool()
    @property
    def lock_location_y(self):
        '''(Boolean) Disable simulation of linear motion along the Y axis'''
        return bool()
    @property
    def lock_location_z(self):
        '''(Boolean) Disable simulation of linear motion along the Z axis'''
        return bool()
    @property
    def lock_rotation_x(self):
        '''(Boolean) Disable simulation of angular motion along the X axis'''
        return bool()
    @property
    def lock_rotation_y(self):
        '''(Boolean) Disable simulation of angular motion along the Y axis'''
        return bool()
    @property
    def lock_rotation_z(self):
        '''(Boolean) Disable simulation of angular motion along the Z axis'''
        return bool()
    @property
    def use_activity_culling(self):
        '''(Boolean) Disable simulation of angular motion along the Z axis'''
        return bool()
    @property
    def use_material_physics_fh(self):
        '''(Boolean) React to force field physics settings in materials'''
        return bool()
    @property
    def use_rotate_from_normal(self):
        '''(Boolean) Use face normal to rotate object, so that it points away
        from the surface'''
        return bool()
    @property
    def form_factor(self):
        '''(Float) Form factor scales the inertia tensor'''
        return float()
    @property
    def use_anisotropic_friction(self):
        '''(Boolean) Enable anisotropic friction'''
        return bool()
    @property
    def friction_coefficients(self):
        '''(Vector 3D) Relative friction coefficients in the in the X, Y and Z
        directions, when anisotropic friction is enabled'''
        return mathutils.Vector()
    @property
    def use_collision_bounds(self):
        '''(Boolean) Specify a collision bounds type other than the default'''
        return bool()
    @property
    def collision_bounds_type(self):
        '''(Enum) Select the collision shape that better fits the object
        
        [BOX, SPHERE, CYLINDER, CONE, CONVEX_HULL, TRIANGLE_MESH, CAPSULE]'''
        return str()
    @property
    def use_collision_compound(self):
        '''(Boolean) Add children to form a compound collision object'''
        return bool()
    @property
    def collision_margin(self):
        '''(Float) Extra margin around object for collision detection, small
        amount required for stability'''
        return float()
    @property
    def soft_body(self):
        '''(GameSoftBodySettings) Settings for Bullet soft body simulation'''
        return GameSoftBodySettings()
    @property
    def use_obstacle_create(self):
        '''(Boolean) Create representation for obstacle simulation'''
        return bool()
    @property
    def obstacle_radius(self):
        '''(Float) Radius of object representation in obstacle simulation'''
        return float()
    @property
    def states_visible(self):
        '''(Boolean[30]) State determining which controllers are displayed'''
        return bool()
    @property
    def used_states(self):
        '''(Boolean[30]) States which are being used by controllers'''
        return bool()
    @property
    def states_initial(self):
        '''(Boolean[30]) Initial state when the game starts'''
        return bool()
    @property
    def show_debug_state(self):
        '''(Boolean) Print state debug info in the game engine'''
        return bool()
    @property
    def use_all_states(self):
        '''(Boolean) Set all state bits'''
        return bool()
    @property
    def show_state_panel(self):
        '''(Boolean) Show state panel'''
        return bool()