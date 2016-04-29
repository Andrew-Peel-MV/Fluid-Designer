from . themespacegradient import ThemeSpaceGradient
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ThemeView3D(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def space(self):
        '''(ThemeSpaceGradient) Settings for space'''
        return ThemeSpaceGradient()
    @property
    def grid(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def wire(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def wire_edit(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
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
    def lamp(self):
        '''(Float[4])'''
        return ''
    @property
    def speaker(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def camera(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def view_overlay(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def empty(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def object_selected(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def object_active(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def object_grouped(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def object_grouped_active(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def transform(self):
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
    def edge_select(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def edge_seam(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def edge_sharp(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def edge_crease(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def edge_facesel(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def freestyle_edge_mark(self):
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
    def nurb_uline(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def nurb_vline(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def nurb_sel_uline(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def nurb_sel_vline(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def act_spline(self):
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
    def lastsel_point(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def extra_edge_len(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def extra_edge_angle(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def extra_face_angle(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def extra_face_area(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def editmesh_active(self):
        '''(Float[4])'''
        return ''
    @property
    def normal(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def vertex_normal(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def split_normal(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def bone_solid(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def bone_pose(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def bone_pose_active(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def frame_current(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def outline_width(self):
        '''(Integer)'''
        return int()
    @property
    def bundle_solid(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def camera_path(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def skin_root(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def clipping_border_3d(self):
        '''(Float[4])'''
        return ''
    @property
    def paint_curve_handle(self):
        '''(Float[4])'''
        return ''
    @property
    def paint_curve_pivot(self):
        '''(Float[4])'''
        return ''