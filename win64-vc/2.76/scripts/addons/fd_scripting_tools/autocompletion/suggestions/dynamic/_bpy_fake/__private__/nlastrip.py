from . nlastrip import NlaStrip
from . action import Action
from . struct import Struct
from . fmodifier import FModifier
from . nlastripfcurves import NlaStripFCurves
from . bpy_struct import bpy_struct
import mathutils

class NlaStrip(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def type(self):
        '''(Enum) Type of NLA Strip
        
        [CLIP, TRANSITION, META, SOUND]'''
        return str()
    @property
    def extrapolation(self):
        '''(Enum) Action to take for gaps past the strip extents
        
        [NOTHING, HOLD, HOLD_FORWARD]'''
        return str()
    @property
    def blend_type(self):
        '''(Enum) Method used for combining strip's result with accumulated
        result
        
        [REPLACE, ADD, SUBTRACT, MULTIPLY]'''
        return str()
    @property
    def frame_start(self):
        '''(Float)'''
        return float()
    @property
    def frame_end(self):
        '''(Float)'''
        return float()
    @property
    def blend_in(self):
        '''(Float) Number of frames at start of strip to fade in influence'''
        return float()
    @property
    def blend_out(self):
        '''(Float)'''
        return float()
    @property
    def use_auto_blend(self):
        '''(Boolean) Number of frames for Blending In/Out is automatically
        determined from overlapping strips'''
        return bool()
    @property
    def action(self):
        '''(Action) Action referenced by this strip'''
        return Action()
    @property
    def action_frame_start(self):
        '''(Float) First frame from action to use'''
        return float()
    @property
    def action_frame_end(self):
        '''(Float) Last frame from action to use'''
        return float()
    @property
    def repeat(self):
        '''(Float) Number of times to repeat the action range'''
        return float()
    @property
    def scale(self):
        '''(Float) Scaling factor for action'''
        return float()
    @property
    def fcurves(self):
        '''(Sequence of FCurve) F-Curves for controlling the strip's influence
        and timing'''
        return NlaStripFCurves()
    @property
    def modifiers(self):
        '''(Sequence of FModifier) Modifiers affecting all the F-Curves in the
        referenced Action'''
        return (FModifier(),)
    @property
    def strips(self):
        '''(Sequence of NlaStrip) NLA Strips that this strip acts as a container
        for (if it is of type Meta)'''
        return (NlaStrip(),)
    @property
    def influence(self):
        '''(Float) Amount the strip contributes to the current result'''
        return float()
    @property
    def strip_time(self):
        '''(Float) Frame of referenced Action to evaluate'''
        return float()
    @property
    def use_animated_influence(self):
        '''(Boolean) Influence setting is controlled by an F-Curve rather than
        automatically determined'''
        return bool()
    @property
    def use_animated_time(self):
        '''(Boolean) Strip time is controlled by an F-Curve rather than
        automatically determined'''
        return bool()
    @property
    def use_animated_time_cyclic(self):
        '''(Boolean) Cycle the animated time within the action start & end'''
        return bool()
    @property
    def active(self):
        '''(Boolean) NLA Strip is active'''
        return bool()
    @property
    def select(self):
        '''(Boolean) NLA Strip is selected'''
        return bool()
    @property
    def mute(self):
        '''(Boolean) NLA Strip is not evaluated'''
        return bool()
    @property
    def use_reverse(self):
        '''(Boolean) NLA Strip is played back in reverse order (only when timing
        is automatically determined)'''
        return bool()
    @property
    def use_sync_length(self):
        '''(Boolean) Update range of frames referenced from action after tweaking
        strip and its keyframes'''
        return bool()