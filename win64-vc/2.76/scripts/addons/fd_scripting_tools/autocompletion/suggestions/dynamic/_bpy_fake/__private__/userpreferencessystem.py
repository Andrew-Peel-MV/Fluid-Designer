from . struct import Struct
from . colorramp import ColorRamp
from . usersolidlight import UserSolidLight
from . bpy_struct import bpy_struct
import mathutils

class UserPreferencesSystem(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use_international_fonts(self):
        '''(Boolean) Use international fonts'''
        return bool()
    @property
    def dpi(self):
        '''(Integer) Font size and resolution for display'''
        return int()
    @property
    def virtual_pixel_mode(self):
        '''(Enum) Modify the pixel size for hi-res devices
        
        [NATIVE, DOUBLE]'''
        return str()
    @property
    def pixel_size(self):
        '''(Float)'''
        return float()
    @property
    def font_path_ui(self):
        '''(String) Path to interface font'''
        return str()
    @property
    def scrollback(self):
        '''(Integer) Maximum number of lines to store for the console buffer'''
        return int()
    @property
    def author(self):
        '''(String) Name that will be used in exported files when format supports
        such feature'''
        return str()
    @property
    def language(self):
        '''(Enum) Language used for translation
        
        [DEFAULT]'''
        return str()
    @property
    def use_translate_tooltips(self):
        '''(Boolean) Translate tooltips'''
        return bool()
    @property
    def use_translate_interface(self):
        '''(Boolean) Translate interface'''
        return bool()
    @property
    def use_translate_new_dataname(self):
        '''(Boolean) Translate new data names (when adding/creating some)'''
        return bool()
    @property
    def use_textured_fonts(self):
        '''(Boolean) Use textures for drawing international fonts'''
        return bool()
    @property
    def solid_lights(self):
        '''(Sequence of UserSolidLight) Lights user to display objects in solid
        draw mode'''
        return (UserSolidLight(),)
    @property
    def use_weight_color_range(self):
        '''(Boolean) Enable color range used for weight visualization in weight
        painting mode'''
        return bool()
    @property
    def weight_color_range(self):
        '''(ColorRamp) Color range used for weight visualization in weight
        painting mode'''
        return ColorRamp()
    @property
    def color_picker_type(self):
        '''(Enum) Different styles of displaying the color picker widget
        
        [CIRCLE_HSV, CIRCLE_HSL, SQUARE_SV, SQUARE_HS, SQUARE_HV]'''
        return str()
    @property
    def use_preview_images(self):
        '''(Boolean) Allow user to choose any codec (Windows only, might generate
        instability)'''
        return bool()
    @property
    def use_scripts_auto_execute(self):
        '''(Boolean) Allow any .blend file to run scripts automatically (unsafe
        with blend files from an untrusted source)'''
        return bool()
    @property
    def use_tabs_as_spaces(self):
        '''(Boolean) Automatically convert all new tabs into spaces for new and
        loaded text files'''
        return bool()
    @property
    def prefetch_frames(self):
        '''(Integer) Number of frames to render ahead during playback (sequencer
        only)'''
        return int()
    @property
    def memory_cache_limit(self):
        '''(Integer) Memory cache limit (in megabytes)'''
        return int()
    @property
    def frame_server_port(self):
        '''(Integer) Frameserver Port for Frameserver Rendering'''
        return int()
    @property
    def gl_clip_alpha(self):
        '''(Float) Clip alpha below this threshold in the 3D textured view'''
        return float()
    @property
    def use_mipmaps(self):
        '''(Boolean) Scale textures for the 3D View (looks nicer but uses more
        memory and slows image reloading)'''
        return bool()
    @property
    def use_16bit_textures(self):
        '''(Boolean) Use 16 bit per component texture for float images'''
        return bool()
    @property
    def use_gpu_mipmap(self):
        '''(Boolean) Generate Image Mipmaps on the GPU'''
        return bool()
    @property
    def image_draw_method(self):
        '''(Enum) Method used for displaying images on the screen
        
        [2DTEXTURE, GLSL, DRAWPIXELS]'''
        return str()
    @property
    def use_vertex_buffer_objects(self):
        '''(Boolean) Use Vertex Buffer Objects (or Vertex Arrays, if unsupported)
        for viewport rendering'''
        return bool()
    @property
    def anisotropic_filter(self):
        '''(Enum) Quality of the anisotropic filtering (values greater than 1.0
        enable anisotropic filtering)
        
        [FILTER_0, FILTER_2, FILTER_4, FILTER_8, FILTER_16]'''
        return str()
    @property
    def gl_texture_limit(self):
        '''(Enum) Limit the texture size to save graphics memory
        
        [CLAMP_OFF, CLAMP_8192, CLAMP_4096, CLAMP_2048, CLAMP_1024, CLAMP_512,
        CLAMP_256, CLAMP_128]'''
        return str()
    @property
    def texture_time_out(self):
        '''(Integer) Time since last access of a GL texture in seconds after
        which it is freed (set to 0 to keep textures allocated)'''
        return int()
    @property
    def texture_collection_rate(self):
        '''(Integer) Number of seconds between each run of the GL texture garbage
        collector'''
        return int()
    @property
    def window_draw_method(self):
        '''(Enum) Drawing method used by the window manager
        
        [AUTOMATIC, TRIPLE_BUFFER, OVERLAP, OVERLAP_FLIP, FULL]'''
        return str()
    @property
    def audio_mixing_buffer(self):
        '''(Enum) Number of samples used by the audio mixing buffer
        
        [SAMPLES_256, SAMPLES_512, SAMPLES_1024, SAMPLES_2048, SAMPLES_4096,
        SAMPLES_8192, SAMPLES_16384, SAMPLES_32768]'''
        return str()
    @property
    def audio_device(self):
        '''(Enum) Audio output device
        
        [NONE, SDL, OPENAL]'''
        return str()
    @property
    def audio_sample_rate(self):
        '''(Enum) Audio sample rate
        
        [RATE_44100, RATE_48000, RATE_96000, RATE_192000]'''
        return str()
    @property
    def audio_sample_format(self):
        '''(Enum) Audio sample format
        
        [U8, S16, S24, S32, FLOAT, DOUBLE]'''
        return str()
    @property
    def audio_channels(self):
        '''(Enum) Audio channel count
        
        [MONO, STEREO, SURROUND4, SURROUND51, SURROUND71]'''
        return str()
    @property
    def screencast_fps(self):
        '''(Integer) Frame rate for the screencast to be played back'''
        return int()
    @property
    def screencast_wait_time(self):
        '''(Integer) Time in milliseconds between each frame recorded for
        screencast'''
        return int()
    @property
    def use_text_antialiasing(self):
        '''(Boolean) Draw user interface text anti-aliased'''
        return bool()
    @property
    def select_method(self):
        '''(Enum) Use OpenGL occlusion queries or selection render mode to
        accelerate selection
        
        [AUTO, GL_SELECT, GL_QUERY]'''
        return str()
    @property
    def multi_sample(self):
        '''(Enum) Enable OpenGL multi-sampling, only for systems that support it,
        requires restart
        
        [NONE, 2, 4, 8, 16]'''
        return str()
    @property
    def use_region_overlap(self):
        '''(Boolean) Draw tool/property regions over the main region, when using
        Triple Buffer'''
        return bool()
    @property
    def compute_device_type(self):
        '''(Enum) Device to use for computation (rendering with Cycles)
        
        [NONE, CUDA]'''
        return str()
    @property
    def compute_device(self):
        '''(Enum) Device to use for computation
        
        [CUDA_0]'''
        return str()
    @property
    def opensubdiv_compute_type(self):
        '''(Enum) Type of computer back-end used with OpenSubdiv
        
        [NONE, CPU, OPENMP, GLSL_TRANSFORM_FEEDBACL, GLSL_COMPUTE]'''
        return str()
    def is_occlusion_query_supported(self):
        '''is_occlusion_query_supported
        
        Returns:
          is_supported: (Boolean) Check if GPU supports Occlusion Queries'''
        return bool()