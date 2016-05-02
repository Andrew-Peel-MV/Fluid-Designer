from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class opengl_dim(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def gl_text_y(self):
        '''(Integer) Change font position in Y axis'''
        return int()
    @property
    def gl_precision(self):
        '''(Integer) Number of decimal precision'''
        return int()
    @property
    def show_label(self):
        '''(Boolean) Display label for this measure'''
        return bool()
    @property
    def gl_arrow_size(self):
        '''(Integer) Arrow size'''
        return int()
    @property
    def gl_width(self):
        '''(Integer) line width'''
        return int()
    @property
    def gl_font_size(self):
        '''(Integer) Text size'''
        return int()
    @property
    def hide(self):
        '''(Boolean) Show/Hide Dimension'''
        return bool()
    @property
    def gl_default_color(self):
        '''(Float[4]) Default Color'''
        return ''
    @property
    def gl_dim_units(self):
        '''(Enum) Units
        
        [1, 2, 3, 4, 5, 6]'''
        return str()
    @property
    def gl_arrow_type(self):
        '''(Enum) Dimension Arrow Type
        
        [99, 1, 2, 3]'''
        return str()
    @property
    def gl_label(self):
        '''(String) Short description (use | for line break)'''
        return str()
    @property
    def gl_text_x(self):
        '''(Integer) Change font position in X axis'''
        return int()
    @property
    def gl_color(self):
        '''(Integer) Color for the measure'''
        return int()