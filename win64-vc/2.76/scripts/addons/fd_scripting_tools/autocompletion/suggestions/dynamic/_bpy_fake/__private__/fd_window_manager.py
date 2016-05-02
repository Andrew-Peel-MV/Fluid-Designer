from . blend_file import blend_file
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class fd_window_manager(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def show_standalone_ui(self):
        '''(Boolean) This shows all of the standalone UI elements. This property
        is only set to False when Fluid Designer is opened from a separate
        application.'''
        return bool()
    @property
    def object_library_path(self):
        '''(String)'''
        return str()
    @property
    def wall_rotation(self):
        '''(Float) Used to store the walls rotation'''
        return float()
    @property
    def data_from_libs(self):
        '''(Sequence of blend_file)'''
        return (blend_file(),)
    @property
    def library_module_path(self):
        '''(String)'''
        return str()
    @property
    def assembly_library_path(self):
        '''(String)'''
        return str()
    @property
    def insert_library_path(self):
        '''(String)'''
        return str()
    @property
    def scene_library_path(self):
        '''(String)'''
        return str()
    @property
    def product_library_path(self):
        '''(String)'''
        return str()
    @property
    def project_templates(self):
        '''(Enum)'''
        return str()
    @property
    def use_opengl_dimensions(self):
        '''(Boolean) Use OpenGL Dimensions'''
        return bool()
    @property
    def project_template_path(self):
        '''(String)'''
        return str()
    @property
    def elevation_scene_index(self):
        '''(Integer)'''
        return int()
    @property
    def material_library_path(self):
        '''(String)'''
        return str()
    @property
    def world_library_path(self):
        '''(String)'''
        return str()
    @property
    def project_path(self):
        '''(String)'''
        return str()