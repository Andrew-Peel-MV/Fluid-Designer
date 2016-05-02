from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . library import Library
from . animdata import AnimData
from . sound import Sound
from . bpy_struct import bpy_struct
import mathutils

class Speaker(bpy_struct):
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
    def muted(self):
        '''(Boolean) Mute the speaker'''
        return bool()
    @property
    def relative(self):
        '''(Boolean) Whether the source is relative to the camera or not'''
        return bool()
    @property
    def sound(self):
        '''(Sound) Sound datablock used by this speaker'''
        return Sound()
    @property
    def volume_max(self):
        '''(Float) Maximum volume, no matter how near the object is'''
        return float()
    @property
    def volume_min(self):
        '''(Float) Minimum volume, no matter how far away the object is'''
        return float()
    @property
    def distance_max(self):
        '''(Float) Maximum distance for volume calculation, no matter how far
        away the object is'''
        return float()
    @property
    def distance_reference(self):
        '''(Float) Reference distance at which volume is 100 %'''
        return float()
    @property
    def attenuation(self):
        '''(Float) How strong the distance affects volume, depending on distance
        model'''
        return float()
    @property
    def cone_angle_outer(self):
        '''(Float) Angle of the outer cone, in degrees, outside this cone the
        volume is the outer cone volume, between inner and outer cone the
        volume is interpolated'''
        return float()
    @property
    def cone_angle_inner(self):
        '''(Float) Angle of the inner cone, in degrees, inside the cone the
        volume is 100 %'''
        return float()
    @property
    def cone_volume_outer(self):
        '''(Float) Volume outside the outer cone'''
        return float()
    @property
    def volume(self):
        '''(Float) How loud the sound is'''
        return float()
    @property
    def pitch(self):
        '''(Float) Playback pitch of the sound'''
        return float()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
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