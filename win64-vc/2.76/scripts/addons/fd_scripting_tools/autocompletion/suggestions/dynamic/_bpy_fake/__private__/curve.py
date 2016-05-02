from . curvesplines import CurveSplines
from . key import Key
from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . library import Library
from . animdata import AnimData
from . idmaterials import IDMaterials
from . cyclesmeshsettings import CyclesMeshSettings
from . object import Object
from . bpy_struct import bpy_struct
import mathutils

class Curve(bpy_struct):
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
    def shape_keys(self):
        '''(Key)'''
        return Key()
    @property
    def splines(self):
        '''(Sequence of Spline) Collection of splines in this curve data object'''
        return CurveSplines()
    @property
    def show_handles(self):
        '''(Boolean) Display Bezier handles in editmode'''
        return bool()
    @property
    def show_normal_face(self):
        '''(Boolean) Display 3D curve normals in editmode'''
        return bool()
    @property
    def path_duration(self):
        '''(Integer) The number of frames that are needed to traverse the path,
        defining the maximum value for the 'Evaluation Time' setting'''
        return int()
    @property
    def use_path(self):
        '''(Boolean) Enable the curve to become a translation path'''
        return bool()
    @property
    def use_path_follow(self):
        '''(Boolean) Make curve path children to rotate along the path'''
        return bool()
    @property
    def use_stretch(self):
        '''(Boolean) Option for curve-deform: make deformed child to stretch
        along entire path'''
        return bool()
    @property
    def use_deform_bounds(self):
        '''(Boolean) Option for curve-deform: Use the mesh bounds to clamp the
        deformation'''
        return bool()
    @property
    def use_radius(self):
        '''(Boolean) Option for paths and curve-deform: apply the curve radius
        with path following it and deforming'''
        return bool()
    @property
    def bevel_resolution(self):
        '''(Integer) Bevel resolution when depth is non-zero and no specific
        bevel object has been defined'''
        return int()
    @property
    def offset(self):
        '''(Float) Offset the curve to adjust the width of a text'''
        return float()
    @property
    def extrude(self):
        '''(Float) Amount of curve extrusion when not using a bevel object'''
        return float()
    @property
    def bevel_depth(self):
        '''(Float) Bevel depth when not using a bevel object'''
        return float()
    @property
    def resolution_u(self):
        '''(Integer) Surface resolution in U direction'''
        return int()
    @property
    def resolution_v(self):
        '''(Integer) Surface resolution in V direction'''
        return int()
    @property
    def render_resolution_u(self):
        '''(Integer) Surface resolution in U direction used while rendering (zero
        uses preview resolution)'''
        return int()
    @property
    def render_resolution_v(self):
        '''(Integer) Surface resolution in V direction used while rendering (zero
        uses preview resolution)'''
        return int()
    @property
    def eval_time(self):
        '''(Float) Parametric position along the length of the curve that Objects
        'following' it should be at (position is evaluated by dividing by the
        'Path Length' value)'''
        return float()
    @property
    def bevel_object(self):
        '''(Object) Curve object name that defines the bevel shape'''
        return Object()
    @property
    def taper_object(self):
        '''(Object) Curve object name that defines the taper (width)'''
        return Object()
    @property
    def dimensions(self):
        '''(Enum) Select 2D or 3D curve type
        
        [2D, 3D]'''
        return str()
    @property
    def fill_mode(self):
        '''(Enum) Mode of filling curve
        
        [FULL, BACK, FRONT, HALF]'''
        return str()
    @property
    def twist_mode(self):
        '''(Enum) The type of tilt calculation for 3D Curves
        
        [Z_UP, MINIMUM, TANGENT]'''
        return str()
    @property
    def bevel_factor_mapping_start(self):
        '''(Enum) Determines how the start bevel factor is mapped to a spline
        
        [RESOLUTION, SEGMENTS, SPLINE]'''
        return str()
    @property
    def bevel_factor_mapping_end(self):
        '''(Enum) Determines how the end bevel factor is mapped to a spline
        
        [RESOLUTION, SEGMENTS, SPLINE]'''
        return str()
    @property
    def twist_smooth(self):
        '''(Float) Smoothing iteration for tangents'''
        return float()
    @property
    def use_fill_deform(self):
        '''(Boolean) Fill curve after applying shape keys and all modifiers'''
        return bool()
    @property
    def use_fill_caps(self):
        '''(Boolean) Fill caps for beveled curves'''
        return bool()
    @property
    def use_map_taper(self):
        '''(Boolean) Map effect of taper object on actually beveled curve'''
        return bool()
    @property
    def use_auto_texspace(self):
        '''(Boolean) Adjust active object's texture space automatically when
        transforming object'''
        return bool()
    @property
    def texspace_location(self):
        '''(Vector 3D) Texture space location'''
        return mathutils.Vector()
    @property
    def texspace_size(self):
        '''(Vector 3D) Texture space size'''
        return mathutils.Vector()
    @property
    def use_uv_as_generated(self):
        '''(Boolean) Uses the UV values as Generated textured coordinates'''
        return bool()
    @property
    def materials(self):
        '''(Sequence of Material)'''
        return IDMaterials()
    @property
    def bevel_factor_start(self):
        '''(Float) Factor that defines from where beveling of spline happens
        (0=from the very beginning, 1=from the very end)'''
        return float()
    @property
    def bevel_factor_end(self):
        '''(Float) Factor that defines to where beveling of spline happens (0=to
        the very beginning, 1=to the very end)'''
        return float()
    @property
    def is_editmode(self):
        '''(Boolean) True when used in editmode'''
        return bool()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def cycles(self):
        '''(CyclesMeshSettings) Cycles mesh settings'''
        return CyclesMeshSettings()
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
    def transform(self, matrix, shape_keys):
        '''Transform curve by a matrix
        
        Parameter:
          matrix: (Matrix) Matrix
          shape_keys: (Boolean) Transform Shape Keys'''
        return 
    def validate_material_indices(self):
        '''Validate material indices of splines or letters, return True when the
        curve has had invalid indices corrected (to default 0)
        
        Returns:
          result: (Boolean)'''
        return bool()