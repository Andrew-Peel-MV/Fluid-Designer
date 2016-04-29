from . movietrackingobject import MovieTrackingObject
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingObjects(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MovieTrackingObject) Active object in this tracking data object'''
        return MovieTrackingObject()
    def new(self, name):
        '''Add tracking object to this movie clip
        
        Parameter:
          name: (String) Name of new object
        
        Returns:
          object: (MovieTrackingObject) New motion tracking object'''
        return MovieTrackingObject()
    def remove(self, object):
        '''Remove tracking object from this movie clip
        
        Parameter:
          object: (MovieTrackingObject) Motion tracking object to be removed'''
        return 
    def get(key): return MovieTrackingObject()
    def __getitem__(key): return MovieTrackingObject()
    def __iter__(key): yield MovieTrackingObject()