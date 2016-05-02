from . struct import Struct
from . keymapitem import KeyMapItem
from . bpy_struct import bpy_struct
import mathutils

class KeyMapItems(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, idname, type, value, any, shift, ctrl, alt, oskey, key_modifier, head):
        '''new
        
        Parameter:
          idname: (String)
          type: (Enum)
          value: (Enum)
          any: (Boolean)
          shift: (Boolean)
          ctrl: (Boolean)
          alt: (Boolean)
          oskey: (Boolean)
          key_modifier: (Enum)
          head:
            (Boolean) Force item to be added at start (not end) of key map so that
            it doesn't get blocked by an existing key map item
        
        Returns:
          item: (KeyMapItem) Added key map item'''
        return KeyMapItem()
    def new_modal(self, propvalue, type, value, any, shift, ctrl, alt, oskey, key_modifier):
        '''new_modal
        
        Parameter:
          propvalue: (String)
          type: (Enum)
          value: (Enum)
          any: (Boolean)
          shift: (Boolean)
          ctrl: (Boolean)
          alt: (Boolean)
          oskey: (Boolean)
          key_modifier: (Enum)
        
        Returns:
          item: (KeyMapItem) Added key map item'''
        return KeyMapItem()
    def remove(self, item):
        '''remove
        
        Parameter:
          item: (KeyMapItem)'''
        return 
    def from_id(self, id):
        '''from_id
        
        Parameter:
          id: (Integer) ID of the item
        
        Returns:
          item: (KeyMapItem)'''
        return KeyMapItem()
    def get(key): return KeyMapItem()
    def __getitem__(key): return KeyMapItem()
    def __iter__(key): yield KeyMapItem()