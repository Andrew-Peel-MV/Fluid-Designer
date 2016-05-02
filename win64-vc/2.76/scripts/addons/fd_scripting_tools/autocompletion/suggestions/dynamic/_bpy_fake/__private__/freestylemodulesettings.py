from . struct import Struct
from . text import Text
from . bpy_struct import bpy_struct
import mathutils

class FreestyleModuleSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def script(self):
        '''(Text) Python script to define a style module'''
        return Text()
    @property
    def use(self):
        '''(Boolean) Enable or disable this style module during stroke rendering'''
        return bool()