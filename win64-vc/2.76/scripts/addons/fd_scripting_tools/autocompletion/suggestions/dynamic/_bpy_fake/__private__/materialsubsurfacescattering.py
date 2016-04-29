from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaterialSubsurfaceScattering(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def radius(self):
        '''(Vector 3D) Mean red/green/blue scattering path length'''
        return mathutils.Vector()
    @property
    def color(self):
        '''(Vector 3D) Scattering color'''
        return mathutils.Vector()
    @property
    def error_threshold(self):
        '''(Float) Error tolerance (low values are slower and higher quality)'''
        return float()
    @property
    def scale(self):
        '''(Float) Object scale factor'''
        return float()
    @property
    def ior(self):
        '''(Float) Index of refraction (higher values are denser)'''
        return float()
    @property
    def color_factor(self):
        '''(Float) Blend factor for SSS colors'''
        return float()
    @property
    def texture_factor(self):
        '''(Float) Texture scattering blend factor'''
        return float()
    @property
    def front(self):
        '''(Float) Front scattering weight'''
        return float()
    @property
    def back(self):
        '''(Float) Back scattering weight'''
        return float()
    @property
    def use(self):
        '''(Boolean) Enable diffuse subsurface scattering effects in a material'''
        return bool()