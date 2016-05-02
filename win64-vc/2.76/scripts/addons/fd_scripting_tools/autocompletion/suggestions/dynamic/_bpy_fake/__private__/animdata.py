from . action import Action
from . struct import Struct
from . animdatadrivers import AnimDataDrivers
from . nlatracks import NlaTracks
from . bpy_struct import bpy_struct
import mathutils

class AnimData(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def nla_tracks(self):
        '''(Sequence of NlaTrack) NLA Tracks (i.e. Animation Layers)'''
        return NlaTracks()
    @property
    def action(self):
        '''(Action) Active Action for this datablock'''
        return Action()
    @property
    def action_extrapolation(self):
        '''(Enum) Action to take for gaps past the Active Action's range (when
        evaluating with NLA)
        
        [NOTHING, HOLD, HOLD_FORWARD]'''
        return str()
    @property
    def action_blend_type(self):
        '''(Enum) Method used for combining Active Action's result with result of
        NLA stack
        
        [REPLACE, ADD, SUBTRACT, MULTIPLY]'''
        return str()
    @property
    def action_influence(self):
        '''(Float) Amount the Active Action contributes to the result of the NLA
        stack'''
        return float()
    @property
    def drivers(self):
        '''(Sequence of FCurve) The Drivers/Expressions for this datablock'''
        return AnimDataDrivers()
    @property
    def use_nla(self):
        '''(Boolean) NLA stack is evaluated when evaluating this block'''
        return bool()