from . struct import Struct
from . themespacegeneric import ThemeSpaceGeneric
from . bpy_struct import bpy_struct
import mathutils

class ThemeImageEditor(bpy_struct):
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
    def face(self):
        '''(Float[4])'''
        return ''
    @property
    def face_select(self):
        '''(Float[4])'''
        return ''
    @property
    def face_dot(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def facedot_size(self):
        '''(Integer)'''
        return int()
    @property
    def freestyle_face_mark(self):
        '''(Float[4])'''
        return ''
    @property
    def editmesh_active(self):
        '''(Float[4])'''
        return ''
    @property
    def wire_edit(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def edge_select(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def scope_back(self):
        '''(Float[4])'''
        return ''
    @property
    def preview_stitch_face(self):
        '''(Float[4])'''
        return ''
    @property
    def preview_stitch_edge(self):
        '''(Float[4])'''
        return ''
    @property
    def preview_stitch_vert(self):
        '''(Float[4])'''
        return ''
    @property
    def preview_stitch_stitchable(self):
        '''(Float[4])'''
        return ''
    @property
    def preview_stitch_unstitchable(self):
        '''(Float[4])'''
        return ''
    @property
    def preview_stitch_active(self):
        '''(Float[4])'''
        return ''
    @property
    def uv_shadow(self):
        '''(Float[4])'''
        return ''
    @property
    def uv_others(self):
        '''(Float[4])'''
        return ''
    @property
    def frame_current(self):
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
    @property
    def paint_curve_handle(self):
        '''(Float[4])'''
        return ''
    @property
    def paint_curve_pivot(self):
        '''(Float[4])'''
        return ''