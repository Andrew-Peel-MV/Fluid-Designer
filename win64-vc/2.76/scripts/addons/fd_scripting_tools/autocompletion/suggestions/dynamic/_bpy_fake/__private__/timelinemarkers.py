from . timelinemarker import TimelineMarker
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class TimelineMarkers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name, frame):
        '''Add a keyframe to the curve
        
        Parameter:
          name: (String) New name for the marker (not unique)
          frame: (Integer) The frame for the new marker
        
        Returns:
          marker: (TimelineMarker) Newly created timeline marker'''
        return TimelineMarker()
    def remove(self, marker):
        '''Remove a timeline marker
        
        Parameter:
          marker: (TimelineMarker) Timeline marker to remove'''
        return 
    def clear(self):
        '''Remove all timeline markers'''
        return 
    def get(key): return TimelineMarker()
    def __getitem__(key): return TimelineMarker()
    def __iter__(key): yield TimelineMarker()