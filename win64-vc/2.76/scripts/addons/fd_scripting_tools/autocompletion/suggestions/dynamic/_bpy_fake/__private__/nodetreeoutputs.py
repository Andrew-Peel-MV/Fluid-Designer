from . struct import Struct
from . nodesocketinterface import NodeSocketInterface
from . bpy_struct import bpy_struct
import mathutils

class NodeTreeOutputs(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, type, name):
        '''Add a socket to this node tree
        
        Parameter:
          type: (String) Data type
          name: (String)
        
        Returns:
          socket: (NodeSocketInterface) New socket'''
        return NodeSocketInterface()
    def remove(self, socket):
        '''Remove a socket from this node tree
        
        Parameter:
          socket: (NodeSocketInterface) The socket to remove'''
        return 
    def clear(self):
        '''Remove all sockets from this node tree'''
        return 
    def move(self, from_index, to_index):
        '''Move a socket to another position
        
        Parameter:
          from_index: (Integer) Index of the socket to move
          to_index: (Integer) Target index for the socket'''
        return 
    def get(key): return NodeSocketInterface()
    def __getitem__(key): return NodeSocketInterface()
    def __iter__(key): yield NodeSocketInterface()