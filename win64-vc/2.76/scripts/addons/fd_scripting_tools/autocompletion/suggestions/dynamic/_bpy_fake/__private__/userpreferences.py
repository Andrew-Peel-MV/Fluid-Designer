from . theme import Theme
from . themestyle import ThemeStyle
from . userpreferencesinput import UserPreferencesInput
from . addons import Addons
from . struct import Struct
from . userpreferencesfilepaths import UserPreferencesFilePaths
from . userpreferencesedit import UserPreferencesEdit
from . userpreferencesview import UserPreferencesView
from . userpreferencessystem import UserPreferencesSystem
from . pathcomparecollection import PathCompareCollection
from . bpy_struct import bpy_struct
import mathutils

class UserPreferences(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active_section(self):
        '''(Enum) Active section of the user preferences shown in the user
        interface
        
        [INTERFACE, EDITING, INPUT, ADDONS, THEMES, FILES, SYSTEM]'''
        return str()
    @property
    def themes(self):
        '''(Sequence of Theme)'''
        return (Theme(),)
    @property
    def ui_styles(self):
        '''(Sequence of ThemeStyle)'''
        return (ThemeStyle(),)
    @property
    def addons(self):
        '''(Sequence of Addon)'''
        return Addons()
    @property
    def autoexec_paths(self):
        '''(Sequence of PathCompare)'''
        return PathCompareCollection()
    @property
    def view(self):
        '''(UserPreferencesView) Preferences related to viewing data'''
        return UserPreferencesView()
    @property
    def edit(self):
        '''(UserPreferencesEdit) Settings for interacting with Blender data'''
        return UserPreferencesEdit()
    @property
    def inputs(self):
        '''(UserPreferencesInput) Settings for input devices'''
        return UserPreferencesInput()
    @property
    def filepaths(self):
        '''(UserPreferencesFilePaths) Default paths for external files'''
        return UserPreferencesFilePaths()
    @property
    def system(self):
        '''(UserPreferencesSystem) Graphics driver and operating system settings'''
        return UserPreferencesSystem()