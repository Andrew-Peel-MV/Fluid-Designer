from . struct import Struct
from . gpencilframes import GPencilFrames
from . gpencilframe import GPencilFrame
from . bpy_struct import bpy_struct
import mathutils

class GPencilLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def info(self):
        '''(String) Layer name'''
        return str()
    @property
    def frames(self):
        '''(Sequence of GPencilFrame) Sketches for this layer on different frames'''
        return GPencilFrames()
    @property
    def active_frame(self):
        '''(GPencilFrame) Frame currently being displayed for this layer'''
        return GPencilFrame()
    @property
    def use_volumetric_strokes(self):
        '''(Boolean) Draw strokes as a series of circular blobs, resulting in a
        volumetric effect'''
        return bool()
    @property
    def color(self):
        '''(Vector 3D) Color for all strokes in this layer'''
        return mathutils.Vector()
    @property
    def alpha(self):
        '''(Float) Layer Opacity'''
        return float()
    @property
    def fill_color(self):
        '''(Vector 3D) Color for filling region bounded by each stroke'''
        return mathutils.Vector()
    @property
    def fill_alpha(self):
        '''(Float) Opacity for filling region bounded by each stroke'''
        return float()
    @property
    def line_width(self):
        '''(Integer) Thickness of strokes (in pixels)'''
        return int()
    @property
    def use_onion_skinning(self):
        '''(Boolean) Ghost frames on either side of frame'''
        return bool()
    @property
    def ghost_before_range(self):
        '''(Integer) Maximum number of frames to show before current frame (0 =
        show only the previous sketch)'''
        return int()
    @property
    def ghost_after_range(self):
        '''(Integer) Maximum number of frames to show after current frame (0 =
        show only the next sketch)'''
        return int()
    @property
    def use_ghost_custom_colors(self):
        '''(Boolean) Use custom colors for ghost frames'''
        return bool()
    @property
    def before_color(self):
        '''(Vector 3D) Base color for ghosts before the active frame'''
        return mathutils.Vector()
    @property
    def after_color(self):
        '''(Vector 3D) Base color for ghosts after the active frame'''
        return mathutils.Vector()
    @property
    def hide(self):
        '''(Boolean) Set layer Visibility'''
        return bool()
    @property
    def lock(self):
        '''(Boolean) Protect layer from further editing and/or frame changes'''
        return bool()
    @property
    def lock_frame(self):
        '''(Boolean) Lock current frame displayed by layer'''
        return bool()
    @property
    def select(self):
        '''(Boolean) Layer is selected for editing in the Dope Sheet'''
        return bool()
    @property
    def show_points(self):
        '''(Boolean) Draw the points which make up the strokes (for debugging
        purposes)'''
        return bool()
    @property
    def show_x_ray(self):
        '''(Boolean) Make the layer draw in front of objects'''
        return bool()
    @property
    def is_stroke_visible(self):
        '''(Boolean) True when opacity of stroke is set high enough to be visible'''
        return bool()
    @property
    def is_fill_visible(self):
        '''(Boolean) True when opacity of fill is set high enough to be visible'''
        return bool()
    def clear(self):
        '''Remove all the grease pencil layer data'''
        return 