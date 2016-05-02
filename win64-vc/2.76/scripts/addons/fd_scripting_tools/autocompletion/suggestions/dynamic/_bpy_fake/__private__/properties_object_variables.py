from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PROPERTIES_Object_Variables(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def is_base_molding(self):
        '''(Boolean) Used to Delete Molding When Using Auto Add Molding Operator'''
        return bool()
    @property
    def is_crown_molding(self):
        '''(Boolean) Used to Delete Molding When Using Auto Add Molding Operator'''
        return bool()