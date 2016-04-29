from . keymap import KeyMap
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class KeyMaps(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name, space_type, region_type, modal):
        '''new
        
        Parameter:
          name: (String)
          space_type: (Enum)
          region_type: (Enum)
          modal: (Boolean)
        
        Returns:
          keymap: (KeyMap) Added key map'''
        return KeyMap()
    def remove(self, keymap):
        '''remove
        
        Parameter:
          keymap: (KeyMap) Removed key map'''
        return 
    def find(self, name, space_type, region_type):
        '''find
        
        Parameter:
          name: (String)
          space_type: (Enum)
          region_type: (Enum)
        
        Returns:
          keymap: (KeyMap) Corresponding key map'''
        return KeyMap()
    def find_modal(self, name):
        '''find_modal
        
        Parameter:
          name: (String)
        
        Returns:
          keymap: (KeyMap) Corresponding key map'''
        return KeyMap()
    def get(key): return KeyMap()
    def __getitem__(key): return KeyMap()
    def __iter__(key): yield KeyMap()