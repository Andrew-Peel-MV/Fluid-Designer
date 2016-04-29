from . movietrackingmarker import MovieTrackingMarker
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingMarkers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def find_frame(self, frame, exact):
        '''Get marker for specified frame
        
        Parameter:
          frame: (Integer) Frame number to find marker for
          exact:
            (Boolean) Get marker at exact frame number rather than get estimated
            marker
        
        Returns:
          marker: (MovieTrackingMarker) Marker for specified frame'''
        return MovieTrackingMarker()
    def insert_frame(self, frame, co):
        '''Insert a new marker at the specified frame
        
        Parameter:
          frame: (Integer) Frame number to insert marker to
          co:
            (Vector 2D) Place new marker at the given frame using specified in
            normalized space coordinates
        
        Returns:
          marker: (MovieTrackingMarker) Newly created marker'''
        return MovieTrackingMarker()
    def delete_frame(self, frame):
        '''Delete marker at specified frame
        
        Parameter:
          frame: (Integer) Frame number to delete marker from'''
        return 
    def get(key): return MovieTrackingMarker()
    def __getitem__(key): return MovieTrackingMarker()
    def __iter__(key): yield MovieTrackingMarker()