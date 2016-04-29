from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class ThemeWidgetColors(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def outline(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def inner(self):
        '''(Float[4])'''
        return ''
    @property
    def inner_sel(self):
        '''(Float[4])'''
        return ''
    @property
    def item(self):
        '''(Float[4])'''
        return ''
    @property
    def text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def text_sel(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def show_shaded(self):
        '''(Boolean)'''
        return bool()
    @property
    def shadetop(self):
        '''(Integer)'''
        return int()
    @property
    def shadedown(self):
        '''(Integer)'''
        return int()