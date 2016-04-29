from . meshpolygonstringpropertylayer import MeshPolygonStringPropertyLayer
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PolygonStringProperties(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name):
        '''Add a string property layer to Mesh
        
        Parameter:
          name: (String) String property name
        
        Returns:
          layer: (MeshPolygonStringPropertyLayer) The newly created layer'''
        return MeshPolygonStringPropertyLayer()
    def get(key): return MeshPolygonStringPropertyLayer()
    def __getitem__(key): return MeshPolygonStringPropertyLayer()
    def __iter__(key): yield MeshPolygonStringPropertyLayer()