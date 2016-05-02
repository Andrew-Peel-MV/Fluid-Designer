from . nodetree import NodeTree
from . texture import Texture
from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . worldlighting import WorldLighting
from . worldtextureslots import WorldTextureSlots
from . worldmistsettings import WorldMistSettings
from . library import Library
from . animdata import AnimData
from . cyclesworldsettings import CyclesWorldSettings
from . cyclesvisibilitysettings import CyclesVisibilitySettings
from . bpy_struct import bpy_struct
import mathutils

class World(bpy_struct):
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
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def texture_slots(self):
        '''(Sequence of WorldTextureSlot) Texture slots defining the mapping and
        influence of textures'''
        return WorldTextureSlots()
    @property
    def active_texture(self):
        '''(Texture) Active texture slot being displayed'''
        return Texture()
    @property
    def active_texture_index(self):
        '''(Integer) Index of active texture slot'''
        return int()
    @property
    def horizon_color(self):
        '''(Vector 3D) Color at the horizon'''
        return mathutils.Vector()
    @property
    def zenith_color(self):
        '''(Vector 3D) Color at the zenith'''
        return mathutils.Vector()
    @property
    def ambient_color(self):
        '''(Vector 3D) Ambient color of the world'''
        return mathutils.Vector()
    @property
    def exposure(self):
        '''(Float) Amount of exponential color correction for light'''
        return float()
    @property
    def color_range(self):
        '''(Float) The color range that will be mapped to 0-1'''
        return float()
    @property
    def use_sky_blend(self):
        '''(Boolean) Render background with natural progression from horizon to
        zenith'''
        return bool()
    @property
    def use_sky_paper(self):
        '''(Boolean) Flatten blend or texture coordinates'''
        return bool()
    @property
    def use_sky_real(self):
        '''(Boolean) Render background with a real horizon, relative to the
        camera angle'''
        return bool()
    @property
    def light_settings(self):
        '''(WorldLighting) World lighting settings'''
        return WorldLighting()
    @property
    def mist_settings(self):
        '''(WorldMistSettings) World mist settings'''
        return WorldMistSettings()
    @property
    def node_tree(self):
        '''(NodeTree) Node tree for node based worlds'''
        return NodeTree()
    @property
    def use_nodes(self):
        '''(Boolean) Use shader nodes to render the world'''
        return bool()
    @property
    def cycles(self):
        '''(CyclesWorldSettings) Cycles world settings'''
        return CyclesWorldSettings()
    @property
    def cycles_visibility(self):
        '''(CyclesVisibilitySettings) Cycles visibility settings'''
        return CyclesVisibilitySettings()
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