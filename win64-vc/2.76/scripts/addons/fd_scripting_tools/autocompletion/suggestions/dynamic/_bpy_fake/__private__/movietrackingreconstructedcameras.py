from . struct import Struct
from . moviereconstructedcamera import MovieReconstructedCamera
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingReconstructedCameras(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def find_frame(self, frame):
        '''Find a reconstructed camera for a give frame number
        
        Parameter:
          frame: (Integer) Frame number to find camera for
        
        Returns:
          camera: (MovieReconstructedCamera) Camera for a given frame'''
        return MovieReconstructedCamera()
    def matrix_from_frame(self, frame):
        '''Return interpolated camera matrix for a given frame
        
        Parameter:
          frame: (Integer) Frame number to find camera for
        
        Returns:
          matrix: (Matrix) Interpolated camera matrix for a given frame'''
        return mathutils.Matrix()
    def get(key): return MovieReconstructedCamera()
    def __getitem__(key): return MovieReconstructedCamera()
    def __iter__(key): yield MovieReconstructedCamera()