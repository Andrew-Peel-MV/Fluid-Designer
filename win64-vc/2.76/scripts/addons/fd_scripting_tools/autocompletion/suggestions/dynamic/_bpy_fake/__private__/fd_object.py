from . mvpromptpage import mvPromptPage
from . struct import Struct
from . opengl_dim import opengl_dim
from . bpy_struct import bpy_struct
import mathutils

class fd_object(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def type(self):
        '''(Enum) Select the Object Type.
        
        [NONE, CAGE, VPDIMX, VPDIMY, VPDIMZ, EMPTY1, EMPTY2, EMPTY3, BPWALL,
        BPASSEMBLY, VISDIM_A, VISDIM_B]'''
        return str()
    @property
    def property_id(self):
        '''(String) This property allows objects to display a custom property
        page. This is the operator bl_id.'''
        return str()
    @property
    def use_as_bool_obj(self):
        '''(Boolean) Use this object cut a hole in the selected mesh'''
        return bool()
    @property
    def opengl_dim(self):
        '''(opengl_dim)'''
        return opengl_dim()
    @property
    def PromptPage(self):
        '''(mvPromptPage) Custom properties assigned to the object. Only access
        from base point object.'''
        return mvPromptPage()
    @property
    def use_as_mesh_hook(self):
        '''(Boolean) Use this object to hook to deform a mesh. Only for Empties'''
        return bool()
    @property
    def name_object(self):
        '''(String) This is the readable name of the object'''
        return str()