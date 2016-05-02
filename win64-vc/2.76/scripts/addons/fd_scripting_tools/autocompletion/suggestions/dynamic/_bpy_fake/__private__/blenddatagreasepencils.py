from . greasepencil import GreasePencil
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataGreasePencils(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def new(self, name):
        '''new
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          grease_pencil: (GreasePencil) New grease pencil datablock'''
        return GreasePencil()
    def remove(self, grease_pencil):
        '''Remove a grease pencil instance from the current blendfile
        
        Parameter:
          grease_pencil: (GreasePencil) Grease Pencil to remove'''
        return 
    def get(key): return GreasePencil()
    def __getitem__(key): return GreasePencil()
    def __iter__(key): yield GreasePencil()