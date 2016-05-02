from . struct import Struct
from . metaball import MetaBall
from . bpy_struct import bpy_struct
import mathutils

class BlendDataMetaBalls(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new metaball to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          metaball: (MetaBall) New metaball datablock'''
        return MetaBall()
    def remove(self, metaball):
        '''Remove a metaball from the current blendfile
        
        Parameter:
          metaball: (MetaBall) Metaball to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return MetaBall()
    def __getitem__(key): return MetaBall()
    def __iter__(key): yield MetaBall()