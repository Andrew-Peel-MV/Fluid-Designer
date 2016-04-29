from . motionpathvert import MotionPathVert
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MotionPath(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def points(self):
        '''(Sequence of MotionPathVert) Cached positions per frame'''
        return (MotionPathVert(),)
    @property
    def frame_start(self):
        '''(Integer) Starting frame of the stored range'''
        return int()
    @property
    def frame_end(self):
        '''(Integer) End frame of the stored range'''
        return int()
    @property
    def length(self):
        '''(Integer) Number of frames cached'''
        return int()
    @property
    def use_bone_head(self):
        '''(Boolean) For PoseBone paths, use the bone head location when
        calculating this path'''
        return bool()
    @property
    def is_modified(self):
        '''(Boolean) Path is being edited'''
        return bool()