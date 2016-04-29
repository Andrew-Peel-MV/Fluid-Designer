from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class AnimVizOnionSkinning(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Method used for determining what ghosts get drawn
        
        [NONE, CURRENT_FRAME, RANGE, KEYS]'''
        return str()
    @property
    def show_only_selected(self):
        '''(Boolean) For Pose-Mode drawing, only draw ghosts for selected bones'''
        return bool()
    @property
    def frame_step(self):
        '''(Integer) Number of frames between ghosts shown (not for 'On
        Keyframes' Onion-skinning method)'''
        return int()
    @property
    def frame_start(self):
        '''(Integer) Starting frame of range of Ghosts to display (not for
        'Around Current Frame' Onion-skinning method)'''
        return int()
    @property
    def frame_end(self):
        '''(Integer) End frame of range of Ghosts to display (not for 'Around
        Current Frame' Onion-skinning method)'''
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