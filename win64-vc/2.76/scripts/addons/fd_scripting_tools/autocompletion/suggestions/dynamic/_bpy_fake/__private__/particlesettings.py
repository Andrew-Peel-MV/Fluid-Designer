from . boidsettings import BoidSettings
from . particledupliweight import ParticleDupliWeight
from . texture import Texture
from . imagepreview import ImagePreview
from . curvemapping import CurveMapping
from . cyclescurvesettings import CyclesCurveSettings
from . struct import Struct
from . id import ID
from . sphfluidsettings import SPHFluidSettings
from . group import Group
from . effectorweights import EffectorWeights
from . fieldsettings import FieldSettings
from . library import Library
from . particlesettingstextureslots import ParticleSettingsTextureSlots
from . animdata import AnimData
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class ParticleSettings(bpy_struct):
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
    def texture_slots(self):
        '''(Sequence of ParticleSettingsTextureSlot) Texture slots defining the
        mapping and influence of textures'''
        return ParticleSettingsTextureSlots()
    @property
    def active_texture(self):
        '''(Texture) Active texture slot being displayed'''
        return Texture()
    @property
    def active_texture_index(self):
        '''(Integer) Index of active texture slot'''
        return int()
    @property
    def is_fluid(self):
        '''(Boolean) Particles were created by a fluid simulation'''
        return bool()
    @property
    def use_react_start_end(self):
        '''(Boolean) Give birth to unreacted particles eventually'''
        return bool()
    @property
    def use_react_multiple(self):
        '''(Boolean) React multiple times'''
        return bool()
    @property
    def regrow_hair(self):
        '''(Boolean) Regrow hair for each frame'''
        return bool()
    @property
    def show_unborn(self):
        '''(Boolean) Show particles before they are emitted'''
        return bool()
    @property
    def use_dead(self):
        '''(Boolean) Show particles after they have died'''
        return bool()
    @property
    def use_emit_random(self):
        '''(Boolean) Emit in random order of elements'''
        return bool()
    @property
    def use_even_distribution(self):
        '''(Boolean) Use even distribution from faces based on face areas or edge
        lengths'''
        return bool()
    @property
    def use_die_on_collision(self):
        '''(Boolean) Particles die when they collide with a deflector object'''
        return bool()
    @property
    def use_size_deflect(self):
        '''(Boolean) Use particle's size in deflection'''
        return bool()
    @property
    def use_rotations(self):
        '''(Boolean) Calculate particle rotations'''
        return bool()
    @property
    def use_dynamic_rotation(self):
        '''(Boolean) Particle rotations are affected by collisions and effectors'''
        return bool()
    @property
    def use_multiply_size_mass(self):
        '''(Boolean) Multiply mass by particle size'''
        return bool()
    @property
    def use_advanced_hair(self):
        '''(Boolean) Use full physics calculations for growing hair'''
        return bool()
    @property
    def lock_boids_to_surface(self):
        '''(Boolean) Constrain boids to a surface'''
        return bool()
    @property
    def use_hair_bspline(self):
        '''(Boolean) Interpolate hair using B-Splines'''
        return bool()
    @property
    def invert_grid(self):
        '''(Boolean) Invert what is considered object and what is not'''
        return bool()
    @property
    def hexagonal_grid(self):
        '''(Boolean) Create the grid in a hexagonal pattern'''
        return bool()
    @property
    def apply_effector_to_children(self):
        '''(Boolean) Apply effectors to children'''
        return bool()
    @property
    def create_long_hair_children(self):
        '''(Boolean) Calculate children that suit long hair well'''
        return bool()
    @property
    def apply_guide_to_children(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_self_effect(self):
        '''(Boolean) Particle effectors affect themselves'''
        return bool()
    @property
    def type(self):
        '''(Enum) Particle Type
        
        [EMITTER, HAIR]'''
        return str()
    @property
    def emit_from(self):
        '''(Enum) Where to emit particles from
        
        [VERT, FACE, VOLUME]'''
        return str()
    @property
    def distribution(self):
        '''(Enum) How to distribute particles on selected element
        
        [JIT, RAND, GRID]'''
        return str()
    @property
    def physics_type(self):
        '''(Enum) Particle physics type
        
        [NO, NEWTON, KEYED, BOIDS, FLUID]'''
        return str()
    @property
    def rotation_mode(self):
        '''(Enum) Particle orientation axis (does not affect Explode modifier's
        results)
        
        [NONE, NOR, NOR_TAN, VEL, GLOB_X, GLOB_Y, GLOB_Z, OB_X, OB_Y, OB_Z]'''
        return str()
    @property
    def angular_velocity_mode(self):
        '''(Enum) What axis is used to change particle rotation with time
        
        [NONE, VELOCITY, HORIZONTAL, VERTICAL, GLOBAL_X, GLOBAL_Y, GLOBAL_Z,
        RAND]'''
        return str()
    @property
    def react_event(self):
        '''(Enum) The event of target particles to react on
        
        [DEATH, COLLIDE, NEAR]'''
        return str()
    @property
    def show_guide_hairs(self):
        '''(Boolean) Show guide hairs'''
        return bool()
    @property
    def show_hair_grid(self):
        '''(Boolean) Show guide hairs'''
        return bool()
    @property
    def show_velocity(self):
        '''(Boolean) Show particle velocity'''
        return bool()
    @property
    def show_size(self):
        '''(Boolean) Show particle size'''
        return bool()
    @property
    def use_render_emitter(self):
        '''(Boolean) Render emitter Object also'''
        return bool()
    @property
    def show_health(self):
        '''(Boolean) Draw boid health'''
        return bool()
    @property
    def use_absolute_path_time(self):
        '''(Boolean) Path timing is in absolute frames'''
        return bool()
    @property
    def use_parent_particles(self):
        '''(Boolean) Render parent particles'''
        return bool()
    @property
    def show_number(self):
        '''(Boolean) Show particle number'''
        return bool()
    @property
    def use_group_pick_random(self):
        '''(Boolean) Pick objects from group randomly'''
        return bool()
    @property
    def use_group_count(self):
        '''(Boolean) Use object multiple times in the same group'''
        return bool()
    @property
    def use_global_dupli(self):
        '''(Boolean) Use object's global coordinates for duplication'''
        return bool()
    @property
    def use_rotation_dupli(self):
        '''(Boolean) Use object's rotation for duplication (global x-axis is
        aligned particle rotation axis)'''
        return bool()
    @property
    def use_scale_dupli(self):
        '''(Boolean) Use object's scale for duplication'''
        return bool()
    @property
    def use_render_adaptive(self):
        '''(Boolean) Draw steps of the particle path'''
        return bool()
    @property
    def use_velocity_length(self):
        '''(Boolean) Multiply line length by particle speed'''
        return bool()
    @property
    def use_whole_group(self):
        '''(Boolean) Use whole group at once'''
        return bool()
    @property
    def use_strand_primitive(self):
        '''(Boolean) Use the strand primitive for rendering'''
        return bool()
    @property
    def draw_method(self):
        '''(Enum) How particles are drawn in viewport
        
        [NONE, RENDER, DOT, CIRC, CROSS, AXIS]'''
        return str()
    @property
    def render_type(self):
        '''(Enum) How particles are rendered
        
        [NONE, HALO, LINE, PATH, OBJECT, GROUP, BILLBOARD]'''
        return str()
    @property
    def draw_color(self):
        '''(Enum) Draw additional particle data as a color
        
        [NONE, MATERIAL, VELOCITY, ACCELERATION]'''
        return str()
    @property
    def draw_size(self):
        '''(Integer) Size of particles on viewport in pixels (0=default)'''
        return int()
    @property
    def child_type(self):
        '''(Enum) Create child particles
        
        [NONE, SIMPLE, INTERPOLATED]'''
        return str()
    @property
    def draw_step(self):
        '''(Integer) How many steps paths are drawn with (power of 2)'''
        return int()
    @property
    def render_step(self):
        '''(Integer) How many steps paths are rendered with (power of 2)'''
        return int()
    @property
    def hair_step(self):
        '''(Integer) Number of hair segments'''
        return int()
    @property
    def bending_random(self):
        '''(Float) Random stiffness of hairs'''
        return float()
    @property
    def keys_step(self):
        '''(Integer)'''
        return int()
    @property
    def adaptive_angle(self):
        '''(Integer) How many degrees path has to curve to make another render
        segment'''
        return int()
    @property
    def adaptive_pixel(self):
        '''(Integer) How many pixels path has to cover to make another render
        segment'''
        return int()
    @property
    def draw_percentage(self):
        '''(Integer) Percentage of particles to display in 3D view'''
        return int()
    @property
    def material(self):
        '''(Integer) Index of material slot used for rendering particles'''
        return int()
    @property
    def material_slot(self):
        '''(Enum) Material slot used for rendering particles
        
        [DUMMY]'''
        return str()
    @property
    def integrator(self):
        '''(Enum) Algorithm used to calculate physics, from the fastest to the
        most stable/accurate: Midpoint, Euler, Verlet, RK4 (Old)
        
        [EULER, VERLET, MIDPOINT, RK4]'''
        return str()
    @property
    def kink(self):
        '''(Enum) Type of periodic offset on the path
        
        [NO, CURL, RADIAL, WAVE, BRAID, SPIRAL]'''
        return str()
    @property
    def kink_axis(self):
        '''(Enum) Which axis to use for offset
        
        [X, Y, Z]'''
        return str()
    @property
    def lock_billboard(self):
        '''(Boolean) Lock the billboards align axis'''
        return bool()
    @property
    def billboard_align(self):
        '''(Enum) In respect to what the billboards are aligned
        
        [X, Y, Z, VIEW, VEL]'''
        return str()
    @property
    def billboard_uv_split(self):
        '''(Integer) Number of rows/columns to split UV coordinates for
        billboards'''
        return int()
    @property
    def billboard_animation(self):
        '''(Enum) How to animate billboard textures
        
        [NONE, AGE, FRAME, ANGLE]'''
        return str()
    @property
    def billboard_offset_split(self):
        '''(Enum) How to offset billboard textures
        
        [NONE, LINEAR, RANDOM]'''
        return str()
    @property
    def billboard_tilt(self):
        '''(Float) Tilt of the billboards'''
        return float()
    @property
    def color_maximum(self):
        '''(Float) Maximum length of the particle color vector'''
        return float()
    @property
    def billboard_tilt_random(self):
        '''(Float) Random tilt of the billboards'''
        return float()
    @property
    def billboard_offset(self):
        '''(Vector 2D)'''
        return mathutils.Vector()
    @property
    def billboard_size(self):
        '''(Vector 2D) Scale billboards relative to particle size'''
        return mathutils.Vector()
    @property
    def billboard_velocity_head(self):
        '''(Float) Scale billboards by velocity'''
        return float()
    @property
    def billboard_velocity_tail(self):
        '''(Float) Scale billboards by velocity'''
        return float()
    @property
    def use_simplify(self):
        '''(Boolean) Remove child strands as the object becomes smaller on the
        screen'''
        return bool()
    @property
    def use_simplify_viewport(self):
        '''(Boolean)'''
        return bool()
    @property
    def simplify_refsize(self):
        '''(Integer) Reference size in pixels, after which simplification begins'''
        return int()
    @property
    def simplify_rate(self):
        '''(Float) Speed of simplification'''
        return float()
    @property
    def simplify_transition(self):
        '''(Float) Transition period for fading out strands'''
        return float()
    @property
    def simplify_viewport(self):
        '''(Float) Speed of Simplification'''
        return float()
    @property
    def frame_start(self):
        '''(Float) Frame number to start emitting particles'''
        return float()
    @property
    def frame_end(self):
        '''(Float) Frame number to stop emitting particles'''
        return float()
    @property
    def lifetime(self):
        '''(Float) Life span of the particles'''
        return float()
    @property
    def lifetime_random(self):
        '''(Float) Give the particle life a random variation'''
        return float()
    @property
    def time_tweak(self):
        '''(Float) A multiplier for physics timestep (1.0 means one frame = 1/25
        seconds)'''
        return float()
    @property
    def timestep(self):
        '''(Float) The simulation timestep per frame (seconds per frame)'''
        return float()
    @property
    def use_adaptive_subframes(self):
        '''(Boolean) Automatically set the number of subframes'''
        return bool()
    @property
    def subframes(self):
        '''(Integer) Subframes to simulate for improved stability and finer
        granularity simulations (dt = timestep / (subframes + 1))'''
        return int()
    @property
    def courant_target(self):
        '''(Float) The relative distance a particle can move before requiring
        more subframes (target Courant number); 0.01-0.3 is the recommended
        range'''
        return float()
    @property
    def jitter_factor(self):
        '''(Float) Amount of jitter applied to the sampling'''
        return float()
    @property
    def effect_hair(self):
        '''(Float) Hair stiffness for effectors'''
        return float()
    @property
    def count(self):
        '''(Integer) Total number of particles'''
        return int()
    @property
    def userjit(self):
        '''(Integer) Emission locations / face (0 = automatic)'''
        return int()
    @property
    def grid_resolution(self):
        '''(Integer) The resolution of the particle grid'''
        return int()
    @property
    def grid_random(self):
        '''(Float) Add random offset to the grid locations'''
        return float()
    @property
    def effector_amount(self):
        '''(Integer) How many particles are effectors (0 is all particles)'''
        return int()
    @property
    def normal_factor(self):
        '''(Float) Let the surface normal give the particle a starting speed'''
        return float()
    @property
    def object_factor(self):
        '''(Float) Let the object give the particle a starting speed'''
        return float()
    @property
    def factor_random(self):
        '''(Float) Give the starting speed a random variation'''
        return float()
    @property
    def particle_factor(self):
        '''(Float) Let the target particle give the particle a starting speed'''
        return float()
    @property
    def tangent_factor(self):
        '''(Float) Let the surface tangent give the particle a starting speed'''
        return float()
    @property
    def tangent_phase(self):
        '''(Float) Rotate the surface tangent'''
        return float()
    @property
    def reactor_factor(self):
        '''(Float) Let the vector away from the target particle's location give
        the particle a starting speed'''
        return float()
    @property
    def object_align_factor(self):
        '''(Vector 3D) Let the emitter object orientation give the particle a
        starting speed'''
        return mathutils.Vector()
    @property
    def angular_velocity_factor(self):
        '''(Float) Angular velocity amount (in radians per second)'''
        return float()
    @property
    def phase_factor(self):
        '''(Float) Rotation around the chosen orientation axis'''
        return float()
    @property
    def rotation_factor_random(self):
        '''(Float) Randomize particle orientation'''
        return float()
    @property
    def phase_factor_random(self):
        '''(Float) Randomize rotation around the chosen orientation axis'''
        return float()
    @property
    def hair_length(self):
        '''(Float) Length of the hair'''
        return float()
    @property
    def mass(self):
        '''(Float) Mass of the particles'''
        return float()
    @property
    def particle_size(self):
        '''(Float) The size of the particles'''
        return float()
    @property
    def size_random(self):
        '''(Float) Give the particle size a random variation'''
        return float()
    @property
    def drag_factor(self):
        '''(Float) Amount of air-drag'''
        return float()
    @property
    def brownian_factor(self):
        '''(Float) Amount of random, erratic particle movement'''
        return float()
    @property
    def damping(self):
        '''(Float) Amount of damping'''
        return float()
    @property
    def length_random(self):
        '''(Float) Give path length a random variation'''
        return float()
    @property
    def child_nbr(self):
        '''(Integer) Number of children/parent'''
        return int()
    @property
    def rendered_child_count(self):
        '''(Integer) Number of children/parent for rendering'''
        return int()
    @property
    def virtual_parents(self):
        '''(Float) Relative amount of virtual parents'''
        return float()
    @property
    def child_size(self):
        '''(Float) A multiplier for the child particle size'''
        return float()
    @property
    def child_size_random(self):
        '''(Float) Random variation to the size of the child particles'''
        return float()
    @property
    def child_radius(self):
        '''(Float) Radius of children around parent'''
        return float()
    @property
    def child_roundness(self):
        '''(Float) Roundness of children around parent'''
        return float()
    @property
    def clump_factor(self):
        '''(Float) Amount of clumping'''
        return float()
    @property
    def clump_shape(self):
        '''(Float) Shape of clumping'''
        return float()
    @property
    def use_clump_curve(self):
        '''(Boolean) Use a curve to define clump tapering'''
        return bool()
    @property
    def clump_curve(self):
        '''(CurveMapping) Curve defining clump tapering'''
        return CurveMapping()
    @property
    def use_clump_noise(self):
        '''(Boolean) Create random clumps around the parent'''
        return bool()
    @property
    def clump_noise_size(self):
        '''(Float) Size of clump noise'''
        return float()
    @property
    def kink_amplitude(self):
        '''(Float) The amplitude of the offset'''
        return float()
    @property
    def kink_amplitude_clump(self):
        '''(Float) How much clump affects kink amplitude'''
        return float()
    @property
    def kink_amplitude_random(self):
        '''(Float) Random variation of the amplitude'''
        return float()
    @property
    def kink_frequency(self):
        '''(Float) The frequency of the offset (1/total length)'''
        return float()
    @property
    def kink_shape(self):
        '''(Float) Adjust the offset to the beginning/end'''
        return float()
    @property
    def kink_flat(self):
        '''(Float) How flat the hairs are'''
        return float()
    @property
    def kink_extra_steps(self):
        '''(Integer) Extra steps for resolution of special kink features'''
        return int()
    @property
    def kink_axis_random(self):
        '''(Float) Random variation of the orientation'''
        return float()
    @property
    def roughness_1(self):
        '''(Float) Amount of location dependent rough'''
        return float()
    @property
    def roughness_1_size(self):
        '''(Float) Size of location dependent rough'''
        return float()
    @property
    def roughness_2(self):
        '''(Float) Amount of random rough'''
        return float()
    @property
    def roughness_2_size(self):
        '''(Float) Size of random rough'''
        return float()
    @property
    def roughness_2_threshold(self):
        '''(Float) Amount of particles left untouched by random rough'''
        return float()
    @property
    def roughness_endpoint(self):
        '''(Float) Amount of end point rough'''
        return float()
    @property
    def roughness_end_shape(self):
        '''(Float) Shape of end point rough'''
        return float()
    @property
    def use_roughness_curve(self):
        '''(Boolean) Use a curve to define roughness'''
        return bool()
    @property
    def roughness_curve(self):
        '''(CurveMapping) Curve defining roughness'''
        return CurveMapping()
    @property
    def child_length(self):
        '''(Float) Length of child paths'''
        return float()
    @property
    def child_length_threshold(self):
        '''(Float) Amount of particles left untouched by child path length'''
        return float()
    @property
    def child_parting_factor(self):
        '''(Float) Create parting in the children based on parent strands'''
        return float()
    @property
    def child_parting_min(self):
        '''(Float) Minimum root to tip angle (tip distance/root distance for long
        hair)'''
        return float()
    @property
    def child_parting_max(self):
        '''(Float) Maximum root to tip angle (tip distance/root distance for long
        hair)'''
        return float()
    @property
    def branch_threshold(self):
        '''(Float) Threshold of branching'''
        return float()
    @property
    def line_length_tail(self):
        '''(Float) Length of the line's tail'''
        return float()
    @property
    def line_length_head(self):
        '''(Float) Length of the line's head'''
        return float()
    @property
    def path_start(self):
        '''(Float) Starting time of drawn path'''
        return float()
    @property
    def path_end(self):
        '''(Float) End time of drawn path'''
        return float()
    @property
    def trail_count(self):
        '''(Integer) Number of trail particles'''
        return int()
    @property
    def keyed_loops(self):
        '''(Integer) Number of times the keys are looped'''
        return int()
    @property
    def use_modifier_stack(self):
        '''(Boolean) Emit particles from mesh with modifiers applied (must use
        same subsurf level for viewport and render for correct results)'''
        return bool()
    @property
    def dupli_group(self):
        '''(Group) Show Objects in this Group in place of particles'''
        return Group()
    @property
    def dupli_weights(self):
        '''(Sequence of ParticleDupliWeight) Weights for all of the objects in
        the dupli group'''
        return (ParticleDupliWeight(),)
    @property
    def active_dupliweight(self):
        '''(ParticleDupliWeight)'''
        return ParticleDupliWeight()
    @property
    def active_dupliweight_index(self):
        '''(Integer)'''
        return int()
    @property
    def dupli_object(self):
        '''(Object) Show this Object in place of particles'''
        return Object()
    @property
    def billboard_object(self):
        '''(Object) Billboards face this object (default is active camera)'''
        return Object()
    @property
    def boids(self):
        '''(BoidSettings)'''
        return BoidSettings()
    @property
    def fluid(self):
        '''(SPHFluidSettings)'''
        return SPHFluidSettings()
    @property
    def effector_weights(self):
        '''(EffectorWeights)'''
        return EffectorWeights()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def force_field_1(self):
        '''(FieldSettings)'''
        return FieldSettings()
    @property
    def force_field_2(self):
        '''(FieldSettings)'''
        return FieldSettings()
    @property
    def cycles(self):
        '''(CyclesCurveSettings) Cycles hair settings'''
        return CyclesCurveSettings()
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