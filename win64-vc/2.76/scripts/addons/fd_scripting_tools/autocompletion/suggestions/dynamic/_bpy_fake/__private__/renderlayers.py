from . scenerenderlayer import SceneRenderLayer
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class RenderLayers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active_index(self):
        '''(Integer) Active index in render layer array'''
        return int()
    @property
    def active(self):
        '''(SceneRenderLayer) Active Render Layer'''
        return SceneRenderLayer()
    def new(self, name):
        '''Add a render layer to scene
        
        Parameter:
          name: (String) New name for the render layer (not unique)
        
        Returns:
          result: (SceneRenderLayer) Newly created render layer'''
        return SceneRenderLayer()
    def remove(self, layer):
        '''Remove a render layer
        
        Parameter:
          layer: (SceneRenderLayer) Render layer to remove'''
        return 
    def get(key): return SceneRenderLayer()
    def __getitem__(key): return SceneRenderLayer()
    def __iter__(key): yield SceneRenderLayer()