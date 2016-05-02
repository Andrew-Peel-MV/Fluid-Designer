from . movietrackingobjects import MovieTrackingObjects
from . movietrackingsettings import MovieTrackingSettings
from . movietrackingplanetracks import MovieTrackingPlaneTracks
from . movietrackingstabilization import MovieTrackingStabilization
from . struct import Struct
from . movietrackingtracks import MovieTrackingTracks
from . movietrackingdopesheet import MovieTrackingDopesheet
from . movietrackingreconstruction import MovieTrackingReconstruction
from . movietrackingcamera import MovieTrackingCamera
from . bpy_struct import bpy_struct
import mathutils

class MovieTracking(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def settings(self):
        '''(MovieTrackingSettings)'''
        return MovieTrackingSettings()
    @property
    def camera(self):
        '''(MovieTrackingCamera)'''
        return MovieTrackingCamera()
    @property
    def tracks(self):
        '''(Sequence of MovieTrackingTrack) Collection of tracks in this tracking
        data object'''
        return MovieTrackingTracks()
    @property
    def plane_tracks(self):
        '''(Sequence of MovieTrackingPlaneTrack) Collection of plane tracks in
        this tracking data object'''
        return MovieTrackingPlaneTracks()
    @property
    def stabilization(self):
        '''(MovieTrackingStabilization)'''
        return MovieTrackingStabilization()
    @property
    def reconstruction(self):
        '''(MovieTrackingReconstruction)'''
        return MovieTrackingReconstruction()
    @property
    def objects(self):
        '''(Sequence of MovieTrackingObject) Collection of objects in this
        tracking data object'''
        return MovieTrackingObjects()
    @property
    def active_object_index(self):
        '''(Integer) Index of active object'''
        return int()
    @property
    def dopesheet(self):
        '''(MovieTrackingDopesheet)'''
        return MovieTrackingDopesheet()