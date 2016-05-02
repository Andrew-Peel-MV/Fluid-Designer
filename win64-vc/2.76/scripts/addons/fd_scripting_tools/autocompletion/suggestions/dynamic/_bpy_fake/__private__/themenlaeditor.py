from . themespacelistgeneric import ThemeSpaceListGeneric
from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeNLAEditor(bpy_struct):
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
    def view_sliders(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def active_action(self):
        '''(Float[4]) Animation data block has active action'''
        return ''
    @property
    def active_action_unset(self):
        '''(Float[4]) Animation data block doesn't have active action'''
        return ''
    @property
    def strips(self):
        '''(Vector 3D) Action-Clip Strip - Unselected'''
        return mathutils.Vector()
    @property
    def strips_selected(self):
        '''(Vector 3D) Action-Clip Strip - Selected'''
        return mathutils.Vector()
    @property
    def transition_strips(self):
        '''(Vector 3D) Transition Strip - Unselected'''
        return mathutils.Vector()
    @property
    def transition_strips_selected(self):
        '''(Vector 3D) Transition Strip - Selected'''
        return mathutils.Vector()
    @property
    def meta_strips(self):
        '''(Vector 3D) Meta Strip - Unselected (for grouping related strips)'''
        return mathutils.Vector()
    @property
    def meta_strips_selected(self):
        '''(Vector 3D) Meta Strip - Selected (for grouping related strips)'''
        return mathutils.Vector()
    @property
    def sound_strips(self):
        '''(Vector 3D) Sound Strip - Unselected (for timing speaker sounds)'''
        return mathutils.Vector()
    @property
    def sound_strips_selected(self):
        '''(Vector 3D) Sound Strip - Selected (for timing speaker sounds)'''
        return mathutils.Vector()
    @property
    def tweak(self):
        '''(Vector 3D) Color for strip/action being 'tweaked' or edited'''
        return mathutils.Vector()
    @property
    def tweak_duplicate(self):
        '''(Vector 3D) Warning/error indicator color for strips referencing the
        strip being tweaked'''
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
    def frame_current(self):
        '''(Vector 3D)'''
        return mathutils.Vector()