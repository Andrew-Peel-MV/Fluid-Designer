from . movietracking import MovieTracking
from . imagepreview import ImagePreview
from . id import ID
from . greasepencil import GreasePencil
from . struct import Struct
from . colormanagedinputcolorspacesettings import ColorManagedInputColorspaceSettings
from . movieclipproxy import MovieClipProxy
from . library import Library
from . animdata import AnimData
from . bpy_struct import bpy_struct
import mathutils

class MovieClip(bpy_struct):
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
    def filepath(self):
        '''(String) Filename of the movie or sequence file'''
        return str()
    @property
    def tracking(self):
        '''(MovieTracking)'''
        return MovieTracking()
    @property
    def proxy(self):
        '''(MovieClipProxy)'''
        return MovieClipProxy()
    @property
    def use_proxy(self):
        '''(Boolean) Use a preview proxy and/or timecode index for this clip'''
        return bool()
    @property
    def size(self):
        '''(Integer[2]) Width and height in pixels, zero when image data cant be
        loaded'''
        return int()
    @property
    def display_aspect(self):
        '''(Vector 2D) Display Aspect for this clip, does not affect rendering'''
        return mathutils.Vector()
    @property
    def source(self):
        '''(Enum) Where the clip comes from
        
        [SEQUENCE, MOVIE]'''
        return str()
    @property
    def use_proxy_custom_directory(self):
        '''(Boolean) Create proxy images in a custom directory (default is movie
        location)'''
        return bool()
    @property
    def grease_pencil(self):
        '''(GreasePencil) Grease pencil data for this movie clip'''
        return GreasePencil()
    @property
    def frame_start(self):
        '''(Integer) Global scene frame number at which this movie starts playing
        (affects all data associated with a clip)'''
        return int()
    @property
    def frame_offset(self):
        '''(Integer) Offset of footage first frame relative to it's file name
        (affects only how footage is loading, does not change data associated
        with a clip)'''
        return int()
    @property
    def frame_duration(self):
        '''(Integer) Detected duration of movie clip in frames'''
        return int()
    @property
    def colorspace_settings(self):
        '''(ColorManagedInputColorspaceSettings) Input color space settings'''
        return ColorManagedInputColorspaceSettings()
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