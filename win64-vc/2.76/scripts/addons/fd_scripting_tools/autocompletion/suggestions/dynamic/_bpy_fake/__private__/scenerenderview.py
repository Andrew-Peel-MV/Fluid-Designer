from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SceneRenderView(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Render view name'''
        return str()
    @property
    def file_suffix(self):
        '''(String) Suffix added to the render images for this view'''
        return str()
    @property
    def camera_suffix(self):
        '''(String) Suffix to identify the cameras to use, and added to the
        render images for this view'''
        return str()
    @property
    def use(self):
        '''(Boolean) Disable or enable the render view'''
        return bool()