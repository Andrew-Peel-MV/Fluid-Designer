from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshEdge(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def vertices(self):
        '''(Integer[2]) Vertex indices'''
        return int()
    @property
    def crease(self):
        '''(Float) Weight used by the Subsurf modifier for creasing'''
        return float()
    @property
    def bevel_weight(self):
        '''(Float) Weight used by the Bevel modifier'''
        return float()
    @property
    def select(self):
        '''(Boolean)'''
        return bool()
    @property
    def hide(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_seam(self):
        '''(Boolean) Seam edge for UV unwrapping'''
        return bool()
    @property
    def use_edge_sharp(self):
        '''(Boolean) Sharp edge for the EdgeSplit modifier'''
        return bool()
    @property
    def is_loose(self):
        '''(Boolean) Loose edge'''
        return bool()
    @property
    def use_freestyle_mark(self):
        '''(Boolean) Edge mark for Freestyle line rendering'''
        return bool()
    @property
    def index(self):
        '''(Integer) Index of this edge'''
        return int()