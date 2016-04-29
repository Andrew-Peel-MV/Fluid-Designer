from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class DisplaySafeAreas(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def title(self):
        '''(Vector 2D) Safe area for text and graphics'''
        return mathutils.Vector()
    @property
    def action(self):
        '''(Vector 2D) Safe area for general elements'''
        return mathutils.Vector()
    @property
    def title_center(self):
        '''(Vector 2D) Safe area for text and graphics in a different aspect
        ratio'''
        return mathutils.Vector()
    @property
    def action_center(self):
        '''(Vector 2D) Safe area for general elements in a different aspect ratio'''
        return mathutils.Vector()