from . struct import Struct
from . context import Context
from . operatorproperties import OperatorProperties
from . bpy_struct import bpy_struct
import mathutils

class Macro(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def properties(self):
        '''(OperatorProperties)'''
        return OperatorProperties()
    @property
    def bl_idname(self):
        '''(String)'''
        return str()
    @property
    def bl_label(self):
        '''(String)'''
        return str()
    @property
    def bl_translation_context(self):
        '''(String)'''
        return str()
    @property
    def bl_description(self):
        '''(String)'''
        return str()
    @property
    def bl_options(self):
        '''(Enum) Options for this operator type
        
        [REGISTER, UNDO, BLOCKING, MACRO, GRAB_CURSOR, PRESET, INTERNAL]'''
        return str()
    def report(self, type, message):
        '''report
        
        Parameter:
          type: (Enum)
          message: (String)'''
        return 
    def poll(self, context):
        '''Test if the operator can be called or not
        
        Parameter:
          context: (Context)
        
        Returns:
          visible: (Boolean)'''
        return bool()
    def draw(self, context):
        '''Draw function for the operator
        
        Parameter:
          context: (Context)'''
        return 