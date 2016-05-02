from . struct import Struct
from . freestylelineset import FreestyleLineSet
from . bpy_struct import bpy_struct
import mathutils

class Linesets(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(FreestyleLineSet) Active line set being displayed'''
        return FreestyleLineSet()
    @property
    def active_index(self):
        '''(Integer) Index of active line set slot'''
        return int()
    def new(self, name):
        '''Add a line set to scene render layer Freestyle settings
        
        Parameter:
          name: (String) New name for the line set (not unique)
        
        Returns:
          lineset: (FreestyleLineSet) Newly created line set'''
        return FreestyleLineSet()
    def remove(self, lineset):
        '''Remove a line set from scene render layer Freestyle settings
        
        Parameter:
          lineset: (FreestyleLineSet) Line set to remove'''
        return 
    def get(key): return FreestyleLineSet()
    def __getitem__(key): return FreestyleLineSet()
    def __iter__(key): yield FreestyleLineSet()