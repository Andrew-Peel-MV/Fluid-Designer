from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class View2D(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def region_to_view(self, x, y):
        '''Transform region coordinates to 2D view
        
        Parameter:
          x: (Integer) Region x coordinate
          y: (Integer) Region y coordinate
        
        Returns:
          result: (Vector 2D) View coordinates'''
        return mathutils.Vector()
    def view_to_region(self, x, y, clip):
        '''Transform 2D view coordinates to region
        
        Parameter:
          x: (Float) 2D View x coordinate
          y: (Float) 2D View y coordinate
          clip: (Boolean) Clip coordinates to the visible region
        
        Returns:
          result: (Integer[2]) Region coordinates'''
        return int()