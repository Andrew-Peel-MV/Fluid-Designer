from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class RegionView3D(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def lock_rotation(self):
        '''(Boolean) Lock view rotation in side views'''
        return bool()
    @property
    def show_sync_view(self):
        '''(Boolean) Sync view position between side views'''
        return bool()
    @property
    def use_box_clip(self):
        '''(Boolean) Clip objects based on what's visible in other side views'''
        return bool()
    @property
    def perspective_matrix(self):
        '''(Matrix) Current perspective matrix (``window_matrix * view_matrix``)'''
        return mathutils.Matrix()
    @property
    def window_matrix(self):
        '''(Matrix) Current window matrix'''
        return mathutils.Matrix()
    @property
    def view_matrix(self):
        '''(Matrix) Current view matrix'''
        return mathutils.Matrix()
    @property
    def view_perspective(self):
        '''(Enum) View Perspective
        
        [PERSP, ORTHO, CAMERA]'''
        return str()
    @property
    def is_perspective(self):
        '''(Boolean)'''
        return bool()
    @property
    def view_location(self):
        '''(Vector 3D) View pivot location'''
        return mathutils.Vector()
    @property
    def view_rotation(self):
        '''(Float[4]) Rotation in quaternions (keep normalized)'''
        return ''
    @property
    def view_distance(self):
        '''(Float) Distance to the view location'''
        return float()
    @property
    def view_camera_zoom(self):
        '''(Float) Zoom factor in camera view'''
        return float()
    @property
    def view_camera_offset(self):
        '''(Vector 2D) View shift in camera view'''
        return mathutils.Vector()
    def update(self):
        '''Recalculate the view matrices'''
        return 