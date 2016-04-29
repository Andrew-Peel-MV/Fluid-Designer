from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialGameSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_backface_culling(self):
        '''(Boolean) Hide Back of the face in Game Engine'''
        return bool()
    @property
    def text(self):
        '''(Boolean) Use material as text in Game Engine'''
        return bool()
    @property
    def invisible(self):
        '''(Boolean) Make face invisible'''
        return bool()
    @property
    def alpha_blend(self):
        '''(Enum) Blend Mode for Transparent Faces
        
        [OPAQUE, ADD, CLIP, ALPHA, ALPHA_SORT, ALPHA_ANTIALIASING]'''
        return str()
    @property
    def face_orientation(self):
        '''(Enum) Especial face orientation options
        
        [NORMAL, HALO, BILLBOARD, SHADOW]'''
        return str()
    @property
    def physics(self):
        '''(Boolean) Use physics properties of materials'''
        return bool()