from . actiongroups import ActionGroups
from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . actionposemarkers import ActionPoseMarkers
from . actionfcurves import ActionFCurves
from . library import Library
from . animdata import AnimData
from . bpy_struct import bpy_struct
import mathutils

class Action(bpy_struct):
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
    def fcurves(self):
        '''(Sequence of FCurve) The individual F-Curves that make up the action'''
        return ActionFCurves()
    @property
    def groups(self):
        '''(Sequence of ActionGroup) Convenient groupings of F-Curves'''
        return ActionGroups()
    @property
    def pose_markers(self):
        '''(Sequence of TimelineMarker) Markers specific to this action, for
        labeling poses'''
        return ActionPoseMarkers()
    @property
    def frame_range(self):
        '''(Vector 2D) The final frame range of all F-Curves within this action'''
        return mathutils.Vector()
    @property
    def id_root(self):
        '''(Enum) Type of ID block that action can be used on - DO NOT CHANGE
        UNLESS YOU KNOW WHAT YOU ARE DOING
        
        [ACTION, ARMATURE, BRUSH, CAMERA, CURVE, FONT, GREASEPENCIL, GROUP,
        IMAGE, KEY, LAMP, LIBRARY, LINESTYLE, LATTICE, MASK, MATERIAL, META,
        MESH, MOVIECLIP, NODETREE, OBJECT, PAINTCURVE, PALETTE, PARTICLE,
        SCENE, SCREEN, SOUND, SPEAKER, TEXT, TEXTURE, WINDOWMANAGER, WORLD]'''
        return str()
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