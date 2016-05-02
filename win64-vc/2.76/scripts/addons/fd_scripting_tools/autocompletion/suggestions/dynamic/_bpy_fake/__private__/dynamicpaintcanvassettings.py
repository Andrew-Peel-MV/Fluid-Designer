from . struct import Struct
from . dynamicpaintsurfaces import DynamicPaintSurfaces
from . bpy_struct import bpy_struct
import mathutils

class DynamicPaintCanvasSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def canvas_surfaces(self):
        '''(Sequence of DynamicPaintSurface) Paint surface list'''
        return DynamicPaintSurfaces()