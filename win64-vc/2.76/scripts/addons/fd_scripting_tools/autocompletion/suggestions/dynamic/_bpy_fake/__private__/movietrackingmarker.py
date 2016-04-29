from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingMarker(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def co(self):
        '''(Vector 2D) Marker position at frame in normalized coordinates'''
        return mathutils.Vector()
    @property
    def frame(self):
        '''(Integer) Frame number marker is keyframed on'''
        return int()
    @property
    def mute(self):
        '''(Boolean) Is marker muted for current frame'''
        return bool()
    @property
    def pattern_corners(self):
        '''(Float[8]) Array of coordinates which represents pattern's corners in
        normalized coordinates relative to marker position'''
        return ''
    @property
    def pattern_bound_box(self):
        '''(Float[4]) Pattern area bounding box in normalized coordinates'''
        return ''
    @property
    def search_min(self):
        '''(Vector 2D) Left-bottom corner of search area in normalized
        coordinates relative to marker position'''
        return mathutils.Vector()
    @property
    def search_max(self):
        '''(Vector 2D) Right-bottom corner of search area in normalized
        coordinates relative to marker position'''
        return mathutils.Vector()
    @property
    def is_keyed(self):
        '''(Boolean) Whether the position of the marker is keyframed or tracked'''
        return bool()