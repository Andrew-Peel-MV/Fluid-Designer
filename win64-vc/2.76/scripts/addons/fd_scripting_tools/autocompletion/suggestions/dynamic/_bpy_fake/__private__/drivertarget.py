from . id import ID
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class DriverTarget(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def id(self):
        '''(ID) ID-block that the specific property used can be found from
        (id_type property must be set first)'''
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
    def data_path(self):
        '''(String) RNA Path (from ID-block) to property used'''
        return str()
    @property
    def bone_target(self):
        '''(String) Name of PoseBone to use as target'''
        return str()
    @property
    def transform_type(self):
        '''(Enum) Driver variable type
        
        [LOC_X, LOC_Y, LOC_Z, ROT_X, ROT_Y, ROT_Z, SCALE_X, SCALE_Y, SCALE_Z]'''
        return str()
    @property
    def transform_space(self):
        '''(Enum) Space in which transforms are used
        
        [WORLD_SPACE, TRANSFORM_SPACE, LOCAL_SPACE]'''
        return str()