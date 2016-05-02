from . cyclescamerasettings import CyclesCameraSettings
from . camerastereodata import CameraStereoData
from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . gpudofsettings import GPUDOFSettings
from . scene import Scene
from . library import Library
from . animdata import AnimData
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class Camera(bpy_struct):
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
    def type(self):
        '''(Enum) Camera types
        
        [PERSP, ORTHO, PANO]'''
        return str()
    @property
    def show_guide(self):
        '''(Enum) Draw overlay
        
        [CENTER, CENTER_DIAGONAL, THIRDS, GOLDEN, GOLDEN_TRIANGLE_A,
        GOLDEN_TRIANGLE_B, HARMONY_TRIANGLE_A, HARMONY_TRIANGLE_B]'''
        return str()
    @property
    def sensor_fit(self):
        '''(Enum) Method to fit image and field of view angle inside the sensor
        
        [AUTO, HORIZONTAL, VERTICAL]'''
        return str()
    @property
    def passepartout_alpha(self):
        '''(Float) Opacity (alpha) of the darkened overlay in Camera view'''
        return float()
    @property
    def angle_x(self):
        '''(Float) Camera lens horizontal field of view'''
        return float()
    @property
    def angle_y(self):
        '''(Float) Camera lens vertical field of view'''
        return float()
    @property
    def angle(self):
        '''(Float) Camera lens field of view'''
        return float()
    @property
    def clip_start(self):
        '''(Float) Camera near clipping distance'''
        return float()
    @property
    def clip_end(self):
        '''(Float) Camera far clipping distance'''
        return float()
    @property
    def lens(self):
        '''(Float) Perspective Camera lens value in millimeters'''
        return float()
    @property
    def sensor_width(self):
        '''(Float) Horizontal size of the image sensor area in millimeters'''
        return float()
    @property
    def sensor_height(self):
        '''(Float) Vertical size of the image sensor area in millimeters'''
        return float()
    @property
    def ortho_scale(self):
        '''(Float) Orthographic Camera scale (similar to zoom)'''
        return float()
    @property
    def draw_size(self):
        '''(Float) Apparent size of the Camera object in the 3D View'''
        return float()
    @property
    def shift_x(self):
        '''(Float) Camera horizontal shift'''
        return float()
    @property
    def shift_y(self):
        '''(Float) Camera vertical shift'''
        return float()
    @property
    def dof_distance(self):
        '''(Float) Distance to the focus point for depth of field'''
        return float()
    @property
    def stereo(self):
        '''(CameraStereoData)'''
        return CameraStereoData()
    @property
    def show_limits(self):
        '''(Boolean) Draw the clipping range and focus point on the camera'''
        return bool()
    @property
    def show_mist(self):
        '''(Boolean) Draw a line from the Camera to indicate the mist area'''
        return bool()
    @property
    def show_passepartout(self):
        '''(Boolean) Show a darkened overlay outside the image area in Camera
        view'''
        return bool()
    @property
    def show_safe_areas(self):
        '''(Boolean) Show TV title safe and action safe areas in Camera view'''
        return bool()
    @property
    def show_safe_center(self):
        '''(Boolean) Show safe areas to fit content in a different aspect ratio'''
        return bool()
    @property
    def show_name(self):
        '''(Boolean) Show the active Camera's name in Camera view'''
        return bool()
    @property
    def show_sensor(self):
        '''(Boolean) Show sensor size (film gate) in Camera view'''
        return bool()
    @property
    def lens_unit(self):
        '''(Enum) Unit to edit lens in for the user interface
        
        [MILLIMETERS, FOV]'''
        return str()
    @property
    def dof_object(self):
        '''(Object) Use this object to define the depth of field focal point'''
        return Object()
    @property
    def gpu_dof(self):
        '''(GPUDOFSettings)'''
        return GPUDOFSettings()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def cycles(self):
        '''(CyclesCameraSettings) Cycles camera settings'''
        return CyclesCameraSettings()
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
    def view_frame(self, scene):
        '''Return 4 points for the cameras frame (before object transformation)
        
        Parameter:
          scene:
            (Scene) Scene to use for aspect calculation, when omitted 1:1 aspect
            is used
        
        Returns:
          result_1: (Vector 3D)
          result_2: (Vector 3D)
          result_3: (Vector 3D)
          result_4: (Vector 3D)'''
        return mathutils.Vector(), mathutils.Vector(), mathutils.Vector(), mathutils.Vector()