from . struct import Struct
from . movietrackingtrack import MovieTrackingTrack
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingTracks(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MovieTrackingTrack) Active track in this tracking data object'''
        return MovieTrackingTrack()
    def new(self, name, frame):
        '''Create new motion track in this movie clip
        
        Parameter:
          name: (String) Name of new track
          frame: (Integer) Frame number to add track on
        
        Returns:
          track: (MovieTrackingTrack) Newly created track'''
        return MovieTrackingTrack()
    def get(key): return MovieTrackingTrack()
    def __getitem__(key): return MovieTrackingTrack()
    def __iter__(key): yield MovieTrackingTrack()