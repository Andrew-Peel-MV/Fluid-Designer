from . struct import Struct
from . palettecolor import PaletteColor
from . bpy_struct import bpy_struct
import mathutils

class PaletteColors(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(PaletteColor)'''
        return PaletteColor()
    def new(self):
        '''Add a new color to the palette
        
        Returns:
          color: (PaletteColor) The newly created color'''
        return PaletteColor()
    def remove(self, color):
        '''Remove a color from the palette
        
        Parameter:
          color: (PaletteColor) The color to remove'''
        return 
    def clear(self):
        '''Remove all colors from the palette'''
        return 
    def get(key): return PaletteColor()
    def __getitem__(key): return PaletteColor()
    def __iter__(key): yield PaletteColor()