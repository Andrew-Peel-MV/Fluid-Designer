from . keymap import KeyMap
from . struct import Struct
from . keymapitems import KeyMapItems
from . keymapitem import KeyMapItem
from . bpy_struct import bpy_struct
import mathutils

class KeyMap(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Name of the key map'''
        return str()
    @property
    def space_type(self):
        '''(Enum) Optional space type keymap is associated with
        
        [EMPTY, VIEW_3D, TIMELINE, GRAPH_EDITOR, DOPESHEET_EDITOR, NLA_EDITOR,
        IMAGE_EDITOR, SEQUENCE_EDITOR, CLIP_EDITOR, TEXT_EDITOR, NODE_EDITOR,
        LOGIC_EDITOR, PROPERTIES, OUTLINER, USER_PREFERENCES, INFO,
        FILE_BROWSER, CONSOLE]'''
        return str()
    @property
    def region_type(self):
        '''(Enum) Optional region type keymap is associated with
        
        [WINDOW, HEADER, CHANNELS, TEMPORARY, UI, TOOLS, TOOL_PROPS, PREVIEW]'''
        return str()
    @property
    def keymap_items(self):
        '''(Sequence of KeyMapItem) Items in the keymap, linking an operator to
        an input event'''
        return KeyMapItems()
    @property
    def is_user_modified(self):
        '''(Boolean) Keymap is defined by the user'''
        return bool()
    @property
    def is_modal(self):
        '''(Boolean) Indicates that a keymap is used for translate modal events
        for an operator'''
        return bool()
    @property
    def show_expanded_items(self):
        '''(Boolean) Expanded in the user interface'''
        return bool()
    @property
    def show_expanded_children(self):
        '''(Boolean) Children expanded in the user interface'''
        return bool()
    def active(self):
        '''active
        
        Returns:
          keymap: (KeyMap) Active key map'''
        return KeyMap()
    def restore_to_default(self):
        '''restore_to_default'''
        return 
    def restore_item_to_default(self, item):
        '''restore_item_to_default
        
        Parameter:
          item: (KeyMapItem)'''
        return 