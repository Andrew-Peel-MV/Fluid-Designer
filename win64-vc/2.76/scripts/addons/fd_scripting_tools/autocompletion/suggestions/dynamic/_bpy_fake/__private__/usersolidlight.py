from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class UserSolidLight(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def use(self):
        '''(Boolean) Enable this OpenGL light in solid draw mode'''
        return bool()
    @property
    def direction(self):
        '''(Vector 3D) Direction that the OpenGL light is shining'''
        return mathutils.Vector()
    @property
    def diffuse_color(self):
        '''(Vector 3D) Diffuse color of the OpenGL light'''
        return mathutils.Vector()
    @property
    def specular_color(self):
        '''(Vector 3D) Color of the light's specular highlight'''
        return mathutils.Vector()