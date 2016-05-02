from . struct import Struct
from . sequenceelement import SequenceElement
from . sequence import Sequence
from . sequencemodifiers import SequenceModifiers
from . bpy_struct import bpy_struct
import mathutils

class Sequence(bpy_struct):
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
        '''(Enum)
        
        [IMAGE, META, SCENE, MOVIE, MOVIECLIP, MASK, SOUND, CROSS, ADD,
        SUBTRACT, ALPHA_OVER, ALPHA_UNDER, GAMMA_CROSS, MULTIPLY, OVER_DROP,
        WIPE, GLOW, TRANSFORM, COLOR, SPEED, MULTICAM, ADJUSTMENT,
        GAUSSIAN_BLUR, TEXT]'''
        return str()
    @property
    def select(self):
        '''(Boolean)'''
        return bool()
    @property
    def select_left_handle(self):
        '''(Boolean)'''
        return bool()
    @property
    def select_right_handle(self):
        '''(Boolean)'''
        return bool()
    @property
    def mute(self):
        '''(Boolean)'''
        return bool()
    @property
    def lock(self):
        '''(Boolean) Lock strip so that it can't be transformed'''
        return bool()
    @property
    def frame_final_duration(self):
        '''(Integer) The length of the contents of this strip after the handles
        are applied'''
        return int()
    @property
    def frame_duration(self):
        '''(Integer) The length of the contents of this strip before the handles
        are applied'''
        return int()
    @property
    def frame_start(self):
        '''(Integer)'''
        return int()
    @property
    def frame_final_start(self):
        '''(Integer) Start frame displayed in the sequence editor after offsets
        are applied, setting this is equivalent to moving the handle, not the
        actual start frame'''
        return int()
    @property
    def frame_final_end(self):
        '''(Integer) End frame displayed in the sequence editor after offsets are
        applied'''
        return int()
    @property
    def frame_offset_start(self):
        '''(Integer)'''
        return int()
    @property
    def frame_offset_end(self):
        '''(Integer)'''
        return int()
    @property
    def frame_still_start(self):
        '''(Integer)'''
        return int()
    @property
    def frame_still_end(self):
        '''(Integer)'''
        return int()
    @property
    def channel(self):
        '''(Integer) Y position of the sequence strip'''
        return int()
    @property
    def use_linear_modifiers(self):
        '''(Boolean) Calculate modifiers in linear space instead of sequencer's
        space'''
        return bool()
    @property
    def blend_type(self):
        '''(Enum)
        
        [REPLACE, CROSS, ADD, SUBTRACT, ALPHA_OVER, ALPHA_UNDER, GAMMA_CROSS,
        MULTIPLY, OVER_DROP]'''
        return str()
    @property
    def blend_alpha(self):
        '''(Float)'''
        return float()
    @property
    def effect_fader(self):
        '''(Float)'''
        return float()
    @property
    def use_default_fade(self):
        '''(Boolean) Fade effect using the built-in default (usually make
        transition as long as effect strip)'''
        return bool()
    @property
    def speed_factor(self):
        '''(Float) Multiply the current speed of the sequence with this number or
        remap current frame to this frame'''
        return float()
    @property
    def modifiers(self):
        '''(Sequence of SequenceModifier) Modifiers affecting this strip'''
        return SequenceModifiers()
    def update(self, data):
        '''Update the strip dimensions
        
        Parameter:
          data: (Boolean) Update strip data'''
        return 
    def strip_elem_from_frame(self, frame):
        '''Return the strip element from a given frame or None
        
        Parameter:
          frame: (Integer) The frame to get the strip element from
        
        Returns:
          elem: (SequenceElement) strip element of the current frame'''
        return SequenceElement()
    def swap(self, other):
        '''swap
        
        Parameter:
          other: (Sequence)'''
        return 