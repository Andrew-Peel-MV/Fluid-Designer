from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ImageUser(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_auto_refresh(self):
        '''(Boolean) Always refresh image on frame changes'''
        return bool()
    @property
    def frame_current(self):
        '''(Integer) Current frame number in image sequence or movie'''
        return int()
    @property
    def use_cyclic(self):
        '''(Boolean) Cycle the images in the movie'''
        return bool()
    @property
    def frame_duration(self):
        '''(Integer) Number of images of a movie to use'''
        return int()
    @property
    def frame_offset(self):
        '''(Integer) Offset the number of the frame to use in the animation'''
        return int()
    @property
    def frame_start(self):
        '''(Integer) Global starting frame of the movie/sequence, assuming first
        picture has a #1'''
        return int()
    @property
    def fields_per_frame(self):
        '''(Integer) Number of fields per rendered frame (2 fields is 1 image)'''
        return int()
    @property
    def multilayer_layer(self):
        '''(Integer) Layer in multilayer image'''
        return int()
    @property
    def multilayer_pass(self):
        '''(Integer) Pass in multilayer image'''
        return int()
    @property
    def multilayer_view(self):
        '''(Integer) View in multilayer image'''
        return int()