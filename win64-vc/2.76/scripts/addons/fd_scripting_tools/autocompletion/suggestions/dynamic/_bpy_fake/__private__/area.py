from . struct import Struct
from . region import Region
from . areaspaces import AreaSpaces
from . bpy_struct import bpy_struct
import mathutils

class Area(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def spaces(self):
        '''(Sequence of Space) Spaces contained in this area, the first being the
        active space (NOTE: Useful for example to restore a previously used 3D
        view space in a certain area to get the old view orientation)'''
        return AreaSpaces()
    @property
    def regions(self):
        '''(Sequence of Region) Regions this area is subdivided in'''
        return (Region(),)
    @property
    def show_menus(self):
        '''(Boolean) Show menus in the header'''
        return bool()
    @property
    def type(self):
        '''(Enum) Current editor type for this area
        
        [EMPTY, VIEW_3D, TIMELINE, GRAPH_EDITOR, DOPESHEET_EDITOR, NLA_EDITOR,
        IMAGE_EDITOR, SEQUENCE_EDITOR, CLIP_EDITOR, TEXT_EDITOR, NODE_EDITOR,
        LOGIC_EDITOR, PROPERTIES, OUTLINER, USER_PREFERENCES, INFO,
        FILE_BROWSER, CONSOLE]'''
        return str()
    @property
    def x(self):
        '''(Integer) The window relative vertical location of the area'''
        return int()
    @property
    def y(self):
        '''(Integer) The window relative horizontal location of the area'''
        return int()
    @property
    def width(self):
        '''(Integer) Area width'''
        return int()
    @property
    def height(self):
        '''(Integer) Area height'''
        return int()
    def tag_redraw(self):
        '''tag_redraw'''
        return 
    def header_text_set(self, text):
        '''Set the header text
        
        Parameter:
          text: (String) New string for the header, no argument clears the text'''
        return 