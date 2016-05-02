from . themespacelistgeneric import ThemeSpaceListGeneric
from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeDopeSheet(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGeneric) Settings for space'''
        return ThemeSpaceGeneric()
    @property
    def space_list(self):
        '''(ThemeSpaceListGeneric) Settings for space list'''
        return ThemeSpaceListGeneric()
    @property
    def grid(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def frame_current(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def value_sliders(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def view_sliders(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def dopesheet_channel(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def dopesheet_subchannel(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def channels(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def channels_selected(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def channel_group(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def active_channels_group(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def long_key(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def long_key_selected(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def keyframe(self):
        '''(Vector 3D) Color of Keyframe'''
        return mathutils.Vector()
    @property
    def keyframe_selected(self):
        '''(Vector 3D) Color of selected keyframe'''
        return mathutils.Vector()
    @property
    def keyframe_extreme(self):
        '''(Vector 3D) Color of extreme keyframe'''
        return mathutils.Vector()
    @property
    def keyframe_extreme_selected(self):
        '''(Vector 3D) Color of selected extreme keyframe'''
        return mathutils.Vector()
    @property
    def keyframe_breakdown(self):
        '''(Vector 3D) Color of breakdown keyframe'''
        return mathutils.Vector()
    @property
    def keyframe_breakdown_selected(self):
        '''(Vector 3D) Color of selected breakdown keyframe'''
        return mathutils.Vector()
    @property
    def keyframe_jitter(self):
        '''(Vector 3D) Color of jitter keyframe'''
        return mathutils.Vector()
    @property
    def keyframe_jitter_selected(self):
        '''(Vector 3D) Color of selected jitter keyframe'''
        return mathutils.Vector()
    @property
    def keyframe_border(self):
        '''(Float[4]) Color of keyframe border'''
        return ''
    @property
    def keyframe_border_selected(self):
        '''(Float[4]) Color of selected keyframe border'''
        return ''
    @property
    def summary(self):
        '''(Float[4]) Color of summary channel'''
        return ''