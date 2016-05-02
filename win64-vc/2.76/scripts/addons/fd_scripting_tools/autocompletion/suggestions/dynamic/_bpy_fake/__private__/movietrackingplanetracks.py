from . movietrackingplanetrack import MovieTrackingPlaneTrack
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingPlaneTracks(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MovieTrackingPlaneTrack) Active plane track in this tracking data
        object'''
        return MovieTrackingPlaneTrack()
    def get(key): return MovieTrackingPlaneTrack()
    def __getitem__(key): return MovieTrackingPlaneTrack()
    def __iter__(key): yield MovieTrackingPlaneTrack()