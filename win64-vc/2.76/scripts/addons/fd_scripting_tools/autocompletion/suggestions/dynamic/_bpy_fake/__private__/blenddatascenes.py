from . scene import Scene
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataScenes(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name):
        '''Add a new scene to the main database
        
        Parameter:
          name: (String) New name for the datablock
        
        Returns:
          scene: (Scene) New scene datablock'''
        return Scene()
    def remove(self, scene):
        '''Remove a scene from the current blendfile
        
        Parameter:
          scene: (Scene) Scene to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return Scene()
    def __getitem__(key): return Scene()
    def __iter__(key): yield Scene()