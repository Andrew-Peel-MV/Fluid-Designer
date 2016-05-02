from . struct import Struct
from . space import Space
from . bpy_struct import bpy_struct
import mathutils

class AreaSpaces(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Space) Space currently being displayed in this area'''
        return Space()
    def get(key): return Space()
    def __getitem__(key): return Space()
    def __iter__(key): yield Space()