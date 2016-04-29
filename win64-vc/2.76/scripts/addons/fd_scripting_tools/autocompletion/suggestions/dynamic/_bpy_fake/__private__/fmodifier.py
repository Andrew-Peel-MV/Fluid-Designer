from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class FModifier(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) F-Curve Modifier Type
        
        [NULL, GENERATOR, FNGENERATOR, ENVELOPE, CYCLES, NOISE, PYTHON,
        LIMITS, STEPPED]'''
        return str()
    @property
    def show_expanded(self):
        '''(Boolean) F-Curve Modifier's panel is expanded in UI'''
        return bool()
    @property
    def mute(self):
        '''(Boolean) F-Curve Modifier will not be evaluated'''
        return bool()
    @property
    def is_valid(self):
        '''(Boolean) F-Curve Modifier has invalid settings and will not be
        evaluated'''
        return bool()
    @property
    def active(self):
        '''(Boolean) F-Curve Modifier is the one being edited'''
        return bool()
    @property
    def use_restricted_range(self):
        '''(Boolean) F-Curve Modifier is only applied for the specified frame
        range to help mask off effects in order to chain them'''
        return bool()
    @property
    def frame_start(self):
        '''(Float) Frame that modifier's influence starts (if Restrict Frame
        Range is in use)'''
        return float()
    @property
    def frame_end(self):
        '''(Float) Frame that modifier's influence ends (if Restrict Frame Range
        is in use)'''
        return float()
    @property
    def blend_in(self):
        '''(Float) Number of frames from start frame for influence to take effect'''
        return float()
    @property
    def blend_out(self):
        '''(Float) Number of frames from end frame for influence to fade out'''
        return float()
    @property
    def use_influence(self):
        '''(Boolean) F-Curve Modifier's effects will be tempered by a default
        factor'''
        return bool()
    @property
    def influence(self):
        '''(Float) Amount of influence F-Curve Modifier will have when not fading
        in/out'''
        return float()