from . struct import Struct
from . meshloopcolorlayer import MeshLoopColorLayer
from . bpy_struct import bpy_struct
import mathutils

class LoopColors(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MeshLoopColorLayer) Active vertex color layer'''
        return MeshLoopColorLayer()
    @property
    def active_index(self):
        '''(Integer) Active vertex color index'''
        return int()
    def new(self, name):
        '''Add a vertex color layer to Mesh
        
        Parameter:
          name: (String) Vertex color name
        
        Returns:
          layer: (MeshLoopColorLayer) The newly created layer'''
        return MeshLoopColorLayer()
    def remove(self, layer):
        '''Remove a vertex color layer
        
        Parameter:
          layer: (MeshLoopColorLayer) The layer to remove'''
        return 
    def get(key): return MeshLoopColorLayer()
    def __getitem__(key): return MeshLoopColorLayer()
    def __iter__(key): yield MeshLoopColorLayer()