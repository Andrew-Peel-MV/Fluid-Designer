from . uilayout import UILayout
from . struct import Struct
from . node import Node
from . context import Context
from . bpy_struct import bpy_struct
import mathutils

class NodeSocket(bpy_struct):
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
    def hide(self):
        '''(Boolean) Hide the socket'''
        return bool()
    @property
    def enabled(self):
        '''(Boolean) Enable the socket'''
        return bool()
    @property
    def link_limit(self):
        '''(Integer) Max number of links allowed for this socket'''
        return int()
    @property
    def is_linked(self):
        '''(Boolean) True if the socket is connected'''
        return bool()
    @property
    def show_expanded(self):
        '''(Boolean) Socket links are expanded in the user interface'''
        return bool()
    @property
    def hide_value(self):
        '''(Boolean) Hide the socket input value'''
        return bool()
    @property
    def node(self):
        '''(Node) Node owning this socket'''
        return Node()
    @property
    def type(self):
        '''(Enum) Data type
        
        [CUSTOM, VALUE, INT, BOOLEAN, VECTOR, STRING, RGBA, SHADER]'''
        return str()
    @property
    def bl_idname(self):
        '''(String)'''
        return str()
    def draw(self, context, layout, node, text):
        '''Draw socket
        
        Parameter:
          context: (Context)
          layout: (UILayout) Layout in the UI
          node: (Node) Node the socket belongs to
          text: (String) Text label to draw alongside properties'''
        return 
    def draw_color(self, context, node):
        '''Color of the socket icon
        
        Parameter:
          context: (Context)
          node: (Node) Node the socket belongs to
        
        Returns:
          color: (Float[4])'''
        return ''