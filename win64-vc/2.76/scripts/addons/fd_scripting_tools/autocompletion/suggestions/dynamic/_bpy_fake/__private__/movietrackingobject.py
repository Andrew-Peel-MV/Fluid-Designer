from . struct import Struct
from . movietrackingobjectplanetracks import MovieTrackingObjectPlaneTracks
from . movietrackingreconstruction import MovieTrackingReconstruction
from . movietrackingobjecttracks import MovieTrackingObjectTracks
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingObject(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name of object'''
        return str()
    @property
    def is_camera(self):
        '''(Boolean) Object is used for camera tracking'''
        return bool()
    @property
    def tracks(self):
        '''(Sequence of MovieTrackingTrack) Collection of tracks in this tracking
        data object'''
        return MovieTrackingObjectTracks()
    @property
    def plane_tracks(self):
        '''(Sequence of MovieTrackingPlaneTrack) Collection of plane tracks in
        this tracking data object'''
        return MovieTrackingObjectPlaneTracks()
    @property
    def reconstruction(self):
        '''(MovieTrackingReconstruction)'''
        return MovieTrackingReconstruction()
    @property
    def scale(self):
        '''(Float) Scale of object solution in camera space'''
        return float()
    @property
    def keyframe_a(self):
        '''(Integer) First keyframe used for reconstruction initialization'''
        return int()
    @property
    def keyframe_b(self):
        '''(Integer) Second keyframe used for reconstruction initialization'''
        return int()