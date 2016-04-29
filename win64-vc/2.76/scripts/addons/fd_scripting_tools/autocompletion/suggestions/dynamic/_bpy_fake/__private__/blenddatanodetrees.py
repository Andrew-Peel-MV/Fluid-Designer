from . nodetree import NodeTree
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class BlendDataNodeTrees(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_updated(self):
        '''(Boolean)'''
        return bool()
    def new(self, name, type):
        '''Add a new node tree to the main database
        
        Parameter:
          name: (String) New name for the datablock
          type: (Enum) The type of node_group to add
        
        Returns:
          tree: (NodeTree) New node tree datablock'''
        return NodeTree()
    def remove(self, tree):
        '''Remove a node tree from the current blendfile
        
        Parameter:
          tree: (NodeTree) Node tree to remove'''
        return 
    def tag(self, value):
        '''tag
        
        Parameter:
          value: (Boolean)'''
        return 
    def get(key): return NodeTree()
    def __getitem__(key): return NodeTree()
    def __iter__(key): yield NodeTree()