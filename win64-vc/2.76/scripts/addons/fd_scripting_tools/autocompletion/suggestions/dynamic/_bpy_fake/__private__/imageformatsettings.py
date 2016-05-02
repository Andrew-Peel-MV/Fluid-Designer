from . colormanageddisplaysettings import ColorManagedDisplaySettings
from . stereo3dformat import Stereo3dFormat
from . struct import Struct
from . colormanagedviewsettings import ColorManagedViewSettings
from . bpy_struct import bpy_struct
import mathutils

class ImageFormatSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def file_format(self):
        '''(Enum) File format to save the rendered images as
        
        [BMP, IRIS, PNG, JPEG, JPEG2000, TARGA, TARGA_RAW, CINEON, DPX,
        OPEN_EXR_MULTILAYER, OPEN_EXR, HDR, TIFF, AVI_JPEG, AVI_RAW,
        FRAMESERVER, H264, FFMPEG, THEORA, XVID]'''
        return str()
    @property
    def color_mode(self):
        '''(Enum) Choose BW for saving grayscale images, RGB for saving red,
        green and blue channels, and RGBA for saving red, green, blue and
        alpha channels
        
        [BW, RGB, RGBA]'''
        return str()
    @property
    def color_depth(self):
        '''(Enum) Bit depth per channel
        
        [8, 10, 12, 16, 32]'''
        return str()
    @property
    def quality(self):
        '''(Integer) Quality for image formats that support lossy compression'''
        return int()
    @property
    def compression(self):
        '''(Integer) Amount of time to determine best compression: 0 = no
        compression with fast file output, 100 = maximum lossless compression
        with slow file output'''
        return int()
    @property
    def use_zbuffer(self):
        '''(Boolean) Save the z-depth per pixel (32 bit unsigned int z-buffer)'''
        return bool()
    @property
    def use_preview(self):
        '''(Boolean) When rendering animations, save JPG preview images in same
        directory'''
        return bool()
    @property
    def exr_codec(self):
        '''(Enum) Codec settings for OpenEXR
        
        [NONE, PXR24, ZIP, PIZ, RLE, ZIPS, B44, B44A, DWAA, DWAB]'''
        return str()
    @property
    def use_jpeg2k_ycc(self):
        '''(Boolean) Save luminance-chrominance-chrominance channels instead of
        RGB colors'''
        return bool()
    @property
    def use_jpeg2k_cinema_preset(self):
        '''(Boolean) Use Openjpeg Cinema Preset'''
        return bool()
    @property
    def use_jpeg2k_cinema_48(self):
        '''(Boolean) Use Openjpeg Cinema Preset (48fps)'''
        return bool()
    @property
    def jpeg2k_codec(self):
        '''(Enum) Codec settings for Jpek2000
        
        [JP2, J2K]'''
        return str()
    @property
    def use_cineon_log(self):
        '''(Boolean) Convert to logarithmic color space'''
        return bool()
    @property
    def cineon_black(self):
        '''(Integer) Log conversion reference blackpoint'''
        return int()
    @property
    def cineon_white(self):
        '''(Integer) Log conversion reference whitepoint'''
        return int()
    @property
    def cineon_gamma(self):
        '''(Float) Log conversion gamma'''
        return float()
    @property
    def views_format(self):
        '''(Enum) Format of multiview media
        
        [INDIVIDUAL, STEREO_3D]'''
        return str()
    @property
    def stereo_3d_format(self):
        '''(Stereo3dFormat) Settings for stereo 3d'''
        return Stereo3dFormat()
    @property
    def view_settings(self):
        '''(ColorManagedViewSettings) Color management settings applied on image
        before saving'''
        return ColorManagedViewSettings()
    @property
    def display_settings(self):
        '''(ColorManagedDisplaySettings) Settings of device saved image would be
        displayed on'''
        return ColorManagedDisplaySettings()