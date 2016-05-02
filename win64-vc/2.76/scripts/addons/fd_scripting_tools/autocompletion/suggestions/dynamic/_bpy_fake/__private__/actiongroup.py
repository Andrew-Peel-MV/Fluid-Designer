from . themebonecolorset import ThemeBoneColorSet
from . struct import Struct
from . fcurve import FCurve
from . bpy_struct import bpy_struct
import mathutils

class ActionGroup(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def channels(self):
        '''(Sequence of FCurve) F-Curves in this group'''
        return (FCurve(),)
    @property
    def select(self):
        '''(Boolean) Action group is selected'''
        return bool()
    @property
    def lock(self):
        '''(Boolean) Action group is locked'''
        return bool()
    @property
    def show_expanded(self):
        '''(Boolean) Action group is expanded'''
        return bool()
    @property
    def color_set(self):
        '''(Enum) Custom color set to use
        
        [DEFAULT, THEME01, THEME02, THEME03, THEME04, THEME05, THEME06,
        THEME07, THEME08, THEME09, THEME10, THEME11, THEME12, THEME13,
        THEME14, THEME15, THEME16, THEME17, THEME18, THEME19, THEME20, CUSTOM]'''
        return str()
    @property
    def is_custom_color_set(self):
        '''(Boolean) Color set is user-defined instead of a fixed theme color set'''
        return bool()
    @property
    def colors(self):
        '''(ThemeBoneColorSet) Copy of the colors associated with the group's
        color set'''
        return ThemeBoneColorSet()