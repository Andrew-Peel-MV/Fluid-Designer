from . movietrackingmarkers import MovieTrackingMarkers
from . greasepencil import GreasePencil
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingTrack(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name of track'''
        return str()
    @property
    def frames_limit(self):
        '''(Integer) Every tracking cycle, this number of frames are tracked'''
        return int()
    @property
    def pattern_match(self):
        '''(Enum) Track pattern from given frame when tracking marker to next
        frame
        
        [KEYFRAME, PREV_FRAME]'''
        return str()
    @property
    def margin(self):
        '''(Integer) Distance from image boundary at which marker stops tracking'''
        return int()
    @property
    def motion_model(self):
        '''(Enum) Default motion model to use for tracking
        
        [Perspective, Affine, LocRotScale, LocScale, LocRot, Loc]'''
        return str()
    @property
    def correlation_min(self):
        '''(Float) Minimal value of correlation between matched pattern and
        reference that is still treated as successful tracking'''
        return float()
    @property
    def use_brute(self):
        '''(Boolean) Use a brute-force translation only pre-track before
        refinement'''
        return bool()
    @property
    def use_mask(self):
        '''(Boolean) Use a grease pencil datablock as a mask to use only
        specified areas of pattern when tracking'''
        return bool()
    @property
    def use_normalization(self):
        '''(Boolean) Normalize light intensities while tracking. Slower'''
        return bool()
    @property
    def markers(self):
        '''(Sequence of MovieTrackingMarker) Collection of markers in track'''
        return MovieTrackingMarkers()
    @property
    def use_red_channel(self):
        '''(Boolean) Use red channel from footage for tracking'''
        return bool()
    @property
    def use_green_channel(self):
        '''(Boolean) Use green channel from footage for tracking'''
        return bool()
    @property
    def use_blue_channel(self):
        '''(Boolean) Use blue channel from footage for tracking'''
        return bool()
    @property
    def use_grayscale_preview(self):
        '''(Boolean) Display what the tracking algorithm sees in the preview'''
        return bool()
    @property
    def use_alpha_preview(self):
        '''(Boolean) Apply track's mask on displaying preview'''
        return bool()
    @property
    def has_bundle(self):
        '''(Boolean) True if track has a valid bundle'''
        return bool()
    @property
    def bundle(self):
        '''(Vector 3D) Position of bundle reconstructed from this track'''
        return mathutils.Vector()
    @property
    def hide(self):
        '''(Boolean) Track is hidden'''
        return bool()
    @property
    def select(self):
        '''(Boolean) Track is selected'''
        return bool()
    @property
    def select_anchor(self):
        '''(Boolean) Track's anchor point is selected'''
        return bool()
    @property
    def select_pattern(self):
        '''(Boolean) Track's pattern area is selected'''
        return bool()
    @property
    def select_search(self):
        '''(Boolean) Track's search area is selected'''
        return bool()
    @property
    def lock(self):
        '''(Boolean) Track is locked and all changes to it are disabled'''
        return bool()
    @property
    def use_custom_color(self):
        '''(Boolean) Use custom color instead of theme-defined'''
        return bool()
    @property
    def color(self):
        '''(Vector 3D) Color of the track in the Movie Clip Editor and the 3D
        viewport after a solve'''
        return mathutils.Vector()
    @property
    def average_error(self):
        '''(Float) Average error of re-projection'''
        return float()
    @property
    def grease_pencil(self):
        '''(GreasePencil) Grease pencil data for this track'''
        return GreasePencil()
    @property
    def weight(self):
        '''(Float) Influence of this track on a final solution'''
        return float()
    @property
    def offset(self):
        '''(Vector 2D) Offset of track from the parenting point'''
        return mathutils.Vector()