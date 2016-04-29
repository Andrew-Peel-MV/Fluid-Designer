from . drivertarget import DriverTarget
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class DriverVariable(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Name to use in scripted expressions/functions (no spaces or
        dots are allowed, and must start with a letter)'''
        return str()
    @property
    def type(self):
        '''(Enum) Driver variable type
        
        [SINGLE_PROP, TRANSFORMS, ROTATION_DIFF, LOC_DIFF]'''
        return str()
    @property
    def targets(self):
        '''(Sequence of DriverTarget) Sources of input data for evaluating this
        variable'''
        return (DriverTarget(),)