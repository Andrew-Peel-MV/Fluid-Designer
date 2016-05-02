from . uilayout import UILayout
from . struct import Struct
from . node import Node
from . context import Context
from . nodesocket import NodeSocket
from . bpy_struct import bpy_struct
import mathutils

class NodeSocketInterface(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Socket name'''
        return str()
    @property
    def identifier(self):
        '''(String) Unique identifier for mapping sockets'''
        return str()
    @property
    def is_output(self):
        '''(Boolean) True if the socket is an output, otherwise input'''
        return bool()
    @property
    def bl_socket_idname(self):
        '''(String)'''
        return str()
    def draw(self, context, layout):
        '''Draw template settings
        
        Parameter:
          context: (Context)
          layout: (UILayout) Layout in the UI'''
        return 
    def draw_color(self, context):
        '''Color of the socket icon
        
        Parameter:
          context: (Context)
        
        Returns:
          color: (Float[4])'''
        return ''
    def register_properties(self, data_rna_type):
        '''Define RNA properties of a socket
        
        Parameter:
          data_rna_type: (Struct) RNA type for special socket properties'''
        return 
    def init_socket(self, node, socket, data_path):
        '''Initialize a node socket instance
        
        Parameter:
          node: (Node) Node of the socket to initialize
          socket: (NodeSocket) Socket to initialize
          data_path: (String) Path to specialized socket data'''
        return 
    def from_socket(self, node, socket):
        '''Setup template parameters from an existing socket
        
        Parameter:
          node: (Node) Node of the original socket
          socket: (NodeSocket) Original socket'''
        return 