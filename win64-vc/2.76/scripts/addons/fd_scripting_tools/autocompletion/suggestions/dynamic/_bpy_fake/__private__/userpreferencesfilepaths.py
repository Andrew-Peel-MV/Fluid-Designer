from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class UserPreferencesFilePaths(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def show_hidden_files_datablocks(self):
        '''(Boolean) Hide files/datablocks that start with a dot (.*)'''
        return bool()
    @property
    def use_filter_files(self):
        '''(Boolean) Display only files with extensions in the image select
        window'''
        return bool()
    @property
    def hide_recent_locations(self):
        '''(Boolean) Hide recent locations in the file selector'''
        return bool()
    @property
    def hide_system_bookmarks(self):
        '''(Boolean) Hide system bookmarks in the file selector'''
        return bool()
    @property
    def show_thumbnails(self):
        '''(Boolean) Open in thumbnail view for images and movies'''
        return bool()
    @property
    def use_relative_paths(self):
        '''(Boolean) Default relative path option for the file selector'''
        return bool()
    @property
    def use_file_compression(self):
        '''(Boolean) Enable file compression when saving .blend files'''
        return bool()
    @property
    def use_load_ui(self):
        '''(Boolean) Load user interface setup when loading .blend files'''
        return bool()
    @property
    def font_directory(self):
        '''(String) The default directory to search for loading fonts'''
        return str()
    @property
    def texture_directory(self):
        '''(String) The default directory to search for textures'''
        return str()
    @property
    def render_output_directory(self):
        '''(String) The default directory for rendering output, for new scenes'''
        return str()
    @property
    def script_directory(self):
        '''(String) Alternate script path, matching the default layout with
        subdirs: startup, addons & modules (requires restart)'''
        return str()
    @property
    def i18n_branches_directory(self):
        '''(String) The path to the '/branches' directory of your local svn-
        translation copy, to allow translating from the UI'''
        return str()
    @property
    def sound_directory(self):
        '''(String) The default directory to search for sounds'''
        return str()
    @property
    def temporary_directory(self):
        '''(String) The directory for storing temporary save files'''
        return str()
    @property
    def render_cache_directory(self):
        '''(String) Where to cache raw render results'''
        return str()
    @property
    def image_editor(self):
        '''(String) Path to an image editor'''
        return str()
    @property
    def animation_player(self):
        '''(String) Path to a custom animation/frame sequence player'''
        return str()
    @property
    def animation_player_preset(self):
        '''(Enum) Preset configs for external animation players
        
        [INTERNAL, DJV, FRAMECYCLER, RV, MPLAYER, CUSTOM]'''
        return str()
    @property
    def save_version(self):
        '''(Integer) The number of old versions to maintain in the current
        directory, when manually saving'''
        return int()
    @property
    def use_auto_save_temporary_files(self):
        '''(Boolean) Automatic saving of temporary files in temp directory, uses
        process ID (Sculpt or edit mode data won't be saved!')'''
        return bool()
    @property
    def auto_save_time(self):
        '''(Integer) The time (in minutes) to wait between automatic temporary
        saves'''
        return int()
    @property
    def use_keep_session(self):
        '''(Boolean) Always load session recovery and save it after quitting
        Blender'''
        return bool()
    @property
    def recent_files(self):
        '''(Integer) Maximum number of recently opened files to remember'''
        return int()
    @property
    def use_save_preview_images(self):
        '''(Boolean) Enables automatic saving of preview images in the .blend
        file'''
        return bool()