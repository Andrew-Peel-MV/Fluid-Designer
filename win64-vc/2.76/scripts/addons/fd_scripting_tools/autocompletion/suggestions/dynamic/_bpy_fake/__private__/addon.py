from . addonpreferences import AddonPreferences
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Addon(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def module(self):
        '''(String) Module name'''
        return str()
    @property
    def preferences(self):
        '''(AddonPreferences)'''
        return AddonPreferences()