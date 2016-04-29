from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieClipProxy(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def build_25(self):
        '''(Boolean) Build proxy resolution 25% of the original footage dimension'''
        return bool()
    @property
    def build_50(self):
        '''(Boolean) Build proxy resolution 50% of the original footage dimension'''
        return bool()
    @property
    def build_75(self):
        '''(Boolean) Build proxy resolution 75% of the original footage dimension'''
        return bool()
    @property
    def build_100(self):
        '''(Boolean) Build proxy resolution 100% of the original footage
        dimension'''
        return bool()
    @property
    def build_undistorted_25(self):
        '''(Boolean) Build proxy resolution 25% of the original undistorted
        footage dimension'''
        return bool()
    @property
    def build_undistorted_50(self):
        '''(Boolean) Build proxy resolution 50% of the original undistorted
        footage dimension'''
        return bool()
    @property
    def build_undistorted_75(self):
        '''(Boolean) Build proxy resolution 75% of the original undistorted
        footage dimension'''
        return bool()
    @property
    def build_undistorted_100(self):
        '''(Boolean) Build proxy resolution 100% of the original undistorted
        footage dimension'''
        return bool()
    @property
    def build_record_run(self):
        '''(Boolean) Build record run time code index'''
        return bool()
    @property
    def build_free_run(self):
        '''(Boolean) Build free run time code index'''
        return bool()
    @property
    def build_free_run_rec_date(self):
        '''(Boolean) Build free run time code index using Record Date/Time'''
        return bool()
    @property
    def quality(self):
        '''(Integer) JPEG quality of proxy images'''
        return int()
    @property
    def timecode(self):
        '''(Enum)
        
        [NONE, RECORD_RUN, FREE_RUN, FREE_RUN_REC_DATE, FREE_RUN_NO_GAPS]'''
        return str()
    @property
    def directory(self):
        '''(String) Location to store the proxy files'''
        return str()