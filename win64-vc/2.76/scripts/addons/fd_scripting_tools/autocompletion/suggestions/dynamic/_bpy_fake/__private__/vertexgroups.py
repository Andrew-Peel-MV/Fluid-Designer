from . struct import Struct
from . vertexgroup import VertexGroup
from . bpy_struct import bpy_struct
import mathutils

class VertexGroups(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(VertexGroup) Vertex groups of the object'''
        return VertexGroup()
    @property
    def active_index(self):
        '''(Integer) Active index in vertex group array'''
        return int()
    def new(self, name):
        '''Add vertex group to object
        
        Parameter:
          name: (String) Vertex group name
        
        Returns:
          group: (VertexGroup) New vertex group'''
        return VertexGroup()
    def remove(self, group):
        '''Delete vertex group from object
        
        Parameter:
          group: (VertexGroup) Vertex group to remove'''
        return 
    def clear(self):
        '''Delete all vertex groups from object'''
        return 
    def get(key): return VertexGroup()
    def __getitem__(key): return VertexGroup()
    def __iter__(key): yield VertexGroup()