from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def speed(self):
        '''(Enum) Limit speed of tracking to make visual feedback easier (this
        does not affect the tracking quality)
        
        [FASTEST, DOUBLE, REALTIME, HALF, QUARTER]'''
        return str()
    @property
    def use_keyframe_selection(self):
        '''(Boolean) Automatically select keyframes when solving camera/object
        motion'''
        return bool()
    @property
    def refine_intrinsics(self):
        '''(Enum) Refine intrinsics during camera solving
        
        [NONE, FOCAL_LENGTH, FOCAL_LENGTH_RADIAL_K1,
        FOCAL_LENGTH_RADIAL_K1_K2, FOCAL_LENGTH_PRINCIPAL_POINT_RADIAL_K1_K2,
        FOCAL_LENGTH_PRINCIPAL_POINT, RADIAL_K1_K2]'''
        return str()
    @property
    def distance(self):
        '''(Float) Distance between two bundles used for scene scaling'''
        return float()
    @property
    def clean_frames(self):
        '''(Integer) Effect on tracks which are tracked less than the specified
        amount of frames'''
        return int()
    @property
    def clean_error(self):
        '''(Float) Effect on tracks which have a larger re-projection error'''
        return float()
    @property
    def clean_action(self):
        '''(Enum) Cleanup action to execute
        
        [SELECT, DELETE_TRACK, DELETE_SEGMENTS]'''
        return str()
    @property
    def show_default_expanded(self):
        '''(Boolean) Show default options expanded in the user interface'''
        return bool()
    @property
    def show_extra_expanded(self):
        '''(Boolean) Show extra options expanded in the user interface'''
        return bool()
    @property
    def use_tripod_solver(self):
        '''(Boolean) Use special solver to track a stable camera position, such
        as a tripod'''
        return bool()
    @property
    def default_frames_limit(self):
        '''(Integer) Every tracking cycle, this number of frames are tracked'''
        return int()
    @property
    def default_pattern_match(self):
        '''(Enum) Track pattern from given frame when tracking marker to next
        frame
        
        [KEYFRAME, PREV_FRAME]'''
        return str()
    @property
    def default_margin(self):
        '''(Integer) Default distance from image boundary at which marker stops
        tracking'''
        return int()
    @property
    def default_motion_model(self):
        '''(Enum) Default motion model to use for tracking
        
        [Perspective, Affine, LocRotScale, LocScale, LocRot, Loc]'''
        return str()
    @property
    def use_default_brute(self):
        '''(Boolean) Use a brute-force translation-only initialization when
        tracking'''
        return bool()
    @property
    def use_default_mask(self):
        '''(Boolean) Use a grease pencil datablock as a mask to use only
        specified areas of pattern when tracking'''
        return bool()
    @property
    def use_default_normalization(self):
        '''(Boolean) Normalize light intensities while tracking (slower)'''
        return bool()
    @property
    def default_correlation_min(self):
        '''(Float) Default minimum value of correlation between matched pattern
        and reference that is still treated as successful tracking'''
        return float()
    @property
    def default_pattern_size(self):
        '''(Integer) Size of pattern area for newly created tracks'''
        return int()
    @property
    def default_search_size(self):
        '''(Integer) Size of search area for newly created tracks'''
        return int()
    @property
    def use_default_red_channel(self):
        '''(Boolean) Use red channel from footage for tracking'''
        return bool()
    @property
    def use_default_green_channel(self):
        '''(Boolean) Use green channel from footage for tracking'''
        return bool()
    @property
    def use_default_blue_channel(self):
        '''(Boolean) Use blue channel from footage for tracking'''
        return bool()
    @property
    def default_weight(self):
        '''(Float) Influence of newly created track on a final solution'''
        return float()
    @property
    def object_distance(self):
        '''(Float) Distance between two bundles used for object scaling'''
        return float()