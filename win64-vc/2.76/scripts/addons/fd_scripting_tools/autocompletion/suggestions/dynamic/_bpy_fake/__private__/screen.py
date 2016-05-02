from . imagepreview import ImagePreview
from . id import ID
from . area import Area
from . struct import Struct
from . scene import Scene
from . library import Library
from . animdata import AnimData
from . bpy_struct import bpy_struct
import mathutils

class Screen(bpy_struct):
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
    def scene(self):
        '''(Scene) Active scene to be edited in the screen'''
        return Scene()
    @property
    def areas(self):
        '''(Sequence of Area) Areas the screen is subdivided into'''
        return (Area(),)
    @property
    def is_animation_playing(self):
        '''(Boolean) Animation playback is active'''
        return bool()
    @property
    def show_fullscreen(self):
        '''(Boolean) An area is maximized, filling this screen'''
        return bool()
    @property
    def use_play_top_left_3d_editor(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_play_3d_editors(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_follow(self):
        '''(Boolean) Follow current frame in editors'''
        return bool()
    @property
    def use_play_animation_editors(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_play_properties_editors(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_play_image_editors(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_play_sequence_editors(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_play_node_editors(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_play_clip_editors(self):
        '''(Boolean)'''
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