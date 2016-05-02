from . themegradientcolors import ThemeGradientColors
from . struct import Struct
from . themepanelcolors import ThemePanelColors
from . bpy_struct import bpy_struct
import mathutils

class ThemeSpaceGradient(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def gradients(self):
        '''(ThemeGradientColors)'''
        return ThemeGradientColors()
    @property
    def title(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def text_hi(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def header(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def header_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def header_text_hi(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def panelcolors(self):
        '''(ThemePanelColors)'''
        return ThemePanelColors()
    @property
    def button(self):
        '''(Float[4])'''
        return ''
    @property
    def button_title(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def button_text(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def button_text_hi(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def tab_active(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def tab_inactive(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def tab_back(self):
        '''(Float[4])'''
        return ''
    @property
    def tab_outline(self):
        '''(Vector 3D)'''
        return mathutils.Vector()