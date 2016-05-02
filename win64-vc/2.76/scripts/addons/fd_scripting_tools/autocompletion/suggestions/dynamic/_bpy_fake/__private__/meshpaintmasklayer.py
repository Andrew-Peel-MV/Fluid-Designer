from . struct import Struct
from . meshpaintmaskproperty import MeshPaintMaskProperty
from . bpy_struct import bpy_struct
import mathutils

class MeshPaintMaskLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def data(self):
        '''(Sequence of MeshPaintMaskProperty)'''
        return (MeshPaintMaskProperty(),)