from . wall import Wall
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Scene_Props(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique name used in the code and scripting'''
        return str()
    @property
    def room_type(self):
        '''(Enum)
        
        [CUSTOM, SINGLE, LSHAPE, USHAPE, SQUARE]'''
        return str()
    @property
    def walls(self):
        '''(Sequence of Wall)'''
        return (Wall(),)
    @property
    def floor_type(self):
        '''(Enum)
        
        [CARPET, TILE, WOOD]'''
        return str()
    @property
    def background_image_scale(self):
        '''(Float) Property used to set the scale properly for background images.'''
        return float()
    @property
    def carpet_material(self):
        '''(Enum)'''
        return str()
    @property
    def wood_floor_material(self):
        '''(Enum)'''
        return str()
    @property
    def wall_material(self):
        '''(Enum)'''
        return str()
    @property
    def tile_material(self):
        '''(Enum)'''
        return str()
    @property
    def wall_index(self):
        '''(Integer)'''
        return int()
    @property
    def paint_type(self):
        '''(Enum)
        
        [TEXTURED]'''
        return str()