from . gpencilstrokepoints import GPencilStrokePoints
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class GPencilStroke(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def points(self):
        '''(Sequence of GPencilStrokePoint) Stroke data points'''
        return GPencilStrokePoints()
    @property
    def draw_mode(self):
        '''(Enum)
        
        [SCREEN, 3DSPACE, 2DSPACE, 2DIMAGE]'''
        return str()
    @property
    def select(self):
        '''(Boolean) Stroke is selected for viewport editing'''
        return bool()