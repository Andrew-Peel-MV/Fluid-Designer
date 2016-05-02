from . struct import Struct
from . masksplines import MaskSplines
from . bpy_struct import bpy_struct
import mathutils

class MaskLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name of layer'''
        return str()
    @property
    def splines(self):
        '''(Sequence of MaskSpline) Collection of splines which defines this
        layer'''
        return MaskSplines()
    @property
    def hide(self):
        '''(Boolean) Restrict visibility in the viewport'''
        return bool()
    @property
    def hide_select(self):
        '''(Boolean) Restrict selection in the viewport'''
        return bool()
    @property
    def hide_render(self):
        '''(Boolean) Restrict renderability'''
        return bool()
    @property
    def select(self):
        '''(Boolean) Layer is selected for editing in the Dope Sheet'''
        return bool()
    @property
    def alpha(self):
        '''(Float) Render Opacity'''
        return float()
    @property
    def blend(self):
        '''(Enum) Method of blending mask layers
        
        [MERGE_ADD, MERGE_SUBTRACT, ADD, SUBTRACT, LIGHTEN, DARKEN, MUL,
        REPLACE, DIFFERENCE]'''
        return str()
    @property
    def invert(self):
        '''(Boolean) Invert the mask black/white'''
        return bool()
    @property
    def falloff(self):
        '''(Enum) Falloff type the feather
        
        [SMOOTH, SPHERE, ROOT, INVERSE_SQUARE, SHARP, LINEAR]'''
        return str()
    @property
    def use_fill_holes(self):
        '''(Boolean) Calculate holes when filling overlapping curves'''
        return bool()
    @property
    def use_fill_overlap(self):
        '''(Boolean) Calculate self intersections and overlap before filling'''
        return bool()