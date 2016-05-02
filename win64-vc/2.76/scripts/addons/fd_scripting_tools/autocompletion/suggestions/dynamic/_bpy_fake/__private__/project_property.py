from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Project_Property(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def global_variable_name(self):
        '''(String)'''
        return str()
    @property
    def project_wizard_variable_name(self):
        '''(String)'''
        return str()
    @property
    def specification_group_name(self):
        '''(String)'''
        return str()
    @property
    def value(self):
        '''(String)'''
        return str()