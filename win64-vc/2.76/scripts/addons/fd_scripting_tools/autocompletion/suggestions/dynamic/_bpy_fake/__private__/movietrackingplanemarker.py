from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingPlaneMarker(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def frame(self):
        '''(Integer) Frame number marker is keyframed on'''
        return int()
    @property
    def corners(self):
        '''(Float[8]) Array of coordinates which represents UI rectangle corners
        in frame normalized coordinates'''
        return ''
    @property
    def mute(self):
        '''(Boolean) Is marker muted for current frame'''
        return bool()