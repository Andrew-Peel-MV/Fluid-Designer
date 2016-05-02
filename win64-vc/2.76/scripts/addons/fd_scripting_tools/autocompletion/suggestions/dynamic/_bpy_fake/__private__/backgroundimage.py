from . movieclipuser import MovieClipUser
from . imageuser import ImageUser
from . struct import Struct
from . movieclip import MovieClip
from . image import Image
from . bpy_struct import bpy_struct
import mathutils

class BackgroundImage(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def source(self):
        '''(Enum) Data source used for background
        
        [IMAGE, MOVIE_CLIP]'''
        return str()
    @property
    def image(self):
        '''(Image) Image displayed and edited in this space'''
        return Image()
    @property
    def clip(self):
        '''(MovieClip) Movie clip displayed and edited in this space'''
        return MovieClip()
    @property
    def image_user(self):
        '''(ImageUser) Parameters defining which layer, pass and frame of the
        image is displayed'''
        return ImageUser()
    @property
    def clip_user(self):
        '''(MovieClipUser) Parameters defining which frame of the movie clip is
        displayed'''
        return MovieClipUser()
    @property
    def offset_x(self):
        '''(Float) Offset image horizontally from the world origin'''
        return float()
    @property
    def offset_y(self):
        '''(Float) Offset image vertically from the world origin'''
        return float()
    @property
    def size(self):
        '''(Float) Size of the background image (ortho view only)'''
        return float()
    @property
    def rotation(self):
        '''(Float) Rotation for the background image (ortho view only)'''
        return float()
    @property
    def use_flip_x(self):
        '''(Boolean) Flip the background image horizontally'''
        return bool()
    @property
    def use_flip_y(self):
        '''(Boolean) Flip the background image vertically'''
        return bool()
    @property
    def opacity(self):
        '''(Float) Image opacity to blend the image against the background color'''
        return float()
    @property
    def view_axis(self):
        '''(Enum) The axis to display the image on
        
        [LEFT, RIGHT, BACK, FRONT, BOTTOM, TOP, ALL, CAMERA]'''
        return str()
    @property
    def show_expanded(self):
        '''(Boolean) Show the expanded in the user interface'''
        return bool()
    @property
    def use_camera_clip(self):
        '''(Boolean) Use movie clip from active scene camera'''
        return bool()
    @property
    def show_background_image(self):
        '''(Boolean) Show this image as background'''
        return bool()
    @property
    def show_on_foreground(self):
        '''(Boolean) Show this image in front of objects in viewport'''
        return bool()
    @property
    def draw_depth(self):
        '''(Enum) Draw under or over everything
        
        [BACK, FRONT]'''
        return str()
    @property
    def frame_method(self):
        '''(Enum) How the image fits in the camera frame
        
        [STRETCH, FIT, CROP]'''
        return str()