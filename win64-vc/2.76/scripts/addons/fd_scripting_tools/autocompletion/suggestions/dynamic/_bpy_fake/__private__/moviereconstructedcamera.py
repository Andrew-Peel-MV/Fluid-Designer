from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieReconstructedCamera(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def frame(self):
        '''(Integer) Frame number marker is keyframed on'''
        return int()
    @property
    def matrix(self):
        '''(Matrix) Worldspace transformation matrix'''
        return mathutils.Matrix()
    @property
    def average_error(self):
        '''(Float) Average error of reconstruction'''
        return float()