from . uvsculpt import UvSculpt
from . meshstatvis import MeshStatVis
from . particleedit import ParticleEdit
from . struct import Struct
from . imagepaint import ImagePaint
from . vertexpaint import VertexPaint
from . unifiedpaintsettings import UnifiedPaintSettings
from . sculpt import Sculpt
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class ToolSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def sculpt(self):
        '''(Sculpt)'''
        return Sculpt()
    @property
    def use_auto_normalize(self):
        '''(Boolean) Ensure all bone-deforming vertex groups add up to 1.0 while
        weight painting'''
        return bool()
    @property
    def use_multipaint(self):
        '''(Boolean) Paint across all selected bones while weight painting'''
        return bool()
    @property
    def vertex_group_user(self):
        '''(Enum) Display unweighted vertices (multi-paint overrides)
        
        [NONE, ACTIVE, ALL]'''
        return str()
    @property
    def vertex_group_subset(self):
        '''(Enum) Filter Vertex groups for Display
        
        [ALL, BONE_DEFORM, OTHER_DEFORM]'''
        return str()
    @property
    def vertex_paint(self):
        '''(VertexPaint)'''
        return VertexPaint()
    @property
    def weight_paint(self):
        '''(VertexPaint)'''
        return VertexPaint()
    @property
    def image_paint(self):
        '''(ImagePaint)'''
        return ImagePaint()
    @property
    def uv_sculpt(self):
        '''(UvSculpt)'''
        return UvSculpt()
    @property
    def particle_edit(self):
        '''(ParticleEdit)'''
        return ParticleEdit()
    @property
    def use_uv_sculpt(self):
        '''(Boolean) Enable brush for UV sculpting'''
        return bool()
    @property
    def uv_sculpt_lock_borders(self):
        '''(Boolean) Disable editing of boundary edges'''
        return bool()
    @property
    def uv_sculpt_all_islands(self):
        '''(Boolean) Brush operates on all islands'''
        return bool()
    @property
    def uv_sculpt_tool(self):
        '''(Enum) Select Tools for the UV sculpt brushes
        
        [PINCH, RELAX, GRAB]'''
        return str()
    @property
    def uv_relax_method(self):
        '''(Enum) Algorithm used for UV relaxation
        
        [LAPLACIAN, HC]'''
        return str()
    @property
    def proportional_edit(self):
        '''(Enum) Proportional Editing mode, allows transforms with distance
        fall-off
        
        [DISABLED, ENABLED, PROJECTED, CONNECTED]'''
        return str()
    @property
    def use_proportional_edit_objects(self):
        '''(Boolean) Proportional editing object mode'''
        return bool()
    @property
    def use_proportional_edit_mask(self):
        '''(Boolean) Proportional editing mask mode'''
        return bool()
    @property
    def use_proportional_action(self):
        '''(Boolean) Proportional editing in action editor'''
        return bool()
    @property
    def use_proportional_fcurve(self):
        '''(Boolean) Proportional editing in FCurve editor'''
        return bool()
    @property
    def lock_markers(self):
        '''(Boolean) Prevent marker editing'''
        return bool()
    @property
    def proportional_edit_falloff(self):
        '''(Enum) Falloff type for proportional editing mode
        
        [SMOOTH, SPHERE, ROOT, INVERSE_SQUARE, SHARP, LINEAR, CONSTANT,
        RANDOM]'''
        return str()
    @property
    def proportional_size(self):
        '''(Float) Display size for proportional editing circle'''
        return float()
    @property
    def normal_size(self):
        '''(Float) Display size for normals in the 3D view'''
        return float()
    @property
    def double_threshold(self):
        '''(Float) Limit for removing duplicates and 'Auto Merge''''
        return float()
    @property
    def use_mesh_automerge(self):
        '''(Boolean) Automatically merge vertices moved to the same location'''
        return bool()
    @property
    def use_snap(self):
        '''(Boolean) Snap during transform'''
        return bool()
    @property
    def use_snap_align_rotation(self):
        '''(Boolean) Align rotation with the snapping target'''
        return bool()
    @property
    def use_snap_grid_absolute(self):
        '''(Boolean) Absolute grid alignment while translating (based on the
        pivot center)'''
        return bool()
    @property
    def snap_element(self):
        '''(Enum) Type of element to snap to
        
        [INCREMENT, VERTEX, EDGE, FACE, VOLUME]'''
        return str()
    @property
    def snap_node_element(self):
        '''(Enum) Type of element to snap to
        
        [GRID, NODE_X, NODE_Y, NODE_XY]'''
        return str()
    @property
    def snap_uv_element(self):
        '''(Enum) Type of element to snap to
        
        [INCREMENT, VERTEX]'''
        return str()
    @property
    def snap_target(self):
        '''(Enum) Which part to snap onto the target
        
        [CLOSEST, CENTER, MEDIAN, ACTIVE]'''
        return str()
    @property
    def use_snap_peel_object(self):
        '''(Boolean) Consider objects as whole when finding volume center'''
        return bool()
    @property
    def use_snap_project(self):
        '''(Boolean) Project individual elements on the surface of other objects'''
        return bool()
    @property
    def use_snap_self(self):
        '''(Boolean) Snap onto itself (editmode)'''
        return bool()
    @property
    def use_grease_pencil_sessions(self):
        '''(Boolean) Allow drawing multiple strokes at a time with Grease Pencil'''
        return bool()
    @property
    def grease_pencil_source(self):
        '''(Enum) Datablock where active Grease Pencil data is found from
        
        [SCENE, OBJECT]'''
        return str()
    @property
    def use_keyframe_insert_auto(self):
        '''(Boolean) Automatic keyframe insertion for Objects and Bones'''
        return bool()
    @property
    def auto_keying_mode(self):
        '''(Enum) Mode of automatic keyframe insertion for Objects and Bones
        
        [ADD_REPLACE_KEYS, REPLACE_KEYS]'''
        return str()
    @property
    def use_record_with_nla(self):
        '''(Boolean) Add a new NLA Track + Strip for every loop/pass made over
        the animation to allow non-destructive tweaking'''
        return bool()
    @property
    def use_keyframe_insert_keyingset(self):
        '''(Boolean) Automatic keyframe insertion using active Keying Set only'''
        return bool()
    @property
    def uv_select_mode(self):
        '''(Enum) UV selection and display mode
        
        [VERTEX, EDGE, FACE, ISLAND]'''
        return str()
    @property
    def use_uv_select_sync(self):
        '''(Boolean) Keep UV and edit mode mesh selection in sync'''
        return bool()
    @property
    def show_uv_local_view(self):
        '''(Boolean) Draw only faces with the currently displayed image assigned'''
        return bool()
    @property
    def mesh_select_mode(self):
        '''(Boolean[3]) Which mesh elements selection works on'''
        return bool()
    @property
    def vertex_group_weight(self):
        '''(Float) Weight to assign in vertex groups'''
        return float()
    @property
    def edge_path_mode(self):
        '''(Enum) The edge flag to tag when selecting the shortest path
        
        [SELECT, SEAM, SHARP, CREASE, BEVEL, FREESTYLE]'''
        return str()
    @property
    def edge_path_live_unwrap(self):
        '''(Boolean) Changing edges seam re-calculates UV unwrap'''
        return bool()
    @property
    def use_bone_sketching(self):
        '''(Boolean) Use sketching to create and edit bones'''
        return bool()
    @property
    def use_etch_quick(self):
        '''(Boolean) Automatically convert and delete on stroke end'''
        return bool()
    @property
    def use_etch_overdraw(self):
        '''(Boolean) Adjust strokes by drawing near them'''
        return bool()
    @property
    def use_etch_autoname(self):
        '''(Boolean) Automatically generate values to replace &N and &S suffix
        placeholders in template names'''
        return bool()
    @property
    def etch_number(self):
        '''(String) Text to replace &N with (e.g. 'Finger.&N' -> 'Finger.1' or
        'Finger.One')'''
        return str()
    @property
    def etch_side(self):
        '''(String) Text to replace &S with (e.g. 'Arm.&S' -> 'Arm.R' or
        'Arm.Right')'''
        return str()
    @property
    def etch_template(self):
        '''(Object) Template armature that will be retargeted to the stroke'''
        return Object()
    @property
    def etch_subdivision_number(self):
        '''(Integer) Number of bones in the subdivided stroke'''
        return int()
    @property
    def etch_adaptive_limit(self):
        '''(Float) Correlation threshold for number of bones in the subdivided
        stroke'''
        return float()
    @property
    def etch_length_limit(self):
        '''(Float) Maximum length of the subdivided bones'''
        return float()
    @property
    def etch_roll_mode(self):
        '''(Enum) Method used to adjust the roll of bones when retargeting
        
        [NONE, VIEW, JOINT]'''
        return str()
    @property
    def etch_convert_mode(self):
        '''(Enum) Method used to convert stroke to bones
        
        [FIXED, LENGTH, ADAPTIVE, RETARGET]'''
        return str()
    @property
    def unified_paint_settings(self):
        '''(UnifiedPaintSettings)'''
        return UnifiedPaintSettings()
    @property
    def statvis(self):
        '''(MeshStatVis)'''
        return MeshStatVis()