from . meshvertexintpropertylayer import MeshVertexIntPropertyLayer
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class VertexIntProperties(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name):
        '''Add a integer property layer to Mesh
        
        Parameter:
          name: (String) Int property name
        
        Returns:
          layer: (MeshVertexIntPropertyLayer) The newly created layer'''
        return MeshVertexIntPropertyLayer()
    def get(key): return MeshVertexIntPropertyLayer()
    def __getitem__(key): return MeshVertexIntPropertyLayer()
    def __iter__(key): yield MeshVertexIntPropertyLayer()