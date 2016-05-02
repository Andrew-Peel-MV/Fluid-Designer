from . struct import Struct
from . obstacle import Obstacle
from . bpy_struct import bpy_struct
import mathutils

class Wall(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def bp_name(self):
        '''(String)'''
        return str()
    @property
    def obstacle_index(self):
        '''(Integer)'''
        return int()
    @property
    def obstacles(self):
        '''(Sequence of Obstacle)'''
        return (Obstacle(),)