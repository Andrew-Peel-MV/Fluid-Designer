from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Timer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def time_step(self):
        '''(Float)'''
        return float()
    @property
    def time_delta(self):
        '''(Float) Time since last step in seconds'''
        return float()
    @property
    def time_duration(self):
        '''(Float) Time since last step in seconds'''
        return float()