from . struct import Struct
from . material import Material
from . bpy_struct import bpy_struct
import mathutils

class BlendDataMaterials(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new material to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          material: (Material) New material datablock'''
        return Material()
    def remove(self, material):
        '''Remove a material from the current blendfile
        
        Parameter:
          material: (Material) Material to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Material()
    def __getitem__(key): return Material()
    def __iter__(key): yield Material()