from . dynamicpaintsurface import DynamicPaintSurface
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class DynamicPaintSurfaces(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active_index(self):
        '''(Integer)'''
        return int()
    @property
    def active(self):
        '''(DynamicPaintSurface) Active Dynamic Paint surface being displayed'''
        return DynamicPaintSurface()
    def get(key): return DynamicPaintSurface()
    def __getitem__(key): return DynamicPaintSurface()
    def __iter__(key): yield DynamicPaintSurface()