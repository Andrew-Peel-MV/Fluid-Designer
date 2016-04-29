from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Space(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def type(self):
        '''(Enum) Space data type
        
        [EMPTY, VIEW_3D, TIMELINE, GRAPH_EDITOR, DOPESHEET_EDITOR, NLA_EDITOR,
        IMAGE_EDITOR, SEQUENCE_EDITOR, CLIP_EDITOR, TEXT_EDITOR, NODE_EDITOR,
        LOGIC_EDITOR, PROPERTIES, OUTLINER, USER_PREFERENCES, INFO,
        FILE_BROWSER, CONSOLE]'''
        return str()
    @property
    def show_locked_time(self):
        '''(Boolean)'''
        return bool()