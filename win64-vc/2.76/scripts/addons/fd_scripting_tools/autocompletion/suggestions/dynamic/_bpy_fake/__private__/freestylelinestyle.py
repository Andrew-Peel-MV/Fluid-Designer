from . linestylealphamodifiers import LineStyleAlphaModifiers
from . nodetree import NodeTree
from . texture import Texture
from . imagepreview import ImagePreview
from . linestyletextureslots import LineStyleTextureSlots
from . id import ID
from . struct import Struct
from . linestylecolormodifiers import LineStyleColorModifiers
from . linestylethicknessmodifiers import LineStyleThicknessModifiers
from . linestylegeometrymodifiers import LineStyleGeometryModifiers
from . library import Library
from . animdata import AnimData
from . bpy_struct import bpy_struct
import mathutils

class FreestyleLineStyle(bpy_struct):
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
    def texture_slots(self):
        '''(Sequence of LineStyleTextureSlot) Texture slots defining the mapping
        and influence of textures'''
        return LineStyleTextureSlots()
    @property
    def active_texture(self):
        '''(Texture) Active texture slot being displayed'''
        return Texture()
    @property
    def active_texture_index(self):
        '''(Integer) Index of active texture slot'''
        return int()
    @property
    def panel(self):
        '''(Enum) Select the property panel to be shown
        
        [STROKES, COLOR, ALPHA, THICKNESS, GEOMETRY, TEXTURE]'''
        return str()
    @property
    def color(self):
        '''(Vector 3D) Base line color, possibly modified by line color modifiers'''
        return mathutils.Vector()
    @property
    def alpha(self):
        '''(Float) Base alpha transparency, possibly modified by alpha
        transparency modifiers'''
        return float()
    @property
    def thickness(self):
        '''(Float) Base line thickness, possibly modified by line thickness
        modifiers'''
        return float()
    @property
    def thickness_position(self):
        '''(Enum) Thickness position of silhouettes and border edges (applicable
        when plain chaining is used with the Same Object option)
        
        [CENTER, INSIDE, OUTSIDE, RELATIVE]'''
        return str()
    @property
    def thickness_ratio(self):
        '''(Float) A number between 0 (inside) and 1 (outside) specifying the
        relative position of stroke thickness'''
        return float()
    @property
    def color_modifiers(self):
        '''(Sequence of LineStyleColorModifier) List of line color modifiers'''
        return LineStyleColorModifiers()
    @property
    def alpha_modifiers(self):
        '''(Sequence of LineStyleAlphaModifier) List of alpha transparency
        modifiers'''
        return LineStyleAlphaModifiers()
    @property
    def thickness_modifiers(self):
        '''(Sequence of LineStyleThicknessModifier) List of line thickness
        modifiers'''
        return LineStyleThicknessModifiers()
    @property
    def geometry_modifiers(self):
        '''(Sequence of LineStyleGeometryModifier) List of stroke geometry
        modifiers'''
        return LineStyleGeometryModifiers()
    @property
    def use_chaining(self):
        '''(Boolean) Enable chaining of feature edges'''
        return bool()
    @property
    def chaining(self):
        '''(Enum) Select the way how feature edges are jointed to form chains
        
        [PLAIN, SKETCHY]'''
        return str()
    @property
    def rounds(self):
        '''(Integer) Number of rounds in a sketchy multiple touch'''
        return int()
    @property
    def use_same_object(self):
        '''(Boolean) If true, only feature edges of the same object are joined'''
        return bool()
    @property
    def use_split_length(self):
        '''(Boolean) Enable chain splitting by curvilinear 2D length'''
        return bool()
    @property
    def split_length(self):
        '''(Float) Curvilinear 2D length for chain splitting'''
        return float()
    @property
    def use_angle_min(self):
        '''(Boolean) Split chains at points with angles smaller than the minimum
        2D angle'''
        return bool()
    @property
    def angle_min(self):
        '''(Float) Minimum 2D angle for splitting chains'''
        return float()
    @property
    def use_angle_max(self):
        '''(Boolean) Split chains at points with angles larger than the maximum
        2D angle'''
        return bool()
    @property
    def angle_max(self):
        '''(Float) Maximum 2D angle for splitting chains'''
        return float()
    @property
    def use_length_min(self):
        '''(Boolean) Enable the selection of chains by a minimum 2D length'''
        return bool()
    @property
    def length_min(self):
        '''(Float) Minimum curvilinear 2D length for the selection of chains'''
        return float()
    @property
    def use_length_max(self):
        '''(Boolean) Enable the selection of chains by a maximum 2D length'''
        return bool()
    @property
    def length_max(self):
        '''(Float) Maximum curvilinear 2D length for the selection of chains'''
        return float()
    @property
    def use_chain_count(self):
        '''(Boolean) Enable the selection of first N chains'''
        return bool()
    @property
    def chain_count(self):
        '''(Integer) Chain count for the selection of first N chains'''
        return int()
    @property
    def use_split_pattern(self):
        '''(Boolean) Enable chain splitting by dashed line patterns'''
        return bool()
    @property
    def split_dash1(self):
        '''(Integer) Length of the 1st dash for splitting'''
        return int()
    @property
    def split_gap1(self):
        '''(Integer) Length of the 1st gap for splitting'''
        return int()
    @property
    def split_dash2(self):
        '''(Integer) Length of the 2nd dash for splitting'''
        return int()
    @property
    def split_gap2(self):
        '''(Integer) Length of the 2nd gap for splitting'''
        return int()
    @property
    def split_dash3(self):
        '''(Integer) Length of the 3rd dash for splitting'''
        return int()
    @property
    def split_gap3(self):
        '''(Integer) Length of the 3rd gap for splitting'''
        return int()
    @property
    def material_boundary(self):
        '''(Boolean) If true, chains of feature edges are split at material
        boundaries'''
        return bool()
    @property
    def use_sorting(self):
        '''(Boolean) Arrange the stacking order of strokes'''
        return bool()
    @property
    def sort_key(self):
        '''(Enum) Select the sort key to determine the stacking order of chains
        
        [DISTANCE_FROM_CAMERA, 2D_LENGTH, PROJECTED_X, PROJECTED_Y]'''
        return str()
    @property
    def sort_order(self):
        '''(Enum) Select the sort order
        
        [DEFAULT, REVERSE]'''
        return str()
    @property
    def integration_type(self):
        '''(Enum) Select the way how the sort key is computed for each chain
        
        [MEAN, MIN, MAX, FIRST, LAST]'''
        return str()
    @property
    def use_dashed_line(self):
        '''(Boolean) Enable or disable dashed line'''
        return bool()
    @property
    def caps(self):
        '''(Enum) Select the shape of both ends of strokes
        
        [BUTT, ROUND, SQUARE]'''
        return str()
    @property
    def dash1(self):
        '''(Integer) Length of the 1st dash for dashed lines'''
        return int()
    @property
    def gap1(self):
        '''(Integer) Length of the 1st gap for dashed lines'''
        return int()
    @property
    def dash2(self):
        '''(Integer) Length of the 2nd dash for dashed lines'''
        return int()
    @property
    def gap2(self):
        '''(Integer) Length of the 2nd gap for dashed lines'''
        return int()
    @property
    def dash3(self):
        '''(Integer) Length of the 3rd dash for dashed lines'''
        return int()
    @property
    def gap3(self):
        '''(Integer) Length of the 3rd gap for dashed lines'''
        return int()
    @property
    def use_texture(self):
        '''(Boolean) Enable or disable textured strokes'''
        return bool()
    @property
    def texture_spacing(self):
        '''(Float) Spacing for textures along stroke length'''
        return float()
    @property
    def node_tree(self):
        '''(NodeTree) Node tree for node-based shaders'''
        return NodeTree()
    @property
    def use_nodes(self):
        '''(Boolean) Use shader nodes for the line style'''
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