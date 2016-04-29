from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class FCurveSample(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def select(self):
        '''(Boolean) Selection status'''
        return bool()
    @property
    def co(self):
        '''(Vector 2D) Point coordinates'''
        return mathutils.Vector()