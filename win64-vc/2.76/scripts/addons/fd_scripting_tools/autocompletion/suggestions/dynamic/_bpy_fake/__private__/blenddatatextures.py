from . struct import Struct
from . texture import Texture
from . bpy_struct import bpy_struct
import mathutils

class BlendDataTextures(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name, type):
        '''Add a new texture to the main database
        
        Parameter:
          name: (String) New name for the datablock
          type: (Enum) The type of texture to add
        
        Returns:
          texture: (Texture) New texture datablock'''
        return Texture()
    def remove(self, texture):
        '''Remove a texture from the current blendfile
        
        Parameter:
          texture: (Texture) Texture to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Texture()
    def __getitem__(key): return Texture()
    def __iter__(key): yield Texture()