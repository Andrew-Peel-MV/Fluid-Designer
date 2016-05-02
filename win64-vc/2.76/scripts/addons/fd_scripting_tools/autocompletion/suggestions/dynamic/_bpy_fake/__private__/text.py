from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . textline import TextLine
from . library import Library
from . animdata import AnimData
from . bpy_struct import bpy_struct
import mathutils

class Text(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique datablock ID name'''
        return str()
    @property
    def users(self):
        '''(Integer) Number of times this datablock is referenced'''
        return int()
    @property
    def use_fake_user(self):
        '''(Boolean) Save this datablock even if it has no users'''
        return bool()
    @property
    def tag(self):
        '''(Boolean) Tools can use this to tag data for their own purposes
        (initial state is undefined)'''
        return bool()
    @property
    def is_updated(self):
        '''(Boolean) Datablock is tagged for recalculation'''
        return bool()
    @property
    def is_updated_data(self):
        '''(Boolean) Datablock data is tagged for recalculation'''
        return bool()
    @property
    def is_library_indirect(self):
        '''(Boolean) Is this ID block linked indirectly'''
        return bool()
    @property
    def library(self):
        '''(Library) Library file the datablock is linked from'''
        return Library()
    @property
    def preview(self):
        '''(ImagePreview) Preview image and icon of this datablock (None if not
        supported for this type of data)'''
        return ImagePreview()
    @property
    def filepath(self):
        '''(String) Filename of the text file'''
        return str()
    @property
    def is_dirty(self):
        '''(Boolean) Text file has been edited since last save'''
        return bool()
    @property
    def is_modified(self):
        '''(Boolean) Text file on disk is different than the one in memory'''
        return bool()
    @property
    def is_in_memory(self):
        '''(Boolean) Text file is in memory, without a corresponding file on disk'''
        return bool()
    @property
    def use_module(self):
        '''(Boolean) Register this text as a module on loading, Text name must
        end with ".py"'''
        return bool()
    @property
    def use_tabs_as_spaces(self):
        '''(Boolean) Automatically converts all new tabs into spaces'''
        return bool()
    @property
    def lines(self):
        '''(Sequence of TextLine) Lines of text'''
        return (TextLine(),)
    @property
    def current_line(self):
        '''(TextLine) Current line, and start line of selection if one exists'''
        return TextLine()
    @property
    def current_character(self):
        '''(Integer) Index of current character in current line, and also start
        index of character in selection if one exists'''
        return int()
    @property
    def current_line_index(self):
        '''(Integer) Index of current TextLine in TextLine collection'''
        return int()
    @property
    def select_end_line(self):
        '''(TextLine) End line of selection'''
        return TextLine()
    @property
    def select_end_character(self):
        '''(Integer) Index of character after end of selection in the selection
        end line'''
        return int()
    def copy(self):
        '''Create a copy of this datablock (not supported for all datablocks)
        
        Returns:
          id: (ID) New copy of the ID'''
        return ID()
    def user_clear(self):
        '''Clear the user count of a datablock so its not saved, on reload the
        data will be removed'''
        return 
    def animation_data_create(self):
        '''Create animation data to this ID, note that not all ID types support
        this
        
        Returns:
          anim_data: (AnimData) New animation data or NULL'''
        return AnimData()
    def animation_data_clear(self):
        '''Clear animation on this this ID'''
        return 
    def update_tag(self, refresh):
        '''Tag the ID to update its display data, e.g. when calling
        :class:`bpy.types.Scene.update`
        
        Parameter:
          refresh: (Enum) Type of updates to perform'''
        return 
    def clear(self):
        '''clear the text block'''
        return 
    def write(self, text):
        '''write text at the cursor location and advance to the end of the text
        block
        
        Parameter:
          text: (String) New text for this datablock'''
        return 