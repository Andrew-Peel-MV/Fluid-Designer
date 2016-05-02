from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeTimeline(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()
    @property
    def grid(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def frame_current(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def time_keyframe(self):
        '''(Vector 3D) Base color for keyframe indicator lines'''
        return mathutils.Vector()
    @property
    def time_grease_pencil(self):
        '''(Vector 3D) Color of Grease Pencil keyframes'''
        return mathutils.Vector()