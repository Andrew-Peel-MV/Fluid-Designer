from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class AnimVizMotionPaths(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Type of range to show for Motion Paths
        
        [CURRENT_FRAME, RANGE]'''
        return str()
    @property
    def bake_location(self):
        '''(Enum) When calculating Bone Paths, use Head or Tips
        
        [HEADS, TAILS]'''
        return str()
    @property
    def show_frame_numbers(self):
        '''(Boolean) Show frame numbers on Motion Paths'''
        return bool()
    @property
    def show_keyframe_highlight(self):
        '''(Boolean) Emphasize position of keyframes on Motion Paths'''
        return bool()
    @property
    def show_keyframe_numbers(self):
        '''(Boolean) Show frame numbers of Keyframes on Motion Paths'''
        return bool()
    @property
    def show_keyframe_action_all(self):
        '''(Boolean) For bone motion paths, search whole Action for keyframes
        instead of in group with matching name only (is slower)'''
        return bool()
    @property
    def frame_step(self):
        '''(Integer) Number of frames between paths shown (not for 'On Keyframes'
        Onion-skinning method)'''
        return int()
    @property
    def frame_start(self):
        '''(Integer) Starting frame of range of paths to display/calculate (not
        for 'Around Current Frame' Onion-skinning method)'''
        return int()
    @property
    def frame_end(self):
        '''(Integer) End frame of range of paths to display/calculate (not for
        'Around Current Frame' Onion-skinning method)'''
        return int()
    @property
    def frame_before(self):
        '''(Integer) Number of frames to show before the current frame (only for
        'Around Current Frame' Onion-skinning method)'''
        return int()
    @property
    def frame_after(self):
        '''(Integer) Number of frames to show after the current frame (only for
        'Around Current Frame' Onion-skinning method)'''
        return int()