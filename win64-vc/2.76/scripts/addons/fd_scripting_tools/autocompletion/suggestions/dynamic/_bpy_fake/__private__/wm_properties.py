from . struct import Struct
from . list_library import List_Library
from . list_module_members import List_Module_Members
from . bpy_struct import bpy_struct
import mathutils

class WM_PROPERTIES(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def lib_products(self):
        '''(Sequence of List_Library)'''
        return (List_Library(),)
    @property
    def module_members(self):
        '''(Sequence of List_Module_Members)'''
        return (List_Module_Members(),)
    @property
    def library_module_tabs(self):
        '''(Enum)
        
        [LIBRARY_DEVELOPMENT, FIND, PROPERTIES]'''
        return str()
    @property
    def lib_insert_index(self):
        '''(Integer)'''
        return int()
    @property
    def lib_product_index(self):
        '''(Integer)'''
        return int()
    @property
    def total_items(self):
        '''(Integer)'''
        return int()
    @property
    def placement_on_product(self):
        '''(Enum)
        
        [LEFT, RIGHT, CENTER]'''
        return str()
    @property
    def export_info(self):
        '''(Enum)
        
        [PROJECT_INFO, CUTPARTS, EDGEBANDING, PRODUCTS]'''
        return str()
    @property
    def current_item(self):
        '''(Integer)'''
        return int()
    @property
    def module_members_index(self):
        '''(Integer)'''
        return int()
    @property
    def path_to_mv_data(self):
        '''(String)'''
        return str()
    @property
    def lib_insert(self):
        '''(List_Library)'''
        return List_Library()
    @property
    def library_types(self):
        '''(Enum)
        
        [PRODUCT, INSERT]'''
        return str()
    @property
    def lib_inserts(self):
        '''(Sequence of List_Library)'''
        return (List_Library(),)