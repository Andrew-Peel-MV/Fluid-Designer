from . struct import Struct
from . keyconfig import KeyConfig
from . bpy_struct import bpy_struct
import mathutils

class KeyConfigurations(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(KeyConfig) Active key configuration (preset)'''
        return KeyConfig()
    @property
    def default(self):
        '''(KeyConfig) Default builtin key configuration'''
        return KeyConfig()
    @property
    def addon(self):
        '''(KeyConfig) Key configuration that can be extended by addons, and is
        added to the active configuration when handling events'''
        return KeyConfig()
    @property
    def user(self):
        '''(KeyConfig) Final key configuration that combines keymaps from the
        active and addon configurations, and can be edited by the user'''
        return KeyConfig()
    def new(self, name):
        '''new
        
        Parameter:
          name: (String)
        
        Returns:
          keyconfig: (KeyConfig) Added key configuration'''
        return KeyConfig()
    def remove(self, keyconfig):
        '''remove
        
        Parameter:
          keyconfig: (KeyConfig) Removed key configuration'''
        return 
    def get(key): return KeyConfig()
    def __getitem__(key): return KeyConfig()
    def __iter__(key): yield KeyConfig()