from . struct import Struct
from . movietrackingtrack import MovieTrackingTrack
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingStabilization(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_2d_stabilization(self):
        '''(Boolean) Use 2D stabilization for footage'''
        return bool()
    @property
    def tracks(self):
        '''(Sequence of MovieTrackingTrack) Collection of tracks used for
        stabilization'''
        return (MovieTrackingTrack(),)
    @property
    def rotation_track(self):
        '''(MovieTrackingTrack) Track used to compensate rotation'''
        return MovieTrackingTrack()
    @property
    def active_track_index(self):
        '''(Integer) Index of active track in stabilization tracks list'''
        return int()
    @property
    def use_autoscale(self):
        '''(Boolean) Automatically scale footage to cover unfilled areas when
        stabilizing'''
        return bool()
    @property
    def scale_max(self):
        '''(Float) Limit the amount of automatic scaling'''
        return float()
    @property
    def influence_location(self):
        '''(Float) Influence of stabilization algorithm on footage location'''
        return float()
    @property
    def influence_scale(self):
        '''(Float) Influence of stabilization algorithm on footage scale'''
        return float()
    @property
    def use_stabilize_rotation(self):
        '''(Boolean) Stabilize horizon line on the shot'''
        return bool()
    @property
    def influence_rotation(self):
        '''(Float) Influence of stabilization algorithm on footage rotation'''
        return float()
    @property
    def filter_type(self):
        '''(Enum) Method to use to filter stabilization
        
        [NEAREST, BILINEAR, BICUBIC]'''
        return str()