from . movietrackingplanemarker import MovieTrackingPlaneMarker
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingPlaneMarkers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def find_frame(self, frame, exact):
        '''Get plane marker for specified frame
        
        Parameter:
          frame: (Integer) Frame number to find marker for
          exact:
            (Boolean) Get plane marker at exact frame number rather than get
            estimated marker
        
        Returns:
          plane_marker: (MovieTrackingPlaneMarker) Plane marker for specified frame'''
        return MovieTrackingPlaneMarker()
    def insert_frame(self, frame):
        '''Insert a new plane marker at the specified frame
        
        Parameter:
          frame: (Integer) Frame number to insert marker to
        
        Returns:
          plane_marker: (MovieTrackingPlaneMarker) Newly created plane marker'''
        return MovieTrackingPlaneMarker()
    def delete_frame(self, frame):
        '''Delete plane marker at specified frame
        
        Parameter:
          frame: (Integer) Frame number to delete plane marker from'''
        return 
    def get(key): return MovieTrackingPlaneMarker()
    def __getitem__(key): return MovieTrackingPlaneMarker()
    def __iter__(key): yield MovieTrackingPlaneMarker()