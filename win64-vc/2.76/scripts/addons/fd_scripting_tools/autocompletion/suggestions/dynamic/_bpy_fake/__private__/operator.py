from . context import Context
from . operatorproperties import OperatorProperties
from . uilayout import UILayout
from . operatoroptions import OperatorOptions
from . struct import Struct
from . macro import Macro
from . event import Event
from . bpy_struct import bpy_struct
import mathutils

class Operator(bpy_struct):
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
    def has_reports(self):
        '''(Boolean) Operator has a set of reports (warnings and errors) from
        last execution'''
        return bool()
    @property
    def layout(self):
        '''(UILayout)'''
        return UILayout()
    @property
    def options(self):
        '''(OperatorOptions) Runtime options'''
        return OperatorOptions()
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
    @property
    def macros(self):
        '''(Sequence of Macro)'''
        return (Macro(),)
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
    def execute(self, context):
        '''Execute the operator
        
        Parameter:
          context: (Context)
        
        Returns:
          result: (Enum)'''
        return str()
    def check(self, context):
        '''Check the operator settings, return True to signal a change to redraw
        
        Parameter:
          context: (Context)
        
        Returns:
          result: (Boolean)'''
        return bool()
    def invoke(self, context, event):
        '''Invoke the operator
        
        Parameter:
          context: (Context)
          event: (Event)
        
        Returns:
          result: (Enum)'''
        return str()
    def modal(self, context, event):
        '''Modal operator function
        
        Parameter:
          context: (Context)
          event: (Event)
        
        Returns:
          result: (Enum)'''
        return str()
    def draw(self, context):
        '''Draw function for the operator
        
        Parameter:
          context: (Context)'''
        return 
    def cancel(self, context):
        '''Called when the operator is canceled
        
        Parameter:
          context: (Context)'''
        return 