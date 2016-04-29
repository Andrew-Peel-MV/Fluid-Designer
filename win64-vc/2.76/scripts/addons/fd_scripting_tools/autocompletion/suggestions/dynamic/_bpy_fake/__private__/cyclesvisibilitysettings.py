from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesVisibilitySettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def camera(self):
        '''(Boolean) Object visibility for camera rays'''
        return bool()
    @property
    def diffuse(self):
        '''(Boolean) Object visibility for diffuse reflection rays'''
        return bool()
    @property
    def glossy(self):
        '''(Boolean) Object visibility for glossy reflection rays'''
        return bool()
    @property
    def transmission(self):
        '''(Boolean) Object visibility for transmission rays'''
        return bool()
    @property
    def shadow(self):
        '''(Boolean) Object visibility for shadow rays'''
        return bool()
    @property
    def scatter(self):
        '''(Boolean) Object visibility for volume scatter rays'''
        return bool()