from . cutpart import Cutpart
from . library_pointer import Library_Pointer
from . struct import Struct
from . edgepart import Edgepart
from . bpy_struct import bpy_struct
import mathutils

class Specification_Group(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def materials(self):
        '''(Sequence of Library_Pointer)'''
        return (Library_Pointer(),)
    @property
    def material_index(self):
        '''(Integer)'''
        return int()
    @property
    def cutparts(self):
        '''(Sequence of Cutpart)'''
        return (Cutpart(),)
    @property
    def cutpart_index(self):
        '''(Integer)'''
        return int()
    @property
    def edgepart_index(self):
        '''(Integer)'''
        return int()
    @property
    def edgeparts(self):
        '''(Sequence of Edgepart)'''
        return (Edgepart(),)