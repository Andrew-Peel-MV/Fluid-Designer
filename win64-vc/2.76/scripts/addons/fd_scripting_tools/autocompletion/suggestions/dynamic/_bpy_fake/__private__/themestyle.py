from . struct import Struct
from . themefontstyle import ThemeFontStyle
from . bpy_struct import bpy_struct
import mathutils

class ThemeStyle(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def panel_title(self):
        '''(ThemeFontStyle)'''
        return ThemeFontStyle()
    @property
    def widget_label(self):
        '''(ThemeFontStyle)'''
        return ThemeFontStyle()
    @property
    def widget(self):
        '''(ThemeFontStyle)'''
        return ThemeFontStyle()