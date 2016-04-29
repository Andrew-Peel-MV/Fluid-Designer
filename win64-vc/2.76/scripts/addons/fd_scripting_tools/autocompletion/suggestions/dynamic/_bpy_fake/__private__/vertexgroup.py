from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class VertexGroup(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Vertex group name'''
        return str()
    @property
    def lock_weight(self):
        '''(Boolean) Maintain the relative weights for the group'''
        return bool()
    @property
    def index(self):
        '''(Integer) Index number of the vertex group'''
        return int()
    def add(self, index, weight, type):
        '''Add vertices to the group
        
        Parameter:
          index: (Integer) Index List
          weight: (Float) Vertex weight
          type: (Enum) Vertex assign mode'''
        return 
    def remove(self, index):
        '''Remove a vertex from the group
        
        Parameter:
          index: (Integer) Index List'''
        return 
    def weight(self, index):
        '''Get a vertex weight from the group
        
        Parameter:
          index: (Integer) The index of the vertex
        
        Returns:
          weight: (Float) Vertex weight'''
        return float()