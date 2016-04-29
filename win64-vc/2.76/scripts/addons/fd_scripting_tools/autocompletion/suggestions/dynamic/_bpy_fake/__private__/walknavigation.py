from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class WalkNavigation(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def mouse_speed(self):
        '''(Float) Speed factor for when looking around, high values mean faster
        mouse movement'''
        return float()
    @property
    def walk_speed(self):
        '''(Float) Base speed for walking and flying'''
        return float()
    @property
    def walk_speed_factor(self):
        '''(Float) Multiplication factor when using the fast or slow modifiers'''
        return float()
    @property
    def view_height(self):
        '''(Float) View distance from the floor when walking'''
        return float()
    @property
    def jump_height(self):
        '''(Float) Maximum height of a jump'''
        return float()
    @property
    def teleport_time(self):
        '''(Float) Interval of time warp when teleporting in navigation mode'''
        return float()
    @property
    def use_gravity(self):
        '''(Boolean) Walk with gravity, or free navigate'''
        return bool()
    @property
    def use_mouse_reverse(self):
        '''(Boolean) Reverse the mouse look'''
        return bool()