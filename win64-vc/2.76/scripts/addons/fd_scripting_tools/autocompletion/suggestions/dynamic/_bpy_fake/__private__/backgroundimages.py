from . struct import Struct
from . backgroundimage import BackgroundImage
from . bpy_struct import bpy_struct
import mathutils

class BackgroundImages(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self):
        '''Add new background image
        
        Returns:
          image: (BackgroundImage) Image displayed as viewport background'''
        return BackgroundImage()
    def remove(self, image):
        '''Remove background image
        
        Parameter:
          image: (BackgroundImage) Image displayed as viewport background'''
        return 
    def clear(self):
        '''Remove all background images'''
        return 
    def get(key): return BackgroundImage()
    def __getitem__(key): return BackgroundImage()
    def __iter__(key): yield BackgroundImage()