from . struct import Struct
from . image import Image
from . bpy_struct import bpy_struct
import mathutils

class MeshTextureFace(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def image(self):
        '''(Image)'''
        return Image()
    @property
    def uv1(self):
        '''(Vector 2D)'''
        return mathutils.Vector()
    @property
    def uv2(self):
        '''(Vector 2D)'''
        return mathutils.Vector()
    @property
    def uv3(self):
        '''(Vector 2D)'''
        return mathutils.Vector()
    @property
    def uv4(self):
        '''(Vector 2D)'''
        return mathutils.Vector()
    @property
    def uv(self):
        '''(Float[8])'''
        return ''
    @property
    def uv_raw(self):
        '''(Float[8]) Fixed size UV coordinates array'''
        return ''