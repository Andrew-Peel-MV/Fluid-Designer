from . id import ID
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaskParent(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def id(self):
        '''(ID) ID-block to which masking element would be parented to or to it's
        property'''
        return ID()
    @property
    def id_type(self):
        '''(Enum) Type of ID-block that can be used
        
        [MOVIECLIP]'''
        return str()
    @property
    def type(self):
        '''(Enum) Parent Type
        
        [POINT_TRACK, PLANE_TRACK]'''
        return str()
    @property
    def parent(self):
        '''(String) Name of parent object in specified data block to which
        parenting happens'''
        return str()
    @property
    def sub_parent(self):
        '''(String) Name of parent sub-object in specified data block to which
        parenting happens'''
        return str()