from . id import ID
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class KeyingSetPath(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def id(self):
        '''(ID) ID-Block that keyframes for Keying Set should be added to (for
        Absolute Keying Sets only)'''
        return ID()
    @property
    def id_type(self):
        '''(Enum) Type of ID-block that can be used
        
        [ACTION, ARMATURE, BRUSH, CAMERA, CURVE, FONT, GREASEPENCIL, GROUP,
        IMAGE, KEY, LAMP, LIBRARY, LINESTYLE, LATTICE, MASK, MATERIAL, META,
        MESH, MOVIECLIP, NODETREE, OBJECT, PAINTCURVE, PALETTE, PARTICLE,
        SCENE, SCREEN, SOUND, SPEAKER, TEXT, TEXTURE, WINDOWMANAGER, WORLD]'''
        return str()
    @property
    def group(self):
        '''(String) Name of Action Group to assign setting(s) for this path to'''
        return str()
    @property
    def group_method(self):
        '''(Enum) Method used to define which Group-name to use
        
        [NAMED, NONE, KEYINGSET]'''
        return str()
    @property
    def data_path(self):
        '''(String) Path to property setting'''
        return str()
    @property
    def array_index(self):
        '''(Integer) Index to the specific setting if applicable'''
        return int()
    @property
    def use_entire_array(self):
        '''(Boolean) When an 'array/vector' type is chosen (Location, Rotation,
        Color, etc.), entire array is to be used'''
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