from . struct import Struct
from . meshpolygonfloatproperty import MeshPolygonFloatProperty
from . bpy_struct import bpy_struct
import mathutils

class MeshPolygonFloatPropertyLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def data(self):
        '''(Sequence of MeshPolygonFloatProperty)'''
        return (MeshPolygonFloatProperty(),)