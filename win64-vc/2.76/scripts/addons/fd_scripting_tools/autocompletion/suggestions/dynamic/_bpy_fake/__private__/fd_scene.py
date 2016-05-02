from . struct import Struct
from . project_property import Project_Property
from . opengl_dim import opengl_dim
from . fd_item import fd_item
from . fd_interface import fd_interface
from . bpy_struct import bpy_struct
import mathutils

class fd_scene(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def initial_view_location(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def elevation_selected(self):
        '''(Boolean)'''
        return bool()
    @property
    def world_library_name(self):
        '''(String) Used to determine what world library is active.'''
        return str()
    @property
    def insert_library_name(self):
        '''(String) Used to determine what insert library is active.'''
        return str()
    @property
    def initial_shade_mode(self):
        '''(String)'''
        return str()
    @property
    def product_category_name(self):
        '''(String) Used to determine what product category is active.'''
        return str()
    @property
    def material_library_name(self):
        '''(String) Used to determine what material library is active.'''
        return str()
    @property
    def object_category_name(self):
        '''(String) Used to determine what object category is active.'''
        return str()
    @property
    def insert_category_name(self):
        '''(String) Used to determine what insert category is active.'''
        return str()
    @property
    def assembly_library_name(self):
        '''(String) Used to determine what assembly library is active.'''
        return str()
    @property
    def opengl_dim(self):
        '''(opengl_dim)'''
        return opengl_dim()
    @property
    def product_library_name(self):
        '''(String) Used to determine what product library is active.'''
        return str()
    @property
    def name_scene(self):
        '''(String) This is the readable name of the scene'''
        return str()
    @property
    def assembly_category_name(self):
        '''(String) Used to determine what assembly category is active.'''
        return str()
    @property
    def scene_library_name(self):
        '''(String) Used to determine what scene library is active.'''
        return str()
    @property
    def world_category_name(self):
        '''(String) Used to determine what world category is active.'''
        return str()
    @property
    def elevation_img_name(self):
        '''(String)'''
        return str()
    @property
    def active_object_index(self):
        '''(Integer) Used is list views to select an object in the
        children_objects collection'''
        return int()
    @property
    def active_object_name(self):
        '''(String) Used to make sure that the correct collection is being
        displayed this is set in the load child objects operator.'''
        return str()
    @property
    def default_wall_depth(self):
        '''(Float) Enter the default depth when drawings walls'''
        return float()
    @property
    def children_objects(self):
        '''(Sequence of fd_item) Collection of all of the children objects of a
        group. Used to display in a list view.'''
        return (fd_item(),)
    @property
    def scene_category_name(self):
        '''(String) Used to determine what scene category is active.'''
        return str()
    @property
    def initial_view_rotation(self):
        '''(Float[4])'''
        return ''
    @property
    def elevation_scene(self):
        '''(Boolean) Scene used for rendering elevations'''
        return bool()
    @property
    def active_addon_name(self):
        '''(String) Used to determine what the addon is active.'''
        return str()
    @property
    def object_library_name(self):
        '''(String) Used to determine what object library is active.'''
        return str()
    @property
    def material_category_name(self):
        '''(String) Used to determine what material category is active.'''
        return str()
    @property
    def project_properties(self):
        '''(Sequence of Project_Property) Collection of all of the User Defined
        Project Properties'''
        return (Project_Property(),)
    @property
    def default_wall_height(self):
        '''(Float) Enter the default height when drawings walls'''
        return float()
    @property
    def ui(self):
        '''(fd_interface)'''
        return fd_interface()
    @property
    def plan_view_scene(self):
        '''(Boolean) Scene used for rendering project plan view'''
        return bool()