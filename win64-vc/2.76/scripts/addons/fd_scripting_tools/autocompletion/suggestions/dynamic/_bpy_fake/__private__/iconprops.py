from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class IconProps(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def scroll(self):
        '''(Integer) Drag to scroll icons'''
        return int()
    @property
    def console(self):
        '''(Boolean) Display the Icons in the console header'''
        return bool()
    @property
    def expand(self):
        '''(Boolean) Expand, to display all icons at once'''
        return bool()
    @property
    def search(self):
        '''(String) Search for icons by name'''
        return str()