from . list_library_item import List_Library_Item
from . struct import Struct
from . cutpart import Cutpart
from . library import Library
from . sheet_stock import Sheet_Stock
from . specification_group import Specification_Group
from . bpy_struct import bpy_struct
import mathutils

class SCENE_PROPERTIES(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def project_name(self):
        '''(String)'''
        return str()
    @property
    def job_email(self):
        '''(String)'''
        return str()
    @property
    def insert_tabs(self):
        '''(Enum) Insert Tabs
        
        [INFO, PROMPTS, OBJECTS, DRIVERS]'''
        return str()
    @property
    def edgeband_index(self):
        '''(Integer)'''
        return int()
    @property
    def designer_name(self):
        '''(String)'''
        return str()
    @property
    def edgebanding(self):
        '''(Sequence of Cutpart)'''
        return (Cutpart(),)
    @property
    def customer_address(self):
        '''(String)'''
        return str()
    @property
    def customer_phone(self):
        '''(String)'''
        return str()
    @property
    def sheets(self):
        '''(Sequence of Sheet_Stock)'''
        return (Sheet_Stock(),)
    @property
    def product_tabs(self):
        '''(Enum) Product Tabs
        
        [INFO, PROMPTS, OBJECTS, DRIVERS]'''
        return str()
    @property
    def sheet_index(self):
        '''(Integer)'''
        return int()
    @property
    def spec_group_tabs(self):
        '''(Enum)
        
        [GLOBALS, MATERIALS, CUTPARTS, EDGEPARTS]'''
        return str()
    @property
    def products(self):
        '''(Sequence of List_Library_Item)'''
        return (List_Library_Item(),)
    @property
    def architect(self):
        '''(String)'''
        return str()
    @property
    def customer_name(self):
        '''(String)'''
        return str()
    @property
    def contractor(self):
        '''(String)'''
        return str()
    @property
    def export_type(self):
        '''(Enum)
        
        [LIBRARYMATCH, SOLIDANALYZER]'''
        return str()
    @property
    def spec_group_index(self):
        '''(Integer)'''
        return int()
    @property
    def spec_groups(self):
        '''(Sequence of Specification_Group)'''
        return (Specification_Group(),)
    @property
    def job_number(self):
        '''(String)'''
        return str()
    @property
    def estimator(self):
        '''(String)'''
        return str()
    @property
    def libraries(self):
        '''(Sequence of Library)'''
        return (Library(),)
    @property
    def product_counter(self):
        '''(Integer) Used to count how many products are in the scene to assign
        item numbers'''
        return int()
    @property
    def product_index(self):
        '''(Integer)'''
        return int()
    @property
    def active_library_name(self):
        '''(String)'''
        return str()