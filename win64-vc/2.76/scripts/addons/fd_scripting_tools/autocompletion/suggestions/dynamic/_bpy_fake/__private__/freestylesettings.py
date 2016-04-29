from . freestylemodules import FreestyleModules
from . linesets import Linesets
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class FreestyleSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def modules(self):
        '''(Sequence of FreestyleModuleSettings) A list of style modules (to be
        applied from top to bottom)'''
        return FreestyleModules()
    @property
    def mode(self):
        '''(Enum) Select the Freestyle control mode
        
        [SCRIPT, EDITOR]'''
        return str()
    @property
    def use_culling(self):
        '''(Boolean) If enabled, out-of-view edges are ignored'''
        return bool()
    @property
    def use_suggestive_contours(self):
        '''(Boolean) Enable suggestive contours'''
        return bool()
    @property
    def use_ridges_and_valleys(self):
        '''(Boolean) Enable ridges and valleys'''
        return bool()
    @property
    def use_material_boundaries(self):
        '''(Boolean) Enable material boundaries'''
        return bool()
    @property
    def use_smoothness(self):
        '''(Boolean) Take face smoothness into account in view map calculation'''
        return bool()
    @property
    def use_advanced_options(self):
        '''(Boolean) Enable advanced edge detection options (sphere radius and Kr
        derivative epsilon)'''
        return bool()
    @property
    def use_view_map_cache(self):
        '''(Boolean) Keep the computed view map and avoid re-calculating it if
        mesh geometry is unchanged'''
        return bool()
    @property
    def sphere_radius(self):
        '''(Float) Sphere radius for computing curvatures'''
        return float()
    @property
    def kr_derivative_epsilon(self):
        '''(Float) Kr derivative epsilon for computing suggestive contours'''
        return float()
    @property
    def crease_angle(self):
        '''(Float) Angular threshold for detecting crease edges'''
        return float()
    @property
    def linesets(self):
        '''(Sequence of FreestyleLineSet)'''
        return Linesets()