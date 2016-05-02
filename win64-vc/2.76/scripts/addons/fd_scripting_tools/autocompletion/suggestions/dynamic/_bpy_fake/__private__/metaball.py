from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . metaballelements import MetaBallElements
from . library import Library
from . animdata import AnimData
from . idmaterials import IDMaterials
from . cyclesmeshsettings import CyclesMeshSettings
from . bpy_struct import bpy_struct
import mathutils

class MetaBall(bpy_struct):
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
    def elements(self):
        '''(Sequence of MetaElement) Meta elements'''
        return MetaBallElements()
    @property
    def update_method(self):
        '''(Enum) Metaball edit update behavior
        
        [UPDATE_ALWAYS, HALFRES, FAST, NEVER]'''
        return str()
    @property
    def resolution(self):
        '''(Float) Polygonization resolution in the 3D viewport'''
        return float()
    @property
    def render_resolution(self):
        '''(Float) Polygonization resolution in rendering'''
        return float()
    @property
    def threshold(self):
        '''(Float) Influence of meta elements'''
        return float()
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
    def materials(self):
        '''(Sequence of Material)'''
        return IDMaterials()
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
    def transform(self, matrix):
        '''Transform meta elements by a matrix
        
        Parameter:
          matrix: (Matrix) Matrix'''
        return 