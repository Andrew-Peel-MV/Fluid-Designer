from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeSequenceEditor(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()
    @property
    def gp_vertex(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def gp_vertex_select(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def gp_vertex_size(self):
        '''(Integer)'''
        return int()
    @property
    def grid(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def window_sliders(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def movie_strip(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def movieclip_strip(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def image_strip(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def scene_strip(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def audio_strip(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def effect_strip(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def transition_strip(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def meta_strip(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def frame_current(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def keyframe(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def draw_action(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def preview_back(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def metadatabg(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def metadatatext(self):
        '''(Vector 3D)'''
        return mathutils.Vector()