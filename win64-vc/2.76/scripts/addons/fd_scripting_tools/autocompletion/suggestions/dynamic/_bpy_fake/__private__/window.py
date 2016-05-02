from . struct import Struct
from . screen import Screen
from . stereo3ddisplay import Stereo3dDisplay
from . bpy_struct import bpy_struct
import mathutils

class Window(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def screen(self):
        '''(Screen) Active screen showing in the window'''
        return Screen()
    @property
    def x(self):
        '''(Integer) Horizontal location of the window'''
        return int()
    @property
    def y(self):
        '''(Integer) Vertical location of the window'''
        return int()
    @property
    def width(self):
        '''(Integer) Window width'''
        return int()
    @property
    def height(self):
        '''(Integer) Window height'''
        return int()
    @property
    def stereo_3d_display(self):
        '''(Stereo3dDisplay) Settings for stereo 3d display'''
        return Stereo3dDisplay()
    def cursor_warp(self, x, y):
        '''Set the cursor position
        
        Parameter:
          x: (Integer)
          y: (Integer)'''
        return 
    def cursor_set(self, cursor):
        '''Set the cursor
        
        Parameter:
          cursor: (Enum)'''
        return 
    def cursor_modal_set(self, cursor):
        '''Restore the previous cursor after calling ``cursor_modal_set``
        
        Parameter:
          cursor: (Enum)'''
        return 
    def cursor_modal_restore(self):
        '''cursor_modal_restore'''
        return 