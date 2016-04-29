from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MetaElement(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Metaball types
        
        [BALL, CAPSULE, PLANE, ELLIPSOID, CUBE]'''
        return str()
    @property
    def co(self):
        '''(Vector 3D)'''
        return mathutils.Vector()
    @property
    def rotation(self):
        '''(Float[4]) Normalized quaternion rotation'''
        return ''
    @property
    def radius(self):
        '''(Float)'''
        return float()
    @property
    def size_x(self):
        '''(Float) Size of element, use of components depends on element type'''
        return float()
    @property
    def size_y(self):
        '''(Float) Size of element, use of components depends on element type'''
        return float()
    @property
    def size_z(self):
        '''(Float) Size of element, use of components depends on element type'''
        return float()
    @property
    def stiffness(self):
        '''(Float) Stiffness defines how much of the element to fill'''
        return float()
    @property
    def use_negative(self):
        '''(Boolean) Set metaball as negative one'''
        return bool()
    @property
    def hide(self):
        '''(Boolean) Hide element'''
        return bool()