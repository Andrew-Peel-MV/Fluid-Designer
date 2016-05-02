from . struct import Struct
from . gpencillayer import GPencilLayer
from . bpy_struct import bpy_struct
import mathutils

class GreasePencilLayers(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(GPencilLayer) Active grease pencil layer'''
        return GPencilLayer()
    @property
    def active_index(self):
        '''(Integer) Index of active grease pencil layer'''
        return int()
    def new(self, name, set_active):
        '''Add a new grease pencil layer
        
        Parameter:
          name: (String) Name of the layer
          set_active: (Boolean) Set the newly created layer to the active layer
        
        Returns:
          layer: (GPencilLayer) The newly created layer'''
        return GPencilLayer()
    def remove(self, layer):
        '''Remove a grease pencil layer
        
        Parameter:
          layer: (GPencilLayer) The layer to remove'''
        return 
    def get(key): return GPencilLayer()
    def __getitem__(key): return GPencilLayer()
    def __iter__(key): yield GPencilLayer()