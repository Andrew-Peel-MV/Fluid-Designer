from . timelinemarker import TimelineMarker
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ActionPoseMarkers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(TimelineMarker) Active pose marker for this action'''
        return TimelineMarker()
    @property
    def active_index(self):
        '''(Integer) Index of active pose marker'''
        return int()
    def new(self, name):
        '''Add a pose marker to the action
        
        Parameter:
          name: (String) New name for the marker (not unique)
        
        Returns:
          marker: (TimelineMarker) Newly created marker'''
        return TimelineMarker()
    def remove(self, marker):
        '''Remove a timeline marker
        
        Parameter:
          marker: (TimelineMarker) Timeline marker to remove'''
        return 
    def get(key): return TimelineMarker()
    def __getitem__(key): return TimelineMarker()
    def __iter__(key): yield TimelineMarker()