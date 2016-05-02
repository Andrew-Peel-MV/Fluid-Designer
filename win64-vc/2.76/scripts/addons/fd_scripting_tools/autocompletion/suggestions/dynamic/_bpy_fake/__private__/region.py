from . struct import Struct
from . view2d import View2D
from . bpy_struct import bpy_struct
import mathutils

class Region(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def id(self):
        '''(Integer) Unique ID for this region'''
        return int()
    @property
    def type(self):
        '''(Enum) Type of this region
        
        [WINDOW, HEADER, CHANNELS, TEMPORARY, UI, TOOLS, TOOL_PROPS, PREVIEW]'''
        return str()
    @property
    def x(self):
        '''(Integer) The window relative vertical location of the region'''
        return int()
    @property
    def y(self):
        '''(Integer) The window relative horizontal location of the region'''
        return int()
    @property
    def width(self):
        '''(Integer) Region width'''
        return int()
    @property
    def height(self):
        '''(Integer) Region height'''
        return int()
    @property
    def view2d(self):
        '''(View2D) 2D view of the region'''
        return View2D()
    def tag_redraw(self):
        '''tag_redraw'''
        return 