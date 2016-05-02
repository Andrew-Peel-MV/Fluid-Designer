from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . armatureeditbones import ArmatureEditBones
from . library import Library
from . animdata import AnimData
from . armaturebones import ArmatureBones
from . bpy_struct import bpy_struct
import mathutils

class Armature(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique datablock ID name'''
        return str()
    @property
    def users(self):
        '''(Integer) Number of times this datablock is referenced'''
        return int()
    @property
    def use_fake_user(self):
        '''(Boolean) Save this datablock even if it has no users'''
        return bool()
    @property
    def tag(self):
        '''(Boolean) Tools can use this to tag data for their own purposes
        (initial state is undefined)'''
        return bool()
    @property
    def is_updated(self):
        '''(Boolean) Datablock is tagged for recalculation'''
        return bool()
    @property
    def is_updated_data(self):
        '''(Boolean) Datablock data is tagged for recalculation'''
        return bool()
    @property
    def is_library_indirect(self):
        '''(Boolean) Is this ID block linked indirectly'''
        return bool()
    @property
    def library(self):
        '''(Library) Library file the datablock is linked from'''
        return Library()
    @property
    def preview(self):
        '''(ImagePreview) Preview image and icon of this datablock (None if not
        supported for this type of data)'''
        return ImagePreview()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def bones(self):
        '''(Sequence of Bone)'''
        return ArmatureBones()
    @property
    def edit_bones(self):
        '''(Sequence of EditBone)'''
        return ArmatureEditBones()
    @property
    def pose_position(self):
        '''(Enum) Show armature in binding pose or final posed state
        
        [POSE, REST]'''
        return str()
    @property
    def draw_type(self):
        '''(Enum)
        
        [OCTAHEDRAL, STICK, BBONE, ENVELOPE, WIRE]'''
        return str()
    @property
    def deform_method(self):
        '''(Enum) Vertex Deformer Method (Game Engine only)
        
        [BLENDER, BGE_CPU]'''
        return str()
    @property
    def ghost_type(self):
        '''(Enum) Method of Onion-skinning for active Action
        
        [CURRENT_FRAME, RANGE, KEYS]'''
        return str()
    @property
    def layers(self):
        '''(Boolean[32]) Armature layer visibility'''
        return bool()
    @property
    def layers_protected(self):
        '''(Boolean[32]) Protected layers in Proxy Instances are restored to
        Proxy settings on file reload and undo'''
        return bool()
    @property
    def show_axes(self):
        '''(Boolean) Draw bone axes'''
        return bool()
    @property
    def show_names(self):
        '''(Boolean) Draw bone names'''
        return bool()
    @property
    def use_deform_delay(self):
        '''(Boolean) Don't deform children when manipulating bones in Pose Mode'''
        return bool()
    @property
    def use_mirror_x(self):
        '''(Boolean) Apply changes to matching bone on opposite side of X-Axis'''
        return bool()
    @property
    def use_auto_ik(self):
        '''(Boolean) Add temporary IK constraints while grabbing bones in Pose
        Mode'''
        return bool()
    @property
    def show_bone_custom_shapes(self):
        '''(Boolean) Draw bones with their custom shapes'''
        return bool()
    @property
    def show_group_colors(self):
        '''(Boolean) Draw bone group colors'''
        return bool()
    @property
    def show_only_ghost_selected(self):
        '''(Boolean)'''
        return bool()
    @property
    def ghost_step(self):
        '''(Integer) Number of frame steps on either side of current frame to
        show as ghosts (only for 'Around Current Frame' Onion-skinning method)'''
        return int()
    @property
    def ghost_size(self):
        '''(Integer) Frame step for Ghosts (not for 'On Keyframes' Onion-skinning
        method)'''
        return int()
    @property
    def ghost_frame_start(self):
        '''(Integer) Starting frame of range of Ghosts to display (not for
        'Around Current Frame' Onion-skinning method)'''
        return int()
    @property
    def ghost_frame_end(self):
        '''(Integer) End frame of range of Ghosts to display (not for 'Around
        Current Frame' Onion-skinning method)'''
        return int()
    @property
    def is_editmode(self):
        '''(Boolean) True when used in editmode'''
        return bool()
    def copy(self):
        '''Create a copy of this datablock (not supported for all datablocks)
        
        Returns:
          id: (ID) New copy of the ID'''
        return ID()
    def user_clear(self):
        '''Clear the user count of a datablock so its not saved, on reload the
        data will be removed'''
        return 
    def animation_data_create(self):
        '''Create animation data to this ID, note that not all ID types support
        this
        
        Returns:
          anim_data: (AnimData) New animation data or NULL'''
        return AnimData()
    def animation_data_clear(self):
        '''Clear animation on this this ID'''
        return 
    def update_tag(self, refresh):
        '''Tag the ID to update its display data, e.g. when calling
        :class:`bpy.types.Scene.update`
        
        Parameter:
          refresh: (Enum) Type of updates to perform'''
        return 
    def transform(self, matrix):
        '''Transform armature bones by a matrix
        
        Parameter:
          matrix: (Matrix) Matrix'''
        return 