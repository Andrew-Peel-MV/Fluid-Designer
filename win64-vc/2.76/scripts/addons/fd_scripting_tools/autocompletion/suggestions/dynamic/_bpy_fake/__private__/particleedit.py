from . struct import Struct
from . particlebrush import ParticleBrush
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class ParticleEdit(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def tool(self):
        '''(Enum)
        
        [NONE, COMB, SMOOTH, ADD, LENGTH, PUFF, CUT, WEIGHT]'''
        return str()
    @property
    def select_mode(self):
        '''(Enum) Particle select and display mode
        
        [PATH, POINT, TIP]'''
        return str()
    @property
    def use_preserve_length(self):
        '''(Boolean) Keep path lengths constant'''
        return bool()
    @property
    def use_preserve_root(self):
        '''(Boolean) Keep root keys unmodified'''
        return bool()
    @property
    def use_emitter_deflect(self):
        '''(Boolean) Keep paths from intersecting the emitter'''
        return bool()
    @property
    def emitter_distance(self):
        '''(Float) Distance to keep particles away from the emitter'''
        return float()
    @property
    def use_fade_time(self):
        '''(Boolean) Fade paths and keys further away from current frame'''
        return bool()
    @property
    def use_auto_velocity(self):
        '''(Boolean) Calculate point velocities automatically'''
        return bool()
    @property
    def show_particles(self):
        '''(Boolean) Draw actual particles'''
        return bool()
    @property
    def use_default_interpolate(self):
        '''(Boolean) Interpolate new particles from the existing ones'''
        return bool()
    @property
    def default_key_count(self):
        '''(Integer) How many keys to make new particles with'''
        return int()
    @property
    def brush(self):
        '''(ParticleBrush)'''
        return ParticleBrush()
    @property
    def draw_step(self):
        '''(Integer) How many steps to draw the path with'''
        return int()
    @property
    def fade_frames(self):
        '''(Integer) How many frames to fade'''
        return int()
    @property
    def type(self):
        '''(Enum)
        
        [PARTICLES, SOFT_BODY, CLOTH]'''
        return str()
    @property
    def is_editable(self):
        '''(Boolean) A valid edit mode exists'''
        return bool()
    @property
    def is_hair(self):
        '''(Boolean) Editing hair'''
        return bool()
    @property
    def object(self):
        '''(Object) The edited object'''
        return Object()
    @property
    def shape_object(self):
        '''(Object) Outer shape to use for tools'''
        return Object()