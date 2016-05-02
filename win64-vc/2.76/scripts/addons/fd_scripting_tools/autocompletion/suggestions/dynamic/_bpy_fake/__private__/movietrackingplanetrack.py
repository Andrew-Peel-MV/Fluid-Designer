from . struct import Struct
from . image import Image
from . movietrackingplanemarkers import MovieTrackingPlaneMarkers
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingPlaneTrack(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name of track'''
        return str()
    @property
    def markers(self):
        '''(Sequence of MovieTrackingPlaneMarker) Collection of markers in track'''
        return MovieTrackingPlaneMarkers()
    @property
    def select(self):
        '''(Boolean) Plane track is selected'''
        return bool()
    @property
    def use_auto_keying(self):
        '''(Boolean) Automatic keyframe insertion when moving plane corners'''
        return bool()
    @property
    def image(self):
        '''(Image) Image displayed in the track during editing in clip editor'''
        return Image()
    @property
    def image_opacity(self):
        '''(Float) Opacity of the image'''
        return float()