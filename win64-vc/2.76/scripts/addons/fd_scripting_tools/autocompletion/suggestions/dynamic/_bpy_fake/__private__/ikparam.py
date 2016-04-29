from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class IKParam(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def ik_solver(self):
        '''(Enum) IK solver for which these parameters are defined
        
        [LEGACY, ITASC]'''
        return str()