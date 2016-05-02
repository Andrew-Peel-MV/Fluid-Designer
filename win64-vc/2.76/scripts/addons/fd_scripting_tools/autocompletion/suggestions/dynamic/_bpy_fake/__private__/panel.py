from . uilayout import UILayout
from . struct import Struct
from . context import Context
from . bpy_struct import bpy_struct
import mathutils

class Panel(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def layout(self):
        '''(UILayout) Defines the structure of the panel in the UI'''
        return UILayout()
    @property
    def text(self):
        '''(String) XXX todo'''
        return str()
    @property
    def bl_idname(self):
        '''(String) If this is set, the panel gets a custom ID, otherwise it
        takes the name of the class used to define the panel. For example, if
        the class name is "OBJECT_PT_hello", and bl_idname is not set by the
        script, then bl_idname = "OBJECT_PT_hello"'''
        return str()
    @property
    def bl_label(self):
        '''(String) The panel label, shows up in the panel header at the right of
        the triangle used to collapse the panel'''
        return str()
    @property
    def bl_translation_context(self):
        '''(String)'''
        return str()
    @property
    def bl_category(self):
        '''(String)'''
        return str()
    @property
    def bl_space_type(self):
        '''(Enum) The space where the panel is going to be used in
        
        [EMPTY, VIEW_3D, TIMELINE, GRAPH_EDITOR, DOPESHEET_EDITOR, NLA_EDITOR,
        IMAGE_EDITOR, SEQUENCE_EDITOR, CLIP_EDITOR, TEXT_EDITOR, NODE_EDITOR,
        LOGIC_EDITOR, PROPERTIES, OUTLINER, USER_PREFERENCES, INFO,
        FILE_BROWSER, CONSOLE]'''
        return str()
    @property
    def bl_region_type(self):
        '''(Enum) The region where the panel is going to be used in
        
        [WINDOW, HEADER, CHANNELS, TEMPORARY, UI, TOOLS, TOOL_PROPS, PREVIEW]'''
        return str()
    @property
    def bl_context(self):
        '''(String) The context in which the panel belongs to. (TODO: explain the
        possible combinations bl_context/bl_region_type/bl_space_type)'''
        return str()
    @property
    def bl_options(self):
        '''(Enum) Options for this panel type
        
        [DEFAULT_CLOSED, HIDE_HEADER]'''
        return str()
    @property
    def use_pin(self):
        '''(Boolean)'''
        return bool()
    def poll(self, context):
        '''If this method returns a non-null output, then the panel can be drawn
        
        Parameter:
          context: (Context)
        
        Returns:
          visible: (Boolean)'''
        return bool()
    def draw(self, context):
        '''Draw UI elements into the panel UI layout
        
        Parameter:
          context: (Context)'''
        return 
    def draw_header(self, context):
        '''Draw UI elements into the panel's header UI layout
        
        Parameter:
          context: (Context)'''
        return 