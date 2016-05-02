from . struct import Struct
from . nodelink import NodeLink
from . nodesocket import NodeSocket
from . bpy_struct import bpy_struct
import mathutils

class NodeLinks(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def new(self, input, output, verify_limits):
        '''Add a node link to this node tree
        
        Parameter:
          input: (NodeSocket) The input socket
          output: (NodeSocket) The output socket
          verify_limits: (Boolean) Remove existing links if connection limit is exceeded
        
        Returns:
          link: (NodeLink) New node link'''
        return NodeLink()
    def remove(self, link):
        '''remove a node link from the node tree
        
        Parameter:
          link: (NodeLink) The node link to remove'''
        return 
    def clear(self):
        '''remove all node links from the node tree'''
        return 
    def get(key): return NodeLink()
    def __getitem__(key): return NodeLink()
    def __iter__(key): yield NodeLink()