from . struct import Struct
from . animvizmotionpaths import AnimVizMotionPaths
from . animvizonionskinning import AnimVizOnionSkinning
from . bpy_struct import bpy_struct
import mathutils

class AnimViz(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def onion_skin_frames(self):
        '''(AnimVizOnionSkinning) Onion Skinning (ghosting) settings for
        visualization'''
        return AnimVizOnionSkinning()
    @property
    def motion_path(self):
        '''(AnimVizMotionPaths) Motion Path settings for visualization'''
        return AnimVizMotionPaths()