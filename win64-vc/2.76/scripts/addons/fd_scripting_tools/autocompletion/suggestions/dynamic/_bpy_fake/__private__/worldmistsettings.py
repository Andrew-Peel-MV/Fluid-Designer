from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class WorldMistSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_mist(self):
        '''(Boolean) Occlude objects with the environment color as they are
        further away'''
        return bool()
    @property
    def intensity(self):
        '''(Float) Overall minimum intensity of the mist effect'''
        return float()
    @property
    def start(self):
        '''(Float) Starting distance of the mist, measured from the camera'''
        return float()
    @property
    def depth(self):
        '''(Float) Distance over which the mist effect fades in'''
        return float()
    @property
    def height(self):
        '''(Float) Control how much mist density decreases with height'''
        return float()
    @property
    def falloff(self):
        '''(Enum) Type of transition used to fade mist
        
        [QUADRATIC, LINEAR, INVERSE_QUADRATIC]'''
        return str()