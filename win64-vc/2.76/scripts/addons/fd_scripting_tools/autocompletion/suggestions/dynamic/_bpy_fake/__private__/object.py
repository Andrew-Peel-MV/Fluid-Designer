from . objectconstraints import ObjectConstraints
from . materialslot import MaterialSlot
from . imagepreview import ImagePreview
from . id import ID
from . greasepencil import GreasePencil
from . mesh import Mesh
from . vertexgroups import VertexGroups
from . posebone import PoseBone
from . shapekey import ShapeKey
from . properties_object_variables import PROPERTIES_Object_Variables
from . scene import Scene
from . animdata import AnimData
from . fd_object import fd_object
from . cyclesobjectblursettings import CyclesObjectBlurSettings
from . animviz import AnimViz
from . action import Action
from . softbodysettings import SoftBodySettings
from . motionpath import MotionPath
from . lodlevel import LodLevel
from . object import Object
from . rigidbodyobject import RigidBodyObject
from . imageuser import ImageUser
from . object_props import Object_Props
from . material import Material
from . pose import Pose
from . object_properties import OBJECT_PROPERTIES
from . fieldsettings import FieldSettings
from . rigidbodyconstraint import RigidBodyConstraint
from . library import Library
from . particlesystems import ParticleSystems
from . dupliobject import DupliObject
from . gameobjectsettings import GameObjectSettings
from . struct import Struct
from . collisionsettings import CollisionSettings
from . group import Group
from . objectmodifiers import ObjectModifiers
from . properties_object_properties import PROPERTIES_Object_Properties
from . cyclesvisibilitysettings import CyclesVisibilitySettings
from . bpy_struct import bpy_struct
import mathutils

class Object(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique datablock ID name'''
        return str()
    @property
    def users(self):
        '''(Integer) Number of times this datablock is referenced'''
        return int()
    @property
    def use_fake_user(self):
        '''(Boolean) Save this datablock even if it has no users'''
        return bool()
    @property
    def tag(self):
        '''(Boolean) Tools can use this to tag data for their own purposes
        (initial state is undefined)'''
        return bool()
    @property
    def is_updated(self):
        '''(Boolean) Datablock is tagged for recalculation'''
        return bool()
    @property
    def is_updated_data(self):
        '''(Boolean) Datablock data is tagged for recalculation'''
        return bool()
    @property
    def is_library_indirect(self):
        '''(Boolean) Is this ID block linked indirectly'''
        return bool()
    @property
    def library(self):
        '''(Library) Library file the datablock is linked from'''
        return Library()
    @property
    def preview(self):
        '''(ImagePreview) Preview image and icon of this datablock (None if not
        supported for this type of data)'''
        return ImagePreview()
    @property
    def data(self):
        '''(ID) Object data'''
        return ID()
    @property
    def type(self):
        '''(Enum) Type of Object
        
        [MESH, CURVE, SURFACE, META, FONT, ARMATURE, LATTICE, EMPTY, CAMERA,
        LAMP, SPEAKER]'''
        return str()
    @property
    def mode(self):
        '''(Enum) Object interaction mode
        
        [OBJECT, EDIT, POSE, SCULPT, VERTEX_PAINT, WEIGHT_PAINT,
        TEXTURE_PAINT, PARTICLE_EDIT]'''
        return str()
    @property
    def layers(self):
        '''(Boolean[20]) Layers the object is on'''
        return bool()
    @property
    def layers_local_view(self):
        '''(Boolean[8]) 3D local view layers the object is on'''
        return bool()
    @property
    def select(self):
        '''(Boolean) Object selection state'''
        return bool()
    @property
    def bound_box(self):
        '''(Float[24]) Object's bounding box in object-space coordinates, all
        values are -1.0 when not available'''
        return ''
    @property
    def parent(self):
        '''(Object) Parent Object'''
        return Object()
    @property
    def parent_type(self):
        '''(Enum) Type of parent relation
        
        [OBJECT, ARMATURE, LATTICE, VERTEX, VERTEX_3, BONE]'''
        return str()
    @property
    def parent_vertices(self):
        '''(Integer[3]) Indices of vertices in case of a vertex parenting
        relation'''
        return int()
    @property
    def parent_bone(self):
        '''(String) Name of parent bone in case of a bone parenting relation'''
        return str()
    @property
    def track_axis(self):
        '''(Enum) Axis that points in 'forward' direction (applies to DupliFrame
        when parent 'Follow' is enabled)
        
        [POS_X, POS_Y, POS_Z, NEG_X, NEG_Y, NEG_Z]'''
        return str()
    @property
    def up_axis(self):
        '''(Enum) Axis that points in the upward direction (applies to DupliFrame
        when parent 'Follow' is enabled)
        
        [X, Y, Z]'''
        return str()
    @property
    def proxy(self):
        '''(Object) Library object this proxy object controls'''
        return Object()
    @property
    def proxy_group(self):
        '''(Object) Library group duplicator object this proxy object controls'''
        return Object()
    @property
    def material_slots(self):
        '''(Sequence of MaterialSlot) Material slots in the object'''
        return (MaterialSlot(),)
    @property
    def active_material(self):
        '''(Material) Active material being displayed'''
        return Material()
    @property
    def active_material_index(self):
        '''(Integer) Index of active material slot'''
        return int()
    @property
    def location(self):
        '''(Vector 3D) Location of the object'''
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
    def scale(self):
        '''(Vector 3D) Scaling of the object'''
        return mathutils.Vector()
    @property
    def dimensions(self):
        '''(Vector 3D) Absolute bounding box dimensions of the object'''
        return mathutils.Vector()
    @property
    def delta_location(self):
        '''(Vector 3D) Extra translation added to the location of the object'''
        return mathutils.Vector()
    @property
    def delta_rotation_euler(self):
        '''(Vector 3D) Extra rotation added to the rotation of the object (when
        using Euler rotations)'''
        return mathutils.Vector()
    @property
    def delta_rotation_quaternion(self):
        '''(Float[4]) Extra rotation added to the rotation of the object (when
        using Quaternion rotations)'''
        return ''
    @property
    def delta_scale(self):
        '''(Vector 3D) Extra scaling added to the scale of the object'''
        return mathutils.Vector()
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
    @property
    def matrix_world(self):
        '''(Matrix) Worldspace transformation matrix'''
        return mathutils.Matrix()
    @property
    def matrix_local(self):
        '''(Matrix) Parent relative transformation matrix - WARNING: Only takes
        into account 'Object' parenting, so e.g. in case of bone parenting you
        get a matrix relative to the Armature object, not to the actual parent
        bone'''
        return mathutils.Matrix()
    @property
    def matrix_basis(self):
        '''(Matrix) Matrix access to location, rotation and scale (including
        deltas), before constraints and parenting are applied'''
        return mathutils.Matrix()
    @property
    def matrix_parent_inverse(self):
        '''(Matrix) Inverse of object's parent matrix at time of parenting'''
        return mathutils.Matrix()
    @property
    def modifiers(self):
        '''(Sequence of Modifier) Modifiers affecting the geometric data of the
        object'''
        return ObjectModifiers()
    @property
    def constraints(self):
        '''(Sequence of Constraint) Constraints affecting the transformation of
        the object'''
        return ObjectConstraints()
    @property
    def game(self):
        '''(GameObjectSettings) Game engine related settings for the object'''
        return GameObjectSettings()
    @property
    def vertex_groups(self):
        '''(Sequence of VertexGroup) Vertex groups of the object'''
        return VertexGroups()
    @property
    def empty_draw_type(self):
        '''(Enum) Viewport display style for empties
        
        [PLAIN_AXES, ARROWS, SINGLE_ARROW, CIRCLE, CUBE, SPHERE, CONE, IMAGE]'''
        return str()
    @property
    def empty_draw_size(self):
        '''(Float) Size of display for empties in the viewport'''
        return float()
    @property
    def empty_image_offset(self):
        '''(Vector 2D) Origin offset distance'''
        return mathutils.Vector()
    @property
    def image_user(self):
        '''(ImageUser) Parameters defining which layer, pass and frame of the
        image is displayed'''
        return ImageUser()
    @property
    def pass_index(self):
        '''(Integer) Index number for the IndexOB render pass'''
        return int()
    @property
    def color(self):
        '''(Float[4]) Object color and alpha, used when faces have the ObColor
        mode enabled'''
        return ''
    @property
    def field(self):
        '''(FieldSettings) Settings for using the object as a field in physics
        simulation'''
        return FieldSettings()
    @property
    def collision(self):
        '''(CollisionSettings) Settings for using the object as a collider in
        physics simulation'''
        return CollisionSettings()
    @property
    def soft_body(self):
        '''(SoftBodySettings) Settings for soft body simulation'''
        return SoftBodySettings()
    @property
    def particle_systems(self):
        '''(Sequence of ParticleSystem) Particle systems emitted from the object'''
        return ParticleSystems()
    @property
    def rigid_body(self):
        '''(RigidBodyObject) Settings for rigid body simulation'''
        return RigidBodyObject()
    @property
    def rigid_body_constraint(self):
        '''(RigidBodyConstraint) Constraint constraining rigid bodies'''
        return RigidBodyConstraint()
    @property
    def hide(self):
        '''(Boolean) Restrict visibility in the viewport'''
        return bool()
    @property
    def hide_select(self):
        '''(Boolean) Restrict selection in the viewport'''
        return bool()
    @property
    def hide_render(self):
        '''(Boolean) Restrict renderability'''
        return bool()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def animation_visualization(self):
        '''(AnimViz) Animation data for this datablock'''
        return AnimViz()
    @property
    def motion_path(self):
        '''(MotionPath) Motion Path for this element'''
        return MotionPath()
    @property
    def use_slow_parent(self):
        '''(Boolean) Create a delay in the parent relationship (beware: this
        isn't renderfarm safe and may be invalid after jumping around the
        timeline)'''
        return bool()
    @property
    def slow_parent_offset(self):
        '''(Float) Delay in the parent relationship'''
        return float()
    @property
    def use_extra_recalc_object(self):
        '''(Boolean) Refresh this object again on frame changes, dependency graph
        hack'''
        return bool()
    @property
    def use_extra_recalc_data(self):
        '''(Boolean) Refresh this object's data again on frame changes,
        dependency graph hack'''
        return bool()
    @property
    def dupli_type(self):
        '''(Enum) If not None, object duplication method to use
        
        [NONE, FRAMES, VERTS, FACES, GROUP]'''
        return str()
    @property
    def use_dupli_frames_speed(self):
        '''(Boolean) Set dupliframes to use the current frame instead of parent
        curve's evaluation time'''
        return bool()
    @property
    def use_dupli_vertices_rotation(self):
        '''(Boolean) Rotate dupli according to vertex normal'''
        return bool()
    @property
    def use_dupli_faces_scale(self):
        '''(Boolean) Scale dupli based on face size'''
        return bool()
    @property
    def dupli_faces_scale(self):
        '''(Float) Scale the DupliFace objects'''
        return float()
    @property
    def dupli_group(self):
        '''(Group) Instance an existing group'''
        return Group()
    @property
    def dupli_frames_start(self):
        '''(Integer) Start frame for DupliFrames'''
        return int()
    @property
    def dupli_frames_end(self):
        '''(Integer) End frame for DupliFrames'''
        return int()
    @property
    def dupli_frames_on(self):
        '''(Integer) Number of frames to use between DupOff frames'''
        return int()
    @property
    def dupli_frames_off(self):
        '''(Integer) Recurring frames to exclude from the Dupliframes'''
        return int()
    @property
    def dupli_list(self):
        '''(Sequence of DupliObject) Object duplis'''
        return (DupliObject(),)
    @property
    def is_duplicator(self):
        '''(Boolean)'''
        return bool()
    @property
    def draw_type(self):
        '''(Enum) Maximum draw type to display object with in viewport
        
        [BOUNDS, WIRE, SOLID, TEXTURED]'''
        return str()
    @property
    def show_bounds(self):
        '''(Boolean) Display the object's bounds'''
        return bool()
    @property
    def draw_bounds_type(self):
        '''(Enum) Object boundary display type
        
        [BOX, SPHERE, CYLINDER, CONE, CAPSULE]'''
        return str()
    @property
    def show_name(self):
        '''(Boolean) Display the object's name'''
        return bool()
    @property
    def show_axis(self):
        '''(Boolean) Display the object's origin and axes'''
        return bool()
    @property
    def show_texture_space(self):
        '''(Boolean) Display the object's texture space'''
        return bool()
    @property
    def show_wire(self):
        '''(Boolean) Add the object's wireframe over solid drawing'''
        return bool()
    @property
    def show_all_edges(self):
        '''(Boolean) Display all edges for mesh objects'''
        return bool()
    @property
    def show_transparent(self):
        '''(Boolean) Display material transparency in the object (unsupported for
        duplicator drawing)'''
        return bool()
    @property
    def show_x_ray(self):
        '''(Boolean) Make the object draw in front of others (unsupported for
        duplicator drawing)'''
        return bool()
    @property
    def grease_pencil(self):
        '''(GreasePencil) Grease Pencil datablock'''
        return GreasePencil()
    @property
    def pose_library(self):
        '''(Action) Action used as a pose library for armatures'''
        return Action()
    @property
    def pose(self):
        '''(Pose) Current pose for armatures'''
        return Pose()
    @property
    def show_only_shape_key(self):
        '''(Boolean) Always show the current Shape for this Object'''
        return bool()
    @property
    def use_shape_key_edit_mode(self):
        '''(Boolean) Apply shape keys in edit mode (for Meshes only)'''
        return bool()
    @property
    def active_shape_key(self):
        '''(ShapeKey) Current shape key'''
        return ShapeKey()
    @property
    def active_shape_key_index(self):
        '''(Integer) Current shape key index'''
        return int()
    @property
    def use_dynamic_topology_sculpting(self):
        '''(Boolean)'''
        return bool()
    @property
    def lod_levels(self):
        '''(Sequence of LodLevel) A collection of detail levels to automatically
        switch between'''
        return (LodLevel(),)
    @property
    def mv(self):
        '''(fd_object)'''
        return fd_object()
    @property
    def cabinetlib(self):
        '''(OBJECT_PROPERTIES)'''
        return OBJECT_PROPERTIES()
    @property
    def lm_cabinet_closet_designer(self):
        '''(PROPERTIES_Object_Properties)'''
        return PROPERTIES_Object_Properties()
    @property
    def lm_moldings(self):
        '''(PROPERTIES_Object_Variables)'''
        return PROPERTIES_Object_Variables()
    @property
    def cycles_visibility(self):
        '''(CyclesVisibilitySettings) Cycles visibility settings'''
        return CyclesVisibilitySettings()
    @property
    def cycles(self):
        '''(CyclesObjectBlurSettings) Cycles object settings'''
        return CyclesObjectBlurSettings()
    @property
    def fd_roombuilder(self):
        '''(Object_Props)'''
        return Object_Props()
    def copy(self):
        '''Create a copy of this datablock (not supported for all datablocks)
        
        Returns:
          id: (ID) New copy of the ID'''
        return ID()
    def user_clear(self):
        '''Clear the user count of a datablock so its not saved, on reload the
        data will be removed'''
        return 
    def animation_data_create(self):
        '''Create animation data to this ID, note that not all ID types support
        this
        
        Returns:
          anim_data: (AnimData) New animation data or NULL'''
        return AnimData()
    def animation_data_clear(self):
        '''Clear animation on this this ID'''
        return 
    def update_tag(self, refresh):
        '''Tag the ID to update its display data, e.g. when calling
        :class:`bpy.types.Scene.update`
        
        Parameter:
          refresh: (Enum) Type of updates to perform'''
        return 
    def convert_space(self, pose_bone, matrix, from_space, to_space):
        '''Convert (transform) the given matrix from one space to another
        
        Parameter:
          pose_bone:
            (PoseBone) Bone to use to define spaces (may be None, in which case
            only the two 'WORLD' and 'LOCAL' spaces are usable)
          matrix: (Matrix) The matrix to transform
          from_space: (Enum) The space in which 'matrix' is currently
          to_space: (Enum) The space to which you want to transform 'matrix'
        
        Returns:
          matrix_return: (Matrix) The transformed matrix'''
        return mathutils.Matrix()
    def calc_matrix_camera(self, x, y, scale_x, scale_y):
        '''Generate the camera projection matrix of this object (mostly useful
        for Camera and Lamp types)
        
        Parameter:
          x: (Integer) Width of the render area
          y: (Integer) Height of the render area
          scale_x: (Float) Width scaling factor
          scale_y: (Float) height scaling factor
        
        Returns:
          result: (Matrix) The camera projection matrix'''
        return mathutils.Matrix()
    def camera_fit_coords(self, scene, coordinates):
        '''Compute the coordinate (and scale for ortho cameras) given object
        should be to 'see' all given coordinates
        
        Parameter:
          scene: (Scene) Scene to get render size information from, if available
          coordinates: (Float) Coordinates to fit in
        
        Returns:
          co_return: (Vector 3D) The location to aim to be able to see all given points
          scale_return:
            (Float) The ortho scale to aim to be able to see all given points (if
            relevant)'''
        return mathutils.Vector(), float()
    def to_mesh(self, scene, apply_modifiers, settings, calc_tessface, calc_undeformed):
        '''Create a Mesh datablock with modifiers applied
        
        Parameter:
          scene: (Scene) Scene within which to evaluate modifiers
          apply_modifiers: (Boolean) Apply modifiers
          settings: (Enum) Modifier settings to apply
          calc_tessface: (Boolean) Calculate tessellation faces
          calc_undeformed: (Boolean) Calculate undeformed vertex coordinates
        
        Returns:
          mesh:
            (Mesh) Mesh created from object, remove it if it is only used for
            export'''
        return Mesh()
    def dupli_list_create(self, scene, settings):
        '''Create a list of dupli objects for this object, needs to be freed
        manually with free_dupli_list to restore the objects real matrix and
        layers
        
        Parameter:
          scene: (Scene) Scene within which to evaluate duplis
          settings: (Enum) Generate texture coordinates for rendering'''
        return 
    def dupli_list_clear(self):
        '''Free the list of dupli objects'''
        return 
    def find_armature(self):
        '''Find armature influencing this object as a parent or via a modifier
        
        Returns:
          ob_arm: (Object) Armature object influencing this object or NULL'''
        return Object()
    def shape_key_add(self, name, from_mix):
        '''Add shape key to this object
        
        Parameter:
          name: (String) Unique name for the new keyblock
          from_mix: (Boolean) Create new shape from existing mix of shapes
        
        Returns:
          key: (ShapeKey) New shape keyblock'''
        return ShapeKey()
    def shape_key_remove(self, key):
        '''Remove a Shape Key from this object
        
        Parameter:
          key: (ShapeKey) Keyblock to be removed'''
        return 
    def ray_cast(self, start, end):
        '''Cast a ray onto in object space
        
        Parameter:
          start: (Vector 3D)
          end: (Vector 3D)
        
        Returns:
          location: (Vector 3D) The hit location of this ray cast
          normal: (Vector 3D) The face normal at the ray cast hit location
          index: (Integer) The face index, -1 when no intersection is found'''
        return mathutils.Vector(), mathutils.Vector(), int()
    def closest_point_on_mesh(self, point, max_dist):
        '''Find the nearest point in object space
        
        Parameter:
          point: (Vector 3D)
          max_dist: (Float)
        
        Returns:
          location: (Vector 3D) The location on the object closest to the point
          normal: (Vector 3D) The face normal at the closest point
          index: (Integer) The face index, -1 when no closest point is found'''
        return mathutils.Vector(), mathutils.Vector(), int()
    def is_visible(self, scene):
        '''Determine if object is visible in a given scene
        
        Parameter:
          scene: (Scene)
        
        Returns:
          result: (Boolean) Object visibility'''
        return bool()
    def is_modified(self, scene, settings):
        '''Determine if this object is modified from the base mesh data
        
        Parameter:
          scene: (Scene)
          settings: (Enum) Modifier settings to apply
        
        Returns:
          result: (Boolean) Object visibility'''
        return bool()
    def is_deform_modified(self, scene, settings):
        '''Determine if this object is modified by a deformation from the base
        mesh data
        
        Parameter:
          scene: (Scene)
          settings: (Enum) Modifier settings to apply
        
        Returns:
          result: (Boolean) Object visibility'''
        return bool()
    def update_from_editmode(self):
        '''Load the objects edit-mode data intp the object data
        
        Returns:
          result: (Boolean) Success'''
        return bool()
    def cache_release(self):
        '''Release memory used by caches associated with this object. Intended to
        be used by render engines only'''
        return 