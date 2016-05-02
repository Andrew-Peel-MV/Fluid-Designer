from . struct import Struct
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class TimelineMarker(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def frame(self):
        '''(Integer) The frame on which the timeline marker appears'''
        return int()
    @property
    def select(self):
        '''(Boolean) Marker selection state'''
        return bool()
    @property
    def camera(self):
        '''(Object) Camera this timeline sets to active'''
        return Object()