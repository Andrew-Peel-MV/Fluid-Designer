from . windowmanager import WindowManager
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataWindowManagers(bpy_struct):
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
    def get(key): return WindowManager()
    def __getitem__(key): return WindowManager()
    def __iter__(key): yield WindowManager()