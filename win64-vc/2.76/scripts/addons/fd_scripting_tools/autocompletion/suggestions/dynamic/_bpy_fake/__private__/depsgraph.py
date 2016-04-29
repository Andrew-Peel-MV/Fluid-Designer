from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class Depsgraph(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    def debug_graphviz(self, filename):
        '''debug_graphviz
        
        Parameter:
          filename: (String) File in which to store graphviz debug output'''
        return 
    def debug_rebuild(self):
        '''debug_rebuild'''
        return 
    def debug_stats(self):
        '''Report the number of elements in the Dependency Graph'''
        return 