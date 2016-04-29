from . struct import Struct
from . material import Material
from . bpy_struct import bpy_struct
import mathutils

class IDMaterials(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def append(self, material):
        '''Add a new material to the data block
        
        Parameter:
          material: (Material) Material to add'''
        return 
    def pop(self, index, update_data):
        '''Remove a material from the data block
        
        Parameter:
          index: (Integer) Index of material to remove
          update_data: (Boolean) Update data by re-adjusting the material slots assigned
        
        Returns:
          material: (Material) Material to remove'''
        return Material()
    def clear(self, update_data):
        '''Remove all materials from the data block
        
        Parameter:
          update_data: (Boolean) Update data by re-adjusting the material slots assigned'''
        return 
    def get(key): return Material()
    def __getitem__(key): return Material()
    def __iter__(key): yield Material()