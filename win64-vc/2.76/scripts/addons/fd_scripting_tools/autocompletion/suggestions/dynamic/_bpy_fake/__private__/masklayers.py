from . masklayer import MaskLayer
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MaskLayers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(MaskLayer) Active layer in this mask'''
        return MaskLayer()
    def new(self, name):
        '''Add layer to this mask
        
        Parameter:
          name: (String) Name of new layer
        
        Returns:
          layer: (MaskLayer) New mask layer'''
        return MaskLayer()
    def remove(self, layer):
        '''Remove layer from this mask
        
        Parameter:
          layer: (MaskLayer) Shape to be removed'''
        return 
    def clear(self):
        '''Remove all mask layers'''
        return 
    def get(key): return MaskLayer()
    def __getitem__(key): return MaskLayer()
    def __iter__(key): yield MaskLayer()