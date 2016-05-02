from . struct import Struct
from . imageformatsettings import ImageFormatSettings
from . bpy_struct import bpy_struct
import mathutils

class BakeSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def cage_object(self):
        '''(String) Object to use as cage instead of calculating the cage from
        the active object with cage extrusion'''
        return str()
    @property
    def filepath(self):
        '''(String) Image filepath to use when saving externally'''
        return str()
    @property
    def width(self):
        '''(Integer) Horizontal dimension of the baking map'''
        return int()
    @property
    def height(self):
        '''(Integer) Vertical dimension of the baking map'''
        return int()
    @property
    def margin(self):
        '''(Integer) Extends the baked result as a post process filter'''
        return int()
    @property
    def cage_extrusion(self):
        '''(Float) Distance to use for the inward ray cast when using selected to
        active'''
        return float()
    @property
    def normal_space(self):
        '''(Enum) Choose normal space for baking
        
        [OBJECT, TANGENT]'''
        return str()
    @property
    def normal_r(self):
        '''(Enum) Axis to bake in red channel
        
        [POS_X, POS_Y, POS_Z, NEG_X, NEG_Y, NEG_Z]'''
        return str()
    @property
    def normal_g(self):
        '''(Enum) Axis to bake in green channel
        
        [POS_X, POS_Y, POS_Z, NEG_X, NEG_Y, NEG_Z]'''
        return str()
    @property
    def normal_b(self):
        '''(Enum) Axis to bake in blue channel
        
        [POS_X, POS_Y, POS_Z, NEG_X, NEG_Y, NEG_Z]'''
        return str()
    @property
    def image_settings(self):
        '''(ImageFormatSettings)'''
        return ImageFormatSettings()
    @property
    def save_mode(self):
        '''(Enum) Choose how to save the baking map
        
        [INTERNAL, EXTERNAL]'''
        return str()
    @property
    def use_selected_to_active(self):
        '''(Boolean) Bake shading on the surface of selected objects to the
        active object'''
        return bool()
    @property
    def use_clear(self):
        '''(Boolean) Clear Images before baking (internal only)'''
        return bool()
    @property
    def use_split_materials(self):
        '''(Boolean) Split external images per material (external only)'''
        return bool()
    @property
    def use_automatic_name(self):
        '''(Boolean) Automatically name the output file with the pass type
        (external only)'''
        return bool()
    @property
    def use_cage(self):
        '''(Boolean) Cast rays to active object from a cage'''
        return bool()