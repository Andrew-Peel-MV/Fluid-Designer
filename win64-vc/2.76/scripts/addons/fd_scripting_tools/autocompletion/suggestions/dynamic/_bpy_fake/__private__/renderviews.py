from . scenerenderview import SceneRenderView
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class RenderViews(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active_index(self):
        '''(Integer) Active index in render view array'''
        return int()
    @property
    def active(self):
        '''(SceneRenderView) Active Render View'''
        return SceneRenderView()
    def new(self, name):
        '''Add a render view to scene
        
        Parameter:
          name: (String) New name for the marker (not unique)
        
        Returns:
          result: (SceneRenderView) Newly created render view'''
        return SceneRenderView()
    def remove(self, view):
        '''Remove a render view
        
        Parameter:
          view: (SceneRenderView) Render view to remove'''
        return 
    def get(key): return SceneRenderView()
    def __getitem__(key): return SceneRenderView()
    def __iter__(key): yield SceneRenderView()