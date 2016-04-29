from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class SmokeCollSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def collision_type(self):
        '''(Enum) Collision type
        
        [COLLSTATIC, COLLRIGID, COLLANIMATED]'''
        return str()