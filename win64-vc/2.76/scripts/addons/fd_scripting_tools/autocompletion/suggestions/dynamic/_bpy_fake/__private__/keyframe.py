from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Keyframe(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def select_left_handle(self):
        '''(Boolean) Left handle selection status'''
        return bool()
    @property
    def select_right_handle(self):
        '''(Boolean) Right handle selection status'''
        return bool()
    @property
    def select_control_point(self):
        '''(Boolean) Control point selection status'''
        return bool()
    @property
    def handle_left_type(self):
        '''(Enum) Handle types
        
        [FREE, VECTOR, ALIGNED, AUTO, AUTO_CLAMPED]'''
        return str()
    @property
    def handle_right_type(self):
        '''(Enum) Handle types
        
        [FREE, VECTOR, ALIGNED, AUTO, AUTO_CLAMPED]'''
        return str()
    @property
    def interpolation(self):
        '''(Enum) Interpolation method to use for segment of the F-Curve from
        this Keyframe until the next Keyframe
        
        [CONSTANT, LINEAR, BEZIER, SINE, QUAD, CUBIC, QUART, QUINT, EXPO,
        CIRC, BACK, BOUNCE, ELASTIC]'''
        return str()
    @property
    def type(self):
        '''(Enum) Type of keyframe (for visual purposes only)
        
        [KEYFRAME, BREAKDOWN, EXTREME, JITTER]'''
        return str()
    @property
    def easing(self):
        '''(Enum) Which ends of the segment between this and the next keyframe
        easing interpolation is applied to
        
        [AUTO, EASE_IN, EASE_OUT, EASE_IN_OUT]'''
        return str()
    @property
    def back(self):
        '''(Float) Amount of overshoot for 'back' easing'''
        return float()
    @property
    def amplitude(self):
        '''(Float) Amount to boost elastic bounces for 'elastic' easing'''
        return float()
    @property
    def period(self):
        '''(Float) Time between bounces for elastic easing'''
        return float()
    @property
    def handle_left(self):
        '''(Vector 2D) Coordinates of the left handle (before the control point)'''
        return mathutils.Vector()
    @property
    def co(self):
        '''(Vector 2D) Coordinates of the control point'''
        return mathutils.Vector()
    @property
    def handle_right(self):
        '''(Vector 2D) Coordinates of the right handle (after the control point)'''
        return mathutils.Vector()