from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class UnitSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def system(self):
        '''(Enum) The unit system to use for button display
        
        [NONE, METRIC, IMPERIAL]'''
        return str()
    @property
    def system_rotation(self):
        '''(Enum) Unit to use for displaying/editing rotation values
        
        [DEGREES, RADIANS]'''
        return str()
    @property
    def scale_length(self):
        '''(Float) Scale to use when converting between blender units and
        dimensions'''
        return float()
    @property
    def use_separate(self):
        '''(Boolean) Display units in pairs (e.g. 1m 0cm)'''
        return bool()