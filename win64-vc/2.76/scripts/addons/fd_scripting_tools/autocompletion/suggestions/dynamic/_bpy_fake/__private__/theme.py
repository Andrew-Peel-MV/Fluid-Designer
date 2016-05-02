from . themelogiceditor import ThemeLogicEditor
from . themeoutliner import ThemeOutliner
from . themeuserpreferences import ThemeUserPreferences
from . themeinfo import ThemeInfo
from . themesequenceeditor import ThemeSequenceEditor
from . themeclipeditor import ThemeClipEditor
from . themeview3d import ThemeView3D
from . struct import Struct
from . themegrapheditor import ThemeGraphEditor
from . themebonecolorset import ThemeBoneColorSet
from . themeimageeditor import ThemeImageEditor
from . themetexteditor import ThemeTextEditor
from . themenodeeditor import ThemeNodeEditor
from . themetimeline import ThemeTimeline
from . themeproperties import ThemeProperties
from . themefilebrowser import ThemeFileBrowser
from . themenlaeditor import ThemeNLAEditor
from . themeuserinterface import ThemeUserInterface
from . themeconsole import ThemeConsole
from . themedopesheet import ThemeDopeSheet
from . bpy_struct import bpy_struct
import mathutils

class Theme(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Name of the theme'''
        return str()
    @property
    def theme_area(self):
        '''(Enum)
        
        [USER_INTERFACE, STYLE, BONE_COLOR_SETS, VIEW_3D, TIMELINE,
        GRAPH_EDITOR, DOPESHEET_EDITOR, NLA_EDITOR, IMAGE_EDITOR,
        SEQUENCE_EDITOR, TEXT_EDITOR, NODE_EDITOR, LOGIC_EDITOR, PROPERTIES,
        OUTLINER, USER_PREFERENCES, INFO, FILE_BROWSER, CONSOLE, CLIP_EDITOR]'''
        return str()
    @property
    def user_interface(self):
        '''(ThemeUserInterface)'''
        return ThemeUserInterface()
    @property
    def view_3d(self):
        '''(ThemeView3D)'''
        return ThemeView3D()
    @property
    def graph_editor(self):
        '''(ThemeGraphEditor)'''
        return ThemeGraphEditor()
    @property
    def file_browser(self):
        '''(ThemeFileBrowser)'''
        return ThemeFileBrowser()
    @property
    def nla_editor(self):
        '''(ThemeNLAEditor)'''
        return ThemeNLAEditor()
    @property
    def dopesheet_editor(self):
        '''(ThemeDopeSheet)'''
        return ThemeDopeSheet()
    @property
    def image_editor(self):
        '''(ThemeImageEditor)'''
        return ThemeImageEditor()
    @property
    def sequence_editor(self):
        '''(ThemeSequenceEditor)'''
        return ThemeSequenceEditor()
    @property
    def properties(self):
        '''(ThemeProperties)'''
        return ThemeProperties()
    @property
    def text_editor(self):
        '''(ThemeTextEditor)'''
        return ThemeTextEditor()
    @property
    def timeline(self):
        '''(ThemeTimeline)'''
        return ThemeTimeline()
    @property
    def node_editor(self):
        '''(ThemeNodeEditor)'''
        return ThemeNodeEditor()
    @property
    def logic_editor(self):
        '''(ThemeLogicEditor)'''
        return ThemeLogicEditor()
    @property
    def outliner(self):
        '''(ThemeOutliner)'''
        return ThemeOutliner()
    @property
    def info(self):
        '''(ThemeInfo)'''
        return ThemeInfo()
    @property
    def user_preferences(self):
        '''(ThemeUserPreferences)'''
        return ThemeUserPreferences()
    @property
    def console(self):
        '''(ThemeConsole)'''
        return ThemeConsole()
    @property
    def bone_color_sets(self):
        '''(Sequence of ThemeBoneColorSet)'''
        return (ThemeBoneColorSet(),)
    @property
    def clip_editor(self):
        '''(ThemeClipEditor)'''
        return ThemeClipEditor()