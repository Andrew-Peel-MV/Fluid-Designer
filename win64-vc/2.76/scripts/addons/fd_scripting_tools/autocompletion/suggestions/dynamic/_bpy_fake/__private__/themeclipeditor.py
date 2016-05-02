from . themespacelistgeneric import ThemeSpaceListGeneric
from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeClipEditor(bpy_struct):
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
    def marker_outline(self):
        '''(Vector 3D) Color of marker's outline'''
        return mathutils.Vector()
    @property
    def marker(self):
        '''(Vector 3D) Color of marker'''
        return mathutils.Vector()
    @property
    def active_marker(self):
        '''(Vector 3D) Color of active marker'''
        return mathutils.Vector()
    @property
    def selected_marker(self):
        '''(Vector 3D) Color of selected marker'''
        return mathutils.Vector()
    @property
    def disabled_marker(self):
        '''(Vector 3D) Color of disabled marker'''
        return mathutils.Vector()
    @property
    def locked_marker(self):
        '''(Vector 3D) Color of locked marker'''
        return mathutils.Vector()
    @property
    def path_before(self):
        '''(Vector 3D) Color of path before current frame'''
        return mathutils.Vector()
    @property
    def path_after(self):
        '''(Vector 3D) Color of path after current frame'''
        return mathutils.Vector()
    @property
    def frame_current(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def strips(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def strips_selected(self):
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