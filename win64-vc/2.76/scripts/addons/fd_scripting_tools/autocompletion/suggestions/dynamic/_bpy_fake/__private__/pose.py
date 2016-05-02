from . struct import Struct
from . posebone import PoseBone
from . bonegroups import BoneGroups
from . ikparam import IKParam
from . animviz import AnimViz
from . bpy_struct import bpy_struct
import mathutils

class Pose(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def bones(self):
        '''(Sequence of PoseBone) Individual pose bones for the armature'''
        return (PoseBone(),)
    @property
    def bone_groups(self):
        '''(Sequence of BoneGroup) Groups of the bones'''
        return BoneGroups()
    @property
    def ik_solver(self):
        '''(Enum) Selection of IK solver for IK chain
        
        [LEGACY, ITASC]'''
        return str()
    @property
    def ik_param(self):
        '''(IKParam) Parameters for IK solver'''
        return IKParam()
    @property
    def animation_visualization(self):
        '''(AnimViz) Animation data for this datablock'''
        return AnimViz()