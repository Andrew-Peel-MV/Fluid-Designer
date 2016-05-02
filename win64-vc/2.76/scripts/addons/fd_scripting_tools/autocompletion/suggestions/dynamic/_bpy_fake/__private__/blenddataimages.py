from . struct import Struct
from . image import Image
from . bpy_struct import bpy_struct
import mathutils

class BlendDataImages(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name, width, height, alpha, float_buffer, stereo3d):
        '''Add a new image to the main database
        
        Parameter:
          name: (String) New name for the datablock
          width: (Integer) Width of the image
          height: (Integer) Height of the image
          alpha: (Boolean) Use alpha channel
          float_buffer: (Boolean) Create an image with floating point color
          stereo3d: (Boolean) Create left and right views
        
        Returns:
          image: (Image) New image datablock'''
        return Image()
    def load(self, filepath):
        '''Load a new image into the main database
        
        Parameter:
          filepath: (String) path of the file to load
        
        Returns:
          image: (Image) New image datablock'''
        return Image()
    def remove(self, image):
        '''Remove an image from the current blendfile
        
        Parameter:
          image: (Image) Image to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Image()
    def __getitem__(key): return Image()
    def __iter__(key): yield Image()