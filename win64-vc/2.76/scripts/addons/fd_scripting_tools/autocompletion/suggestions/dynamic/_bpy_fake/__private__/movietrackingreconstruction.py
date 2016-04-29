from . movietrackingreconstructedcameras import MovieTrackingReconstructedCameras
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingReconstruction(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_valid(self):
        '''(Boolean) Is tracking data contains valid reconstruction information'''
        return bool()
    @property
    def average_error(self):
        '''(Float) Average error of reconstruction'''
        return float()
    @property
    def cameras(self):
        '''(Sequence of MovieReconstructedCamera) Collection of solved cameras'''
        return MovieTrackingReconstructedCameras()