from . struct import Struct
from . keymaps import KeyMaps
from . bpy_struct import bpy_struct
import mathutils

class KeyConfig(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Name of the key configuration'''
        return str()
    @property
    def keymaps(self):
        '''(Sequence of KeyMap) Key maps configured as part of this configuration'''
        return KeyMaps()
    @property
    def is_user_defined(self):
        '''(Boolean) Indicates that a keyconfig was defined by the user'''
        return bool()