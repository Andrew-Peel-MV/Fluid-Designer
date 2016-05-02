from . struct import Struct
from . node import Node
from . nodesocket import NodeSocket
from . bpy_struct import bpy_struct
import mathutils

class NodeLink(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def is_valid(self):
        '''(Boolean)'''
        return bool()
    @property
    def from_node(self):
        '''(Node)'''
        return Node()
    @property
    def to_node(self):
        '''(Node)'''
        return Node()
    @property
    def from_socket(self):
        '''(NodeSocket)'''
        return NodeSocket()
    @property
    def to_socket(self):
        '''(NodeSocket)'''
        return NodeSocket()
    @property
    def is_hidden(self):
        '''(Boolean) Link is hidden due to invisible sockets'''
        return bool()