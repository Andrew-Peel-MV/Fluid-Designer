from . themespacelistgeneric import ThemeSpaceListGeneric
from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeGraphEditor(bpy_struct):
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
    def window_sliders(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def channels_region(self):
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
    def channel_group(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def active_channels_group(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def vertex(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def vertex_select(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def vertex_size(self):
        '''(Integer)'''
        return int()
    @property
    def vertex_unreferenced(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_free(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_auto(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_vect(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_sel_vect(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_align(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_sel_free(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_sel_auto(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_sel_align(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_auto_clamped(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_sel_auto_clamped(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def lastsel_point(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_vertex(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_vertex_select(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def handle_vertex_size(self):
        '''(Integer)'''
        return int()