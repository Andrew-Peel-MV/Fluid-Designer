from . uilayout import UILayout
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class UIPopupMenu(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def layout(self):
        '''(UILayout)'''
        return UILayout()