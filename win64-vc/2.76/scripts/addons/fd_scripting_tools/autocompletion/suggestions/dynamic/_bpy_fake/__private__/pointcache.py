from . pointcaches import PointCaches
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class PointCache(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def frame_start(self):
        '''(Integer) Frame on which the simulation starts'''
        return int()
    @property
    def frame_end(self):
        '''(Integer) Frame on which the simulation stops'''
        return int()
    @property
    def frame_step(self):
        '''(Integer) Number of frames between cached frames'''
        return int()
    @property
    def index(self):
        '''(Integer) Index number of cache files'''
        return int()
    @property
    def compression(self):
        '''(Enum) Compression method to be used
        
        [NO, LIGHT, HEAVY]'''
        return str()
    @property
    def is_baked(self):
        '''(Boolean)'''
        return bool()
    @property
    def is_baking(self):
        '''(Boolean)'''
        return bool()
    @property
    def use_disk_cache(self):
        '''(Boolean) Save cache files to disk (.blend file must be saved first)'''
        return bool()
    @property
    def is_outdated(self):
        '''(Boolean)'''
        return bool()
    @property
    def is_frame_skip(self):
        '''(Boolean)'''
        return bool()
    @property
    def name(self):
        '''(String) Cache name'''
        return str()
    @property
    def filepath(self):
        '''(String) Cache file path'''
        return str()
    @property
    def info(self):
        '''(String) Info on current cache status'''
        return str()
    @property
    def use_external(self):
        '''(Boolean) Read cache from an external location'''
        return bool()
    @property
    def use_library_path(self):
        '''(Boolean) Use this file's path for the disk cache when library linked
        into another file (for local bakes per scene file, disable this
        option)'''
        return bool()
    @property
    def point_caches(self):
        '''(Sequence of PointCache) Point cache list'''
        return PointCaches()