from . meshtexturepolylayer import MeshTexturePolyLayer
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class UVTextures(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MeshTexturePolyLayer) Active UV Map'''
        return MeshTexturePolyLayer()
    @property
    def active_index(self):
        '''(Integer) Active UV Map index'''
        return int()
    def new(self, name):
        '''Add a UV map layer to Mesh
        
        Parameter:
          name: (String) UV map name
        
        Returns:
          layer: (MeshTexturePolyLayer) The newly created layer'''
        return MeshTexturePolyLayer()
    def remove(self, layer):
        '''Remove a vertex color layer
        
        Parameter:
          layer: (MeshTexturePolyLayer) The layer to remove'''
        return 
    def get(key): return MeshTexturePolyLayer()
    def __getitem__(key): return MeshTexturePolyLayer()
    def __iter__(key): yield MeshTexturePolyLayer()