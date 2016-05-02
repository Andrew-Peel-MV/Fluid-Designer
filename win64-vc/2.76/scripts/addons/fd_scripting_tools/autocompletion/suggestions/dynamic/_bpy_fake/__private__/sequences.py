from . scene import Scene
from . sequence import Sequence
from . struct import Struct
from . movieclip import MovieClip
from . mask import Mask
from . bpy_struct import bpy_struct
import mathutils

class Sequences(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new_clip(self, name, clip, channel, frame_start):
        '''Add a new movie clip sequence
        
        Parameter:
          name: (String) Name for the new sequence
          clip: (MovieClip) Movie clip to add
          channel: (Integer) The channel for the new sequence
          frame_start: (Integer) The start frame for the new sequence
        
        Returns:
          sequence: (Sequence) New Sequence'''
        return Sequence()
    def new_mask(self, name, mask, channel, frame_start):
        '''Add a new mask sequence
        
        Parameter:
          name: (String) Name for the new sequence
          mask: (Mask) Mask to add
          channel: (Integer) The channel for the new sequence
          frame_start: (Integer) The start frame for the new sequence
        
        Returns:
          sequence: (Sequence) New Sequence'''
        return Sequence()
    def new_scene(self, name, scene, channel, frame_start):
        '''Add a new scene sequence
        
        Parameter:
          name: (String) Name for the new sequence
          scene: (Scene) Scene to add
          channel: (Integer) The channel for the new sequence
          frame_start: (Integer) The start frame for the new sequence
        
        Returns:
          sequence: (Sequence) New Sequence'''
        return Sequence()
    def new_image(self, name, filepath, channel, frame_start):
        '''Add a new image sequence
        
        Parameter:
          name: (String) Name for the new sequence
          filepath: (String) Filepath to image
          channel: (Integer) The channel for the new sequence
          frame_start: (Integer) The start frame for the new sequence
        
        Returns:
          sequence: (Sequence) New Sequence'''
        return Sequence()
    def new_movie(self, name, filepath, channel, frame_start):
        '''Add a new movie sequence
        
        Parameter:
          name: (String) Name for the new sequence
          filepath: (String) Filepath to movie
          channel: (Integer) The channel for the new sequence
          frame_start: (Integer) The start frame for the new sequence
        
        Returns:
          sequence: (Sequence) New Sequence'''
        return Sequence()
    def new_sound(self, name, filepath, channel, frame_start):
        '''Add a new sound sequence
        
        Parameter:
          name: (String) Name for the new sequence
          filepath: (String) Filepath to movie
          channel: (Integer) The channel for the new sequence
          frame_start: (Integer) The start frame for the new sequence
        
        Returns:
          sequence: (Sequence) New Sequence'''
        return Sequence()
    def new_effect(self, name, type, channel, frame_start, frame_end, seq1, seq2, seq3):
        '''Add a new effect sequence
        
        Parameter:
          name: (String) Name for the new sequence
          type: (Enum) type for the new sequence
          channel: (Integer) The channel for the new sequence
          frame_start: (Integer) The start frame for the new sequence
          frame_end: (Integer) The end frame for the new sequence
          seq1: (Sequence) Sequence 1 for effect
          seq2: (Sequence) Sequence 2 for effect
          seq3: (Sequence) Sequence 3 for effect
        
        Returns:
          sequence: (Sequence) New Sequence'''
        return Sequence()
    def remove(self, sequence):
        '''Remove a Sequence
        
        Parameter:
          sequence: (Sequence) Sequence to remove'''
        return 
    def get(key): return Sequence()
    def __getitem__(key): return Sequence()
    def __iter__(key): yield Sequence()