from . struct import Struct
from . nodesocket import NodeSocket
from . bpy_struct import bpy_struct
import mathutils

class NodeOutputs(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, type, name, identifier):
        '''Add a socket to this node
        
        Parameter:
          type: (String) Data type
          name: (String)
          identifier: (String) Unique socket identifier
        
        Returns:
          socket: (NodeSocket) New socket'''
        return NodeSocket()
    def remove(self, socket):
        '''Remove a socket from this node
        
        Parameter:
          socket: (NodeSocket) The socket to remove'''
        return 
    def clear(self):
        '''Remove all sockets from this node'''
        return 
    def move(self, from_index, to_index):
        '''Move a socket to another position
        
        Parameter:
          from_index: (Integer) Index of the socket to move
          to_index: (Integer) Target index for the socket'''
        return 
    def get(key): return NodeSocket()
    def __getitem__(key): return NodeSocket()
    def __iter__(key): yield NodeSocket()