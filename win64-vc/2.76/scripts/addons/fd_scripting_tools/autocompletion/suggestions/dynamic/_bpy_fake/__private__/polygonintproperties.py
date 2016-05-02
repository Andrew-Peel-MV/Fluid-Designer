from . struct import Struct
from . meshpolygonintpropertylayer import MeshPolygonIntPropertyLayer
from . bpy_struct import bpy_struct
import mathutils

class PolygonIntProperties(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, name):
        '''Add a integer property layer to Mesh
        
        Parameter:
          name: (String) Int property name
        
        Returns:
          layer: (MeshPolygonIntPropertyLayer) The newly created layer'''
        return MeshPolygonIntPropertyLayer()
    def get(key): return MeshPolygonIntPropertyLayer()
    def __getitem__(key): return MeshPolygonIntPropertyLayer()
    def __iter__(key): yield MeshPolygonIntPropertyLayer()