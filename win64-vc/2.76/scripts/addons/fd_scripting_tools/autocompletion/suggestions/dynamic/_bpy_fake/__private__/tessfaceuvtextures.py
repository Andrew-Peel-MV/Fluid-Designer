from . struct import Struct
from . meshtexturefacelayer import MeshTextureFaceLayer
from . bpy_struct import bpy_struct
import mathutils

class TessfaceUVTextures(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MeshTextureFaceLayer) Active UV Map'''
        return MeshTextureFaceLayer()
    @property
    def active_index(self):
        '''(Integer) Active UV Map index'''
        return int()
    def new(self, name):
        '''Add a UV tessface-texture layer to Mesh (only for meshes with no
        polygons)
        
        Parameter:
          name: (String) UV map name
        
        Returns:
          layer: (MeshTextureFaceLayer) The newly created layer'''
        return MeshTextureFaceLayer()
    def get(key): return MeshTextureFaceLayer()
    def __getitem__(key): return MeshTextureFaceLayer()
    def __iter__(key): yield MeshTextureFaceLayer()