from . struct import Struct
from . image import Image
from . bpy_struct import bpy_struct
import mathutils

class MeshTexturePoly(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def image(self):
        '''(Image)'''
        return Image()