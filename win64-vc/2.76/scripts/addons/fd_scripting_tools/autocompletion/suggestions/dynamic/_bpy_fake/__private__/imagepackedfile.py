from . struct import Struct
from . packedfile import PackedFile
from . bpy_struct import bpy_struct
import mathutils

class ImagePackedFile(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def packed_file(self):
        '''(PackedFile)'''
        return PackedFile()
    @property
    def filepath(self):
        '''(String)'''
        return str()