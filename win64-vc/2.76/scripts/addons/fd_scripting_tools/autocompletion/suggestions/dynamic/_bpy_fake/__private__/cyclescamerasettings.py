from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class CyclesCameraSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def aperture_type(self):
        '''(Enum) Use f-stop number or aperture radius
        
        [RADIUS, FSTOP]'''
        return str()
    @property
    def aperture_fstop(self):
        '''(Float) F-stop ratio (lower numbers give more defocus, higher numbers
        give a sharper image)'''
        return float()
    @property
    def aperture_size(self):
        '''(Float) Radius of the aperture for depth of field (higher values give
        more defocus)'''
        return float()
    @property
    def aperture_blades(self):
        '''(Integer) Number of blades in aperture for polygonal bokeh (at least
        3)'''
        return int()
    @property
    def aperture_rotation(self):
        '''(Float) Rotation of blades in aperture'''
        return float()
    @property
    def aperture_ratio(self):
        '''(Float) Distortion to simulate anamorphic lens bokeh'''
        return float()
    @property
    def panorama_type(self):
        '''(Enum) Distortion to use for the calculation
        
        [EQUIRECTANGULAR, FISHEYE_EQUIDISTANT, FISHEYE_EQUISOLID, MIRRORBALL]'''
        return str()
    @property
    def fisheye_fov(self):
        '''(Float) Field of view for the fisheye lens'''
        return float()
    @property
    def fisheye_lens(self):
        '''(Float) Lens focal length (mm)'''
        return float()
    @property
    def latitude_min(self):
        '''(Float) Minimum latitude (vertical angle) for the equirectangular lens'''
        return float()
    @property
    def latitude_max(self):
        '''(Float) Maximum latitude (vertical angle) for the equirectangular lens'''
        return float()
    @property
    def longitude_min(self):
        '''(Float) Minimum longitude (horizontal angle) for the equirectangular
        lens'''
        return float()
    @property
    def longitude_max(self):
        '''(Float) Maximum longitude (horizontal angle) for the equirectangular
        lens'''
        return float()