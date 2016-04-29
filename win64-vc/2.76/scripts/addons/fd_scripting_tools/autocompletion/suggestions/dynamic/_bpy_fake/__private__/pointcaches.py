from . struct import Struct
from . pointcache import PointCache
from . bpy_struct import bpy_struct
import mathutils

class PointCaches(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active_index(self):
        '''(Integer)'''
        return int()
    def get(key): return PointCache()
    def __getitem__(key): return PointCache()
    def __iter__(key): yield PointCache()