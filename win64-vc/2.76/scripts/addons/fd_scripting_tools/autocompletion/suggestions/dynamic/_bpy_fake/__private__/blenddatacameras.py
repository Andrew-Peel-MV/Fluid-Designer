from . camera import Camera
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataCameras(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new camera to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          camera: (Camera) New camera datablock'''
        return Camera()
    def remove(self, camera):
        '''Remove a camera from the current blendfile
        
        Parameter:
          camera: (Camera) Camera to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Camera()
    def __getitem__(key): return Camera()
    def __iter__(key): yield Camera()