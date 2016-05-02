from . struct import Struct
from . material import Material
from . bpy_struct import bpy_struct
import mathutils

class MaterialSlot(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def material(self):
        '''(Material) Material datablock used by this material slot'''
        return Material()
    @property
    def link(self):
        '''(Enum) Link material to object or the object's data
        
        [OBJECT, DATA]'''
        return str()
    @property
    def name(self):
        '''(String) Material slot name'''
        return str()