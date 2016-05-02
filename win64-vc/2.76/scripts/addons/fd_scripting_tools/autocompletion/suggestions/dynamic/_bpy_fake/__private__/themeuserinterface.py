from . themewidgetcolors import ThemeWidgetColors
from . struct import Struct
from . themewidgetstatecolors import ThemeWidgetStateColors
from . bpy_struct import bpy_struct
import mathutils

class ThemeUserInterface(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def wcol_regular(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_tool(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_radio(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_text(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_option(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_toggle(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_num(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_numslider(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_box(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_menu(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_pulldown(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_menu_back(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_pie_menu(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_tooltip(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_menu_item(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_scroll(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_progress(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_list_item(self):
        '''(ThemeWidgetColors)'''
        return ThemeWidgetColors()
    @property
    def wcol_state(self):
        '''(ThemeWidgetStateColors)'''
        return ThemeWidgetStateColors()
    @property
    def menu_shadow_fac(self):
        '''(Float) Blending factor for menu shadows'''
        return float()
    @property
    def menu_shadow_width(self):
        '''(Integer) Width of menu shadows, set to zero to disable'''
        return int()
    @property
    def icon_file(self):
        '''(String)'''
        return str()
    @property
    def icon_alpha(self):
        '''(Float) Transparency of icons in the interface, to reduce contrast'''
        return float()
    @property
    def widget_emboss(self):
        '''(Float[4]) Color of the 1px shadow line underlying widgets'''
        return ''
    @property
    def axis_x(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def axis_y(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def axis_z(self):
        '''(Vector 3D)'''
        return mathutils.Vector()