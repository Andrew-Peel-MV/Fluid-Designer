from . node import Node
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Nodes(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def active(self):
        '''(Node) Active node in this tree'''
        return Node()
    def new(self, type):
        '''Add a node to this node tree
        
        Parameter:
          type:
            (String) Type of node to add (Warning: should be same as
            node.bl_idname, not node.type!)
        
        Returns:
          node: (Node) New node'''
        return Node()
    def remove(self, node):
        '''Remove a node from this node tree
        
        Parameter:
          node: (Node) The node to remove'''
        return 
    def clear(self):
        '''Remove all nodes from this node tree'''
        return 
    def get(key): return Node()
    def __getitem__(key): return Node()
    def __iter__(key): yield Node()