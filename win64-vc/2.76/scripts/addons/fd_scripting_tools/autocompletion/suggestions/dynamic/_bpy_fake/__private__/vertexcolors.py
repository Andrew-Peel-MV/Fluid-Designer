from . struct import Struct
from . meshcolorlayer import MeshColorLayer
from . bpy_struct import bpy_struct
import mathutils

class VertexColors(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MeshColorLayer) Active vertex color layer'''
        return MeshColorLayer()
    @property
    def active_index(self):
        '''(Integer) Active vertex color index'''
        return int()
    def new(self, name):
        '''Add a vertex color layer to Mesh
        
        Parameter:
          name: (String) Vertex color name
        
        Returns:
          layer: (MeshColorLayer) The newly created layer'''
        return MeshColorLayer()
    def get(key): return MeshColorLayer()
    def __getitem__(key): return MeshColorLayer()
    def __iter__(key): yield MeshColorLayer()