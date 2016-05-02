from . themespacelistgeneric import ThemeSpaceListGeneric
from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeNodeEditor(bpy_struct):
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
    def node_selected(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def node_active(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def wire(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def wire_inner(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def wire_select(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def selected_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def node_backdrop(self):
        '''(Float[4])'''
        return ''
    @property
    def converter_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def color_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def group_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def group_socket_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def frame_node(self):
        '''(Float[4])'''
        return ''
    @property
    def matte_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def distor_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def noodle_curving(self):
        '''(Integer) Curving of the noodle'''
        return int()
    @property
    def input_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def output_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def filter_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def vector_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def texture_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def shader_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def script_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def pattern_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def layout_node(self):
        '''(Vector 3D)'''
        return mathutils.Vector()