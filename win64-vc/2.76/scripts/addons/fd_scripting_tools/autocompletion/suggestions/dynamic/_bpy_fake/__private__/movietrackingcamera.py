from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MovieTrackingCamera(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def distortion_model(self):
        '''(Enum) Distortion model used for camera lenses
        
        [POLYNOMIAL, DIVISION]'''
        return str()
    @property
    def sensor_width(self):
        '''(Float) Width of CCD sensor in millimeters'''
        return float()
    @property
    def focal_length(self):
        '''(Float) Camera's focal length'''
        return float()
    @property
    def focal_length_pixels(self):
        '''(Float) Camera's focal length'''
        return float()
    @property
    def units(self):
        '''(Enum) Units used for camera focal length
        
        [PIXELS, MILLIMETERS]'''
        return str()
    @property
    def principal(self):
        '''(Vector 2D) Optical center of lens'''
        return mathutils.Vector()
    @property
    def k1(self):
        '''(Float) First coefficient of third order polynomial radial distortion'''
        return float()
    @property
    def k2(self):
        '''(Float) Second coefficient of third order polynomial radial distortion'''
        return float()
    @property
    def k3(self):
        '''(Float) Third coefficient of third order polynomial radial distortion'''
        return float()
    @property
    def division_k1(self):
        '''(Float) First coefficient of second order division distortion'''
        return float()
    @property
    def division_k2(self):
        '''(Float) First coefficient of second order division distortion'''
        return float()
    @property
    def pixel_aspect(self):
        '''(Float) Pixel aspect ratio'''
        return float()