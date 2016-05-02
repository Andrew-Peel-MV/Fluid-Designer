from . struct import Struct
from . meshvertexstringpropertylayer import MeshVertexStringPropertyLayer
from . bpy_struct import bpy_struct
import mathutils

class VertexStringProperties(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name):
        '''Add a string property layer to Mesh
        
        Parameter:
          name: (String) String property name
        
        Returns:
          layer: (MeshVertexStringPropertyLayer) The newly created layer'''
        return MeshVertexStringPropertyLayer()
    def get(key): return MeshVertexStringPropertyLayer()
    def __getitem__(key): return MeshVertexStringPropertyLayer()
    def __iter__(key): yield MeshVertexStringPropertyLayer()