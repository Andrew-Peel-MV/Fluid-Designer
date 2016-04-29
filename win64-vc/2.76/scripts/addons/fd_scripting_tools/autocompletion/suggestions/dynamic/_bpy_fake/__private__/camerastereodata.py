from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CameraStereoData(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def convergence_mode(self):
        '''(Enum)
        
        [OFFAXIS, PARALLEL, TOE]'''
        return str()
    @property
    def pivot(self):
        '''(Enum)
        
        [LEFT, RIGHT, CENTER]'''
        return str()
    @property
    def interocular_distance(self):
        '''(Float) Set the distance between the eyes - the stereo plane distance
        / 30 should be fine'''
        return float()
    @property
    def convergence_distance(self):
        '''(Float) The converge point for the stereo cameras (often the distance
        between a projector and the projection screen)'''
        return float()