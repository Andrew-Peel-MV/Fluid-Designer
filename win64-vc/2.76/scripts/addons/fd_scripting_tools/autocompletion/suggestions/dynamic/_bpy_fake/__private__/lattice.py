from . key import Key
from . latticepoint import LatticePoint
from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . library import Library
from . animdata import AnimData
from . bpy_struct import bpy_struct
import mathutils

class Lattice(bpy_struct):
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
    def points_u(self):
        '''(Integer) Point in U direction (can't be changed when there are shape
        keys)'''
        return int()
    @property
    def points_v(self):
        '''(Integer) Point in V direction (can't be changed when there are shape
        keys)'''
        return int()
    @property
    def points_w(self):
        '''(Integer) Point in W direction (can't be changed when there are shape
        keys)'''
        return int()
    @property
    def interpolation_type_u(self):
        '''(Enum)
        
        [KEY_LINEAR, KEY_CARDINAL, KEY_CATMULL_ROM, KEY_BSPLINE]'''
        return str()
    @property
    def interpolation_type_v(self):
        '''(Enum)
        
        [KEY_LINEAR, KEY_CARDINAL, KEY_CATMULL_ROM, KEY_BSPLINE]'''
        return str()
    @property
    def interpolation_type_w(self):
        '''(Enum)
        
        [KEY_LINEAR, KEY_CARDINAL, KEY_CATMULL_ROM, KEY_BSPLINE]'''
        return str()
    @property
    def use_outside(self):
        '''(Boolean) Only draw, and take into account, the outer vertices'''
        return bool()
    @property
    def vertex_group(self):
        '''(String) Vertex group to apply the influence of the lattice'''
        return str()
    @property
    def shape_keys(self):
        '''(Key)'''
        return Key()
    @property
    def points(self):
        '''(Sequence of LatticePoint) Points of the lattice'''
        return (LatticePoint(),)
    @property
    def is_editmode(self):
        '''(Boolean) True when used in editmode'''
        return bool()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
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
        '''Transform lattice by a matrix
        
        Parameter:
          matrix: (Matrix) Matrix
          shape_keys: (Boolean) Transform Shape Keys'''
        return 