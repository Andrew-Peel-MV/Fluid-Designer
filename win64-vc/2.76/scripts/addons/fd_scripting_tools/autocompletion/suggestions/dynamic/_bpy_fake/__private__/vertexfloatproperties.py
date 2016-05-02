from . meshvertexfloatpropertylayer import MeshVertexFloatPropertyLayer
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class VertexFloatProperties(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name):
        '''Add a float property layer to Mesh
        
        Parameter:
          name: (String) Float property name
        
        Returns:
          layer: (MeshVertexFloatPropertyLayer) The newly created layer'''
        return MeshVertexFloatPropertyLayer()
    def get(key): return MeshVertexFloatPropertyLayer()
    def __getitem__(key): return MeshVertexFloatPropertyLayer()
    def __iter__(key): yield MeshVertexFloatPropertyLayer()