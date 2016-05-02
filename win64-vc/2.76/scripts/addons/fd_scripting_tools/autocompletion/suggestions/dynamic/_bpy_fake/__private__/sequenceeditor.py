from . sequences import Sequences
from . struct import Struct
from . sequence import Sequence
from . bpy_struct import bpy_struct
import mathutils

class SequenceEditor(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def sequences(self):
        '''(Sequence of Sequence) Top-level strips only'''
        return Sequences()
    @property
    def sequences_all(self):
        '''(Sequence of Sequence) All strips, recursively including those inside
        metastrips'''
        return (Sequence(),)
    @property
    def meta_stack(self):
        '''(Sequence of Sequence) Meta strip stack, last is currently edited meta
        strip'''
        return (Sequence(),)
    @property
    def active_strip(self):
        '''(Sequence) Sequencer's active strip'''
        return Sequence()
    @property
    def show_overlay(self):
        '''(Boolean) Partial overlay on top of the sequencer'''
        return bool()
    @property
    def use_overlay_lock(self):
        '''(Boolean)'''
        return bool()
    @property
    def overlay_frame(self):
        '''(Integer)'''
        return int()
    @property
    def proxy_storage(self):
        '''(Enum) How to store proxies for this project
        
        [PER_STRIP, PROJECT]'''
        return str()
    @property
    def proxy_dir(self):
        '''(String)'''
        return str()