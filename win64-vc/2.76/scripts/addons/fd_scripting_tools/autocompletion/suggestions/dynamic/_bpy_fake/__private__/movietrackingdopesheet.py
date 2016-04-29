from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingDopesheet(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def sort_method(self):
        '''(Enum) Method to be used to sort channels in dopesheet view
        
        [NAME, LONGEST, TOTAL, AVERAGE_ERROR]'''
        return str()
    @property
    def use_invert_sort(self):
        '''(Boolean) Invert sort order of dopesheet channels'''
        return bool()
    @property
    def show_only_selected(self):
        '''(Boolean) Only include channels relating to selected objects and data'''
        return bool()
    @property
    def show_hidden(self):
        '''(Boolean) Include channels from objects/bone that aren't visible'''
        return bool()