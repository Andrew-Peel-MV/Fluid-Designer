from . nlastrips import NlaStrips
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class NlaTrack(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def strips(self):
        '''(Sequence of NlaStrip) NLA Strips on this NLA-track'''
        return NlaStrips()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def active(self):
        '''(Boolean) NLA Track is active'''
        return bool()
    @property
    def is_solo(self):
        '''(Boolean) NLA Track is evaluated itself (i.e. active Action and all
        other NLA Tracks in the same AnimData block are disabled)'''
        return bool()
    @property
    def select(self):
        '''(Boolean) NLA Track is selected'''
        return bool()
    @property
    def mute(self):
        '''(Boolean) NLA Track is not evaluated'''
        return bool()
    @property
    def lock(self):
        '''(Boolean) NLA Track is locked'''
        return bool()