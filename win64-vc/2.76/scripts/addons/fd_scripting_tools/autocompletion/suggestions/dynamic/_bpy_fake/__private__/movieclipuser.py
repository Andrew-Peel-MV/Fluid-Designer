from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieClipUser(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def frame_current(self):
        '''(Integer) Current frame number in movie or image sequence'''
        return int()
    @property
    def proxy_render_size(self):
        '''(Enum) Draw preview using full resolution or different proxy
        resolutions
        
        [PROXY_25, PROXY_50, PROXY_75, PROXY_100, FULL]'''
        return str()
    @property
    def use_render_undistorted(self):
        '''(Boolean) Render preview using undistorted proxy'''
        return bool()