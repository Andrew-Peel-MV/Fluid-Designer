from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class OperatorOptions(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_grab_cursor(self):
        '''(Boolean) True when the cursor is grabbed'''
        return bool()
    @property
    def is_invoke(self):
        '''(Boolean) True when invoked (even if only the execute callbacks
        available)'''
        return bool()
    @property
    def use_cursor_region(self):
        '''(Boolean) Enable to use the region under the cursor for modal
        execution'''
        return bool()