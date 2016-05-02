from . movietrackingplanetrack import MovieTrackingPlaneTrack
from . struct import Struct
from . movietrackingtrack import MovieTrackingTrack
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingObjectPlaneTracks(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MovieTrackingTrack) Active track in this tracking data object'''
        return MovieTrackingTrack()
    def get(key): return MovieTrackingPlaneTrack()
    def __getitem__(key): return MovieTrackingPlaneTrack()
    def __iter__(key): yield MovieTrackingPlaneTrack()