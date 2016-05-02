from . imageuser import ImageUser
from . stereo3dformat import Stereo3dFormat
from . packedfile import PackedFile
from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . colormanagedinputcolorspacesettings import ColorManagedInputColorspaceSettings
from . imagepackedfile import ImagePackedFile
from . scene import Scene
from . library import Library
from . animdata import AnimData
from . renderslots import RenderSlots
from . bpy_struct import bpy_struct
import mathutils

class Image(bpy_struct):
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
        '''(String) Image/Movie file name'''
        return str()
    @property
    def filepath_raw(self):
        '''(String) Image/Movie file name (without data refreshing)'''
        return str()
    @property
    def file_format(self):
        '''(Enum) Format used for re-saving this file
        
        [BMP, IRIS, PNG, JPEG, JPEG2000, TARGA, TARGA_RAW, CINEON, DPX,
        OPEN_EXR_MULTILAYER, OPEN_EXR, HDR, TIFF, AVI_JPEG, AVI_RAW,
        FRAMESERVER, H264, FFMPEG, THEORA, XVID]'''
        return str()
    @property
    def source(self):
        '''(Enum) Where the image comes from
        
        [FILE, SEQUENCE, MOVIE, GENERATED, VIEWER]'''
        return str()
    @property
    def type(self):
        '''(Enum) How to generate the image
        
        [IMAGE, MULTILAYER, UV_TEST, RENDER_RESULT, COMPOSITING]'''
        return str()
    @property
    def packed_file(self):
        '''(PackedFile) First packed file of the image'''
        return PackedFile()
    @property
    def packed_files(self):
        '''(Sequence of ImagePackedFile) Collection of packed images'''
        return (ImagePackedFile(),)
    @property
    def field_order(self):
        '''(Enum) Order of video fields (select which lines are displayed first)
        
        [EVEN, ODD]'''
        return str()
    @property
    def use_fields(self):
        '''(Boolean) Use fields of the image'''
        return bool()
    @property
    def use_view_as_render(self):
        '''(Boolean) Apply render part of display transformation when displaying
        this image on the screen'''
        return bool()
    @property
    def use_alpha(self):
        '''(Boolean) Use the alpha channel information from the image or make
        image fully opaque'''
        return bool()
    @property
    def use_deinterlace(self):
        '''(Boolean) Deinterlace movie file on load'''
        return bool()
    @property
    def use_multiview(self):
        '''(Boolean) Use Multiple Views (when available)'''
        return bool()
    @property
    def is_stereo_3d(self):
        '''(Boolean) Image has left and right views'''
        return bool()
    @property
    def is_multiview(self):
        '''(Boolean) Image has more than one view'''
        return bool()
    @property
    def is_dirty(self):
        '''(Boolean) Image has changed and is not saved'''
        return bool()
    @property
    def generated_type(self):
        '''(Enum) Generated image type
        
        [BLANK, UV_GRID, COLOR_GRID]'''
        return str()
    @property
    def generated_width(self):
        '''(Integer) Generated image width'''
        return int()
    @property
    def generated_height(self):
        '''(Integer) Generated image height'''
        return int()
    @property
    def use_generated_float(self):
        '''(Boolean) Generate floating point buffer'''
        return bool()
    @property
    def generated_color(self):
        '''(Float[4]) Fill color for the generated image'''
        return ''
    @property
    def mapping(self):
        '''(Enum) Mapping type to use for this image in the game engine
        
        [UV, REFLECTION]'''
        return str()
    @property
    def display_aspect(self):
        '''(Vector 2D) Display Aspect for this image, does not affect rendering'''
        return mathutils.Vector()
    @property
    def use_animation(self):
        '''(Boolean) Use as animated texture in the game engine'''
        return bool()
    @property
    def frame_start(self):
        '''(Integer) Start frame of an animated texture'''
        return int()
    @property
    def frame_end(self):
        '''(Integer) End frame of an animated texture'''
        return int()
    @property
    def fps(self):
        '''(Integer) Speed of the animation in frames per second'''
        return int()
    @property
    def use_tiles(self):
        '''(Boolean) Use of tilemode for faces (default shift-LMB to pick the
        tile for selected faces)'''
        return bool()
    @property
    def tiles_x(self):
        '''(Integer) Degree of repetition in the X direction'''
        return int()
    @property
    def tiles_y(self):
        '''(Integer) Degree of repetition in the Y direction'''
        return int()
    @property
    def use_clamp_x(self):
        '''(Boolean) Disable texture repeating horizontally'''
        return bool()
    @property
    def use_clamp_y(self):
        '''(Boolean) Disable texture repeating vertically'''
        return bool()
    @property
    def bindcode(self):
        '''(Integer) OpenGL bindcode'''
        return int()
    @property
    def render_slots(self):
        '''(Sequence of RenderSlot) Render slots of the image'''
        return RenderSlots()
    @property
    def has_data(self):
        '''(Boolean) True if this image has data'''
        return bool()
    @property
    def depth(self):
        '''(Integer) Image bit depth'''
        return int()
    @property
    def size(self):
        '''(Integer[2]) Width and height in pixels, zero when image data cant be
        loaded'''
        return int()
    @property
    def resolution(self):
        '''(Vector 2D) X/Y pixels per meter'''
        return mathutils.Vector()
    @property
    def frame_duration(self):
        '''(Integer) Duration (in frames) of the image (1 when not a
        video/sequence)'''
        return int()
    @property
    def pixels(self):
        '''(Float) Image pixels in floating point values'''
        return float()
    @property
    def channels(self):
        '''(Integer) Number of channels in pixels buffer'''
        return int()
    @property
    def is_float(self):
        '''(Boolean) True if this image is stored in float buffer'''
        return bool()
    @property
    def colorspace_settings(self):
        '''(ColorManagedInputColorspaceSettings) Input color space settings'''
        return ColorManagedInputColorspaceSettings()
    @property
    def alpha_mode(self):
        '''(Enum) Representation of alpha information in the RGBA pixels
        
        [STRAIGHT, PREMUL]'''
        return str()
    @property
    def views_format(self):
        '''(Enum) Mode to load image views
        
        [INDIVIDUAL, STEREO_3D]'''
        return str()
    @property
    def stereo_3d_format(self):
        '''(Stereo3dFormat) Settings for stereo 3d'''
        return Stereo3dFormat()
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
    def save_render(self, filepath, scene):
        '''Save image to a specific path using a scenes render settings
        
        Parameter:
          filepath: (String) Save path
          scene: (Scene) Scene to take image parameters from'''
        return 
    def save(self):
        '''Save image to its source path'''
        return 
    def pack(self, as_png, data, data_len):
        '''Pack an image as embedded data into the .blend file
        
        Parameter:
          as_png: (Boolean) Pack the image as PNG (needed for generated/dirty images)
          data: (String) Raw data (bytes, exact content of the embedded file)
          data_len: (Integer) length of given data (mandatory if data is provided)'''
        return 
    def unpack(self, method):
        '''Save an image packed in the .blend file to disk
        
        Parameter:
          method: (Enum) How to unpack'''
        return 
    def reload(self):
        '''Reload the image from its source path'''
        return 
    def update(self):
        '''Update the display image from the floating point buffer'''
        return 
    def scale(self, width, height):
        '''Scale the image in pixels
        
        Parameter:
          width: (Integer) Width
          height: (Integer) Height'''
        return 
    def gl_touch(self, frame, filter, mag):
        '''Delay the image from being cleaned from the cache due inactivity
        
        Parameter:
          frame: (Integer) Frame of image sequence or movie
          filter:
            (Integer) The texture minifying function to use if the image wasn't
            loaded
          mag:
            (Integer) The texture magnification function to use if the image
            wasn't loaded
        
        Returns:
          error: (Integer) OpenGL error value'''
        return int()
    def gl_load(self, frame, filter, mag):
        '''Load the image into OpenGL graphics memory
        
        Parameter:
          frame: (Integer) Frame of image sequence or movie
          filter: (Integer) The texture minifying function
          mag: (Integer) The texture magnification function
        
        Returns:
          error: (Integer) OpenGL error value'''
        return int()
    def gl_free(self):
        '''Free the image from OpenGL graphics memory'''
        return 
    def filepath_from_user(self, image_user):
        '''Return the absolute path to the filepath of an image frame specified
        by the image user
        
        Parameter:
          image_user: (ImageUser) Image user of the image to get filepath for
        
        Returns:
          filepath: (String) The resulting filepath from the image and it's user'''
        return str()
    def buffers_free(self):
        '''Free the image buffers from memory'''
        return 