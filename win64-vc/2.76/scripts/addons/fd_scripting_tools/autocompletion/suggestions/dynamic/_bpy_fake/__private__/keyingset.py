from . keyingsetinfo import KeyingSetInfo
from . keyingsetpaths import KeyingSetPaths
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class KeyingSet(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def bl_idname(self):
        '''(String) If this is set, the Keying Set gets a custom ID, otherwise it
        takes the name of the class used to define the Keying Set (for
        example, if the class name is "BUILTIN_KSI_location", and bl_idname is
        not set by the script, then bl_idname = "BUILTIN_KSI_location")'''
        return str()
    @property
    def bl_label(self):
        '''(String)'''
        return str()
    @property
    def bl_description(self):
        '''(String) A short description of the keying set'''
        return str()
    @property
    def type_info(self):
        '''(KeyingSetInfo) Callback function defines for built-in Keying Sets'''
        return KeyingSetInfo()
    @property
    def paths(self):
        '''(Sequence of KeyingSetPath) Keying Set Paths to define settings that
        get keyframed together'''
        return KeyingSetPaths()
    @property
    def is_path_absolute(self):
        '''(Boolean) Keying Set defines specific paths/settings to be keyframed
        (i.e. is not reliant on context info)'''
        return bool()
    @property
    def use_insertkey_override_needed(self):
        '''(Boolean) Override default setting to only insert keyframes where
        they're needed in the relevant F-Curves'''
        return bool()
    @property
    def use_insertkey_override_visual(self):
        '''(Boolean) Override default setting to insert keyframes based on
        'visual transforms''''
        return bool()
    @property
    def use_insertkey_override_xyz_to_rgb(self):
        '''(Boolean) Override default setting to set color for newly added
        transformation F-Curves (Location, Rotation, Scale) to be based on the
        transform axis'''
        return bool()
    @property
    def use_insertkey_needed(self):
        '''(Boolean) Only insert keyframes where they're needed in the relevant
        F-Curves'''
        return bool()
    @property
    def use_insertkey_visual(self):
        '''(Boolean) Insert keyframes based on 'visual transforms''''
        return bool()
    @property
    def use_insertkey_xyz_to_rgb(self):
        '''(Boolean) Color for newly added transformation F-Curves (Location,
        Rotation, Scale) is based on the transform axis'''
        return bool()
    def refresh(self):
        '''Refresh Keying Set to ensure that it is valid for the current context
        (call before each use of one)'''
        return 