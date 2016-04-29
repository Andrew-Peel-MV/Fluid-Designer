from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class UserPreferencesEdit(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def material_link(self):
        '''(Enum) Toggle whether the material is linked to object data or the
        object block
        
        [OBDATA, OBJECT]'''
        return str()
    @property
    def object_align(self):
        '''(Enum) When adding objects from a 3D View menu, either align them with
        that view or with the world
        
        [WORLD, VIEW]'''
        return str()
    @property
    def use_enter_edit_mode(self):
        '''(Boolean) Enter Edit Mode automatically after adding a new object'''
        return bool()
    @property
    def use_drag_immediately(self):
        '''(Boolean) Moving things with a mouse drag confirms when releasing the
        button'''
        return bool()
    @property
    def undo_steps(self):
        '''(Integer) Number of undo steps available (smaller values conserve
        memory)'''
        return int()
    @property
    def undo_memory_limit(self):
        '''(Integer) Maximum memory usage in megabytes (0 means unlimited)'''
        return int()
    @property
    def use_global_undo(self):
        '''(Boolean) Global undo works by keeping a full copy of the file itself
        in memory, so takes extra memory'''
        return bool()
    @property
    def use_auto_keying(self):
        '''(Boolean) Automatic keyframe insertion for Objects and Bones (default
        setting used for new Scenes)'''
        return bool()
    @property
    def auto_keying_mode(self):
        '''(Enum) Mode of automatic keyframe insertion for Objects and Bones
        (default setting used for new Scenes)
        
        [ADD_REPLACE_KEYS, REPLACE_KEYS]'''
        return str()
    @property
    def use_keyframe_insert_available(self):
        '''(Boolean) Automatic keyframe insertion in available F-Curves'''
        return bool()
    @property
    def use_auto_keying_warning(self):
        '''(Boolean) Show warning indicators when transforming objects and bones
        if auto keying is enabled'''
        return bool()
    @property
    def use_keyframe_insert_needed(self):
        '''(Boolean) Keyframe insertion only when keyframe needed'''
        return bool()
    @property
    def use_visual_keying(self):
        '''(Boolean) Use Visual keying automatically for constrained objects'''
        return bool()
    @property
    def use_insertkey_xyz_to_rgb(self):
        '''(Boolean) Color for newly added transformation F-Curves (Location,
        Rotation, Scale) and also Color is based on the transform axis'''
        return bool()
    @property
    def keyframe_new_interpolation_type(self):
        '''(Enum) Interpolation mode used for first keyframe on newly added
        F-Curves (subsequent keyframes take interpolation from preceding
        keyframe)
        
        [CONSTANT, LINEAR, BEZIER, SINE, QUAD, CUBIC, QUART, QUINT, EXPO,
        CIRC, BACK, BOUNCE, ELASTIC]'''
        return str()
    @property
    def keyframe_new_handle_type(self):
        '''(Enum) Handle type for handles of new keyframes
        
        [FREE, VECTOR, ALIGNED, AUTO, AUTO_CLAMPED]'''
        return str()
    @property
    def use_negative_frames(self):
        '''(Boolean) Current frame number can be manually set to a negative value'''
        return bool()
    @property
    def fcurve_unselected_alpha(self):
        '''(Float) Amount that unselected F-Curves stand out from the background
        (Graph Editor)'''
        return float()
    @property
    def grease_pencil_manhattan_distance(self):
        '''(Integer) Pixels moved by mouse per axis when drawing stroke'''
        return int()
    @property
    def grease_pencil_euclidean_distance(self):
        '''(Integer) Distance moved by mouse when drawing stroke to include'''
        return int()
    @property
    def use_grease_pencil_smooth_stroke(self):
        '''(Boolean) Smooth the final stroke'''
        return bool()
    @property
    def use_grease_pencil_simplify_stroke(self):
        '''(Boolean) Simplify the final stroke'''
        return bool()
    @property
    def grease_pencil_eraser_radius(self):
        '''(Integer) Radius of eraser 'brush''''
        return int()
    @property
    def grease_pencil_default_color(self):
        '''(Float[4]) Color of new Grease Pencil layers'''
        return ''
    @property
    def sculpt_paint_overlay_color(self):
        '''(Vector 3D) Color of texture overlay'''
        return mathutils.Vector()
    @property
    def use_duplicate_mesh(self):
        '''(Boolean) Causes mesh data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_surface(self):
        '''(Boolean) Causes surface data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_curve(self):
        '''(Boolean) Causes curve data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_text(self):
        '''(Boolean) Causes text data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_metaball(self):
        '''(Boolean) Causes metaball data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_armature(self):
        '''(Boolean) Causes armature data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_lamp(self):
        '''(Boolean) Causes lamp data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_material(self):
        '''(Boolean) Causes material data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_texture(self):
        '''(Boolean) Causes texture data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_fcurve(self):
        '''(Boolean) Causes F-curve data to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_action(self):
        '''(Boolean) Causes actions to be duplicated with the object'''
        return bool()
    @property
    def use_duplicate_particle(self):
        '''(Boolean) Causes particle systems to be duplicated with the object'''
        return bool()
    @property
    def node_margin(self):
        '''(Integer) Minimum distance between nodes for Auto-offsetting nodes'''
        return int()