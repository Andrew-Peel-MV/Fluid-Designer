from . struct import Struct
from . freestylemodulesettings import FreestyleModuleSettings
from . bpy_struct import bpy_struct
import mathutils

class FreestyleModules(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self):
        '''Add a style module to scene render layer Freestyle settings
        
        Returns:
          module: (FreestyleModuleSettings) Newly created style module'''
        return FreestyleModuleSettings()
    def remove(self, module):
        '''Remove a style module from scene render layer Freestyle settings
        
        Parameter:
          module: (FreestyleModuleSettings) Style module to remove'''
        return 
    def get(key): return FreestyleModuleSettings()
    def __getitem__(key): return FreestyleModuleSettings()
    def __iter__(key): yield FreestyleModuleSettings()