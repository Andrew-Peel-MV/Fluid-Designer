from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class fd_interface(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def show_debug_tools(self):
        '''(Boolean) Show Debug Tools'''
        return bool()
    @property
    def render_type_tabs(self):
        '''(Enum)
        
        [PRR, NPR]'''
        return str()
    @property
    def use_default_blender_interface(self):
        '''(Boolean) Show Default Blender interface'''
        return bool()
    @property
    def interface_object_tabs(self):
        '''(Enum)
        
        [INFO, DISPLAY, MATERIAL, CONSTRAINTS, MODIFIERS, MESHDATA, CURVEDATA,
        TEXTDATA, EMPTYDATA, LIGHTDATA, CAMERADATA, DRIVERS, TOKENS]'''
        return str()
    @property
    def library_tabs(self):
        '''(Enum)
        
        [SCENE, PRODUCT, INSERT, ASSEMBLY, OBJECT, MATERIAL, WORLD]'''
        return str()
    @property
    def group_driver_tabs(self):
        '''(Enum)
        
        [LOC_X, LOC_Y, LOC_Z, ROT_X, ROT_Y, ROT_Z, DIM_X, DIM_Y, DIM_Z,
        PROMPTS]'''
        return str()
    @property
    def group_tabs(self):
        '''(Enum) Group Tabs
        
        [INFO, SETTINGS, PROMPTS, OBJECTS, DRIVERS]'''
        return str()
    @property
    def interface_group_tabs(self):
        '''(Enum)
        
        [INFO, SETTINGS, PROMPTS, OBJECTS, DRIVERS]'''
        return str()