from . vectorfont import VectorFont
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataFonts(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def load(self, filepath):
        '''Load a new font into the main database
        
        Parameter:
          filepath: (String) path of the font to load
        
        Returns:
          vfont: (VectorFont) New font datablock'''
        return VectorFont()
    def remove(self, vfont):
        '''Remove a font from the current blendfile
        
        Parameter:
          vfont: (VectorFont) Font to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return VectorFont()
    def __getitem__(key): return VectorFont()
    def __iter__(key): yield VectorFont()