from . meshpolygonfloatpropertylayer import MeshPolygonFloatPropertyLayer
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PolygonFloatProperties(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name):
        '''Add a float property layer to Mesh
        
        Parameter:
          name: (String) Float property name
        
        Returns:
          layer: (MeshPolygonFloatPropertyLayer) The newly created layer'''
        return MeshPolygonFloatPropertyLayer()
    def get(key): return MeshPolygonFloatPropertyLayer()
    def __getitem__(key): return MeshPolygonFloatPropertyLayer()
    def __iter__(key): yield MeshPolygonFloatPropertyLayer()