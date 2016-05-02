from . struct import Struct
from . context import Context
from . keyingset import KeyingSet
from . anytype import AnyType
from . bpy_struct import bpy_struct
import mathutils

class KeyingSetInfo(bpy_struct):
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
    def bl_options(self):
        '''(Enum) Keying Set options to use when inserting keyframes
        
        [INSERTKEY_NEEDED, INSERTKEY_VISUAL, INSERTKEY_XYZ_TO_RGB]'''
        return str()
    def poll(self, context):
        '''Test if Keying Set can be used or not
        
        Parameter:
          context: (Context)
        
        Returns:
          ok: (Boolean)'''
        return bool()
    def iterator(self, context, ks):
        '''Call generate() on the structs which have properties to be keyframed
        
        Parameter:
          context: (Context)
          ks: (KeyingSet)'''
        return 
    def generate(self, context, ks, data):
        '''Add Paths to the Keying Set to keyframe the properties of the given
        data
        
        Parameter:
          context: (Context)
          ks: (KeyingSet)
          data: (AnyType)'''
        return 